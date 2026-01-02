from probo.components.forms.mui_form import ProboFormField
from probo.components.state.props import StateProps  # 1
from probo.components.component import Component  # 1
from probo.components.tag_functions.self_closing import doctype  # 1
from probo.styles.plain_css import CssRule  # 1

from typing import Dict, List, Any, Union, Optional

from dataclasses import dataclass, field

import uuid


@dataclass
class ElementStateConfig:
    """
    Configuration for Individual Elements within a Component.
    """

    tag: str
    config_id: str = field(default_factory=lambda: uuid.uuid4().hex)
    s_state: str = field(default_factory=str)
    d_state: str = field(default_factory=str)
    c_state: str = field(default_factory=str)
    is_custom = False
    props: StateProps = field(default_factory=StateProps)
    bind_to: str = field(default_factory=str)
    i_state = False
    hide_dynamic = False
    is_void_element: bool = False
    attrs: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(
        self,
    ):
        self.config_id = f"{self.tag}=={self.config_id}"


@dataclass
class StateConfig:
    """
    Configures the 'Brain' (Data & Logic).
    """

    s_data: Dict[str, Any] = field(default_factory=dict)
    d_data: Dict[str, Any] = field(default_factory=dict)
    props: Dict[str, Any] = field(default_factory=dict)
    elements_state_config: List[ElementStateConfig] = field(default_factory=list)
    # Flags
    strict: bool = False
    require_props: bool = False


@dataclass
class StyleConfig:
    """
    Configures the 'Skin' (CSS & Frameworks).
    Pluggable: Can handle raw CSS, Theme Lists, or Framework classes.
    """

    # 1. JIT CSS Rules (Dict or List of Rules)
    css: Union[Dict, List[CssRule]] = field(default_factory=dict)

    # 2. Root Element Overrides (Inline styles or specific ID styling)
    root_css: Dict[str, str] = field(default_factory=dict)

    # 3. Bootstrap 5 Support
    # List of classes to auto-append to the root element (e.g. ['card', 'p-3'])
    root_bs5_classes: List[str] = field(default_factory=list)


@dataclass
class ComponentConfig:
    """
    The Master Configuration.
    Defines the Component's Identity, Structure, State, and Style.
    usage:
    from probo.shortcuts import Flow
    from probo.shortcuts.configs import ComponentConfig, StateConfig, StyleConfig, ElementState

    # 1. Define the Config
    card_config = ComponentConfig(
        name="UserCard",
        template="<div id='card'> <$ ... $> </div>",

        # Define Elements & Data
        elements=[ElementState('span', d_state='username')],
        state=StateConfig(
            d_data={'username': 'Youness'},
            strict=True
        ),

        # Define Styles (CSS + Bootstrap)
        style=StyleConfig(
            # Custom JIT CSS
            css={'#card': {'border': '1px solid black'}},
            # Bootstrap Classes for the root
            bs5_classes=['card', 'shadow-sm', 'p-3']
        )
    )

    # 2. Build
    comp = Flow.component(card_config)

    # 3. Render
    # Result: <div id='card' class='card shadow-sm p-3'>...</div>
    # CSS: #card { border: 1px solid black; }
    comp.render()

    This architecture is scalable, type-safe, and supports your specific requirement of mixing JIT CSS with Bootstrap classes seamlessly.
    """

    name: str
    template: str

    # Composition
    state_config: StateConfig = field(default_factory=StateConfig)
    style_config: StyleConfig = field(default_factory=StyleConfig)
    children: Dict[str, Any] = field(
        default_factory=dict
    )  # Child Components or Elements
    props: Dict[str, Any] = field(default_factory=dict)  # Incoming Props
    root_element: str = None  # Default root element tag
    root_attrs: Dict[str, str] = field(default_factory=dict)  # Attributes for root


@dataclass
class SEOConfig:
    """
    Advanced Meta Tags for Social Media (Open Graph, Twitter) and Search.
    """

    # Standard
    description: str = ""
    keywords: List[str] = field(default_factory=list)
    canonical_url: Optional[str] = None
    robots: str = "index, follow"

    # Open Graph (Facebook/LinkedIn)
    og_title: Optional[str] = None  # Defaults to page title if None
    og_type: str = "website"
    og_url: Optional[str] = None
    og_image: Optional[str] = None
    og_site_name: Optional[str] = None

    # Twitter Card
    twitter_card: str = "summary_large_image"
    twitter_site: Optional[str] = None  # @username
    twitter_creator: Optional[str] = None


