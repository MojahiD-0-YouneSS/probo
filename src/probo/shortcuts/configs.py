from probo.components.forms.probo_form import ProboFormField
from probo.components.state.props import StateProps  # 1
from probo.components.component import Component  # 1
from probo.components.tag_functions.self_closing import doctype  # 1
from probo.styles.plain_css import CssRule  # 1

from typing import Dict, List, Any, Union, Optional

from dataclasses import dataclass, field

import uuid

@dataclass
class ElementStateConfig:
    """Defines the stateful configuration for an individual element within a component.

    This configuration object acts as a schema for elements that require 
    state tracking, data binding, or conditional rendering. It separates 
    static properties from dynamic state behaviors, allowing ProboUI 
    to manage element transitions efficiently.

    Attributes:
        tag (str): The HTML tag name (e.g., 'div', 'button').
        config_id (str): A unique identifier for this specific configuration. 
            Automatically generated and prefixed with the tag name.
        s_state (str): Static state identifier or CSS class string.
        d_state (str): Dynamic state identifier, often used for reactive updates.
        c_state (str): Custom or conditional state identifier.
        is_custom (bool): Flag indicating if the element uses a non-standard 
            custom implementation.
        props (StateProps): An instance of StateProps for handling 
            component-level data.
        bind_to (str): The name of the property or data key this element 
            is synchronized with.
        i_state (bool): Initial state flag (e.g., is this the default view?).
        hide_dynamic (bool): If True, prevents the rendering of dynamic 
            content for this element.
        is_void_element (bool): Indicates if the element is self-closing (e.g., <br>).
        attrs (Dict[str, Any]): A dictionary of standard HTML attributes.
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
    """Configures the 'Brain' of a component by defining its data and logic schema.

    This dataclass acts as a central registry for all data used to hydrate a 
    component's elements. It categorizes data by its mutability (Static vs. 
    Dynamic) and enforces structural integrity through validation flags.

    Attributes:
        s_data (Dict[str, Any]): Static data dictionary. Contains values that 
            remain constant throughout the component's lifecycle.
        d_data (Dict[str, Any]): Dynamic data dictionary. Contains reactive 
            values typically updated via user interaction or AJAX.
        props (Dict[str, Any]): External properties passed into the component, 
            often sourced from `RequestProps`.
        elements_state_config (List[ElementStateConfig]): A list of element-level 
            blueprints that this state configuration will be applied to.
        strict (bool): If True, the compiler should raise an error if an 
            element tries to bind to a key that doesn't exist in the data.
        require_props (bool): If True, the component will fail to initialize 
            unless the `props` dictionary is populated.
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
    """Configures the 'Skin' of a component, managing CSS rules and framework integration.

    This dataclass provides a pluggable interface for styling, supporting raw 
    CSS rules, JIT (Just-In-Time) styling, and utility classes from frameworks 
    like Bootstrap 5. It distinguishes between component-wide rules and 
    overrides applied specifically to the root element.

    Attributes:
        css (Union[Dict, List[CssRule]]): A collection of CSS rules. Can be 
            passed as a dictionary of selectors/properties or a list of 
            `CssRule` objects for JIT injection.
        root_css (Dict[str, str]): Inline styles or specific property 
            overrides applied directly to the component's root HTML element.
        root_bs5_classes (List[str]): A list of Bootstrap 5 utility classes 
            (e.g., ['container', 'mt-5', 'shadow-sm']) to be automatically 
            appended to the root element's class attribute.
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
    """The master configuration blueprint for a ProboUI Component.

    This dataclass uses composition to aggregate state, style, and structural 
    definitions into a single object. It serves as the primary input for 
    factory functions that 'compile' these configurations into renderable 
    component instances.

    Attributes:
        name (str): The unique identifier for the component (e.g., 'UserCard').
        template (str): The raw HTML or Probo-template string used as the 
            base layout.
        state_config (StateConfig): The 'Brain' of the component, defining 
            static/dynamic data and element-level state mappings.
        style_config (StyleConfig): The 'Skin' of the component, handling 
            CSS rules, Bootstrap classes, and root overrides.
        children (Dict[str, Any]): A registry of child components or elements 
            mapped to named slots within the template.
        props (Dict[str, Any]): External data passed from a parent context 
            or request to hydrate the component.
        root_element (Optional[str]): The HTML tag used for the component's 
            outermost wrapper (e.g., 'section', 'div').
        root_attrs (Dict[str, str]): A dictionary of HTML attributes 
            applied directly to the root element.
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
    """Configures SEO and Social Media metadata for a page or component.

    This dataclass manages standard search engine directives (description, 
    keywords, robots) alongside Open Graph (OG) and Twitter Card protocols. 
    It ensures that the resulting HTML `<head>` is optimized for both search 
    engine crawlers and social media link previews.

    Attributes:
        accept_seo_attrs (bool): Class-level flag to enable/disable SEO processing.
        description (str): A brief summary of the page content (max ~160 chars).
        keywords (List[str]): A list of search terms relevant to the content.
        canonical_url (Optional[str]): The preferred URL for this page to 
            prevent duplicate content issues.
        robots (str): Instructions for crawlers (e.g., "index, follow", "noindex").
        og_title (Optional[str]): The title as it should appear in Open Graph 
            previews. Defaults to the page title if not set.
        og_type (str): The type of object (e.g., "website", "article", "book").
        og_url (Optional[str]): The canonical URL used as the ID for the 
            social graph.
        og_image (Optional[str]): URL of the image to display in social shares.
        og_site_name (Optional[str]): The name of the overall website.
        twitter_card (str): The type of Twitter card (e.g., "summary", 
            "summary_large_image").
        twitter_site (Optional[str]): The Twitter handle of the website 
            (e.g., "@ProboUI").
        twitter_creator (Optional[str]): The Twitter handle of the 
            content creator.
    """
    accept_seo_attrs=True
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
    """Configures the structural and metadata requirements of the HTML <head>.

    This dataclass aggregates essential page-level configurations, including 
    character encoding, viewport settings, and assets (CSS/JS). It uses 
    composition to include SEO-specific metadata, allowing for a decoupled 
    management of technical head tags and marketing/search meta tags.

    Attributes:
        title (str): The text displayed in the browser tab and search results.
        charset (str): The character encoding for the document (default "UTF-8").
        viewport (str): Configuration for responsive design and mobile scaling.
        seo (Optional[SEOConfig]): An optional instance of SEOConfig for advanced 
            meta and social media tags.
        css_links (List[str]): A list of URLs for external stylesheets.
        js_scripts (List[str]): A list of URLs for external JavaScript files.
        extra_meta (Dict[str, str]): A dictionary for any additional meta tags 
            not covered by standard SEO (e.g., theme-color, author).
    """
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
    """The root configuration for assembling a complete HTML document.

    This dataclass acts as the top-level manifest for the ProboUI compiler. 
    It defines the global document properties (language, doctype) and 
    orchestrates the relationship between page metadata and the structural 
    layout of the body.

    Attributes:
        head_config (HeadConfig): Configuration for title, meta tags, SEO, 
            and external assets.
        body (Union[str, Component, ComponentConfig]): The primary content 
            of the page. Accepts a raw HTML string, an instantiated 
            `Component` object, or a `ComponentConfig` blueprint for compilation.
        layout_config (Union[LayoutConfig, SemanticLayoutConfig]): Defines the 
            structural wrapper or grid system the body will be injected into.
        lang (str): The language attribute for the `<html>` tag (default "en").
        doc_type_func (str): The function or string used to generate the 
            document type declaration (defaulting to the `doctype` utility).
    """

    head_config: HeadConfig = field(default_factory=HeadConfig)

    # The body content. Can be a string, a Component, or a ComponentConfig
    body: Union[str, Component, ComponentConfig] = ""
    layout_config: Union["LayoutConfig", "SemanticLayoutConfig"] = ""
    lang: str = "en"
    doc_type_func: str = doctype

