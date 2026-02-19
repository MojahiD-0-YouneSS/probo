from probo.styles.frameworks.bs5.components.navbar import BS5NavBar


# ==============================================================================
#  BS5NavBar Tests
# ==============================================================================

def test_bs5_navbar_render_basic_structure():
    """1. Render basic navbar container."""
    # Usage: BS5NavBar("Item 1", "Item 2", id="main-nav")
    nav = BS5NavBar(id="main-nav")
    nav.add_navbar_brand('hello',)
    html = nav.render()

    # It should render a <nav> with class navbar
    assert '<nav' in html
    assert 'class="navbar"' in html
    assert 'id="main-nav"' in html
    # Usually wraps content in container-fluid
    assert 'container-fluid' in html


def test_bs5_navbar_brand():
    """2. Render navbar with a brand element."""
    nav = BS5NavBar()

    # Add Brand (defaults to div, but often 'a')
    nav.add_navbar_brand("MyBrand", tag='a', href="/")

    html = nav.render()

    assert '<a href="/"' in html
    assert 'class="navbar-brand"' in html
    assert 'MyBrand' in html


def test_bs5_navbar_text():
    """3. Render navbar text."""
    nav = BS5NavBar()

    nav.add_navbar_text("Signed in as User")

    html = nav.render()

    assert '<span class="navbar-text">' in html
    assert 'Signed in as User' in html


def test_bs5_navbar_custom_theme():
    """4. Render with theme classes (dark mode, background)."""
    # Helper attributes often passed to init
    nav = BS5NavBar(Class="navbar-dark bg-primary")

    html = nav.render()

    assert 'navbar-dark' in html
    assert 'bg-primary' in html


def test_bs5_navbar_state_blocking():
    """5. State: Navbar hidden when constraints not met."""
    nav = BS5NavBar(
        render_constraints={"show_nav": True}
    )
    nav.add_navbar_brand("Hidden Brand")

    # Render with False -> Hidden
    html = nav.render(override_props={"show_nav": False})

    assert not html


def test_bs5_navbar_state_passing():
    """6. State: Navbar visible when constraints met."""
    nav = BS5NavBar(
        render_constraints={"is_active": True}
    )
    nav.add_navbar_brand("Visible Brand")
    nav.include_env_props(is_active=True,)
    # Render with True -> Visible
    html = nav.render()

    assert "navbar" in html
    assert "Visible Brand" in html