@dataclass
class HeadConfig:
    title: str = "MUI Page"
    charset: str = "UTF-8"
    viewport: str = "width=device-width, initial-scale=1.0"

    # Composition: SEO is now its own dedicated object
    seo: Optional[SEOConfig] = None

    # Assets
    css_links: List[str] = field(default_factory=list)
    js_scripts: List[str] = field(default_factory=list)
    extra_meta: Dict[str, str] = field(default_factory=dict)


@dataclass
class PageConfig:
    """
    Configuration for a Full HTML Document.
    """

    head_config: HeadConfig = field(default_factory=HeadConfig)

    # The body content. Can be a string, a Component, or a ComponentConfig
    body: Union[str, Component, ComponentConfig] = ""
    layout_config: Union["LayoutConfig", "SemanticLayoutConfig"] = ""
    lang: str = "en"
    doc_type_func: str = doctype


@dataclass
class XmlConfig:
    """
    Configuration for XML Data Labeling / Feeds.
    """

    root_tag: str
    attributes: Dict[str, str] = field(default_factory=dict)
    content: Any = ""  # Can be string, list of Elements, or Dict (for auto-conversion)

    # XML Specifics
    declaration: str = '<?xml version="1.0" encoding="UTF-8"?>'
    is_cdata: bool = False  # Wrap content in <![CDATA[...]]>


@dataclass
class ListConfig:
    """
    Configuration for Repeated Elements (Collections).
    Replaces manual loop() calls.
    """

    items: list  # The data source
    wrapper_tag: str = "div"  # e.g., 'ul', 'div'
    wrapper_attrs: Dict[str, str] = field(default_factory=dict)

    # The Renderer: A function that takes an item and returns an Element/String
    item_renderer: Any = None


@dataclass
class FormConfig:
    """
    Configuration for Forms (Connecting the Bridge).
    """

    action: str = ""
    method: str = "post"

    # Mode A: Django Integration
    request: Any = None  # The Django request object
    form_class: Any = None  # The Django Form Class

    # Mode B: Manual
    fields: list = field(default_factory=list)  # List of ProboFormField
    csrf_token: str = None

    def __on_init__(self):
        if not self.request or not self.form_class:
            # Ensure fields are ProboFormField instances
            self.fields = [
                field if isinstance(field, ProboFormField) else ProboFormField(**field)
                for field in self.fields
            ]


@dataclass
class LayoutConfig:
    """
    Configuration for a Reusable Page Layout.
    Example: A Dashboard Layout with fixed Sidebar and Header.
    """

    # Fixed Regions (Components or HTML strings)
    layout_slots: list[str] = field(default_factory=list)

    # The main content wrapper configuration
    # e.g. <main id="content"> or <div class="container">
    wrapper_tag: str = "main"
    wrapper_attrs: Dict[str, str] = field(default_factory=dict)
    wrapper_index: int = field(default_factory=int)
    # Default content for slots if not provided during swap
    defaults: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SemanticLayoutConfig:
    """
    Configuration for a Reusable Page Layout.
    Example: A Dashboard Layout with fixed Sidebar and Header.
    """

    # Fixed Regions (Components or HTML strings)
    header: Any = None
    footer: Any = None
    sidebar: Any = None

    sections: Dict[str, Any] = field(default_factory=dict)
    articles: Dict[str, Any] = field(default_factory=dict)

    # The main content wrapper configuration
    # e.g. <main id="content"> or <div class="container">
    wrapper_tag: str = "main"
    wrapper_attrs: Dict[str, str] = field(default_factory=dict)

    # Default content for slots if not provided during swap
    defaults: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TableConfig:
    """Config for Flow.datatable."""

    columns: List[str]  # Keys to display
    data: List[Dict]  # List of dicts or objects
    table_class: str = "table table-striped"
    actions: List[Any] = field(default_factory=list)  # Edit/Delete buttons


@dataclass
class ThemeConfig:
    """Config for Flow.theme (CSS Variables)."""

    colors: Dict[str, str] = field(default_factory=dict)
    typography: Dict[str, str] = field(default_factory=dict)
    spacing: str = "0.25rem"
