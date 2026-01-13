from probo.styles.frameworks.bs5.components import (
    BS5Button,BS5CloseButton,BS5ButtonGroup,BS5ButtonToolbar,
)

# ==============================================================================
#  1. BS5Button Tests
# ==============================================================================

def test_bs5_button_render_basic():
    """1. Render basic button with variant and content."""
    btn = BS5Button(content="Click Me", variant="success")
    html = btn.render()
    
    assert '<button' in html
    assert 'class="btn btn-success"' in html
    assert '>Click Me</button>' in html

def test_bs5_button_render_attributes_and_size():
    """2. Render button with size and custom attributes."""
    btn = BS5Button(content="Submit", size="lg", type="submit", Id="submit-btn")
    html = btn.render()
    
    assert 'class="btn btn-primary btn-lg"' in html  # Assuming primary is default variant if not specified
    assert 'type="submit"' in html
    assert 'id="submit-btn"' in html

def test_bs5_button_render_outline_variant():
    """3. Render outline variant button."""
    btn = BS5Button(content="Outline", variant="outline-danger")
    html = btn.render()
    
    assert 'class="btn btn-outline-danger"' in html

def test_bs5_button_render_link_variant():
    """4. Render link style button."""
    btn = BS5Button(content="Link Style", variant="link")
    html = btn.render()
    
    assert 'class="btn btn-link"' in html

def test_bs5_button_state_constraints_blocking():
    """5. State: Button hidden when constraints not met."""
    btn = BS5Button(content="Admin Action", render_constaints={"is_admin": True})
    
    # Render without props -> should be empty/None
    html = btn.render()
    assert not html

def test_bs5_button_state_constraints_passing():
    """6. State: Button visible when constraints met via override_props."""
    btn = BS5Button(content="Admin Action", render_constaints={"is_admin": True})
    
    html = btn.render(override_props={"is_admin": True})
    assert "Admin Action" not in html
def test_bs5_button_state_constraints_passing_global():
    """6. State: Button visible when constraints met via override_props."""
    btn = BS5Button(content="Admin Action", render_constaints={"is_admin": True})
    
    html = btn.render(override_props={"is_admin": True},add_to_global=True)
    assert "Admin Action" in html


# ==============================================================================
#  2. BS5CloseButton Tests
# ==============================================================================

def test_bs5_close_button_render_default():
    """1. Render default close button."""
    btn = BS5CloseButton()
    html = btn.render()
    
    assert '<button' in html
    assert 'class="btn-close"' in html
    assert 'aria-label="Close"' in html # Standard accessibility attr

def test_bs5_close_button_render_disabled():
    """2. Render disabled close button."""
    btn = BS5CloseButton(disabled=True)
    html = btn.render()
    
    assert 'disabled' in html
    assert 'aria-label="Close"' in html

def test_bs5_close_button_render_white_variant():
    """3. Render white variant (for dark backgrounds)."""
    btn = BS5CloseButton(variant="white")
    html = btn.render()
    
    assert 'class="btn-close btn-close-white"' in html

def test_bs5_close_button_render_custom_attrs():
    """4. Render with custom attributes (e.g. data-bs-dismiss)."""
    btn = BS5CloseButton(data_bs_dismiss="modal")
    html = btn.render()
    
    assert 'data-bs-dismiss="modal"' in html

def test_bs5_close_button_state_blocking():
    """5. State: Close button hidden via constraints."""
    btn = BS5CloseButton(render_constaints={"show_close": True})
    html = btn.render(override_props={"show_close": False})
    assert not html

def test_bs5_close_button_state_passing():
    """6. State: Close button visible via constraints."""
    btn = BS5CloseButton(render_constaints={"show_close": True})
    html = btn.render(override_props={"show_close": True},add_to_global=True,)
    assert "btn-close" in html


# ==============================================================================
#  3. BS5ButtonGroup Tests
# ==============================================================================

def test_bs5_btn_group_render_basic():
    """1. Render basic button group container."""
    # Assuming constructor accepts *btns directly or they are added later
    grp = BS5ButtonGroup()
    grp.add_btn(content="Left")
    grp.add_btn(content="Right")
    
    html = grp.render()
    
    assert 'class="btn-group"' in html
    assert 'role="group"' in html
    assert '>Left</button>' in html
    assert '>Right</button>' in html

