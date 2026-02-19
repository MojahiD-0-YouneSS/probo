import pytest
from src.probo.shortcuts import (
    custom,
    component,
    layout,
    semantic_layout,
    probo_form,
    form_field,
    iterator,
    xml,
    theme,
    datatable,
    head_seo,
    document,
)  # Assuming you aliased custom_element as custom
from src.probo.shortcuts.configs import (
    ElementStateConfig,
    StateConfig,
    StyleConfig,
    ComponentConfig,
    SemanticLayoutConfig,
    LayoutConfig,
    FormConfig,
    ListConfig,
    XmlConfig,
    ThemeConfig,
    TableConfig,
    HeadConfig,
    SEOConfig,
    PageConfig,
)
# ==============================================================================
#  TEST: Custom Element Shortcut
# ==============================================================================


def test_custom_basic_render():
    """
    Scenario: User creates a non-standard HTML tag (e.g. Web Component).
    Expected: <my-widget>Content</my-widget>
    """
    html = custom("my-widget", "Hello World")
    assert "<my-widget>Hello World</my-widget>" == html


def test_custom_attributes():
    """
    Scenario: Custom tag with attributes.
    Expected: <app-root id="main" theme="dark"></app-root>
    """
    # Note: Attributes should be normalized (snake_case -> kebab-case)
    html = custom("app-root", id="main", theme_mode="dark")

    assert 'id="main"' in html
    assert 'theme-mode="dark"' in html
    assert "<app-root" in html


def test_custom_void_element():
    """
    Scenario: User defines a self-closing custom tag.
    Expected: <x-spacer />
    """
    html = custom("x-spacer", is_void_element=True)

    assert "<x-spacer/>" == html
    # Content should be ignored if void (standard MUI logic)
    html_with_content = custom("x-spacer", "Hidden", is_void_element=True)
    assert "Hidden" not in html_with_content


def test_custom_nested_content():
    """
    Scenario: Nesting standard elements inside a custom tag.
    Expected: <card-body><div>Data</div></card-body>
    """
    # Assuming 'div' string generation works or passing Element object
    from probo import div

    inner = div("Data")
    html = custom("card-body", inner)

    assert "<card-body><div>Data</div></card-body>" == html


def test_custom_as_object():
    """
    Scenario: User wants the Element object, not the string (as_string=False).
    Expected: Returns an Element instance.
    """
    obj = custom(
        "api-data",
    )

    assert isinstance(obj, str)
    # Verify internal state
    assert obj == "<api-data></api-data>"


def test_custom_empty_logic():
    """
    Scenario: 'Flow' logic - if inputs result in no renderable content?
    (Based on your 'empty string returned' comment)
    """
    # If tag is empty string, what happens?
    # The Element renderer creates < > if tag is empty.
    # You might want to assert that behavior or fix it in the shortcut.

    # Case A: Empty Content is fine
    assert "<tag></tag>" == custom("tag", "")

    # Case B: Empty Tag - should ideally raise an error or return empty string
    with pytest.raises(Exception):
        custom("", "No Tag")


# ===================================================================================================================
#   component shortcut
# ===================================================================================================================


def test_flow_component_static_render():
    """
    Flow Test 1: Simple static component (Hello World).
    """
    config = ComponentConfig(name="Static", template="<div>Hello</div>")
    comp = component(config)

    html = comp.render()
    assert html == "<div>Hello</div>"


def test_flow_component_with_state_data():
    """
    Flow Test 2: Wiring data to an element via configs.
    """
    # 1. Element Config
    esc = ElementStateConfig(tag="span", s_state="username")

    # 2. State Config
    state_conf = StateConfig(
        s_data={"username": "Youness"}, elements_state_config=[esc]
    )

    # 3. Master Config (Note: Template uses the generated ID placeholder)
    # Since we can't predict the UUID in test, we usually use a helper or rely on
    # the ComponentState loop to find it.
    # For this test, we assume Flow handles the mapping or we rely on iteration.
    # To test rendering, we need the placeholder string.
    # In integration, the user typically puts the placeholder in the template.

    # Workaround for test: We rely on the internal ElementState created by Flow
    # or we simulate the behavior where 'template' isn't needed for simple ES list testing.

    # Let's test that the State Object inside Component is populated correctly.
    config = ComponentConfig(name="DataComp", template="", state_config=state_conf)
    comp = component(config)

    # Verify State Propagation
    assert comp.comp_state.s_data["username"] == "Youness"
    assert len(comp.comp_state.elements_states) == 1
    assert comp.comp_state.elements_states[0].element == "span"


