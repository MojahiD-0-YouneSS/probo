from probo.styles.frameworks.bs5.components import (
    BS5Badge
)


# ==============================================================================
#  BS5Badge Tests
# ==============================================================================

def test_bs5_badge_render_basic():
    """1. Render standard badge with variant."""
    badge = BS5Badge(content="New", variant="secondary")
    html = badge.render()

    assert '<span' in html
    assert 'class="badge bg-secondary"' in html
    assert '>New</span>' in html


def test_bs5_badge_render_pill_and_attrs():
    """2. Render rounded-pill badge with custom attributes."""
    # User adds 'rounded-pill' via Class or manual classes logic in kwargs
    # Assuming BS5Element handles kwargs -> attrs -> class merging Id
    badge = BS5Badge(content="99+", variant="danger", Class="rounded-pill", Id="notif-badge")
    html = badge.render()

    assert 'rounded-pill' in html
    assert 'bg-danger' in html
    assert 'id="notif-badge"' in html


def test_bs5_badge_heading_context():
    """3. Render badge inside a heading (add_heading_badge)."""
    badge = BS5Badge(content="v1.0", variant="primary")

    # Wrap it in H2
    badge.add_heading_badge(heading_content="MUI Release", heading="h2", Class="mt-3")

    html = badge.render()

    # Should render <h2 ...>MUI Release <span ...>v1.0</span></h2>
    assert '<h2' in html
    assert 'class="mt-3"' in html
    assert 'MUI Release' in html
    # Badge is inside
    assert '<span class="badge bg-primary">v1.0</span>' in html


def test_bs5_badge_heading_button():
    """4. Render badge inside a custom tag (e.g. button or h5)."""
    badge = BS5Badge(content="4", variant="light", Class="text-dark")

    # Simulating "Notifications <badge>" inside a button
    badge.add_button_badge(button_content="Notifications", tag="button", type="button", Class="btn btn-primary")

    html = badge.render()

    assert '<button type="button" class="btn btn-primary">' in html
    assert 'Notifications' in html
    assert '<span class="badge bg-light text-dark">4</span>' in html


def test_bs5_badge_state_logic_gate():
    """5. State: Hide badge if 'show_new' prop is False."""
    # Note: Requires base Component to support 'render_constraints' or manually wired StateProps
    # Assuming standard Component behavior where we inject a state object that gates rendering.

    # Manually constructing logic since BS5Badge doesn't expose state args in __init__ yet
    # We use the base Component's mechanism
    props_rule = {'show_new': True}

    badge = BS5Badge("Hidden",render_constraints=props_rule)
    html = badge.render()
    assert 'Hidden' not in html

    html = badge.render(props_rule,add_to_global=True)
    assert 'Hidden' in html