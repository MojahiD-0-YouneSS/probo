import pytest
from mui import (
    Component, ComponentState, ElementState, StateProps,
    Template, Head, MastodonForm, MastodonFormField,
    CssRule, CssSelector,
    div, h1, h2, h3, h5, p, a, button, section, header, footer, nav, article, Input, textarea,
    doctype, html, body
)

# ==============================================================================
#  1. SHARED ASSETS (The Theme & Layout)
# ==============================================================================

@pytest.fixture
def shop_theme():
    """
    Defines the global Design System and Layout using Direct API.
    """
    # 1. Global CSS Rules (Manual CssRule objects)
    global_rules = {
        "body":CssRule(font_family="sans-serif", margin="0"),
        ".container":CssRule(max_width="1140px", margin="0 auto", padding="1rem"),
        ".btn":CssRule(display="inline-block", padding="0.5rem 1rem", background="#007bff", color="white"),
        "header":CssRule(background="#343a40", color="white", padding="1rem"),
        "footer":CssRule(background="#f8f9fa", padding="2rem", text_align="center")
    }

    # 2. The Master Layout (Template Object)
    # Replaces Flow.layout
    layout_tmpl = Template(
        separator="\n",
        header=header(
            nav(
                a("Home", href="/"), " | ",
                a("Shop", href="/shop"), " | ",
                a("About", href="/about"), " | ",
                a("Contact", href="/contact")
            )
        ),
        # 'main' is our content slot
        main=div("<!-- Page Content -->", Class="container"), 
        footer=footer("© 2025 Mastodon Shop")
    )
    
    # 3. Inject CSS into Head
    layout_tmpl.head = Head()
    for sel,rule in global_rules.items():
        layout_tmpl.head.register_style(f'{sel}{rule.render()}')

    return layout_tmpl

# ==============================================================================
#  2. PAGE BUILDER HELPER
# ==============================================================================

def render_shop_page(title_text, content, layout_template):
    """
    Assembles the final document using raw HTML tags.
    """
    # 1. Configure Head
    layout_template.head.set_title(f"{title_text} | Mastodon Shop")
    layout_template.head.register_meta(charset="UTF-8")
    
    # 2. Swap Content
    # We render the component/element to string first
    html_content = content.render()[0] if hasattr(content, 'render') else str(content)
    
    # If the content had JIT CSS (tuple return), extract it
    if hasattr(content, 'render'):
        render_res = content.render()
        if isinstance(render_res, tuple):
            html_content, css_content = render_res
            if css_content:
                layout_template.head.register_style(css_content)

    layout_template.swap_component(main=html_content)
    
    # 3. Build Document (Doctype + HTML)
    # Flow.document replaces this manual wrapping:
    return doctype() + html(
        layout_template.head,
        body(layout_template.render()) # Template renders body contents
    )


# ==============================================================================
#  3. TEST SCENARIOS
# ==============================================================================

def test_page_01_home(shop_theme):
    """PAGE 1: HOME (Component + CssRule)"""
    
    # 1. Define Style
    hero_style = {".hero":CssRule( text_align="center", padding="4rem", background="#e9ecef")}
    
    # 2. Define Component
    hero = Component(
        name="Hero",
        template=section(h1("Welcome to Future Commerce"), p("We sell dreams."), Class="hero")
    )
    hero.load_css_rules(**hero_style)
    
    # 3. Render
    full_html = render_shop_page("Home", hero, shop_theme)
    assert "<title>Home | Mastodon Shop</title>" in full_html
    assert "Welcome to Future Commerce" in full_html
    assert ".hero {" in full_html
    assert "text-align:center" in full_html

def test_page_02_about(shop_theme):
    """PAGE 2: ABOUT (Raw Elements)"""
    
    # 1. Build Content using direct tags
    content = article(
        h1("About Us", Class="mb-4"),
        p("We are a team of Python developers building the future of UI."),
        id="about-content"
    )
    
    # 2. Render
    full_html = render_shop_page("About", content, shop_theme)
    
    assert 'id="about-content"' in full_html
    assert "Python developers" in full_html
    assert "<header>" in full_html

def test_page_03_product_listing(shop_theme):
    """PAGE 3: SHOP LISTING (Python Loop)"""
    
    # 1. Data
    products = [
        {'id': 1, 'name': 'Laptop', 'price': 999},
        {'id': 2, 'name': 'Phone', 'price': 599},
    ]

    # 2. Loop Logic (Replaces Flow.iterator)
    cards = []
    for item in products:
        card = div(
            div(
                h3(item['name'], Class="card-title"),
                p(f"${item['price']}", Class="card-text"),
                a("View", href=f"/shop/{item['id']}", Class="btn"),
                Class="card-body"
            ),
            Class="card mb-4 col-md-4"
        )
        cards.append(card)
        
    grid = div(*cards, Class="product-grid row")
    
    # 3. Render
    full_html = render_shop_page("Shop", grid, shop_theme)
    print(full_html)
    assert '<div class="product-grid row">' in full_html
    assert 'Laptop' in full_html
    assert 'Phone' in full_html
    assert 'href="/shop/1"' in full_html

def test_page_04_product_details(shop_theme):
    """PAGE 4: PRODUCT DETAIL (ComponentState + ElementState)"""
    
    # 1. Define Logic Elements
    es_name = ElementState(element='h1', d_state='name')
    es_price = ElementState(element='span', d_state='price', **{'class': 'h3'})
    
    # 2. Component State
    state = ComponentState(
        *[es_name, es_price],# Register elements
        d_data={'name': 'Super Laptop', 'price': '$999.00'},
    )
    
    # 3. HTMX Button (Manual attrs)
    btn = button("Add to Cart", **{'hx-post': '/api/cart/add', 'hx-swap': 'none', 'style': 'background: green'})
    
    # 4. Component
    # Note usage of es.placeholder
    template_str = div(
        es_name.placeholder,
        div("Price: ", es_price.placeholder),
        p("In Stock"),
        btn,
        Class="detail-view"
    )
    
    comp = Component(name="ProductDetail", template=template_str, state=state)
    
    # 5. Render
    full_html = render_shop_page("Super Laptop", comp.render(), shop_theme)
    print(full_html)
    assert "<h1>Super Laptop</h1>" in full_html
    assert "$999.00" in full_html
    assert 'hx-post="/api/cart/add"' in full_html

def test_page_05_contact(shop_theme):
    """PAGE 5: CONTACT (MastodonForm)"""
    
    # 1. Define Fields (MFF)
    f_name = MastodonFormField(tag_name='input', field_name='name', **{'type': 'text', 'placeholder': 'Name'})
    f_msg = MastodonFormField(tag_name='textarea', field_name='message', **{'rows': 5, 'placeholder': 'Msg'})
    
    # 2. Define Form (MF)
    # Passing fields via *args
    form = MastodonForm(
        "/contact/send", 
        f_name, f_msg, 
        method="POST", 
        manual=True, 
        csrf_token="manual-token-x"
    )
    
    # 3. Render
    content = div(
        h2("Get in Touch"),
        form.render(),
        Class="contact-section"
    )
    
    full_html = render_shop_page("Contact", content, shop_theme)
    print(full_html)
    assert 'action="/contact/send"' in full_html
    assert 'name="name"' in full_html
    assert '<textarea' in full_html
    assert 'value="manual-token-x"' in full_html