from probo.styles.frameworks.bs5.components.toast import BS5Toast

# ==============================================================================
#  BS5Toast Tests
# ==============================================================================

def test_bs5_toast_render_basic():
    """1. Render basic toast structure."""
    # Usage: BS5Toast(header_content, body_content)
    toast = BS5Toast(
        header_content="Notification",
        body_content="Action successful."
    )
    html = toast.render()

    # Base Structure
    assert '<div role="alert" aria-live="assertive" aria-atomic="true" class="toast"' in html
    assert 'role="alert"' in html
    assert 'aria-live="assertive"' in html

    # Header
    assert '<div class="toast-header">' in html
    assert 'Notification' in html
    assert 'class="btn-close"' in html  # Auto-close button

    # Body
    assert '<div class="toast-body">' in html
    assert 'Action successful.' in html


def test_bs5_toast_render_fluent_add():
    """2. Render using add_toast method."""
    toast = BS5Toast(include_container=False)  # Init empty without container
    toast2 = BS5Toast(include_container=True)  # Init empty without container

    # Add Toast via method
    toast.add_toast(
        header_content="Alert",
        body_content="Something happened.",
        btn_position="header",  # Close button in header
        id="myToast"
    )
    toast2.add_toast(
        header_content="Alert",
        body_content="Something happened.",
        btn_position="header",  # Close button in header
        id="myToast"
    )

    html = toast.render()
    html2 = toast2.render()

    assert 'id="myToast"' not in html
    assert 'class="toast-header"' not in html
    assert 'data-bs-dismiss="toast"' not in html

    assert 'id="myToast"' in html2
    assert 'class="toast-header"' in html2
    assert 'data-bs-dismiss="toast"' in html2


def test_bs5_toast_container_wrapper():
    """3. Render inside a Toast Container (for positioning)."""
    # include_container=True wraps toasts in a container div
    toast = BS5Toast(include_container=True,)
    toast.template.attr_manager.set_bulk_attr( Class="position-fixed bottom-0 end-0 p-3")
    toast.add_toast(header_content="Hi", body_content="Hello")

    html = toast.render()

    # Check wrapper
    assert '<div class="toast-container position-fixed bottom-0 end-0 p-3"' in html
    # Check toast inside
    assert '<div role="alert" aria-live="assertive" aria-atomic="true" class="toast"' in html


def test_bs5_toast_custom_attributes():
    """4. Render with custom attributes (autohide, delay)."""
    toast = BS5Toast(
        header_content="Delayed",
        body_content="Body",
        data_bs_autohide="false",
        data_bs_delay="5000"
    )
    html = toast.render()

    assert 'data-bs-autohide="false"' in html
    assert 'data-bs-delay="5000"' in html


def test_bs5_toast_state_blocking():
    """5. State: Toast hidden when constraints not met."""
    toast = BS5Toast(
        header_content="Secret",
        body_content="Data",
        render_constraints={"show_toast": True}
    )

    # Render with False -> Hidden
    html = toast.render(override_props={"show_toast": False})

    assert not html


def test_bs5_toast_state_passing():
    """6. State: Toast visible when constraints met."""
    toast = BS5Toast(
        header_content="Public",
        body_content="Info",
        render_constraints={"is_active": True}
    )
    toast.include_env_props(is_active=True)
    # Render with True -> Visible
    html = toast.render()

    assert "toast" in html
    assert "Public" in html