def test_bs5_btn_group_render_vertical():
    """2. Render vertical button group."""
    grp = BS5ButtonGroup(variant="vertical")
    grp.add_btn(content="Top")
    
    html = grp.render()
    assert 'class="btn-group-vertical"' in html

def test_bs5_btn_group_render_sizing():
    """3. Render button group with size applied."""
    grp = BS5ButtonGroup(size="lg")
    grp.add_btn(content="Large")
    
    html = grp.render()
    assert 'class="btn-group btn-group-lg"' in html

def test_bs5_btn_group_render_checkbox_button():
    """4. Render checkbox button toggle inside group."""
    grp = BS5ButtonGroup()
    grp.add_check_box_btn(content="Check me", override_input_attr={'id':'btn-check-1','autocomplete':"off"},**{'for':"btn-check-1"})
    
    html = grp.render()
    # Should render <input type="checkbox" class="btn-check" ...> <label class="btn ...">...</label>
    assert '<input' in html
    assert 'type="checkbox" class="btn-check"' in html
    assert 'id="btn-check-1"' in html
    assert '<label for="btn-check-1" class="btn btn-primary"' in html

def test_bs5_btn_group_state_blocking():
    """5. State: Hide entire group based on constraints."""
    grp = BS5ButtonGroup(render_constaints={"has_permissions": True})
    grp.add_btn(content="Action")
    
    html = grp.render(override_props={"has_permissions": False})
    assert not html

def test_bs5_btn_group_state_passing():
    """6. State: Show group based on constraints."""
    grp = BS5ButtonGroup(render_constaints={"has_permissions": True})
    grp.add_btn(content="Action")
    
    html = grp.render(override_props={"has_permissions": True},add_to_global=True)
    assert "btn-group" in html
    assert "Action" in html


# ==============================================================================
#  4. BS5ButtonToolbar Tests
# ==============================================================================

def test_bs5_toolbar_render_basic():
    """1. Render basic toolbar with groups."""
    toolbar = BS5ButtonToolbar()
    
    grp1 = BS5ButtonGroup()
    grp1.add_btn("1")
    
    grp2 = BS5ButtonGroup()
    grp2.add_btn("2")
    
    toolbar.add_btn_grp(grp1)
    toolbar.add_btn_grp(grp2)
    
    html = toolbar.render()
    
    assert '<div role="toolbar" class="btn-toolbar"' in html
    assert 'role="toolbar"' in html
    # Should contain both groups
    assert html.count('class="btn-group"') == 2

def test_bs5_toolbar_render_custom_attrs():
    """2. Render toolbar with aria-label or other attributes."""
    toolbar = BS5ButtonToolbar(aria_label="Toolbar with button groups")
    html = toolbar.render()
    
    assert 'aria-label="Toolbar with button groups"' in html

def test_bs5_toolbar_render_spacing():
    """3. Test spacing utilities if applied (usually between groups)."""
    toolbar = BS5ButtonToolbar()
    grp1 = BS5ButtonGroup(Class="me-2") # Margin end
    grp1.add_btn("A")
    toolbar.add_btn_grp(grp1)
    
    html = toolbar.render()
    assert 'class="btn-group me-2"' in html

def test_bs5_toolbar_render_input_group_mix():
    """4. Integration: Toolbar mixing button groups (future input groups)."""
    # Assuming for now just ensuring structure holds arbitrary content/groups
    toolbar = BS5ButtonToolbar()
    grp = BS5ButtonGroup()
    grp.add_btn("B")
    toolbar.add_btn_grp(grp)
    
    html = toolbar.render()
    assert "btn-toolbar" in html
    assert "btn-group" in html

def test_bs5_toolbar_state_blocking():
    """5. State: Hide toolbar via constraints."""
    toolbar = BS5ButtonToolbar(render_constaints={"show_tools": True})
    html = toolbar.render(override_props={"show_tools": False})
    assert not html

def test_bs5_toolbar_state_passing():
    """6. State: Show toolbar via constraints."""
    toolbar = BS5ButtonToolbar(render_constaints={"show_tools": True})
    grp = BS5ButtonGroup()
    grp.add_btn("Tool")
    toolbar.add_btn_grp(grp)
    
    html = toolbar.render(override_props={"show_tools": True},add_to_global=True)
    assert "btn-toolbar" in html
    assert "Tool" in html

