from src.probo.components.attributes import (
    ElementAttributeValidator,
    Tag,
    VoidTags,
)
from enum import Enum
import tempfile
import webbrowser
import os
from collections import OrderedDict
from src.probo.utility import render_attributes

MARKER = chr(31)
CONTENT_MARKER = f"@probo:{MARKER}"


class Element:
    """A class to create HTML elements with attributes and content."""

    def __init__(
        self,
        tag=str(),
        content: str = "",
        is_list: bool = False,
        is_natural: bool = False,
        **attrs,
    ):
        self.element: str | list[str] = str()
        self.is_list: bool = is_list
        self.is_natural: bool = is_natural
        self.content: str = content or str()
        self.attrs: dict[str, str] = attrs
        self.tag = tag
        if self.tag:
            self.element = self.build_tag(self.tag).replace(MARKER, "")

    def __getattr__(self, name):
        self.tag = name

        if self._tag_loader(name):
            return getattr(self, name)
        else:
            raise AttributeError(
                f"Tag '{name}' is not defined as {self.__name__} method. "
            )

    def _tag_loader(self, name: str) -> bool:
        try:
            attr = Tag[name.upper()]
            method = self.make_private_handler(attr)
            method_name = f"{attr.name.lower()}"  # name-mangled to be private
            setattr(self, method_name, method)
            return True
        except:
            return False

    def make_private_handler(self, attr):
        def handler(*args, **kwargs):
            is_args = False
            if args or kwargs:
                parsed = self._element_parser(*args, **kwargs)
                tag = parsed["tag"]
                attrs_dict = parsed["attrs"]
                content = parsed["content"]
                self.attrs.update(attrs_dict)
                if CONTENT_MARKER in self.content:
                    self.content = self.content.replace(CONTENT_MARKER, content)
                else:
                    self.content += content
                # is_args = True
            # if is_args:
            # string = self.build_tag(tag)  # assuming Tag.A is valid
            # else:
            string = self.build_tag(attr)  # assuming Tag.A is valid
            if self.is_list:
                self.element = string.split(MARKER)
            else:
                if self.is_natural:
                    self.element = string.replace(MARKER, "\n")
                else:
                    self.element = string.replace(MARKER, "")
            self.attrs.clear()
            return self

        return handler

    def _element_parser(self, *args, **kwargs):
        """
        Smart HTML handler. Accepts:
        - tag name: str
        - attrs: dict or kwargs
        - context: str, ElementObj, or anything
        """
        tag = None
        attrs_dict = {}
        content = " "
        element_obj = None
        for arg in args:
            if isinstance(arg, str) and Tag.get(arg) and not tag:
                try:
                    result = Tag.get(arg)
                    if result:
                        tag = result
                        element_obj = self.__class__(
                            is_list=self.is_list, is_natural=self.is_natural
                        )
                except Exception as e:
                    content = f'<strong style="color:red;size:120px;">{e}</strong>'
                    break
            elif isinstance(arg, str):
                content += arg
            elif isinstance(arg, dict):
                attrs_dict.update(arg)
            elif hasattr(arg, "_Element_tag_loader"):
                content += arg.element
            elif isinstance(arg, (str, int, float)):
                content += str(arg)
        attrs_dict.update(kwargs)
        if element_obj and tag:
            try:
                func = getattr(element_obj, tag.value[0])
                content = func(content, **attrs_dict).element
                attrs_dict.clear()
            except:
                pass
        if not tag:
            tag = tag or Tag.get("div")
        return {
            "tag": tag,
            "attrs": attrs_dict,
            "content": content,
        }

    def build_tag(self, tag, is_custom=False):
        if not isinstance(tag, Enum):
            tag = Tag.get(str(tag))
        if not is_custom:
            flag = self.element_health(opening_tag=f"<{tag.value[0]}>")
            if isinstance(flag, str):
                return flag
        if tag.value[1]["void"]:
            if self.tag == "doctype":
                return f"<{tag.value[0]}{self.render_attrs()}>"
            else:
                return f"<{tag.value[0]}{self.render_attrs()}/>"
        else:
            return f"<{tag.value[0]}{self.render_attrs()}>{MARKER}{self.render_content()}{MARKER}</{tag.value[0]}>"

    def render_attrs(self):
        """Render the attributes of the element as a string."""
        if not self.attrs:
            return str()
        # attr_string = " " + " ".join(f'{key.lower().replace('_','-') if '_' in key.lower() else key.lower()}="{value}"' for key, value in self.attrs.items())
        attr_string = f" {render_attributes(self.tag, self.attrs)}"
        return attr_string

    def element_health(self, opening_tag: str):
        """Check if the element is valid and return it or an error message."""

        attribute_value = ElementAttributeValidator(
            element_tag=opening_tag, **self.attrs
        )
        if attribute_value.is_valid or not self.attrs:
            self.attrs = attribute_value.valid_attrs
            return self
        else:
            error_attrs_string = " ".join(attribute_value.error_attrs)
            message = f'<div style="color:red;"><strong> "{opening_tag[1:-1]}" element don\' accept these attributes "{error_attrs_string}" </strong> element string: ""{opening_tag}""</div>\n'
            attribute_value.error_attrs.clear()
            return message

    def stringify_element(
        self,
    ):
        """Convert the element to a string representation."""
        if self.is_list:
            self.element = "".join(self.element)
        return self

    def render_content(self):
        """Render the content of the element."""
        if not self.content:
            return str()
        content_string = f"{self.content.replace(CONTENT_MARKER, self.element) if CONTENT_MARKER in self.content and self.element else self.content}"
        self.content = ""
        return content_string

    def set_attrs(self, **attributes):
        """Set attributes for the element."""
        self.attrs = attributes
        return self

    def set_content(self, content: str, extend=False):
        """
        Set the content for the element.
        """
        if extend:
            self.content += content
        else:
            self.content = content
        return self

    def raw(self, *string, inner=False, is_comment=False) -> "Element":
        STRING = "".join(["<!--", *string, "-->"])

        if inner:
            self.content += "<!--" + STRING + "-->" if is_comment else STRING

        if self.is_list:
            self.element.extend(
                ["<!--", *string, "-->"]
            ) if is_comment else self.element.extend(list(string))
        else:
            self.element += "<!--" + STRING + "-->" if is_comment else STRING
        return self

    def set_data(self, *string) -> "Element":
        self.content += " ".join(
            [f'<$probo-var name="{str(string_arg)}"/>' for string_arg in string]
        )
        return self

    def custom_element(self, cstm_tag, content="", is_void_element=False, **attrs):
        tag = Enum(
            "tag",
            {
                cstm_tag.upper(): [
                    cstm_tag.lower(),
                    {
                        "void": True
                        if cstm_tag.lower() in VoidTags.VOID_TAGS.value
                        or is_void_element
                        else False
                    },
                ]
            },
        )
        if tag or attrs:
            self.attrs.update(attrs)
            if CONTENT_MARKER in self.content:
                self.content = self.content.replace(CONTENT_MARKER, content)
            else:
                self.content += content
        string = self.build_tag(tag[cstm_tag.upper()], is_custom=True)
        if self.is_list:
            self.element = string.split(MARKER)
        else:
            if self.is_natural:
                self.element = string.replace(MARKER, "\n")
            else:
                self.element = string.replace(MARKER, "")
        self.attrs.clear()
        return self

    def __str__(
        self,
    ):
        return str(self.stringify_element().element)