@dataclass
class XmlConfig:
    """Configures the structure and properties for XML data generation and feeds.

    This dataclass defines the schema for an XML node or a full document. It 
    supports custom root tags, attributes, and content types, including the 
    ability to wrap data in CDATA blocks for safe transmission of reserved 
    characters.

    Attributes:
        root_tag (str): The name of the XML element (e.g., 'item', 'rss', 'url').
        attributes (Dict[str, str]): A mapping of attribute names to their 
            values for the root tag.
        content (Any): The internal data of the element. Supports raw strings, 
            lists of child `XmlConfig` instances, or dictionaries for 
            automated tree conversion.
        declaration (str): The XML prolog/header specifying the version and 
            encoding. Defaults to version 1.0 UTF-8.
        is_cdata (bool): If True, wraps the content within a <![CDATA[ ]]> 
            block to prevent parser errors with special characters.
    """

    root_tag: str
    attributes: Dict[str, str] = field(default_factory=dict)
    content: Any = ""  # Can be string, list of Elements, or Dict (for auto-conversion)

    # XML Specifics
    declaration: str = '<?xml version="1.0" encoding="UTF-8"?>'
    is_cdata: bool = False  # Wrap content in <![CDATA[...]]>

@dataclass
class ListConfig:
    """Configures the automated rendering of repeated data collections.

    This dataclass abstracts the logic required to iterate over a data source 
     and wrap each rendered item within a container. It replaces manual 
    template loops with a declarative structure, improving readability and 
    maintainability of collection-based components.

    Attributes:
        items (list): The raw data collection to be iterated over (e.g., a 
            list of dicts or objects).
        wrapper_tag (str): The HTML element used to wrap the entire collection 
            (e.g., 'ul' for lists, 'div' for grids). Defaults to "div".
        wrapper_attrs (Dict[str, str]): HTML attributes applied to the 
            wrapper element.
        item_renderer (Optional[Callable[[Any], Any]]): A function or 
            component factory that takes a single item from `items` and 
            returns a renderable object or string.
    """

    items: list  # The data source
    wrapper_tag: str = "div"  # e.g., 'ul', 'div'
    wrapper_attrs: Dict[str, str] = field(default_factory=dict)

    # The Renderer: A function that takes an item and returns an Element/String
    item_renderer: Any = None

