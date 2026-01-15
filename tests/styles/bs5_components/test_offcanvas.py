from probo.styles.frameworks.bs5.components.offcanvas import BS5Offcanvas


# ==============================================================================
#  BS5Offcanvas Tests
# ==============================================================================

def test_bs5_offcanvas_render_basic():
    """1. Render basic offcanvas structure."""
    # Usage: BS5Offcanvas(id="myOffcanvas")
    offcanvas = BS5Offcanvas(id="demoOffcanvas")
    offcanvas.add_offcanvas_header('demo Offcanvas title',Id='demoOffcanvasLabel')
    offcanvas.add_trigger('demoOffcanvas','button',Id='demoOffcanvasLabel')
    html = offcanvas.render()

    assert '<div' in html
    assert 'class="offcanvas offcanvas-start"' in html  # Default position
    assert 'tabindex="-1"' in html
    assert 'id="demoOffcanvas"' in html
    assert 'aria-labelledby="demoOffcanvasLabel"' in html  # Standard accessibility


def test_bs5_offcanvas_render_positions():
    """2. Render different positions (start, end, top, bottom)."""
    # Test End
    off_end = BS5Offcanvas(position="end")
    assert "offcanvas-end" in off_end.render()

    # Test Top
    off_top = BS5Offcanvas(position="top")
    assert "offcanvas-top" in off_top.render()

    # Test Bottom
    off_bottom = BS5Offcanvas(position="bottom")
    assert "offcanvas-bottom" in off_bottom.render()


def test_bs5_offcanvas_header_body():
    """3. Render Header (Title + Close Btn) and Body."""
    offcanvas = BS5Offcanvas(Id="off1")

    # Add Header with Title
    offcanvas.add_offcanvas_header(content="Menu", tag="h5")

    # Add Body
    offcanvas.add_offcanvas_body(content="<p>Nav links here</p>")

    html = offcanvas.render()
    print(html)
    # Header Check
    assert '<div class="offcanvas-header">' in html
    assert '<h5 id="off1Label" class="offcanvas-title">Menu</h5>' in html
    assert 'class="btn-close"' in html  # Should auto-add close button
    assert 'data-bs-dismiss="offcanvas"' in html

    # Body Check
    assert '<div class="offcanvas-body">' in html
    assert '<p>Nav links here</p>' in html


def test_bs5_offcanvas_render_attributes():
    """4. Render with backdrop/scroll attributes."""
    # Enable scrolling, disable backdrop
    offcanvas = BS5Offcanvas(data_bs_scroll="true", data_bs_backdrop="false")
    html = offcanvas.render()

    assert 'data-bs-scroll="true"' in html
    assert 'data-bs-backdrop="false"' in html


def test_bs5_offcanvas_state_blocking():
    """5. State: Offcanvas hidden when constraints not met."""
    offcanvas = BS5Offcanvas(
        id="adminPanel",
        render_constraints={"is_superuser": True}
    )

    # Render with False -> Hidden
    html = offcanvas.render(override_props={"is_superuser": False})

    assert not html


def test_bs5_offcanvas_state_passing():
    """6. State: Offcanvas visible when constraints met."""
    offcanvas = BS5Offcanvas(
        id="userPanel",
        render_constraints={"is_active": True}
    )
    offcanvas.include_env_props(is_active=True)
    # Render with True -> Visible
    html = offcanvas.render()

    assert "offcanvas" in html
    assert "id=\"userPanel\"" in html