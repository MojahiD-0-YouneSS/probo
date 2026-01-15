from probo.styles.frameworks.bs5.components.nav import BS5Nav

# ==============================================================================
#  BS5Nav Tests
# ==============================================================================

def test_bs5_nav_render_basic():
    """1. Render basic nav structure."""
    # Usage: BS5Nav("Link 1", "Link 2", ...)
    nav = BS5Nav(id="main-nav")

    # Add items manually to test API
    nav.add_nav_item("Link 1")
    nav.add_nav_link("Active Link", active=True, href="#",)

    html = nav.render()

    # Base class
    assert '<ul id="main-nav" class="nav"' in html or '<nav class="nav"' in html
    assert 'id="main-nav"' in html

    # Item check
    assert '<li class="nav-item">Link 1</li>' in html

    # Active Link check
    assert '<a href="#" aria-current="page" class="nav-link active"' in html
    assert 'aria-current="page"' in html # Standard BS5 for active links

def test_bs5_nav_render_variants():
    """2. Render Tabs and Pills variants."""
    # Tabs
    tabs = BS5Nav(is_tab=True)
    assert "nav-tabs" in tabs.render()

    # Pills
    pills = BS5Nav(is_pill=True)
    assert "nav-pills" in pills.render()

    # Fill/Justified
    fill = BS5Nav(is_fill=True)
    assert "nav-fill" in fill.render()

def test_bs5_nav_render_vertical():
    """3. Render vertical layout (flex-column)."""
    nav = BS5Nav(Class="flex-column")
    html = nav.render()

    assert "flex-column" in html

def test_bs5_nav_fluent_links():
    """4. Render using add_nav_link shortcut."""
    nav = BS5Nav()
    nav.add_nav_link("Home", href="/")
    nav.add_nav_link("Disabled", Class='disabled')

    html = nav.render()

    assert '<a href="/" class="nav-link">Home</a>' in html
    assert 'class="nav-link disabled"' in html
    assert 'aria-disabled="true"' in html