class Head:
    """
    Manages the <head> section of an HTML document.

    This class acts as a smart registry for metadata, links, scripts, and titles.
    It uses a key-based system to handle overwrites, allowing child templates
    or components to replace metadata defined in parent layouts (e.g., changing
    the page title dynamically).

    Args:
        *head_strings: Initial list of elements (title, meta tags, etc.) to add.

    Attributes:
        _registry (OrderedDict): Internal storage ensuring insertion order and unique keys.

    Example:
        >>> head = Head()
        >>> head.set_title("Home Page")
        >>> head.register_meta(name="description", content="Welcome")
        >>> print(head.render())
        <head><title>Home Page</title><meta name="description" content="Welcome"></head>
    """

    def __init__(self, *head_strings):
        self.head_strings = list(head_strings)
        self._registry = OrderedDict()
        self.meta_tags = []
        self.link_tags = []
        self.script_tags = []
        self.style_tags = []
        self.title = None
        self._var_attrs = {}
        for item in head_strings:
            self.add(item)

    def add(self, element, key=None):
        """
        Smartly adds an element to the head.
        If a key matches an existing element, it OVERWRITES it.
        """
        # 1. Determine Key
        if key is None:
            key = self._generate_key(element)

        # 2. Store (Overwrite if exists)
        self._registry[key] = (
            element.element if isinstance(element, Element) else str(element)
        )
        return self

    def _generate_key(self, element):
        """Auto-generates keys based on element type/attributes."""
        # Assuming element has .tag_name and .attrs properties
        tag = getattr(element, "tag", "unknown")
        attrs = getattr(element, "attrs", {}) or self._var_attrs

        if tag == "title":
            self.title = element.element
            return "title"  # Singleton

        if tag == "meta":
            if "name" in attrs:
                return f"meta:name:{attrs['name']}"
            if "property" in attrs:  # For OpenGraph
                return f"meta:property:{attrs['property']}"
            if "charset" in attrs:
                return "meta:charset"
            self.meta_tags.append(element.element)
        if tag == "link":
            self.link_tags.append(element.element)
            if "rel" in attrs:
                return f"link:rel:{attrs['rel']}"
        if tag == "script":
            self.script_tags.append(element.element)
        if tag == "style":
            self.style_tags.append(element.element)
        # Fallback: Use a UUID if we can't identify it uniquely
        # or just append a random counter if you want to allow duplicates by default
        import uuid

        return f"{tag}:{uuid.uuid4().hex[:8]}"

    def set_title(self, title: str, **title_attrs):
        title = Element().set_attrs(**title_attrs).set_content(title).title()
        self._var_attrs = title_attrs
        return self.add(title)

    def register_meta(self, **meta_attrs):
        meta_tag = Element().set_attrs(**meta_attrs).meta()
        self._var_attrs = meta_attrs
        return self.add(meta_tag)

    def register_link(self, **link_attrs):
        link_tag = Element().set_attrs(**link_attrs).link()
        self._var_attrs = link_attrs
        return self.add(link_tag)

    def register_script(self, content="", **attrs):
        script_tag = Element().set_attrs(**attrs).set_content(content).script()
        self._var_attrs = attrs
        return self.add(script_tag)

    def register_style(self, content=""):
        style_tag = Element().set_content(content).style()
        return self.add(style_tag)

    def render(self, *extra_head_content):
        """
        Render the full <head> tag with all registered tags and content.
        """
        for x in extra_head_content:
            self.add(x)
        head_tag = (
            Element()
            .set_content("".join([el for el in self._registry.values()]))
            .head()
            .element
        )
        return head_tag


