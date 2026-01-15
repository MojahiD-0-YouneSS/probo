from probo.styles.frameworks.bs5.components.modal import (
    BS5Modal,
)

# ==============================================================================
#  BS5Modal Tests
# ==============================================================================

def test_bs5_modal_render_basic_structure():
    """1. Render basic modal container structure."""
    # Usage: BS5Modal(content="", id="myModal")
    # Note: 'content' in init usually populates the body or is ignored if specific add_ methods used
    modal = BS5Modal(content="Default Body", id="testModal")
    html = modal.render()

    # Check hierarchy
    assert '<div id="testModal" class="modal"' in html
    assert 'id="testModal"' in html
    # Assuming init content goes to body if not specified otherwise
    assert 'Default Body' in html


def test_bs5_modal_trigger_button():
    """2. Render with a trigger button."""
    modal = BS5Modal(content="", id="triggerModal")

    # Add Trigger
    modal.add_trigger_btn(
        content="Open Modal",
        Class="btn btn-primary",
        data_bs_target="#triggerModal"
    )

    html = ''.join( x.render() for x in modal.triggers)

    # Button should act as toggle
    assert '<button' in html
    assert 'data-bs-toggle="modal"' in html
    assert 'data-bs-target="#triggerModal"' in html
    assert 'Open Modal' in html


def test_bs5_modal_full_content_sections():
    """3. Render Header, Body, and Footer explicitly."""
    modal = BS5Modal(content="")  # Init empty

    # 1. Header
    modal.add_modal_header(other_content="", title="Modal Title")

    # 2. Body
    modal.add_modal_body(content="<p>Main content here</p>")

    # 3. Footer
    modal.add_modal_footer(content='<button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>')

    html = modal.render()

    # Verify Header
    assert '<div class="modal-header">' in html
    assert '<h5 class="modal-title">Modal Title</h5>' in html

    # Verify Body
    assert '<div class="modal-body">' in html
    assert '<p>Main content here</p>' in html

    # Verify Footer
    assert '<div class="modal-footer">' in html
    assert 'data-bs-dismiss="modal"' in html


def test_bs5_modal_custom_attributes():
    """4. Render with static backdrop and scrolling."""
    # 'static' backdrop prevents closing when clicking outside
    modal = BS5Modal(
        content="Static",
        id="staticBackdrop",
        data_bs_backdrop="static",
        data_bs_keyboard="false"
    )

    html = modal.render()

    assert 'data-bs-backdrop="static"' in html
    assert 'data-bs-keyboard="false"' in html
    assert 'id="staticBackdrop"' in html


def test_bs5_modal_state_blocking():
    """5. State: Modal hidden when constraints not met."""
    modal = BS5Modal(
        content="Secret Data",
        id="secretModal",
        render_constraints={"can_view": True}
    )

    # Render with False -> Hidden
    html = modal.render(override_props={"can_view": False})

    assert not html


def test_bs5_modal_state_passing():
    """6. State: Modal visible when constraints met."""
    modal = BS5Modal(
        content="Public Data",
        id="publicModal",
        render_constraints={"is_active": True}
    )

    # Render with True -> Visible
    html = modal.render(override_props={"is_active": True},add_to_global=True,)

    assert "modal" in html
    assert "Public Data" in html
