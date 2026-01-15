from probo.styles.frameworks.bs5.components.scrollspy import BS5Scrollspy


# ==============================================================================
#  BS5Scrollspy Tests
# ==============================================================================

def test_bs5_scrollspy_render_basic():
    """1. Render basic scrollspy container attached to a target nav."""
    # Usage: BS5Scrollspy(target="#navbar-example")
    spy = BS5Scrollspy(target="#my-nav", id="scroll-container")
    html = spy.render()

    assert 'data-bs-spy="scroll"' in html
    assert 'data-bs-target="#my-nav"' in html
    assert 'id="scroll-container"' in html
    # Usually has position relative and overflow
    # Note: Styles might be applied via class or style attr depending on impl.
    # We check the critical data attributes.


def test_bs5_scrollspy_add_items():
    """2. Render scrollspy with content sections."""
    spy = BS5Scrollspy(target="#list-example")

    # Add sections linked to nav
    spy.add_scrollpy_item(item_id="list-item-1", content="Section 1 Content", tag="h4")
    spy.add_scrollpy_item(item_id="list-item-2", content="Section 2 Content", tag="p")

    html = spy.render()

    # Check Section 1
    assert '<h4 id="list-item-1">' in html
    assert 'Section 1 Content' in html

    # Check Section 2
    assert '<p id="list-item-2">' in html
    assert 'Section 2 Content' in html


def test_bs5_scrollspy_custom_attributes():
    """3. Render with custom scrollspy options (offset, method)."""
    spy = BS5Scrollspy(
        target="#navbar",
        data_bs_offset="0",
        data_bs_smooth_scroll="true",
        tabindex="0"
    )
    html = spy.render()

    assert 'data-bs-offset="0"' in html
    assert 'data-bs-smooth-scroll="true"' in html
    assert 'tabindex="0"' in html


def test_bs5_scrollspy_item_structure():
    """4. Verify structure of added items with classes."""
    spy = BS5Scrollspy(target="#nav")
    spy.add_scrollpy_item(
        item_id="section1",
        content="Detail",
        tag="div",
        Class="p-3"
    )

    html = spy.render()
    assert '<div id="section1" class="p-3">' in html
    assert 'Detail' in html


def test_bs5_scrollspy_state_blocking():
    """5. State: Scrollspy hidden when constraints not met."""
    spy = BS5Scrollspy(
        target="#secure-nav",
        render_constraints={"can_view_docs": True}
    )

    # Render with False -> Hidden
    html = spy.render(override_props={"can_view_docs": False})

    assert not html


def test_bs5_scrollspy_state_passing():
    """6. State: Scrollspy visible when constraints met."""
    spy = BS5Scrollspy(
        target="#public-nav",
        render_constraints={"is_active": True}
    )
    spy.include_env_props(is_active=True)
    # Render with True -> Visible
    html = spy.render()

    assert 'data-bs-spy="scroll"' in html
    assert 'data-bs-target="#public-nav"' in html


def test_bs5_scrollspy_nested_nav_target():
    """7. Test scrollspy targeting a nested nav structure."""
    # Scrollspy can target nested navs (nav-pills inside nav)
    spy = BS5Scrollspy(target="#nested-nav", data_bs_root_margin="0px 0px -40%")
    html = spy.render()

    assert 'data-bs-target="#nested-nav"' in html
    assert 'data-bs-root-margin="0px 0px -40%"' in html


def test_bs5_scrollspy_list_group_integration():
    """8. Test scrollspy targeting a list-group (common alternative to nav)."""
    spy = BS5Scrollspy(target="#list-example")
    spy.add_scrollpy_item(item_id="list-item-1", content="...")
    html = spy.render()

    # Should work identically, validation is on the target attribute
    assert 'data-bs-target="#list-example"' in html
    assert 'id="list-item-1"' in html


def test_bs5_scrollspy_smooth_scroll_keyword():
    """9. Verify specific smooth-scroll handling if passed as boolean."""
    spy = BS5Scrollspy(target="#nav", data_bs_smooth_scroll='true')
    html = spy.render()

    # Check if it converted kwarg to data attribute
    assert 'data-bs-smooth-scroll="true"' in html


def test_bs5_scrollspy_method_offset():
    """10. Verify explicit method configuration (position vs offset)."""
    spy = BS5Scrollspy(target="#nav", data_bs_method="offset")
    html = spy.render()

    assert 'data-bs-method="offset"' in html