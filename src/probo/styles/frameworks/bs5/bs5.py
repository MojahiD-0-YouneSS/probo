from probo.styles.frameworks.bs5.layout import Layout
from probo.styles.frameworks.bs5.typography import Typography
from probo.styles.frameworks.bs5.forms import Form
from probo.styles.frameworks.bs5.utilities import Utilities
from probo.styles.frameworks.bs5.comp_enum import Components
from probo.components.base import ElementAttributeManipulator
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
        self.get_attr(attr)

    def get_attr(self, attr):
        og_attr = attr.replace("_", "-")
        enum_cls = (
            og_attr if og_attr in set(self.enums) else None
        )  # print(f'{og_attr} not fond in {self.enums}')
        self.kls_value = enum_cls

class BS5ElementStyle:
    """A manager for Bootstrap 5 utility classes on a specific HTML element.

    This class serves as a stateful container for CSS classes. It uses a 
    `PropsProxy` to resolve high-level property definitions into standard 
    Bootstrap 5 class strings (e.g., mapping 'padding=3' to 'p-3').

    Attributes:
        tag (str): The HTML tag associated with this style (e.g., 'div', 'button').
        classes (list[str]): A collection of resolved Bootstrap class strings.
    """
    def __init__(
        self,
        tag,
    ):
        self.tag = tag
        self.classes = []

    def add(self, *values):
        """Resolves and appends one or more Bootstrap classes to the element.

        Uses `PropsProxy` to translate input values into valid BS5 utilities.
        Empty or None values are automatically ignored.

        Args:
            *values: Arbitrary values or property definitions recognized 
                by the PropsProxy engine.

        Returns:
            self: Enables fluent method chaining.
        """
        for value in values:
            if not value:
                continue
            kls = PropsProxy(self, value).kls_value

            if kls:
                self.classes.append(kls)
        return self

    def remove(self, value):
        """Removes a specific class from the element if it exists.

        Args:
            value (str): The exact class string to remove.

        Returns:
            self: Enables fluent method chaining.
        """
        if value in self.classes:
            self.classes.remove(value)
        return self

    def toggle(self, value, add_cls=True):
        """Adds or removes a class based on a conditional flag.

        Args:
            value (Any): The property or class to toggle.
            add_cls (bool): If True, the class is added; if False, it is removed.

        Returns:
            self: Enables fluent method chaining.
        """
        kls = PropsProxy(self, value).kls_value
        if not (kls not in self.classes and not add_cls):
            if kls and add_cls:
                self.classes.append(kls)
            else:
                self.classes.remove(value)
        return self

    def render(self):
        """Serializes the class list into a space-separated string.

        Returns:
            str: A string suitable for an HTML 'class' attribute 
                (e.g., "container mt-5 d-flex").
        """
        return " ".join(self.classes)

class BS5Element:
    """The core structural building block for Bootstrap 5 components.

    This class manages the lifecycle of an HTML element, including its 
    CSS classes and internal content. It provides a flexible API for 
    nesting elements and overriding existing content within the ProboUI tree.

    Attributes:
        tag (str): The HTML tag name (e.g., 'div', 'main', 'section').
        classes (BS5ElementStyle): The style manager for Bootstrap utilities.
        content (list): A collection of child elements, strings, or components.
    """
    def __init__(
        self, tag: str, content: str = "", classes: Optional[list] = None, **attrs
    ):
        self.tag = tag
        self.content = content.render()  if hasattr(content, "render") else content
        # Ensure classes is a list, avoiding shared mutable defaults
        self.classes = (
            [c for c in classes if c is not None] if classes is not None else []
        )
        self.attrs = attrs

    @property
    def attr_manager(self) -> ElementAttributeManipulator:
        return ElementAttributeManipulator(self.attrs)
    
    def add(self, *new_classes: str):
        """Appends Bootstrap utility classes to the element.

        This method proxies directly to the underlying BS5ElementStyle 
        instance to ensure class resolution and deduplication.

        Args:
            *new_classes: One or more Bootstrap class strings or 
                Proxy-compatible properties.

        Returns:
            self: Enables fluent method chaining.
        """

        self.classes.extend(new_classes)
        return self

    def include(self, *content,first=False,override=False):
        """Adds child content or elements to this container.

        Allows for flexible manipulation of the element's inner HTML 
        by supporting prepending, appending, or complete replacement.

        Args:
            *content: The content to be added (strings, other BS5Elements, etc.).
            first (bool): If True, inserts the content at the beginning 
                of the list. Defaults to False.
            override (bool): If True, clears existing content before 
                adding new content. Defaults to False.

        Returns:
            self: Enables fluent method chaining.
        """

        rendered_content = []
        for item in content:
            if hasattr(item, "render"):
                rendered_content.append(item.render())
            else:
                rendered_content.append(str(item))

        # Append to existing content
        if override:
            self.content = "".join(rendered_content)
        elif first and not override:
            self.content = "".join(rendered_content)+self.content
        else:
            self.content += "".join(rendered_content)
        return self

    def render(self) -> str:
        """Serializes the element and all nested children into an HTML string.

        This performs the final assembly, joining resolved classes and 
        recursively rendering child content.

        Returns:
            str: A complete HTML tag string (e.g., '<div class="p-3">...</div>').
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

        return Element(tag=self.tag, content=str(self.content), **self.attrs).element

class BS5:
    """The central orchestrator and factory for Bootstrap 5 components.

    BS5 manages the mapping of internal keys to Bootstrap class strings and 
    provides factory methods to generate structured `BS5Element` instances. 
    It acts as the top-level interface for building responsive layouts.

    Attributes:
        elements (dict): A registry of created or managed elements.
        class_map (dict): A lookup table for mapping abstract keys to 
            specific Bootstrap 5 utility classes.
    """

    def __init__(self, **styles: BS5ElementStyle):
        self.elements = {}
        self.registry = styles

    def render(
        self,
        target_elemnt=None,
    ) -> str:
        """Serializes the specified element or the entire registry into HTML.

        Args:
            target_element (Any, optional): A specific BS5Element to render. 
                If None, it renders the default root or managed collection.

        Returns:
            str: The final HTML output string.
        """
        if target_elemnt is not None and target_elemnt in self.elements:
            return self.elements[target_elemnt]
        else:
            return " ".join([v.render() for k, v in self.registry.items()])

    def __str__(self):
        return self.render()

    def add_new(self, element=None, class_obj=None):
        """Registers a new element type or class mapping into the BS5 context.

        This allows for extending the factory with custom components or 
        specialized Bootstrap utility combinations.

        Args:
            element (str, optional): The name/tag of the element to register.
            class_obj (Any, optional): The style or class definition to 
                associate with the element.
        """
        if element is not None and class_obj is not None:
            self.elements[element] = class_obj.render()
            self.registry[element] = class_obj
        return self

    def get_cls_string(self, key: str) -> str:
        """Resolves a shorthand key into a full Bootstrap 5 class string.

        Args:
            key (str): The internal lookup key (e.g., 'primary-btn').

        Returns:
            str: The corresponding Bootstrap class (e.g., 'btn btn-primary').
        """

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
        """Factory method to create and configure a new BS5Element.

        This is the primary way to generate components. It automatically 
        assigns the correct Bootstrap classes based on the provided key.

        Args:
            key (str): The element type or class key to look up.
            content (str): The initial inner HTML or text content.
            **attrs: Additional HTML attributes (id, data-*, etc.).

        Returns:
            BS5Element: A fully initialized and configured element instance.
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
