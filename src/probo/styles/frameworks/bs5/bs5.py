from probo.styles.frameworks.bs5.layout import Layout
from probo.styles.frameworks.bs5.typography import Typography
from probo.styles.frameworks.bs5.forms import Form
from probo.styles.frameworks.bs5.utilities import Utilities
from probo.styles.frameworks.bs5.components.comp_enum import Components
from typing import Optional
from enum import Enum


class BS5Props(Enum):
    layout = Layout()
    typography = Typography()
    form = Form()
    urilities = Utilities()
    components = Components()


def _unpack_props():
    base = []
    for k in BS5Props._member_names_:
        try:
            base.extend(BS5Props[k].value.values_as_list)
        except Exception as e:
            print(e)
    return base


BS5_PROPS_AS_LIST = _unpack_props()


class PropsProxy:
    def __init__(self, parent, attr):
        self.parent = parent
        self.enums = BS5_PROPS_AS_LIST
        self.kls_value = None
        self.__getattr__(attr)

    def __getattr__(self, attr):
        og_attr = attr.replace("_", "-")
        enum_cls = (
            og_attr if og_attr in self.enums else None
        )  # print(f'{og_attr} not fond in {self.enums}')
        self.kls_value = enum_cls


class BS5ElementStyle:
    def __init__(
        self,
        tag,
    ):
        self.tag = tag
        self.classes = []

    def add(self, *values):
        for value in values:
            if not value:
                continue
            kls = PropsProxy(self, value).kls_value

            if kls:
                self.classes.append(kls)
        return self

    def remove(self, value):
        if value in self.classes:
            self.classes.remove(value)
        return self

    def toggle(self, value, add_cls=True):
        kls = PropsProxy(self, value).kls_value
        if not (kls not in self.classes and not add_cls):
            if kls and add_cls:
                self.classes.append(kls)
            else:
                self.classes.remove(value)
        return self

    def render(self):
        return " ".join(self.classes)


class BS5Element:
    """
    A dedicated builder for Bootstrap 5 elements.
    Manages the 'class' attribute specifically while delegating rendering to Element.
    """

    def __init__(
        self, tag: str, content: str = "", classes: Optional[list] = None, **attrs
    ):
        self.tag = tag
        self.content = content
        # Ensure classes is a list, avoiding shared mutable defaults
        self.classes = (
            [c for c in classes if c is not None] if classes is not None else []
        )
        self.attrs = attrs

    def add(self, *new_classes: str):
        """Fluent API to add Bootstrap classes."""
        self.classes.extend(new_classes)
        return self

    def include(self, *content):
        """
        Adds content to the element.
        If content is another BS5Element, it renders it.
        """
        rendered_content = []
        for item in content:
            if hasattr(item, "render"):
                rendered_content.append(item.render())
            else:
                rendered_content.append(str(item))

        # Append to existing content
        self.content += "".join(rendered_content)
        return self

    def render(self) -> str:
        """
        Constructs the final Element with the combined class string.
        """
        # Join classes with spaces
        final_class_str = " ".join(self.classes)

        # Merge with any class passed in attrs (avoiding overwrites)
        if "Class" in self.attrs:  # Handling your alias
            final_class_str += f" {self.attrs.pop('Class')}"
        if final_class_str:
            self.attrs["Class"] = final_class_str.strip()
        # Delegate to the Core Engine
        from probo.components.elements import Element

        return Element(tag=self.tag, content=self.content, **self.attrs).element


class BS5:
    def __init__(self, **styles: BS5ElementStyle):
        self.elements = {}
        self.registry = styles

    def render(
        self,
        target_elemnt=None,
    ) -> str:
        if target_elemnt is not None and target_elemnt in self.elements:
            return self.elements[target_elemnt]
        else:
            return " ".join([v.render() for k, v in self.registry.items()])

    def __str__(self):
        return self.render()

    def add_new(self, element=None, class_obj=None):
        if element is not None and class_obj is not None:
            self.elements[element] = class_obj.render()
            self.registry[element] = class_obj
        return self

    def get_cls_string(self, key: str) -> str:
        """Returns just the class string (Old behavior)."""
        # Convert selector-like key 'btn#x2' -> internal key 'btn__x2' if needed
        # For now assuming direct mapping based on your snippet
        clean_key = key.replace("#", "__").replace(".", "_")
        if clean_key in self.registry:
            return " ".join(self.registry[clean_key].classes)
        return ""

    def _normalize_key(self, key: str) -> str:
        """
        Converts a selector-style key to a python-valid kwarg key.

        Mappings:
        - '#' (ID)    -> '__' (Double Underscore)
        - '.' (Class) -> '_'  (Single Underscore)
        - '-' (Kebab) -> '_'  (Single Underscore)

        Example: 'h5.card-title' -> 'h5_card_title'
        Example: 'btn#submit-btn' -> 'btn__submit_btn'
        """
        return key.replace("#", "__").replace(".", "_").replace("-", "_")

    def get_element(self, key: str, content: str = "", **attrs) -> BS5Element:
        """
        Returns a BS5Element configured with the stored styles.
        Usage: bs5.get_element('btn#x2', 'Click Me')
        """
        clean_key = self._normalize_key(key)

        if clean_key in self.registry:
            style_obj = self.registry[clean_key]

            # Create the element using the stored Tag and Classes
            return BS5Element(
                tag=style_obj.tag,
                content=content,
                classes=style_obj.classes.copy(),  # Copy to prevent mutation of the registry
                **attrs,
            )

        # Fallback if key not found (or raise error)
        raise ValueError(f"BS5 Style '{key}' not found in registry.")