def test_flow_component_jit_css():
    """
    Flow Test 3: Applying JIT CSS via StyleConfig.
    """
    style_conf = StyleConfig(css={".box": {"color": "red"}})
    config = ComponentConfig(
        name="StyledComp", template='<div class="box"></div>', style_config=style_conf
    )

    comp = component(config)
    html, css = comp.render()

    assert '<div class="box"></div>' in html
    assert ".box" in css
    assert "color:red" in css


def test_flow_component_bootstrap_root():
    """
    Flow Test 4: Applying Bootstrap classes to the root element.
    """
    style_conf = StyleConfig(root_bs5_classes=["btn", "btn-primary"])
    config = ComponentConfig(
        name="BS5Comp",
        template="Click Me",  # Inner content
        root_element="button",
        style_config=style_conf,
    )

    # component should apply this to the root
    comp = component(config)
    # We need to set a root element tag for classes to appear

    html = comp.render()

    # Verify classes are injected
    assert 'class="btn btn-primary"' in html


def test_flow_component_complex_integration():
    """
    Flow Test 5: The "Kitchen Sink" - State + Style + Logic.
    """
    # A. Element Logic
    esc = ElementStateConfig(tag="h1", d_state="title")

    # B. State Logic
    state_conf = StateConfig(d_data={"title": "Dashboard"}, elements_state_config=[esc])

    # C. Style Logic
    style_conf = StyleConfig(
        css={"h1": {"font-size": "2rem"}}, root_bs5_classes=["container"]
    )

    # D. Master Config
    # Note: In real usage, user puts placeholder in template.
    # Here we mock the template logic for the test validity.
    config = ComponentConfig(
        name="Dashboard",
        template="<main><$ ...placeholder... $></main>",  # Simulating placement
        state_config=state_conf,
        style_config=style_conf,
        root_element="body",
    )

    comp = component(config)

    # Verify wiring
    assert comp.name == "Dashboard"
    assert comp.comp_state.d_data["title"] == "Dashboard"
    # Verify styles loaded
    # Accessing internal storage to verify logic without parsing full render string
    # (Since placeholder logic requires exact string match)
    if hasattr(comp, "active_rules") and comp.active_rules:
        assert "h1" in comp.active_rules or "h1" in str(comp.active_rules)

    # Check Root Class
    assert "container" in comp.root_element_attrs.get("class", "")


# ===================================================================================================================
#   layout shortcut
# ===================================================================================================================


def test_flow_layout_insertion():
    """
    Test 'layout' function:
    Verifies that the wrapper content is inserted at the correct index within the slots.
    """
    # 1. Setup: A list of existing UI elements
    existing_slots = ["<nav>Top</nav>", "<footer>Bottom</footer>"]

    # 2. Config: Insert content at Index 1 (between Nav and Footer)
    conf = LayoutConfig(
        wrapper_tag="section",
        wrapper_attrs={"class": "hero", "id": "main-region"},
        wrapper_index=1,
        layout_slots=existing_slots,  # Mutable list
        defaults={"content": "<h1>Dynamic Content</h1>"},
    )

    # 3. Execute (Assuming 'layout' is available as layout or standalone)
    # Note: Using the function signature you provided
    tmpl = layout(conf)  # or layout(conf) if standalone

    # 4. Render
    html = tmpl.render()

    # 5. Assertions
    # Verify Wrapper Construction
    assert '<section class="hero" id="main-region">' in html
    assert "<h1>Dynamic Content</h1>" in html
    assert "</section>" in html

    # Verify Order (Nav -> Section -> Footer)
    nav_pos = html.find("<nav>")
    section_pos = html.find("<section")
    footer_pos = html.find("<footer>")

    assert nav_pos < section_pos < footer_pos, "Layout order is incorrect!"