@dataclass
class FormConfig:
    """Configures HTML forms by bridging backend data with UI representation.

    This dataclass supports two operational modes: 
    1. **Django Mode**: Uses a Django request and Form class to auto-generate 
       fields and validation state.
    2. **Manual Mode**: Uses a list of `ProboFormField` instances for custom, 
       non-framework-specific form construction.

    Attributes:
        action (str): The URL where the form data will be submitted.
        method (str): The HTTP method for submission (default "post").
        request (Any): Optional Django request object used for CSRF and 
            data binding.
        form_class (Any): Optional Django Form or ModelForm class.
        fields (List[ProboFormField]): A collection of field configurations. 
            In manual mode, these define the inputs.
        csrf_token (Optional[str]): A manual CSRF token string if not using 
            the Django request object.
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
    """Configures a reusable structural skeleton for page layouts.

    This dataclass defines the 'slots' (named regions) of a page, such as 
    headers, footers, and sidebars. It allows for a standardized wrapping 
    strategy for the main content and provides default values for regions 
    to ensure structural integrity during partial renders or HTMX swaps.

    Attributes:
        layout_slots (List[str]): A list of named identifiers representing 
            available regions in the layout (e.g., ['header', 'footer', 'sidebar']).
        wrapper_tag (str): The HTML element used to encase the primary 
            page content. Defaults to "main".
        wrapper_attrs (Dict[str, str]): HTML attributes (id, class, style) 
            applied to the main content wrapper.
        wrapper_index (int): The positional index of the main content 
            within the overall document flow relative to other slots.
        defaults (Dict[str, Any]): Fallback content (strings or Components) 
            to render if a specific slot is not populated during a request.
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
    """Configures a page layout using explicit HTML5 semantic regions.

    This dataclass prioritizes document outline integrity by providing 
    dedicated slots for standard semantic tags. It allows for the 
    organization of content into headers, footers, and sidebars, while 
    offering flexible registries for multiple sections and articles.

    Attributes:
        header (Optional[Any]): Content for the <header> region.
        footer (Optional[Any]): Content for the <footer> region.
        sidebar (Optional[Any]): Content for the <aside> or sidebar region.
        sections (Dict[str, Any]): A mapping of content to be wrapped in 
            <section> tags, keyed by section ID or name.
        articles (Dict[str, Any]): A mapping of content to be wrapped in 
            <article> tags, perfect for blog posts or recipe cards.
        wrapper_tag (str): The HTML element used for the main content area. 
            Defaults to "main".
        wrapper_attrs (Dict[str, str]): HTML attributes (id, class) applied 
            to the main content wrapper.
        defaults (Dict[str, Any]): Fallback content to be used if the 
            primary slots are not populated.
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
    """Configures the automated rendering of data grids and tables.

    This dataclass acts as the blueprint for `Flow.datatable`, mapping raw 
    data collections to structured HTML tables. It supports column 
    selection, CSS styling for framework integration (like Bootstrap), 
    and the injection of row-level action components (e.g., buttons).

    Attributes:
        columns (List[str]): The specific keys from the data dictionary to 
            be displayed as table headers and columns.
        data (List[Dict]): The raw data source, typically a list of 
            dictionaries or objects whose keys match the `columns` list.
        table_class (str): CSS classes applied to the table tag. Defaults 
            to "table table-striped" for Bootstrap 5 compatibility.
        actions (List[Any]): A list of renderable components (e.g., Edit, 
            Delete buttons) to be appended to each row.
    """

    columns: List[str]  # Keys to display
    data: List[Dict]  # List of dicts or objects
    table_class: str = "table table-striped"
    actions: List[Any] = field(default_factory=list)  # Edit/Delete buttons

@dataclass
class ThemeConfig:
    """Configures the global design tokens and CSS variables for the application.

    This dataclass acts as a registry for 'Flow.theme' settings. It aggregates 
    design tokens like primary colors, font stacks, and base spacing units, 
    which are typically compiled into CSS custom properties (:root variables) 
    to ensure visual consistency across all components.

    Attributes:
        colors (Dict[str, str]): A mapping of semantic color names to their 
            values (e.g., {'primary': '#007bff', 'accent': '#ffc107'}).
        typography (Dict[str, str]): Configuration for font families, sizes, 
            and weights (e.g., {'base-font': 'Inter, sans-serif'}).
        spacing (str): The base unit for the layout's spacing scale (e.g., 
            '0.25rem' or '4px').
    """

    colors: Dict[str, str] = field(default_factory=dict)
    typography: Dict[str, str] = field(default_factory=dict)
    spacing: str = "0.25rem"
    dark_mode_overrides: Dict[str, str] = field(default_factory=dict)

    breakpoints: Dict[str, str] = field(default_factory=lambda: {
        "sm": "576px", "md": "768px", "lg": "992px", "xl": "1200px"
    })
    z_index: Dict[str, int] = field(default_factory=lambda: {
        "modal": 1050, "sticky": 1020, "overlay": 1000
    })
    shadows: Dict[str, str] = field(default_factory=dict)
    border_radius: str = "0.5rem"