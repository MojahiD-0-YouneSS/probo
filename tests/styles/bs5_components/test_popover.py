from probo.styles.frameworks.bs5.components.popover import BS5Popover


# ==============================================================================
#  BS5Popover Tests
# ==============================================================================

def test_bs5_popover_render_basic():
    """1. Render basic popover trigger button."""
    # Usage: BS5Popover(content="Popover Body Text")
    pop = BS5Popover(content="Help info here", id="pop1")
    html = pop.render()

    assert '<button' in html
    assert 'data-bs-toggle="popover"' in html
    assert 'data-bs-content="Help info here"' in html
    assert 'id="pop1"' in html
    # Default position usually right
    assert 'data-bs-placement="right"' in html


def test_bs5_popover_render_options():
    """2. Render with title, specific position, and custom tag."""
    pop = BS5Popover(
        content="Details",
        href="#",
        title="Info",
        position="top",
        tag="a",

    )
    html = pop.render()

    assert '<a href="#"' in html
    assert 'title="Info"' in html
    assert 'data-bs-placement="top"' in html


def test_bs5_popover_render_triggers():
    """3. Render with specific triggers (e.g. focus/hover)."""
    # data-bs-trigger="focus" is common for dismissible popovers
    pop = BS5Popover(
        content="Dismissible",
        data_bs_trigger="focus",
        Class="btn btn-secondary"
    )
    html = pop.render()

    assert 'data-bs-trigger="focus"' in html
    assert 'class="btn btn-secondary"' in html


def test_bs5_popover_add_wrapper():
    """
    4. Test add_wraper method.
    Useful for disabled elements that need a wrapper to capture clicks.
    """
    # Logic: Initialize empty or basic, then wrap specific content?
    # Based on your API: add_wraper(content, tag='span')
    pop = BS5Popover(content="Disabled info")

    html = pop.render()

    assert '<span' not in html
    assert 'data-bs-toggle="popover"' in html  # Attrs moved to wrapper
    assert '<button disabled>Disabled</button>' not in html
    pop = BS5Popover(content="Disabled info",wraper_content='<button disabled>Disabled</button>',is_wraped=True)

    html = pop.render()

    assert '<span' in html
    assert 'data-bs-toggle="popover"' in html  # Attrs moved to wrapper
    assert '<button disabled>Disabled</button>' in html


def test_bs5_popover_state_blocking():
    """5. State: Popover hidden when constraints not met."""
    pop = BS5Popover(
        content="Secret Tip",
        render_constraints={"show_tips": True}
    )

    # Render with False -> Hidden
    html = pop.render(override_props={"show_tips": False})

    assert not html


def test_bs5_popover_state_passing():
    """6. State: Popover visible when constraints met."""
    pop = BS5Popover(
        content="Public Tip",
        render_constraints={"help_mode": True}
    )
    pop.include_env_props(help_mode=True)
    # Render with True -> Visible
    html = pop.render()

    assert 'data-bs-toggle="popover"' in html
    assert "Public Tip" in html