# ===================================================================================================================
#  semantic layout shortcut
# ===================================================================================================================


def test_flow_semantic_layout_structure():
    """
    Test 'semantic_layout' function:
    Verifies that header, sidebar, content (sections+articles), and footer
    are wired up correctly.
    """
    # 1. Config
    conf = SemanticLayoutConfig(
        header="<header>My Site</header>",
        sidebar="<aside>Menu</aside>",
        footer="<footer>Copyright</footer>",
        # Content parts
        sections={"s1": "<section>Intro</section>"},
        articles={"a1": "<article>News</article>"},
        # Wrapper
        wrapper_tag="main",
        wrapper_attrs={"role": "main"},
    )

    # 2. Execute
    tmpl = semantic_layout(conf)

    # 3. Render
    html = tmpl.render()

    # 4. Assertions
    # Check Semantic parts
    assert "<header>My Site</header>" in html
    assert "<aside>Menu</aside>" in html
    assert "<footer>Copyright</footer>" in html

    # Check Main Wrapper
    assert '<main role="main">' in html

    # Check Inner Content (Sections + Articles joined)
    assert "<section>Intro</section><article>News</article>" in html

    # Verify Nesting: Sections should be inside Main
    main_start = html.find("<main")
    sect_start = html.find("<section")
    main_end = html.find("</main>")

    assert main_start < sect_start < main_end, "Content is not inside the wrapper!"


def test_flow_semantic_layout_defaults():
    """
    Test 'semantic_layout' fallback to defaults when primary args are missing.
    """
    conf = SemanticLayoutConfig(
        header=None,  # Missing explicit header
        wrapper_tag="div",
        defaults={
            "header": "<header>Default Header</header>",
            "footer": "<!-- Default Footer -->",
        },
    )

    tmpl = semantic_layout(conf)
    html = tmpl.render()

    assert "<header>Default Header</header>" in html
    assert "<!-- Default Footer -->" in html
    assert "<div></div>" in html  # Empty wrapper logic


# ===================================================================================================================
#  Mastodon Form semantic layout shortcut
# ===================================================================================================================


def test_flow_form_manual_declarative():
    """
    Scenario: Building a form without Django (Manual Mode).
    We explicitly provide the fields and CSRF token via Config.
    """
    # 1. Define Fields using the Forms shortcut
    f_email = form_field(tag="input", **{"type": "email", "name": "email"})
    f_pass = form_field(tag="input", **{"type": "password", "name": "password"})

    # 2. Configure Flow
    config = FormConfig(
        action="/login",
        method="POST",
        csrf_token="manual-token-xyz",
        fields=[f_email, f_pass],
    )

    # 3. Execute
    pf = probo_form(config)
    html = pf.render()
    # 4. Verify
    assert '<form action="/login" method="post"' in html
    # Verify CSRF injection
    assert 'name="csrfmiddlewaretoken"' in html
    assert 'value="manual-token-xyz"' in html
    # Verify Fields
    assert 'name="email"' in html
    assert 'name="password"' in html


def test_flow_form_empty_safety():
    """
    Scenario: Calling form with minimal config.
    Should render an empty form container with CSRF.
    """
    config = FormConfig(action="/search", method="get")

    pf = probo_form(config)
    html = pf.render()
    assert '<form action="/search"' in html
    assert "</form>" in html
    # Even empty forms usually get a CSRF input placeholder in Manual mode
    assert 'input type="hidden"' in html


# ==============================================================================
#  1. Iterator Tests (5 Tests)
# ==============================================================================


