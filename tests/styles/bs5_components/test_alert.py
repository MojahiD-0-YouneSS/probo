from probo.styles.frameworks.bs5.components import (
     BS5Alert, 
)
    
# ==============================================================================
#  BS5Alert Tests
# ==============================================================================

def test_bs5_alert_render_basic():
    """1. Render basic alert with content and color variant."""
    alert = BS5Alert(content="Success message!", color_variant="success")
    html = alert.render()
    
    assert '<div' in html
    assert 'class="alert alert-success"' in html
    assert 'role="alert"' in html
    assert 'Success message!' in html

def test_bs5_alert_render_dismissible():
    """2. Render dismissible alert with close button."""
    alert = BS5Alert(content="Close me", color_variant="warning", is_dismissible=True, Class='fade show')
    html = alert.render()
    
    assert 'alert-dismissible fade show' in html
    assert '<button type="button" data-bs-dismiss="alert" aria-label="Close" class="btn-close"' in html
    assert '<div role="alert"' in html

def test_bs5_alert_add_icon_and_content():
    """3. Render alert with icon and additional content (heading)."""
    # Assuming has_icon=True preps the container, and add_icon injects the specific icon
    alert = BS5Alert(content="Something went wrong", color_variant="danger", has_icon=True)
    
    # Add specific icon class (e.g., Bootstrap Icons)
    alert.add_svg_icon("bi-exclamation-triangle-fill")
    
    # Add heading and more text
    alert.add_additional_content(content=" Please try again.", alert_heading="Error!")
    
    html = alert.render()
    # Check Icon
    assert '<svg width="24" height="24" role="img" aria-label="Danger" class="bi"' in html
    
    # Check Heading (Bootstrap alert-heading class)
    assert '<h4 class="alert-heading">Error!</h4>' in html
    
    # Check Combined Content
    assert "Something went wrong" in html
    assert "Please try again." in html

def test_bs5_alert_render_attributes():
    """4. Render with custom attributes."""
    alert = BS5Alert(content="Info", Id="my-alert", style="margin-top: 10px;")
    html = alert.render()
    
    assert 'id="my-alert"' in html
    assert 'style="margin-top: 10px;"' in html

def test_bs5_alert_state_constraints_blocking():
    """5. State: Alert hidden when constraints not met."""
    # Logic: Only show if 'has_error' is True
    alert = BS5Alert(
        content="System Error", 
        color_variant="danger",
        render_constraints={"has_error": True} # Note: Assuming this kwarg exists on base
    )
    
    # Render with False prop -> Hidden
    html = alert.render(override_props={"has_error": False})
    
    assert not html

def test_bs5_alert_state_constraints_passing():
    """6. State: Alert visible when constraints met."""
    alert = BS5Alert(
        content="System Operational", 
        color_variant="success",
        render_constraints={"status_ok": True}
    )
    
    # Render with True prop -> Visible
    html = alert.render(override_props={"status_ok": True},add_to_global=True,)
    
    assert "alert-success" in html
    assert "System Operational" in html

# ==============================================================================
#  BS5Alert SVG Tests
# ==============================================================================

def test_bs5_alert_svg_inline_path():
    """2. Render with inline SVG Path via path_d argument."""
    alert = BS5Alert(content="Warning!", color_variant="warning")
    
    # Path data
    d_data = "M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233..."
    alert.add_svg_icon('jkhuhnihlgilg',path_d=d_data)
    
    html = alert.render()
    
    assert '<svg' in html
    assert f'<path d="{d_data}"' in html
    assert 'xmlns="http://www.w3.org/2000/svg"' in html
    # Should NOT have use tag
    assert '<use' not in html

def test_bs5_alert_svg_symbol_definition():
    """3. Render hidden SVG symbol block."""
    alert = BS5Alert(content="Check Symbols", color_variant="success")
    
    # Define two symbols
    symbols = {
        'check-circle': 'M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0z',
        'info-fill': 'M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16z'
    }
    
    alert.add_svg_symbol_icon(**symbols)
    
    html = alert.render()
    
    # Container check
    assert 'style="display: none;"' in html
    
    # Symbol 1
    assert '<symbol id="check-circle"' in html
    assert 'viewBox="0 0 16 16"' in html
    assert '<path d="M16 8A8 8' in html
    
    # Symbol 2
    assert '<symbol id="info-fill"' in html
    assert '<path d="M8 16A8 8' in html

def test_bs5_alert_svg_custom_viewbox_symbol():
    """4. Render symbol with custom viewBox."""
    alert = BS5Alert(content="Custom ViewBox")
    
    alert.add_svg_symbol_icon(
        symbol_attrs={'viewBox': "0 0 24 24"},
        my_icon="M0 0h24v24H0z"
    )
    
    html = alert.render()
    assert 'viewBox="0 0 24 24"' in html

def test_bs5_alert_integration_symbol_and_use():
    """5. Integration: Define symbol AND use it."""
    alert = BS5Alert(content="Linked Icon")
    
    # 1. Define Symbol
    alert.add_svg_symbol_icon(my_custom_icon="M10 10...")
    
    # 2. Use it
    alert.add_svg_icon("my_custom_icon")
    
    html = alert.render()
    
    # Verify both parts exist
    assert '<symbol id="my_custom_icon"' in html
    assert '<use xlink:href="bootstrap-icons.svg#my_custom_icon"' in html
