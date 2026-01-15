from probo.styles.frameworks.bs5.components import (
    BS5Breadcrumb,
)
# ==============================================================================
#  BS5Breadcrumb Tests
# ==============================================================================

def test_bs5_breadcrumb_render_basic():
    """1. Render basic structure with items."""
    # Last item "Data" should be active
    bc = BS5Breadcrumb("Home", "Library", "Data")
    html = bc.render()

    assert '<nav aria-label="breadcrumb">' in html
    assert '<ol class="breadcrumb">' in html

    # Check Inactive Items (Links)
    assert '<li class="breadcrumb-item"><a href="#">Home</a></li>' in html
    assert '<li class="breadcrumb-item"><a href="#">Library</a></li>' in html

    # Check Active Item (No Link, aria-current)
    assert '<li aria-current="page" class="breadcrumb-item active">Data</li>' in html


def test_bs5_breadcrumb_render_custom_links():
    """2. Render with specific URLs (tuples)."""
    bc = BS5Breadcrumb("Details",
        url_dict={"Home": "/","Products": "/shop"},
    )
    html = bc.render()

    assert '<a href="/">' in html
    assert '<a href="/shop">' in html
    assert 'Details' in html

def test_bs5_breadcrumb_render_attrs():
    """4. Render with custom root attributes."""
    bc = BS5Breadcrumb("Home", "Page", Id="my-crumb", Class="bg-light")
    html = bc.render()

    assert 'id="my-crumb"' in html
    assert 'bg-light' in html


def test_bs5_breadcrumb_state_constraints_blocking():
    """5. State: Breadcrumb hidden when constraints not met."""
    # Logic: Only show if 'show_nav' is True
    bc = BS5Breadcrumb("Home", "Admin", render_constraints={"is_admin": True})

    # Render without props -> Should be hidden
    html = bc.render(override_props={"is_admin": False})

    assert not html


def test_bs5_breadcrumb_state_constraints_passing():
    """6. State: Breadcrumb visible when constraints met."""
    bc = BS5Breadcrumb("Home", "Profile", render_constraints={"is_user": True})

    # Render with matching props
    html = bc.render(override_props={"is_user": True},add_to_global=True)

    assert '<nav' in html
    assert 'Profile' in html