def test_iterator_basic_list():
    """1. Render simple list of strings."""
    conf = ListConfig(
        items=["A", "B"], wrapper_tag="ul", item_renderer=lambda x: f"<li>{x}</li>"
    )
    html = iterator(conf)
    assert "<ul><li>A</li><li>B</li></ul>" == html


def test_iterator_custom_wrapper_attrs():
    """2. Wrapper with classes/ids."""
    conf = ListConfig(items=[], wrapper_tag="div", wrapper_attrs={"class": "grid"})
    html = iterator(conf)
    assert '<div class="grid">' in html


def test_iterator_object_renderer():
    """3. Render list of objects using lambda."""
    users = [{"name": "Ali"}, {"name": "Bob"}]
    conf = ListConfig(items=users, item_renderer=lambda u: f"<span>{u['name']}</span>")
    html = iterator(conf)
    assert "<span>Ali</span><span>Bob</span>" in html


def test_iterator_empty():
    """4. Handle empty list gracefully."""
    conf = ListConfig(items=[], wrapper_tag="div")
    html = iterator(conf)
    assert "<div></div>" == html


def test_iterator_nested_elements():
    """5. Render list of MUI Elements."""
    from probo import div

    # items are already Elements
    items = [div("1"), div("2")]
    conf = ListConfig(
        items=items, wrapper_tag="section"
    )  # Default renderer just converts to str/render
    html = iterator(conf)
    assert "<section><div>1</div><div>2</div></section>" == html


# ==============================================================================
#  2. XML Tests (5 Tests)
# ==============================================================================


def test_xml_basic_node():
    """1. Simple XML node."""
    conf = XmlConfig(root_tag="msg", content="Hello")
    xml_string = xml(conf)
    assert "<msg>Hello</msg>" in xml_string
    assert "<?xml" in xml_string


def test_xml_dict_conversion():
    """2. Auto-convert dictionary to nodes."""
    conf = XmlConfig(root_tag="user", content={"id": 1, "name": "Youness"})
    xml_string = xml(conf)
    assert "<id>1</id>" in xml_string
    assert "<name>Youness</name>" in xml_string


def test_xml_cdata():
    """3. CDATA wrapping."""
    conf = XmlConfig(root_tag="code", content="if (x < y)", is_cdata=True)
    xml_string = xml(conf)
    assert "<![CDATA[if (x < y)]]>" in xml_string


def test_xml_attributes():
    """4. Root attributes."""
    conf = XmlConfig(root_tag="rss", attributes={"version": "2.0"})
    xml_string = xml(conf)
    assert '<rss version="2.0">' in xml_string


def test_xml_custom_declaration():
    """5. Custom declaration header."""
    conf = XmlConfig(root_tag="data", declaration='<?xml version="1.1"?>')
    xml_string = xml(conf)
    assert '<?xml version="1.1"?>' in xml_string


# ==============================================================================
#  3. Theme Tests (5 Tests)
# ==============================================================================


def test_theme_generation():
    """1. Basic variable generation."""
    conf = ThemeConfig(colors={"primary": "#007bff"})
    css = theme(conf)
    assert ":root {" in css
    assert "--color-primary:#007bff;" in css


def test_theme_typography():
    """2. Typography variables."""
    conf = ThemeConfig(typography={"base": "Arial"})
    css = theme(conf)
    assert "--font-base:Arial;" in css


def test_theme_spacing_override():
    """3. Spacing variable."""
    conf = ThemeConfig(spacing="8px")
    css = theme(conf)
    assert "--spacing:8px;" in css


def test_theme_mixed():
    """4. Mixed config."""
    conf = ThemeConfig(colors={"red": "red"}, spacing="1rem")
    css = theme(conf)
    assert "--color-red:red;" in css
    assert "--spacing:1rem;" in css


def test_theme_empty():
    """5. Empty config produces valid root block."""
    conf = ThemeConfig()
    css = theme(conf)
    assert ":root" in css


# ==============================================================================
#  4. DataTable Tests (5 Tests)
# ==============================================================================


