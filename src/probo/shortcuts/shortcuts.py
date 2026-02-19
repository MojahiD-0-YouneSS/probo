from probo.components.forms.probo_form import (
    ProboForm,
    ProboFormField,
)  # 3
from probo.components.state.component_state import (
    ComponentState,
)  # 2
from probo.components.component import (
    Component,
)  # 1
from probo.components.elements import (
    Element,
    Head,
    Template,
)  # 3
from probo.request.transformer import (
    RequestDataTransformer,
)  # 2) # 2
from probo.styles.plain_css import (
    CssRule,
)  # 8
from probo.context.context_logic import loop

from probo.shortcuts.configs import (
    ComponentConfig,
    HeadConfig,
    PageConfig,
    XmlConfig,
    ListConfig,
    FormConfig,
    LayoutConfig,
    TableConfig,
    ThemeConfig,
    SemanticLayoutConfig,
    StateConfig,
    SEOConfig,
    StyleConfig,
    ElementStateConfig,
)  # 17
from probo.shortcuts.shortcuts_utils import (
    make_es_from_esc,
)


def custom(tag: str, content: str = "", is_void_element: bool = False, **attrs) -> str:
    """Instantly creates and renders a custom HTML tag string.

    This utility serves as a functional shortcut for the `Element` factory, 
    bypassing the need for manual instantiation and method chaining. It is 
    ideal for generating simple, non-stateful HTML fragments or for use 
    within list comprehensions where immediate string output is required.

    Args:
        tag: The HTML tag name (e.g., 'section', 'my-web-component').
        content: The inner HTML or text content for the element.
        is_void_element: If True, renders the tag as a self-closing element 
            (e.g., <tag />).
        **attrs: Arbitrary keyword arguments to be converted into HTML 
            attributes (e.g., class_='active', id='main').

    Returns:
        str: The fully rendered HTML string.
    """
    return (
        Element()
        .custom_element(tag, content=content, is_void_element=is_void_element, **attrs)
        .stringify_element()
        .element
    )

def set_data(*variables) -> str:
    """Instantly injects data variables into an element and renders it to a string.

    This utility serves as a functional shortcut for the `Element.set_data` 
    pipeline. It allows for the rapid association of data-heavy attributes 
    or internal state variables with an HTML fragment, immediately 
    outputting the final string representation.

    Args:
        *variables: A variable number of data points, dictionaries, or 
            objects to be bound to the element's data attributes or context.

    Returns:
        str: The fully rendered HTML string containing the injected data.
    """
    return Element().set_data(*variables).stringify_element().element

def form_field(tag, **kwargs) -> ProboFormField:
    """A functional factory for creating ProboFormField instances.

    This utility simplifies the creation of form field configurations by 
    wrapping the `ProboFormField` constructor. It allows for a declarative 
    definition of HTML inputs, textareas, and selects while mapping arbitrary 
    keyword arguments directly to field attributes.

    Args:
        tag (str): The HTML tag name or type of the field (e.g., 'input', 
            'textarea', 'select').
        **kwargs: Additional attributes and configurations for the field, 
            such as `type`, `name`, `label`, `value`, or `class_`.

    Returns:
        ProboFormField: A structural blueprint of the form field ready 
            to be processed by a FormHandler or Component.
    """
    return ProboFormField(tag_name=tag, **kwargs)

