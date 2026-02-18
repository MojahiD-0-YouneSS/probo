from probo.components.attributes import (
    ElementAttributeValidator,
    Tag,
)
from enum import Enum
import tempfile
import webbrowser
import os
from collections import OrderedDict
from probo.utility import render_attributes
from typing import Any, Self

MARKER = chr(31)
CONTENT_MARKER = f"@probo:{MARKER}"
Tag.thaw()
class Element:
    """A dynamic HTML element factory and renderer.

    This class utilizes meta-programming to support any HTML tag as a method 
    (e.g., `element.div()`). It handles attribute validation, content nesting 
    using markers, and supports different output formats like lists or 
    'natural' (newline-separated) strings.

    Attributes:
        element (Union[str, List[str]]): The rendered HTML output.
        tag (str): The current HTML tag being processed.
        content (str): Inner HTML or text content.
        is_list (bool): If True, `element` is stored as a list of strings 
            split by MARKER.
        is_natural (bool): If True, MARKERs are replaced by newlines.
        attrs (dict): Dictionary of HTML attributes for the current tag.
    """
    validator = ElementAttributeValidator()

    def __init__(
        self,
        tag:str="",
        content: str = "",
        is_list: bool = False,
        is_natural: bool = False,
        collect_history:bool=False,
        probo_pretty_error:bool=False,
        probo_custom_attrs:bool=False,
        **attrs:dict[str,Any],
    ):
        """Initializes the Element with configuration flags and initial data.

        Args:
            tag: Optional initial tag name.
            content: Initial inner content.
            is_list: Whether to return the rendered element as a list.
            is_natural: Whether to use newlines for formatting.
            probo_pretty_error: If True, renders validation errors as HTML blocks instead of raising ValueErrors.
            probo_custom_attrs: If True, skips standard HTML attribute validation.
            **attrs: Initial HTML attributes.
        """
        self.element: str | list[str] = str()
        self.is_list: bool = is_list
        self.is_natural: bool = is_natural
        self.content: str = content or str()
        self.probo_pretty_error=probo_pretty_error
        self.probo_custom_attrs=probo_custom_attrs
        self.collect_history=collect_history
        self.collect_to_end=True
        self.attrs: dict[str, str] = attrs
        self.tag = tag
        self.use_sibling = False
        self.sibling_element = self.element = str()
        if self.tag:
            self.element = self.build_tag(Tag.get(self.tag)).replace(MARKER, "")

    def __getattr__(self, name:str) -> Any:
        """Dynamically loads and returns a handler for a requested HTML tag.

        If the name corresponds to a valid HTML tag in the `Tag` registry, 
        it creates a private handler method and attaches it to the instance.

        Args:
            name: The name of the HTML tag (e.g., 'div', 'section').

        Returns:
            Callable: A handler function that processes the tag's content 
                and attributes.

        Raises:
            AttributeError: If the tag is not recognized in the registry.
        """
        name = name.lower()
        self.tag = name
        method=self._tag_loader(name)
        if method:
            # return getattr(self, name)
            return method
        else:
            raise AttributeError(
                f"Tag '{name}' is not defined as Element method. "
            )
 
    @property
    def reset_sebling(self):
        self.use_sibling=False
        self.sibling_element=str()
        self.element=str()

    def _tag_loader(self, name: str) -> bool:

        try:
            attr = Tag.get(name)
            method = self.make_private_handler(attr)
            if name == 'doctype':
                method_name = name
            else:
                method_name = attr.value[0]  # name-mangled to be private
            setattr(self, method_name, method)
            return method
        except:
            return False

    def make_private_handler(self, tag_enum:str)-> (...):
        # def handler(*args, reset_sibling=False,is_sibling=False,set_as_content=False,append_to_end=True,**kwargs):
        #     kwargs.update({"reset_sibling":reset_sibling,"is_sibling":is_sibling,"set_as_content":set_as_content,"append_to_end":append_to_end})
        #     return self._tag_method_core(tag_enum, args, kwargs)
        def handler(*args, reset_sibling=False,is_sibling=False,set_as_content=False,append_to_end=True,**kwargs):
            if is_sibling and not reset_sibling:
                self.use_sibling=True
            if reset_sibling:
                self.reset_sebling
            self.collect_to_end=append_to_end

            if args or kwargs:
                parsed = self._element_parser(*args, **kwargs)
                attrs_dict = parsed["attrs"]
                content = parsed["content"]
                self.attrs.update(attrs_dict)
                if not is_sibling and not reset_sibling and self.sibling_element and self.collect_history and not set_as_content:
                    if self.collect_to_end:
                        content += self.sibling_element
                    else:
                        content = self.sibling_element+content

                    self.reset_sebling
                
                if self.collect_to_end:
                    self.content += content
                else:
                    self.content = content+self.content

            
            string = self.build_tag(tag_enum)
            if self.is_list:
                self.element = string.split(MARKER)
            else:
                if self.is_natural:
                    self.element = string.replace(MARKER, "\n")
                else:
                    self.element = string.replace(MARKER, "")
            if self.use_sibling and self.element and not set_as_content:
                    self.sibling_element += self.element
            if set_as_content:
                    
                if self.collect_to_end:
                    self.content += self.element
                else:
                    self.content = self.element + self.content

            self.attrs.clear()
            return self
        return handler

    def _tag_method_core(self, t_enum, args, kwargs) -> Self:
        """
        THE MONOLITH: Consolidates parsing, pipeline logic, and tag construction.
        Reduces 268M calls to ~80M by inlining the hot-path.
        """
        # 1. Pipeline Flags
        is_sib = kwargs.pop('is_sibling', False)
        reset_sib = kwargs.pop('reset_sibling', False)
        set_cont = kwargs.pop('set_as_content', False)
        app_end = kwargs.pop('append_to_end', True)

        if reset_sib:
            self.use_sibling = False
            self.sibling_element = self.element = ""
        
        if is_sib and not reset_sib:
            self.use_sibling = True
        
        self.collect_to_end = app_end

        # 2. Optimized Content Parsing (Inlined _element_parser logic)
        parsed_content = ""
        if args or kwargs:
            # Fast-path for single string content
            if len(args) == 1 and type(args[0]) is str:
                parsed_content = args[0]
            else:
                # DSL / Mixed Parsing
                content_parts = []
                idx = 0
                while idx < len(args):
                    arg = args[idx]
                    if type(arg) is str and arg.upper() in Tag:
                        # Recursive DSL shorthand handling
                        sub_tag = Tag.get(arg).value[0]
                        sub_c = args[idx+1] if idx+1 < len(args) and type(args[idx+1]) is str else ""
                        sub_a = args[idx+2] if idx+2 < len(args) and type(args[idx+2]) is dict else {}
                        # Build minimal nested string
                        parsed_content += f"<{sub_tag}>{sub_c}</{sub_tag}>"
                        idx += 2 # Skip consumed args
                    elif isinstance(arg, str):
                        parsed_content += f" {arg}"
                    elif isinstance(arg, dict):
                        kwargs.update(arg)
                    else:
                        parsed_content += str(arg)
                    idx += 1
            
            # History Consolidation
            if not is_sib and not reset_sib and self.sibling_element and self.collect_history and not set_cont:
                if self.collect_to_end: parsed_content += self.sibling_element
                else: parsed_content = self.sibling_element + parsed_content
                self.use_sibling = False
                self.sibling_element = ""

            if self.collect_to_end: self.content += parsed_content
            else: self.content = parsed_content + self.content

        # 3. Health & Attributes (Inlined element_health logic)
        t_name = t_enum.value[0]
        
        # Attribute Rendering
        attr_str = ""
        if kwargs:
            # Inline attribute loop for speed
            for k, v in kwargs.items():
                if k =="Class": k = "class"
                elif k == "Id": k = "id"
                else: k = k.replace("_", "-")
                attr_str += f' {k}="{v}"'

        # 4. Tag Construction (Inlined build_tag logic)
        is_void = t_enum.value[1]["void"]
        
        if is_void:
            tag_str = f"<{t_name}{attr_str}>" if t_name == "doctype" else f"<{t_name}{attr_str}/>"
        else:
            # We use MARKER as the separation point for list output
            tag_str = f"<{t_name}{attr_str}>{MARKER}{self.content}{MARKER}</{t_name}>"
            self.content = "" # Reset content after consumption

        # 5. Output Management
        if self.is_list:
            self.element = tag_str.split(MARKER)
        else:
            sep = "\n" if self.is_natural else ""
            self.element = tag_str.replace(MARKER, sep)

        if self.use_sibling and self.element and not set_cont:
            self.sibling_element += self.element
            
        if set_cont:
            if self.collect_to_end: self.content += self.element
            else: self.content = self.element + self.content

        return self

    def _element_parser(self, *args, **kwargs) -> dict[str,str]:
        """Parses mixed arguments into structured HTML components.

        Accepts a flexible variety of arguments to determine the tag, 
        attributes, and inner content.

        Args:
            *args: Can include strings (content or tag names), dictionaries 
                (attributes), or other Element objects.
            **kwargs: Standard HTML attributes.

        Returns:
            dict: A dictionary containing 'tag', 'attrs', and 'content'.
        """
        if len(args) == 1 and type(args[0]) is str:
            return {"attrs": kwargs, "content": args[0]}
        
        tag = None
        attrs_dict = {}
        content = ""

        is_sub_content = False
        sub_content = ""

        
        for arg in args:
            if is_sub_content:
                sub_content=str(arg)
                is_sub_content=False
                continue
            if isinstance(arg, str) and arg in Tag.keys_set:
                tag = Tag.get(arg)
                is_sub_content=True
            elif isinstance(arg, str):
                content += f' {arg}'
            elif isinstance(arg, dict):
                attrs_dict.update(arg)
            else:
                content += str(arg)
        if tag:
            netsed_el =self.custom_element(tag.value[0], sub_content, **attrs_dict).element
            if self.collect_to_end:
               content += netsed_el
            else:
                content = netsed_el + content
            attrs_dict.clear()
            
        attrs_dict.update(kwargs)
        
        # print(content)
        return {
            "attrs": attrs_dict,
            "content": content,
        }

    def build_tag(self, tag:Tag, is_custom:bool=False) -> str:
        """Constructs the physical HTML string for a given tag.

        Handles the distinction between void elements (like <img/>) and 
        standard elements (like <div>content</div>), and manages 
        internal MARKER placement.

        Args:
            tag: The tag definition (usually a member of the Tag Enum).
            is_custom: If True, bypasses standard tag health checks.

        Returns:
            str: The raw HTML string including MARKERs.
        """
        tag_value = tag.value
        if not is_custom:
            flag = self.element_health(opening_tag=f"<{tag_value[0]}>")
            if isinstance(flag, str):
                return flag
        if self.collect_history and not self.use_sibling:
            if self.collect_to_end:
                self.content+=self.stringify_element().element
            else:
                self.content= ''.join([self.stringify_element().element,self.content])
        if tag_value[1]["void"]:
            if self.tag == "doctype":
                return f"<{tag_value[0]}{self.render_attrs()}>"
            else:
                
                return f"<{tag_value[0]}{self.render_attrs()}/>"
        else:
            return f"<{tag_value[0]}{self.render_attrs()}>{MARKER}{self.render_content()}{MARKER}</{tag_value[0]}>"

    def render_attrs(self) -> str:
        """Render the attributes of the element as a string."""
        if not self.attrs:
            return str()
        attr_string = f" {render_attributes(self.tag, self.attrs)}"
        return attr_string

    def conserve_probo_flags(self,) -> Self:
        if not self.probo_custom_attrs:
            self.probo_custom_attrs=self.attrs.get('probo_custom_attrs',False)
        if not self.probo_pretty_error:
            self.probo_pretty_error=self.attrs.get('probo_pretty_error',False)
        self.attrs = {k:v for k,v in self.attrs.items() if k not in ['probo_pretty_error','probo_custom_attrs']}
        return self
    
    def element_health(self, opening_tag: str) -> str|Self:
        """Validates attributes against HTML standards.

        Args:
            opening_tag: The string representation of the opening tag 
                for error reporting.

        Returns:
            Either the self instance if valid, or a 'pretty error' HTML string 
            if invalid and `probo_pretty_error` is enabled.

        Raises:
            ValueError: If attributes are invalid and `probo_pretty_error` 
                is False.
        """
        if 'probo_pretty_error' in self.attrs or 'probo_custom_attrs' in self.attrs:
            self.conserve_probo_flags()
        if self.probo_custom_attrs:
            return self
        self.validator.hydrate_validator(
            opening_tag, self.attrs
        )
        
        if self.validator.is_valid or not self.attrs:
            self.attrs = self.validator.valid_attrs
            return self
        else:
            error_attrs_string = " ".join(self.validator.error_attrs)
            if self.probo_pretty_error:
                message = f'''<div style="color:red; border:1px solid #f00; padding:8px; margin:8px 0; background:#fee; font-family:monospace;">
                    <strong>Render Error: invalid_attr for </strong> &quot;{opening_tag[1:-1]}&quot; element does <strong>not accept</strong> these attributes: &quot;{error_attrs_string}&quot;<br>
                    <strong>Element string:</strong> &quot;{opening_tag}&quot;
                </div>'''
                self.validator.error_attrs.clear()
                return message
            else:
                message = f'''"{opening_tag[1:-1]}" element don't accept these attributes "{error_attrs_string}". element string: ""{opening_tag}""'''
                self.validator.error_attrs.clear()
                raise ValueError(message)

    def stringify_element(
        self,
    ) -> Self:
        """Convert the element to a string representation."""
        if self.is_list:
            self.element = "".join(self.element)
        return self

    def render_content(self) -> str:
        """Render the content of the element."""
        if not self.content:
            return str()
        content_string = self.content
        self.content = ""
        return content_string

    def set_attrs(self, **attributes:dict[str,Any]) -> Self:
        """Set attributes for the element."""
        self.attrs = attributes
        return self

    def render(self) -> list[str] | str:
        """Returns the final rendered representation of the element.

        Returns:
            The HTML string or list of strings.
        """
        return self.element

    def set_content(self, content: str, extend:bool=False) -> Self:
        """
        Set the content for the element.
        """
        if self.collect_history:
            self.content+=self.stringify_element().element
        if extend:
            self.content += content
        else:
            self.content = content
        return self

    def raw(self, *string:tuple[str], inner:bool=False, is_comment:bool=False) -> Self:
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

    def set_data(self, *string:tuple[str]) -> Self:
        self.content += " ".join(
            [f'<$probo-var name="{str(string_arg)}"/>' for string_arg in string]
        )
        return self

    def custom_element(self, cstm_tag:str, content:str="", is_void_element:bool=False, **attrs:dict[str,Any]) -> Self:
        if cstm_tag in Tag.keys_set:
            tag = Tag.values_map[cstm_tag]
        else:
            tag = None
        if not tag:
            tag = Enum(
                "tag",
                {
                    cstm_tag.upper(): [
                        cstm_tag.lower(),
                        {
                            "void": is_void_element,
                        },
                    ]
                },
            )[cstm_tag.upper()]
        if tag or attrs:
            self.attrs.update(attrs)
            self.content += content
        string = self.build_tag(tag, is_custom=True)
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
    Manages the head section of an HTML document.

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
        >>> output:
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
        """Adds an element to the head registry with intelligent overwriting.

        Args:
            element: The element to add. Can be a ProboUI `Element` 
                instance or a raw string.
            key: Optional unique identifier. If None, a key is auto-generated 
                based on the tag type and attributes.

        Returns:
            The Head instance for chainable calls.
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
        """Generates a unique key based on the element's tag and attributes.

        Logic:
            - 'title' tags always use the key "title" (singleton).
            - 'meta' tags use 'meta:name:{value}' or 'meta:property:{value}'.
            - 'link' tags use 'link:rel:{value}'.
            - Others fall back to a tag name with a unique short UUID.

        Args:
            element: The element object to analyze.

        Returns:
            A string key used for registry storage.
        """
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
        """Registers the page title. Overwrites any existing title tag.

        Args:
            title: The text content for the title tag.
            **title_attrs: HTML attributes for the title tag.

        Returns:
            The Head instance for chainable calls.
        """
        title = Element().set_attrs(**title_attrs).set_content(title).title()
        self._var_attrs = title_attrs
        return self.add(title)

    def register_meta(self, **meta_attrs):
        """Creates and registers a <meta> tag with the specified attributes.

        This method leverages the `Element` factory to build the tag and then 
        passes it to the `add` method, where `_generate_key` ensures that 
        unique meta tags (like 'description' or 'viewport') overwrite 
        any existing versions.

        Args:
            **meta_attrs: Attributes for the meta tag (e.g., name="description", 
                content="site info").

        Returns:
            The Head instance for chainable calls.
        """
        meta_tag = Element().set_attrs(**meta_attrs).meta()
        self._var_attrs = meta_attrs
        return self.add(meta_tag)

    def register_link(self, **link_attrs):
        """Creates and registers a <link> tag.

        Commonly used for stylesheets, favicons, or canonical URLs. The 
        registry uses the 'rel' attribute to determine if a link should 
        be unique or appended.

        Args:
            **link_attrs: Attributes for the link tag (e.g., rel="stylesheet", 
                href="/style.css").

        Returns:
            The Head instance for chainable calls.
        """
        link_tag = Element().set_attrs(**link_attrs).link()
        self._var_attrs = link_attrs
        return self.add(link_tag)

    def register_script(self, content="", **attrs):
        """Creates and registers a script tag.

        Supports both external scripts (via 'src' attribute) and inline 
        JavaScript content.

        Args:
            content: The inline JavaScript code, if any. Defaults to empty.
            **attrs: Attributes for the script tag (e.g., src="/main.js", 
                defer=True).

        Returns:
            The Head instance for chainable calls.
        """
        script_tag = Element().set_attrs(**attrs).set_content(content).script()
        self._var_attrs = attrs
        return self.add(script_tag)

    def register_style(self, content=""):
        """Creates and registers an inline style block.

        Args:
            content: The raw CSS string to be placed inside the style tag.

        Returns:
            The Head instance for chainable calls.
        """
        style_tag = Element().set_content(content).style()
        return self.add(style_tag)

    def render(self, *extra_head_content):
        """Renders the final <head> block as a single HTML string.

        Args:
            *extra_head_content: Optional additional elements to add 
                immediately before rendering.

        Returns:
            A string containing the full <head> tag and its children.
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
        """Updates or replaces components in the body slots.

        This is the primary method for layout inheritance, allowing you to 
        replace a 'main' slot while keeping the 'header' and 'footer' intact.

        Args:
            **kwargs: Component names and their new content/objects.

        Returns:
            The Template instance for chaining.
        """
        self.components.update(kwargs)
        return self

    def load_base_template(self, template: str, use_as_base=False):
        """Loads an external base template string.

        Args:
            template: The raw HTML string of the base template.
            use_as_base: If True, sets the internal switch to use this base.

        Returns:
            The Template instance for chaining.
        """
        if use_as_base:
            self.switch_base = True
        if template:
            self.__loaded_base = template
        else:
            self.switch_base = False

        return self

    def _get_separator_html(self) -> str:
        """Resolves the separator type into its final HTML/string form.

        Returns:
            The rendered separator string (e.g., an '<hr/>' tag or newline).
        """
        if self.separator == "hr":
            return Element().hr().render()
        elif self.separator == "comment":
            return "\n<!-- Section Break -->\n"
        return self.separator

    def render(self) -> str:
        """Assembles the final HTML document.

        Performs a render pass over all body components. If a component 
        returns a tuple containing CSS, that CSS is automatically hoisted 
        into the `<head>` via `register_style`.

        Returns:
            A complete, valid HTML5 document string.
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
        """Renders the template and opens it in the system's default browser.

        Creates a temporary file on disk and utilizes the `webbrowser` 
        module to display the current state of the template.
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
