from probo.styles.frameworks.bs5.components.tooltips import BS5Tooltips


# ==============================================================================
#  BS5Tooltips Tests
# ==============================================================================

def test_bs5_tooltip_render_basic():
    """1. Render basic tooltip trigger button."""
    # Usage: BS5Tooltips(content="Hover Me", title="Tooltip Text")
    tt = BS5Tooltips(content="Hover Me", title="Tooltip Text", id="tt1")
    html = tt.render()

    assert '<button' in html
    assert 'data-bs-toggle="tooltip"' in html
    assert 'title="Tooltip Text"' in html
    assert 'Hover Me' in html
    assert 'id="tt1"' in html


def test_bs5_tooltip_render_placement():
    """2. Render with specific placement (bottom/left/right)."""
    tt = BS5Tooltips(content="Info", title="Help", placement="left")
    html = tt.render()

    assert 'data-bs-placement="left"' in html


def test_bs5_tooltip_render_custom_tag():
    """3. Render on a link (<a>) instead of button."""
    tt = BS5Tooltips(
        content="Link",
        title="Go home",
        tag="a",
        href="/home",
        Class="text-decoration-none"
    )
    html = tt.render()

    assert '<a data-bs-toggle="tooltip" data-bs-placement="top" title="Go home" href="/home"' in html
    assert 'class="text-decoration-none"' in html
    # Should NOT have type="button" for anchor
    assert 'type="button"' not in html


def test_bs5_tooltip_render_html_title():
    """4. Render with HTML content in title (requires data-bs-html="true")."""
    tt = BS5Tooltips(
        content="HTML Tip",
        title="<em>Italic</em>",
        data_bs_html="true"
    )
    html = tt.render()

    assert 'data-bs-html="true"' in html
    assert 'title="<em>Italic</em>"' in html


def test_bs5_tooltip_state_blocking():
    """5. State: Tooltip trigger hidden when constraints not met."""
    tt = BS5Tooltips(
        content="Secret",
        title="Info",
        render_constraints={"is_admin": True}
    )
    tt.include_env_props(is_active=False)
    # Render with False -> Hidden
    html = tt.render()

    assert not html


def test_bs5_tooltip_state_passing():
    """6. State: Tooltip trigger visible when constraints met."""
    tt = BS5Tooltips(
        content="Public",
        title="Info",
        render_constraints={"is_active": True}
    )
    tt.include_env_props(is_active=True)
    # Render with True -> Visible
    html = tt.render()

    assert "data-bs-toggle" in html
    assert "Public" in html