def component(config: ComponentConfig) -> Component:
    """The master factory function for instantiating ProboUI Components.

    This function acts as the primary 'compiler' in the ProboUI pipeline. It 
    consumes a `ComponentConfig` blueprint and performs the following 
    orchestration:
    1. Initializes a `Component` instance with the provided identity (name).
    2. Hydrates the component's internal tree using the `StateConfig`.
    3. Applies visual rules defined in the `StyleConfig`.
    4. Registers children and incoming properties for rendering.

    Args:
        config (ComponentConfig): The comprehensive configuration object 
            containing the template, state, style, and child elements.

    Returns:
        Component: A live component object ready to be rendered to an 
            HTML string or manipulated by the framework.
    """
    # 1. Build State (The Brain)
    # We unpack the specific StateConfig dataclass
    es_list = list()
    for esc in config.state_config.elements_state_config:
        es = make_es_from_esc(esc)
        es_list.append(es)
        config.template = config.template.replace(esc.config_id, es.placeholder)

    state_obj = ComponentState(
        *es_list,  # ElementStates are passed as *args to CS
        s_data=config.state_config.s_data,
        d_data=config.state_config.d_data,
        strict=config.state_config.strict,
        # require_props_definition=config.state_config.require_props,
        **config.state_config.props,
    )

    # 2. Initialize Component (The Structure)
    comp = Component(
        name=config.name,
        template=str(config.template),
        state=state_obj,
        *config.children,
        **config.props,
    )

    # 3. Apply Styles (The Skin)
    style_conf = config.style_config

    # A. JIT CSS Rules
    if style_conf.css:
        # change_skin handles dicts or lists of rules automatically
        comp.load_css_rules(**style_conf.css)

    # B. Root Element Styles (kwargs)
    if style_conf.root_css:
        comp.change_skin(root_css=style_conf.root_css)

    # C. Bootstrap 5 Classes
    if style_conf.root_bs5_classes:
        bs5_string = " ".join(style_conf.root_bs5_classes)
        current = config.root_attrs.get("class", "")
        config.root_attrs["class"] = f"{current} {bs5_string}".strip()
    if config.root_element:
        comp.set_root_element(config.root_element, **config.root_attrs)

    return comp

def layout(config: LayoutConfig) -> Template:
    """Transforms a layout configuration into a renderable Template engine.

    This function acts as the high-level orchestrator for page structure. It 
    consumes a `LayoutConfig` to define the structural boundaries (slots) 
    of a page and returns a `Template` instance. This instance is responsible 
    for injecting specific component content into the defined layout 
    regions during the final render pass.

    Args:
        config (LayoutConfig): The structural blueprint defining wrapper tags, 
            attribute metadata, and named content slots.

    Returns:
        Template: A document-level object prepared to receive body content 
            and global metadata for full HTML generation.
    """
    wrapper_tag = config.wrapper_tag
    wrapper_attrs = config.wrapper_attrs
    wrapper_index = config.wrapper_index

    # Default content for slots if not provided during swap
    defaults = config.defaults
    content = custom(wrapper_tag, "".join(defaults.values()), **wrapper_attrs)
    if len(config.layout_slots) > wrapper_index:
        config.layout_slots.insert(wrapper_index, content)

    template_slots = {
        "layout_slots": (config.layout_slots),
    }
    return Template(separator="\n", **template_slots)

def semantic_layout(config: SemanticLayoutConfig) -> Template:
    """Orchestrates a Template instance based on HTML5 semantic regions.

    This utility functions as a specialized compiler for structural layouts. 
    It maps the explicit regions defined in a `SemanticLayoutConfig` (header, 
    footer, aside, sections) into a `Template` object. This ensures that 
    the final document follows a logical outline, improving accessibility 
    and search engine visibility.

    Args:
        config (SemanticLayoutConfig): The blueprint defining specific 
            semantic slots and their corresponding wrapper attributes.

    Returns:
        Template: A document-level engine initialized with semantic regions, 
            ready to accept page-specific content.
    """
    header = config.header
    footer = config.footer
    sidebar = config.sidebar

    sections = "".join(config.sections.values())
    articles = "".join(config.articles.values())

    # The main content wrapper configuration
    # e.g. <main id="content"> or <div class="container">
    wrapper_tag = config.wrapper_tag
    wrapper_attrs = config.wrapper_attrs

    # Default content for slots if not provided during swap
    defaults = config.defaults
    content = custom(wrapper_tag, sections + articles, **wrapper_attrs)
    template_slots = {
        "header": header or defaults.get("header", ""),
        "sidebar": sidebar or defaults.get("sidebar", ""),
        "content": content,
        "footer": footer or defaults.get("footer", ""),
    }
    return Template(separator="\n", **template_slots)

