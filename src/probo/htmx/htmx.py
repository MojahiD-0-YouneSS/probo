from src.probo.components.tag_functions import script as Srpt
from typing import Dict, Any, Optional, List
from src.probo.htmx.htmx_enum import (
    HxAttr,
    HxBoolValue,
    HxSwap,
    HxTrigger,
    HxParams,
    HxSyncStrategy,
)
from src.probo.components.elements import Element
from src.probo.utility import render_attributes as r

HTMX_CDN_URL = "https://unpkg.com/htmx.org@1.9.10"

LOCAL_TEMPO_PATH = "/static/js/htmx.min.js"


class Ajax:
    """Helper to build HTMX AJAX attributes"""

    def __init__(
        self,
    ):
        self.AJAX_HX_DICT = dict()

    def hx_get(self, url: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.GET.value] = url
        return self

    def hx_post(self, url: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.POST.value] = url
        return self

    def hx_put(self, url: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.PUT.value] = url
        return self

    def hx_patch(self, url: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.PATCH.value] = url
        return self

    def hx_delete(self, url: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.DELETE.value] = url
        return self

    def hx_target(self, selector: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.TARGET.value] = selector
        return self

    def hx_trigger(self, trigger_str: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.TRIGGER.value] = trigger_str
        return self

    def hx_swap(self, swap_str: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.SWAP.value] = swap_str
        return self

    def hx_indicator(self, selector: str) -> Dict[str, str]:
        self.AJAX_HX_DICT[HxAttr.INDICATOR.value] = selector
        return self

    def get_values(self):
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
        """
        :param use_cdn: Use CDN link or local script path
        :param local_path: Path to local `htmx.min.js` if not using CDN
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
            if element not in template_info.get("tags", []):
                raise ValueError("elemet not in tag")

    def set_attr(self, **attrs) -> "HTMXElement":
        for attribute, value in attrs.items():
            try:
                attr_name = HxAttr[attribute.upper()].value
            except:
                attr_name = attribute
            self.hx_attrs[attr_name] = value
        return self

    def get_attr(self, attribute: str) -> Any:
        attr_name = self.hx_attrs.get(attribute, None)
        return attr_name

    def del_attr(self, attribute: str) -> "HTMXElement":
        self.hx_attrs.pop(attribute, None)
        return self

    def build_trigger_string(
        self,
        event: str,
        modifiers: Optional[Dict[str, str]] = None,
        filters: Optional[List[str]] = None,
    ) -> "HTMXElement":
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
        base = HxSwap[name].value if name in HxSwap else name
        parts = [base]
        if modifiers:
            parts.extend(f"{k}:{v}" for k, v in modifiers.items())
        self.hx_attrs[HxAttr.SWAP.value] = " ".join(parts)
        return self

    def build_sync_string(self, element: str, strategy: str) -> "HTMXElement":
        self.hx_attrs[HxAttr.SYNC.value] = (
            f"{element}:{HxSyncStrategy[strategy].value if strategy in HxSyncStrategy else strategy}"
        )
        return self

    def render(
        self,
        as_string=True,
    ) -> str | dict[str, str]:
        if self.AJAX_HX_DICT:
            self.hx_attrs.update(self.AJAX_HX_DICT)
        if self.element_tag:
            return (
                Element(content=self.content, **self.hx_attrs)
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
        self.elements = htmx_elemets
        self.script_tag = self.get_script_tag(use_cdn, local_path)

    def get_script_tag(self, use_cdn: bool = True, local_path: Optional[str] = None):
        """Return a script element for HTMX JS"""
        src = HTMX_CDN_URL if use_cdn else (local_path or LOCAL_TEMPO_PATH)
        return Srpt(src=src)

    def include(self, **htmx_elemets: dict[str, str]):
        self.elements.update(htmx_elemets)
        return self

    def add(self, element, value):
        self.elements[element] = value
        return self

    def render(self, element=None, all_elements=False, as_string=True):
        if all_elements:
            return "".join([el.render() for el in self.elements.values()])
        el = self.elements.get(element, None)
        if el:
            return el.render() if as_string else el
        else:
            return el