class Template:
    """
    Represents a full HTML Document.
    Acts as a Layout Manager allowing components to be swapped by name.

    This class serves as the skeleton for pages. It manages the global <head>
    and organizes body content into named slots (header, main, footer).
    It supports dynamic component swapping, making it ideal for layout inheritance.

    Args:
        separator (str, optional): String or HTML to place between body components. Defaults to "\n".
        **components (dict): Named slots for the body content (e.g., header=..., main=...).

    Attributes:
        head (Head): The managed Head instance for this document.
        components (OrderedDict): The ordered registry of body components.

    Example:
        >>> # Define Layout
        >>> layout = Template(
        ...     header="<nav>...</nav>",
        ...     main="<!-- Content -->",
        ...     footer="<footer>...</footer>"
        ... )
        >>>
        >>> # Swap Content
        >>> layout.swap_component(main="<h1>Hello World</h1>")
        >>>
        >>> # Render
        >>> html = layout.render()
    """

    def __init__(self, separator: str = "\n", **components):
        """
        Initialize the template.
        Args:
            separator: String or HTML to place between body components.
            **components: Named slots for the body (e.g., header=..., main=...)
        """
        self.separator = separator

        # 1. Initialize Smart Head (Standard HTML5 Defaults)
        self.head = Head()
        self.head.register_meta(charset="UTF-8")
        self.head.register_meta(
            name="viewport", content="width=device-width, initial-scale=1.0"
        )
        self.head.set_title("probo Page")
        self.__loaded_base = ""
        # 2. Initialize Body Slots (OrderedDict preserves insertion order)
        self.components = OrderedDict(components)

    def swap_component(self, **kwargs):
        """
        Updates or adds components to the body slots.
        Usage: template.swap_component(main=NewComponent())
        """
        self.components.update(kwargs)
        return self

    def load_base_template(self, template: str, use_as_base=False):
        if use_as_base:
            self.switch_base = True
        if template:
            self.__loaded_base = template
        else:
            self.switch_base = False

        return self

    def _get_separator_html(self) -> str:
        """Resolves the separator into a string."""
        if self.separator == "hr":
            return hr().render()
        elif self.separator == "comment":
            return "\n<!-- Section Break -->\n"
        return self.separator

    def render(self) -> str:
        """
        Assembles the full document: DOCTYPE + HTML(HEAD + BODY).
        """
        # 1. Render Body Components
        rendered_parts = []
        for comp in self.components.values():
            if hasattr(comp, "render"):
                # It's a Component/Element -> Render it
                # Handle tuple return from Component (html, css)
                result = comp.render()
                if isinstance(result, tuple):
                    # If component returned CSS, inject it into HEAD automatically
                    # This is a "Pro" feature: Automatic Style hoisting
                    html_str, css_str = result
                    if css_str:
                        self.head.register_style(css_str)
                    rendered_parts.append(html_str)
                else:
                    rendered_parts.append(result)
            else:
                # It's a string
                rendered_parts.append(str(comp))

        # 2. Join Body parts
        sep = self._get_separator_html()
        body_content = sep.join(rendered_parts)

        # 3. Construct the Tree
        # doctype() returns string "<!DOCTYPE html>"
        # html(...) wraps head and body

        # Note: We use your functional tags here
        document = (
            Element().doctype().element
            + Element()
            .set_attrs(lang="en")
            .set_content(
                self.head.render() + Element().set_content(body_content).body().element
            )
            .html()
            .element
        )

        return document

    def preview(self):
        """
        Renders and opens the template in the default web browser.
        """
        html_content = self.render()

        with tempfile.NamedTemporaryFile(
            "w", delete=False, suffix=".html", encoding="utf-8"
        ) as f:
            f.write(html_content)
            f.flush()
            url = f"file://{os.path.abspath(f.name)}"
            print(f"Opening preview: {url}")
            webbrowser.open(url)