def probo_form(config: FormConfig) -> ProboForm:
    """Compiles a FormConfig into a functional ProboForm instance.

    This factory function serves as the constructor for the framework's form 
    handling system. It processes the configuration to determine the source 
    of truth for the fields (Django vs. Manual) and initializes a `ProboForm` 
    object capable of rendering itself, handling CSRF protection, and 
    interfacing with HTMX for partial updates.

    Args:
        config (FormConfig): The configuration object containing field 
            definitions, action/method metadata, and optional Django 
            integration hooks.

    Returns:
        ProboForm: A live form object ready to be rendered as HTML or 
            passed to a FormHandler for server-side processing.
    """
    if config.request and config.form_class:
        rdt = RequestDataTransformer(config.request, config.form_class)
        mf = ProboForm(config.action, request_data=rdt, method=config.method)
    else:
        mf = ProboForm(
            config.action,
            *config.fields,
            method=config.method,
            manual=True,
            csrf_token=config.csrf_token,
        )
    return mf

def iterator(config: ListConfig) -> str:
    """Compiles a ListConfig into a single, wrapped HTML string.

    This utility serves as the execution engine for repeated elements. It 
    iterates through the provided data source, applies the `item_renderer` 
    to each item, and assembles the results into a structured HTML fragment 
    defined by the configuration's wrapper tag and attributes.

    Args:
        config (ListConfig): The configuration blueprint containing the 
            items, the rendering function, and the wrapper metadata.

    Returns:
        str: A fully rendered HTML string representing the entire collection.
    """
    rendered = loop(config.items, config.item_renderer)

    content = "".join(r.render() if hasattr(r, "render") else str(r) for r in rendered)

    return custom(config.wrapper_tag, content, **config.wrapper_attrs)

def xml(config: XmlConfig) -> str:
    """Compiles an XmlConfig blueprint into a valid XML string.

    This utility serves as the execution engine for XML generation. It 
    recursively processes the `content` of the configuration—handling raw 
    strings, lists of child nodes, or dictionaries—and applies the 
    appropriate XML declaration and CDATA wrapping as specified.

    Args:
        config (XmlConfig): The blueprint defining the root tag, attributes, 
            content structure, and XML-specific directives.

    Returns:
        str: A fully formatted XML string, including the prolog/declaration 
            and any necessary CDATA sections.
    """
    content = config.content

    # Auto-convert Dict to XML nodes
    if isinstance(content, dict):
        content = "".join(custom(k, str(v)) for k, v in content.items())

    # Wrap in CDATA if requested
    if config.is_cdata:
        content = f"<![CDATA[{content}]]>"

    root = custom(config.root_tag, content, **config.attributes)
    return f"{config.declaration}\n{root}"

def theme(config: ThemeConfig) -> str:
    """Compiles a ThemeConfig blueprint into a CSS variable block.

    This utility serves as the design-to-code translator for ProboUI. It 
    iterates through the colors, typography, and spacing tokens defined 
    in the configuration and formats them into standard CSS custom properties 
    (variables) typically wrapped in a `:root` selector.

    Args:
        config (ThemeConfig): The configuration blueprint containing 
            semantic colors, font stacks, and spacing units.

    Returns:
        str: A string of CSS variables ready to be injected into a 
            `style` tag within the document `head`.
    """

    css_vars = {}
    for k, v in config.colors.items():
        css_vars[f"--color-{k}"] = v

    for k, v in config.typography.items():
        css_vars[f"--font-{k}"] = v

    if config.spacing:
        css_vars["--spacing"] = config.spacing

    # Return the rendered CSS rule string
    return f":root {CssRule(**css_vars).render()}"

def datatable(config: TableConfig) -> str:
    """Compiles a TableConfig blueprint into a fully formatted HTML table string.

    This utility serves as the execution engine for data grids. It iterates 
    through the `columns` to build the table header, then processes the 
    `data` list to generate rows. It also handles the injection of 
    row-level actions (like buttons or links) and applies framework-specific 
    CSS classes.

    Args:
        config (TableConfig): The configuration blueprint containing column 
            definitions, raw data, CSS classes, and action components.

    Returns:
        str: A fully rendered HTML <table> string ready for inclusion 
            in a component or page.
    """
    # Header
    th_str = "".join(f"<th>{col.title()}</th>" for col in config.columns)
    thead = f"<thead><tr>{th_str}</tr></thead>"

    # Body
    rows = []
    for row in config.data:
        # Handle dict access or object attribute access
        td_str = ""
        for col in config.columns:
            val = row.get(col, "") if isinstance(row, dict) else getattr(row, col, "")
            td_str += f"<td>{val}</td>"
        rows.append(f"<tr>{td_str}</tr>")

    tbody = f"<tbody>{''.join(rows)}</tbody>"

    return f'<table class="{config.table_class}">{thead}{tbody}</table>'