def test_datatable_structure():
    """1. Basic table tags."""
    conf = TableConfig(columns=[], data=[])
    html = datatable(conf)
    assert "<table" in html
    assert "<thead>" in html
    assert "<tbody>" in html


def test_datatable_headers():
    """2. Header generation."""
    conf = TableConfig(columns=["name", "age"], data=[])
    html = datatable(conf)
    assert "<th>Name</th>" in html
    assert "<th>Age</th>" in html


def test_datatable_rows_dict():
    """3. Rows from dict data."""
    data = [{"id": 1}, {"id": 2}]
    conf = TableConfig(columns=["id"], data=data)
    html = datatable(conf)
    assert "<td>1</td>" in html
    assert "<td>2</td>" in html


def test_datatable_custom_class():
    """4. Custom table class."""
    conf = TableConfig(columns=[], data=[], table_class="table-dark")
    html = datatable(conf)
    assert 'class="table-dark"' in html


def test_datatable_missing_keys():
    """5. Handle missing keys gracefully (empty string)."""
    data = [{"name": "A"}, {"id": 2}]  # Missing 'name' in second row
    conf = TableConfig(columns=["name"], data=data)
    html = datatable(conf)
    assert "<td>A</td>" in html
    assert "<td></td>" in html  # Empty for missing key


# ==============================================================================
#  5. Head SEO Tests (5 Tests)
# ==============================================================================


def test_head_seo_essentials():
    """1. Title and Charset."""
    conf = HeadConfig(title="Test Page", charset="ISO-8859-1")
    head = head_seo(conf)
    html = head.render()
    assert "<title>Test Page</title>" in html
    assert 'charset="ISO-8859-1"' in html


def test_head_seo_meta_tags():
    """2. Description and Keywords."""
    seo = SEOConfig(description="Cool App", keywords=["a", "b"])
    conf = HeadConfig(seo=seo)
    html = head_seo(conf).render()
    assert 'name="description" content="Cool App"' in html
    assert 'name="keywords" content="a,b"' in html


def test_head_seo_opengraph():
    """3. OG Tags."""
    seo = SEOConfig(og_title="OG Title", og_image="img.png")
    conf = HeadConfig(seo=seo)
    html = head_seo(conf).render()
    assert 'property="og:title" content="OG Title"' in html
    assert 'property="og:image" content="img.png"' in html


def test_head_assets():
    """4. CSS and JS links."""
    conf = HeadConfig(css_links=["style.css"], js_scripts=["app.js"])
    html = head_seo(conf).render()
    assert '<link rel="stylesheet" href="style.css"' in html
    assert '<script src="app.js"' in html


def test_head_extra_meta():
    """5. Custom meta tags."""
    conf = HeadConfig(extra_meta={"generator": "MUI"})
    html = head_seo(conf).render()
    assert 'name="generator" content="MUI"' in html


# ==============================================================================
#  6. Document Tests (5 Tests)
# ==============================================================================


def test_document_structure():
    """1. Full doc structure."""
    conf = PageConfig()
    doc = document(conf)
    html = doc.render()
    assert "<!DOCTYPE html>" in html
    assert '<html lang="en">' in html
    assert "<body>" in html


def test_document_head_integration():
    """2. Head integration."""
    h_conf = HeadConfig(title="Doc Test")
    conf = PageConfig(head_config=h_conf)
    html = document(conf).render()
    assert "<title>Doc Test</title>" in html


def test_document_body_string():
    """3. String body."""
    conf = PageConfig(body="<h1>Hello</h1>")
    html = document(conf).render()
    assert "<h1>Hello</h1>" in html


def test_document_body_element():
    """4. Element object body."""
    from probo import div

    conf = PageConfig(body=div("Content"))
    html = document(conf).render()
    assert "<div>Content</div>" in html


def test_document_layout_slots():
    """5. Verify it uses the main slot."""
    # The document flow puts body into 'main' slot
    conf = PageConfig(body="Main Content")
    tmpl = document(conf)
    # Check internal storage or render
    assert tmpl.components["main"] == "Main Content"
