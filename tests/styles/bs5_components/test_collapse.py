from probo.styles.frameworks.bs5.components.collapse import BS5Collapse

# ==============================================================================
#  BS5Collapse Tests
# ==============================================================================

def test_bs5_collapse_render_basic():
    """1. Render basic collapse container with ID and content."""
    # Note: ID is crucial for collapse logic
    col = BS5Collapse(content="Hidden Text", id="myCollapse")
    html = col.render()

    assert '<div' in html
    assert 'class="collapse"' in html
    assert 'id="myCollapse"' in html
    assert 'Hidden Text' in html


def test_bs5_collapse_render_multicollapse():
    """2. Render with multi-collapse support."""
    col = BS5Collapse(content="Multi Content", is_multicollapse=True, id="multi1")
    html = col.render()

    # Should have both classes
    assert 'class="collapse multi-collapse"' in html
    assert 'id="multi1"' in html


def test_bs5_collapse_button_trigger():
    """3. Render with a Button trigger."""
    col = BS5Collapse(content="Details", Id="btnTarget")

    # Add trigger via API
    col.add_button_trigger(content="Toggle", classes=["btn", "btn-primary"])

    html = col.trigger.render()

    # Verify Button
    assert '<button' in html
    assert 'class="btn btn-primary"' in html
    assert 'data-bs-toggle="collapse"' in html
    assert 'data-bs-target="#btnTarget"' in html
    assert 'aria-controls="btnTarget"' in html

    # Verify Content not existence
    assert 'id="btnTarget"' not in html


def test_bs5_collapse_link_trigger():
    """4. Render with a Link (<a>) trigger."""
    col = BS5Collapse(content="Link Details", Id="linkTarget")

    # Add trigger via API
    col.add_link_trigger(content="Read More", classes=["link-primary"])

    html = col.trigger.render()

    # Verify Link
    assert '<a' in html
    assert 'class="link-primary"' in html
    assert 'href="#linkTarget"' in html  # Link uses href for target
    assert 'role="button"' in html  # Accessibility best practice
    assert 'data-bs-toggle="collapse"' in html


def test_bs5_collapse_state_blocking():
    """5. State: Collapse hidden when constraints not met."""
    col = BS5Collapse(
        content="Secret",
        id="secret",
        render_constraints={"show_secret": True}
    )

    # Render with False -> Hidden
    html = col.render(override_props={"show_secret": False})

    assert not html


def test_bs5_collapse_state_passing():
    """6. State: Collapse visible when constraints met."""
    col = BS5Collapse(
        content="Public",
        id="public",
        render_constraints={"show_public": True}
    )

    # Render with True -> Visible
    html = col.render(override_props={"show_public": True},add_to_global=True)

    assert "collapse" in html
    assert "Public" in html