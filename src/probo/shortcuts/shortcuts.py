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
)  # 17
from probo.shortcuts.shortcuts_utils import (
    make_es_from_esc,
)


def custom(tag: str, content: str = "", is_void_element: bool = False, **attrs) -> str:
    """Creates a custom HTML tag string immediately."""
    return (
        Element()
        .custom_element(tag, content=content, is_void_element=is_void_element, **attrs)
        .stringify_element()
        .element
    )


def set_data(*variables) -> str:
    """Creates a custom HTML tag string immediately."""
    return Element().set_data(*variables).stringify_element().element


def form_field(tag, **kwargs) -> ProboFormField:
    return ProboFormField(tag_name=tag, **kwargs)


def component(config: ComponentConfig) -> Component:
    """
    a shortcut to Builds a Component from a Configuration Object.
    Handles State, Styles (CSS/BS5), and Structure in one pass.
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
        require_props_definition=config.state_config.require_props,
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
    """
    a shortcut Generates a Reusable sementic Layout Template.
    Wires up Header, Footer, Sidebar, and a Main Content Wrapper.
    Returns a Template object ready for .swap_component().
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
    """
    a shortcut Generates a Reusable sementic Layout Template.
    Wires up Header, Footer, Sidebar, and a Main Content Wrapper.
    Returns a Template object ready for .swap_component().
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


def probo_form(config: FormConfig) -> str:
    """a shortcut Builds a Form (Django or Manual)."""
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
    return mf.render()


def iterator(config: ListConfig) -> str:
    """
    shortcut Generates a list of items wrapped in a container.
    """
    rendered = loop(config.items, config.item_renderer)

    content = "".join(r.render() if hasattr(r, "render") else str(r) for r in rendered)

    return custom(config.wrapper_tag, content, **config.wrapper_attrs)


def xml(config: XmlConfig) -> str:
    """
    shortcut to Generates an XML Document or Fragment.
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
    """
    Generates the :root CSS variables block.
    Returns the raw CSS string.
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
    """
    Generates a clean HTML Table.
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
    """
    Constructs a fully populated Head object with SEO metadata.
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
            head.register_meta(name="description", content=s.description)
        if s.keywords:
            head.register_meta(name="keywords", content=",".join(s.keywords))
        if s.canonical_url:
            head.register_link(rel="canonical", href=s.canonical_url)
        if s.robots:
            head.register_meta(name="robots", content=s.robots)

        # Social (Open Graph)
        if s.og_title:
            head.register_meta(property="og:title", content=s.og_title)
        if s.og_type:
            head.register_meta(property="og:type", content=s.og_type)
        if s.og_image:
            head.register_meta(property="og:image", content=s.og_image)

        # Twitter
        if s.twitter_card:
            head.register_meta(name="twitter:card", content=s.twitter_card)
        if s.twitter_creator:
            head.register_meta(name="twitter:creator", content=s.twitter_creator)

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
    """
    Assembles a full HTML Document Template.
    Wires up Head + Body + Layout.
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
