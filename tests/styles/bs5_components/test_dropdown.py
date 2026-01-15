from probo.styles.frameworks.bs5.components.dropdown import BS5Dropdown


# ==============================================================================
#  BS5Dropdown Tests
# ==============================================================================

def test_bs5_dropdown_render_basic_structure():
    """1. Render basic dropdown structure with button and menu."""
    dd = BS5Dropdown(id="dropdown-container")

    # Add Trigger Button
    dd.add_btn(content="Dropdown Button", id="dropdownMenuButton1")

    # Add Menu Items
    dd.add_menu(
        '<a class="dropdown-item" href="#">Action</a>',
        '<a class="dropdown-item" href="#">Another action</a>'
    )

    html = dd.render()

    # Container
    assert '<div id="dropdown-container" class="dropdown"' in html

    # Button
    assert '<button' in html
    assert 'class="dropdown-toggle"' in html
    assert 'data-bs-toggle="dropdown"' in html
    assert 'Dropdown Button' in html

    # Menu
    assert '<ul class="dropdown-menu"' in html
    assert 'Action' in html
    assert 'Another action' in html


def test_bs5_dropdown_button_customization():
    """2. Render dropdown button with custom classes/attributes."""
    dd = BS5Dropdown()

    # Customizing the button (e.g. secondary variant, large size)
    dd.add_btn(
        content="Options",
        Class="btn btn-secondary btn-lg",
        type="button"
    )

    html = dd.render()

    assert 'class="dropdown-toggle btn btn-secondary btn-lg"' in html
    assert 'type="button"' in html
    assert 'Options' in html


def test_bs5_dropdown_menu_attributes():
    """3. Render dropdown menu with custom attributes (e.g. dark mode)."""
    dd = BS5Dropdown()
    dd.add_btn("Menu")

    # Customizing the menu (ul)
    dd.add_menu(
        '<li><a class="dropdown-item" href="#">Item</a></li>',
        Class="dropdown-menu-dark",
        aria_labelledby="dropdownMenuButton"
    )

    html = dd.render()

    assert 'class="dropdown-menu dropdown-menu-dark"' in html
    assert 'aria-labelledby="dropdownMenuButton"' in html
    assert 'Item' in html


def test_bs5_dropdown_direction_classes():
    """4. Render dropdown with specific direction classes on root."""
    # Example: Dropup or Dropend
    dd = BS5Dropdown(is_btn_group=True,Class="dropup")
    dd.add_btn("Dropup")
    dd.add_menu("Item")

    html = dd.render()

    assert 'class="btn-group dropup"' in html
    assert 'Dropup' in html


def test_bs5_dropdown_state_blocking():
    """5. State: Dropdown hidden when constraints not met."""
    dd = BS5Dropdown(
        id="admin-menu",
        render_constraints={"is_admin": True}
    )
    dd.add_btn("Admin Options")

    # Render with False -> Hidden
    html = dd.render(override_props={"is_admin": False})

    assert not html


def test_bs5_dropdown_state_passing():
    """6. State: Dropdown visible when constraints met."""
    dd = BS5Dropdown(
        id="user-menu",
        render_constraints={"is_authenticated": True}
    )
    dd.add_btn("My Profile")

    # Render with True -> Visible
    html = dd.render(override_props={"is_authenticated": True},add_to_global=True)

    assert "dropdown" in html
    assert "My Profile" in html