def head_seo(config: HeadConfig) -> Head:
    """Compiles a HeadConfig blueprint into a functional Head object.

    This factory function serves as the central hub for document-level 
    metadata. It processes the configuration to initialize a `Head` instance 
    that manages:
    1. SEO essentials (Title, Description, Keywords).
    2. Social Graph tags (OpenGraph, Twitter Cards).
    3. Resource linking (Stylesheets, Scripts, Favicons).
    4. Character encoding and Viewport settings.

    Args:
        config (HeadConfig): The declarative blueprint containing 
            all metadata and external asset references.

    Returns:
        Head: A live Head object capable of stringifying into a 
            valid HTML <head> block.
    """

    head = Head()

    # 1. Essentials
    head.set_title(config.title)
    head.register_meta(charset=config.charset)
    head.register_meta(name="viewport", content=config.viewport)

    # 2. SEO Config (If present)
    if config.seo:
        s = config.seo
        if s.description:
            head.register_meta(name="description", content=s.description,probo_custom_attrs=s.accept_seo_attrs)
        if s.keywords:
            head.register_meta(name="keywords", content=",".join(s.keywords),probo_custom_attrs=s.accept_seo_attrs)
        if s.canonical_url:
            head.register_link(rel="canonical", href=s.canonical_url,probo_custom_attrs=s.accept_seo_attrs)
        if s.robots:
            head.register_meta(name="robots", content=s.robots,probo_custom_attrs=s.accept_seo_attrs)

        # Social (Open Graph)
        if s.og_title:
            head.register_meta(property="og:title", content=s.og_title,probo_custom_attrs=s.accept_seo_attrs)
        if s.og_type:
            head.register_meta(property="og:type", content=s.og_type,probo_custom_attrs=s.accept_seo_attrs)
        if s.og_image:
            head.register_meta(property="og:image", content=s.og_image,probo_custom_attrs=s.accept_seo_attrs)

        # Twitter
        if s.twitter_card:
            head.register_meta(name="twitter:card", content=s.twitter_card,probo_custom_attrs=s.accept_seo_attrs)
        if s.twitter_creator:
            head.register_meta(name="twitter:creator", content=s.twitter_creator,probo_custom_attrs=s.accept_seo_attrs)

    # 3. Assets
    for css in config.css_links:
        head.register_link(rel="stylesheet", href=css)
    for js in config.js_scripts:
        head.register_script(src=js, defer=True)

    # 4. Extra Meta
    for name, content in config.extra_meta.items():
        head.register_meta(name=name, content=content)

    return head

def document(config: PageConfig) -> Template:
    """The master orchestrator that compiles a PageConfig into a full HTML Template.

    This function represents the final stage of the ProboUI compilation 
    pipeline. It integrates all sub-configurations (Head, Theme, Layout, 
    and Components) into a cohesive Template instance. It is the primary 
    entry point for generating complete, production-ready web documents.

    Args:
        config (PageConfig): The root configuration object containing the 
            entire state and structure of the page.

    Returns:
        Template: A fully hydrated document engine ready to be stringified 
            into the final HTML response.
    """
    # 1. Build Head
    head_obj = head_seo(config.head_config)

    # 2. Prepare Body
    # If body is a Component or Config, render it to string/html
    body_content = config.body
    if hasattr(body_content, "render"):
        body_content = body_content.render()[0]

    # 3. Assemble Template
    # We use a standard layout where 'main' is the body slot
    slots = {"main": body_content}

    # If PageConfig has layout info (optional future expansion), handle here
    # For now, standard document structure

    tmpl = Template(separator="\n", **slots)
    tmpl.head = head_obj

    return tmpl
