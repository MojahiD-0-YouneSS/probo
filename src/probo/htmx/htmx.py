from probo.components.tag_functions import script as Srpt
from typing import Dict, Any, Optional, List
from probo.htmx.htmx_enum import (
    HxAttr,
    HxBoolValue,
    HxSwap,
    HxTrigger,
    HxParams,
    HxSyncStrategy,
)
from probo.utility import render_attributes as r
# from probo.components.elements import Element
from probo.components.tag_classes.block_tags import EL
from probo.components.base import ElementAttributeManipulator

HTMX_CDN_URL = "https://unpkg.com/htmx.org@1.9.10"

LOCAL_TEMPO_PATH = "/static/js/htmx.min.js"


class Ajax:
    """Helper class for building HTMX AJAX attributes using a fluent interface.

    This class provides a chainable API to construct a dictionary of HTMX 
    attributes (e.g., hx-get, hx-target). It abstracts away the string keys 
    defined in `HxAttr`, preventing typos and improving IDE autocompletion 
    for HTMX-heavy components.

    Attributes:
        AJAX_HX_DICT (Dict[str, str]): Internal storage for the mapped 
            HTMX attribute keys and their values.
    """

    def __init__(
        self,
    ):
        self.AJAX_HX_DICT = dict()

    def hx_get(self, url: str) -> Dict[str, str]:
        """Sets the hx-get attribute to the specified URL.

        Args:
            url: The endpoint to fetch via a GET request.

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.GET.value] = url
        return self

    def hx_post(self, url: str) -> Dict[str, str]:
        """Sets the hx-post attribute to the specified URL.

        Args:
            url: The endpoint to send data to via a POST request.

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.POST.value] = url
        return self

    def hx_put(self, url: str) -> Dict[str, str]:
        """Specifies the target element to be updated by the AJAX response.

        Args:
            selector: A CSS selector (e.g., "#content", ".result") indicating 
                where the response HTML should be injected.

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.PUT.value] = url
        return self

    def hx_patch(self, url: str) -> Dict[str, str]:
        """Defines how the response will be swapped into the target.

        Args:
            swap_str: The swap strategy (e.g., "innerHTML", "outerHTML", "beforebegin").

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.PATCH.value] = url
        return self
    
    def hx_swap_oob(self,) -> Dict[str, str]:
        """Enables 'Out of Band' swaps for this element.

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.SWAP_OOB.value] = True
        return self

    def hx_delete(self, url: str) -> Dict[str, str]:
        """Sets the hx-delete attribute for resource removal.

        Args:
            url: The endpoint to send the DELETE request to.

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.DELETE.value] = url
        return self

    def hx_target(self, selector: str) -> Dict[str, str]:
        """Specifies an element to show a loading indicator during the request.

        Args:
            selector: A CSS selector for the loading indicator element.

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.TARGET.value] = selector
        return self

    def hx_trigger(self, trigger_str: str) -> Dict[str, str]:
        """Specifies the event that triggers the AJAX request.

        Args:
            trigger_str: The event type (e.g., "click", "keyup delay:500ms", "revealed").

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.TRIGGER.value] = trigger_str
        return self

    def hx_swap(self, swap_str: str) -> Dict[str, str]:
        """Defines how the response will be swapped into the target.

        Args:
            swap_str: The swap strategy (e.g., "innerHTML", "outerHTML", "beforebegin").

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.SWAP.value] = swap_str
        return self

    def hx_indicator(self, selector: str) -> Dict[str, str]:
        """Specifies an element to show a loading indicator during the request.

        Args:
            selector: A CSS selector for the loading indicator element.

        Returns:
            The Ajax instance for method chaining.
        """
        self.AJAX_HX_DICT[HxAttr.INDICATOR.value] = selector
        return self

    def get_values(self):
        """Retrieves the final dictionary of HTMX attributes.

        Returns:
            A dictionary containing all configured hx-* attributes.
        """
        return self.AJAX_HX_DICT

class HTMXElement(Ajax):
    """
    Represents a single HTMX configuration.
    Can be rendered as a full HTML Element OR just a string of Attributes.

    This class provides a fluent API for building HTMX interactions. It supports
    standard attributes like hx-get, hx-post, hx-target, and hx-swap, normalized
    from Python snake_case (hx_get) to HTML kebab-case (hx-get).

    Args:
        element_tag (str, optional): The HTML tag name (e.g., 'button'). If None, renders attributes only.
        content (str, optional): The inner content of the element (if tag is provided).
        template_info: a dict with tags attrs exists in a the template to avoid deat referencing
        **hx_attrs: Arbitrary HTMX attributes (e.g., hx_post='/api/save', hx_target='#result').

    Attributes:
        attrs (dict): The normalized dictionary of HTML attributes.

    Example:
        >>> # Fluent API
        >>> btn = HTMXElement("button", content="Save")
        >>> btn.hx_post("/save").hx_target("#status").hx_swap("outerHTML")
        >>> print(btn.render())
        <button hx-post="/save" hx-target="#status" hx-swap="outerHTML">Save</button>

        >>> # Attribute Bag
        >>> attrs = HTMXElement().hx_get("/search").hx_trigger("keyup")
        >>> print(attrs.render())
        hx-get="/search" hx-trigger="keyup"
    """

    def __init__(
        self,
        element_tag: str = None,
        content: str = None,
        template_info: dict = None,
        **hx_attrs,
    ):
        """Initializes the HTMX element with tag, content, and attributes.

        Validates the provided tag against `template_info` if available to 
        prevent dead references in specific layouts.

        Args:
            element_tag: The HTML tag name. If None, the object renders 
                as an attribute string.
            content: Inner content for the element.
            template_info: Registry of allowed tags and attributes for 
                safety checks.
            **hx_attrs: Initial HTMX attributes (e.g., hx_get="/api").
        
        Raises:
            ValueError: If `element_tag` is provided but not found in 
                `template_info['tags']`.
        """

        self.hx_params = HxParams
        self.hx_bool_val = HxBoolValue
        self.hx_funcs = Ajax
        self.hx_attrs = hx_attrs
        self.element_tag = element_tag
        self.content = content or str()
        self.template_info = template_info or dict()
        super().__init__()

        if template_info and template_info.get("tags", []):
            if self.element_tag not in template_info.get("tags", []):
                raise ValueError("elemet not in tag")

    @property
    def attr_manager(self) -> ElementAttributeManipulator:
        return ElementAttributeManipulator(self.hx_attrs)
    
    def set_attr(self, **attrs) -> "HTMXElement":
        """Sets multiple attributes, automatically resolving HxAttr Enums.

        Args:
            **attrs: Attribute keys and values. Keys are converted to 
                HTMX kebab-case if they match `HxAttr` members.

        Returns:
            The HTMXElement instance for chaining.
        """
        for attribute, value in attrs.items():
            try:
                attr_name = HxAttr[attribute.upper()].value
            except:
                attr_name = attribute
            self.hx_attrs[attr_name] = value
        return self

    def get_attr(self, attribute: str) -> Any:
        """Constructs a complex hx-trigger string with modifiers and filters.

        Args:
            event: The base event (e.g., 'click', 'keyup'). Resolved 
                via `HxTrigger` enum if present.
            modifiers: Suffixes like {'delay': '500ms', 'once': ''}.
            filters: Logic expressions in brackets, e.g., ['ctrlKey'].

        Returns:
            The HTMXElement instance for chaining.

        Examples:
            >>> btn.build_trigger_string("keyup", modifiers={"delay": "500ms"}, filters=["target.value.length > 3"])
            # Produces: hx-trigger="keyup delay:500ms [target.value.length > 3]"
        """
        attr_name = self.hx_attrs.get(attribute, None)
        return attr_name

    def del_attr(self, attribute: str) -> "HTMXElement":
        """Removes a specific attribute from the element's attribute registry.

        This method safely attempts to remove an attribute. If the attribute 
        does not exist, it fails silently and returns the instance.

        Args:
            attribute: The key of the attribute to be removed (e.g., 'hx-get').

        Returns:
            The HTMXElement instance for method chaining.
        """
        self.hx_attrs.pop(attribute, None)
        return self

    def build_trigger_string(
        self,
        event: str,
        modifiers: Optional[Dict[str, str]] = None,
        filters: Optional[List[str]] = None,
    ) -> "HTMXElement":
        """Constructs a complex hx-trigger string with modifiers and filters.

        This method builds the standard HTMX trigger syntax: 
        "event modifier:value [filter]". It automatically resolves common 
        events from the `HxTrigger` enum.

        Args:
            event: The triggering event (e.g., 'click', 'keyup'). 
                Will be resolved via `HxTrigger` if the key exists.
            modifiers: Suffixes that modify event behavior 
                (e.g., {'delay': '500ms', 'once': 'true'}).
            filters: A list of JavaScript expressions that must be true 
                for the event to trigger (e.g., ['ctrlKey', 'target.value != ""']).

        Returns:
            The HTMXElement instance for method chaining.

        Examples:
            >>> # Basic trigger
            >>> element.build_trigger_string("click")
            
            >>> # Trigger with delay and condition
            >>> element.build_trigger_string(
            ...     "keyup", 
            ...     modifiers={"delay": "1s"}, 
            ...     filters=["target.value.length > 3"]
            ... )
            # Result: hx-trigger="keyup delay:1s [target.value.length > 3]"
        """
        base = HxTrigger[event].value if event in HxTrigger else event
        parts = [base]

        if modifiers:
            parts.extend(f"{k}:{v}" for k, v in modifiers.items())

        if filters:
            parts.append(f"[{' and '.join(filters)}]")

        self.hx_attrs[HxAttr.TRIGGER.value] = " ".join(parts)
        return self

    def build_swap_string(
        self, name: str, modifiers: Optional[Dict[str, str]] = None
    ) -> "HTMXElement":
        """Constructs an hx-swap string with timing or transition modifiers.

        Args:
            name: The swap strategy (e.g., 'innerHTML', 'outerHTML').
            modifiers: Dict of modifiers like {'transition': 'true', 'swap': '1s'}.

        Returns:
            The HTMXElement instance for chaining.
        """
        base = HxSwap[name].value if name in HxSwap else name
        parts = [base]
        if modifiers:
            parts.extend(f"{k}:{v}" for k, v in modifiers.items())
        self.hx_attrs[HxAttr.SWAP.value] = " ".join(parts)
        return self

    def build_sync_string(self, element: str, strategy: str) -> "HTMXElement":
        """Constructs an hx-sync string to coordinate AJAX requests between elements.

        Args:
            element: CSS selector of the element to synchronize with.
            strategy: The sync strategy (e.g., 'drop', 'abort', 'replace').

        Returns:
            The HTMXElement instance for chaining.
        """
        self.hx_attrs[HxAttr.SYNC.value] = (
            f"{element}:{HxSyncStrategy[strategy].value if strategy in HxSyncStrategy else strategy}"
        )
        return self

    def render(
        self,
        as_string=True,
    ) -> str | dict[str, str]:
        """Renders the configuration as HTML or an attribute dictionary.

        Assembles internal AJAX dictionaries from the parent `Ajax` class 
        before finalizing the output.

        Args:
            as_string: If True and no `element_tag` exists, returns a 
                formatted attribute string. If False, returns the raw dict.

        Returns:
            The rendered HTML element string, an attribute string, or 
            the attribute dictionary.
        """
        if self.AJAX_HX_DICT:
            self.hx_attrs.update(self.AJAX_HX_DICT)
        if self.element_tag:
            return (
                EL.set_attrs(**self.hx_attrs).set_content(self.content)
                .custom_element(
                    self.element_tag,
                )
                .element
            )
        if as_string:
            return f" {r(self.element_tag, self.hx_attrs)}"
        else:
            return self.hx_attrs

class HTMX:
    """
    The 'Bucket' or Registry for HTMX configurations.
    Holds multiple HTMXElement configurations by name for reuse across templates.

    This acts as a central store for your application's interactive behaviors,
    allowing you to define HTMX logic in one place and inject it into various
    components or templates by name.

    Args:
        use_cdn (bool, optional): If True, provides the HTMX CDN script tag via get_script_tag(). Defaults to True.
        local_path (str, optional): Path to local HTMX script if use_cdn is False.
        **htmx_elemets (HTMXElement): Named HTMXElement instances passed as keyword arguments.

    Example:
        >>> btn = HTMXElement("button","click me!!", hx_post="/save")
        >>> bucket = HTMX(save_btn=btn)
        >>> print(bucket.elements.get("save_btn").render())
        <button hx-post="/save">click me!!</button>
    """

    def __init__(
        self,
        use_cdn: bool = True,
        local_path: Optional[str] = None,
        **htmx_elemets: dict[str, HTMXElement],
    ):
        """Initializes the registry and configures the HTMX library source.

        Args:
            use_cdn: If True, uses the official HTMX CDN URL.
            local_path: Optional file path to a local `htmx.min.js`.
            **htmx_elemets: Named keyword arguments of HTMXElement instances.
        """
        self.elements = htmx_elemets
        self.script_tag = self.get_script_tag(use_cdn, local_path)

    def get_script_tag(self, use_cdn: bool = True, local_path: Optional[str] = None):
        """Generates the `script` tag required to load the HTMX library.

        Args:
            use_cdn: Whether to target the remote CDN.
            local_path: Local fallback path if CDN is not used.

        Returns:
            A script element instance (e.g., `Srpt`) configured with the correct source.
        """
        src = HTMX_CDN_URL if use_cdn else (local_path or LOCAL_TEMPO_PATH)
        return Srpt(src=src)

    def include(self, **htmx_elemets: dict[str, str]):
        """Bulk updates the registry with new named HTMX configurations.

        Args:
            **htmx_elemets: Keyword arguments mapping names to HTMXElements.

        Returns:
            The HTMX instance for method chaining.
        """
        self.elements.update(htmx_elemets)
        return self

    def add(self, element, value):
        """Adds or overwrites a single named configuration in the registry.

        Args:
            element: The unique name/key for the configuration.
            value: The HTMXElement instance to store.

        Returns:
            The HTMX instance for method chaining.
        """
        self.elements[element] = value
        return self

    def render(self, element=None, all_elements=False, as_string=True):
        """Renders registered configurations into HTML or retrieves the object.

        Args:
            element: The name of a specific configuration to render.
            all_elements: If True, renders every item in the registry 
                concatenated into a single string.
            as_string: If True, returns the rendered HTML string; 
                otherwise, returns the `HTMXElement` object.

        Returns:
            The rendered HTML string, the HTMXElement object, or None 
            if the key is not found.
        """
        if all_elements:
            return "".join([el.render() for el in self.elements.values()])
        el = self.elements.get(element, None)
        if el:
            return el.render() if as_string else el
        else:
            return el
