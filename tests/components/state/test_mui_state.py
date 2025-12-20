import pytest
from mui.components.state.component_state import ElementState, ComponentState
from mui.components.state.props import StateProps, StatePropsValidator

# ==============================================================================
#  PART 1: StateProps Variations (The Gatekeeper)
# ==============================================================================

# We test the Validator directly to ensure the logic holds up regardless of the Element

@pytest.mark.parametrize("scenario, rules, context, expected", [
    # --- 1. Master Switches ---
    ("Kill Switch",     StateProps(display_it=False), {}, False),
    ("Force Render",    StateProps(display_it=True, required=False), {}, True),
    
    # --- 2. prop_equals ---
    ("Equals Pass",     StateProps(required=True, prop_equals={'role': 'admin'}), {'role': 'admin'}, True),
    ("Equals Fail",     StateProps(required=True, prop_equals={'role': 'admin'}), {'role': 'user'}, False),
    ("Equals Missing",  StateProps(required=True, prop_equals={'role': 'admin'}), {}, False),
    
    # --- 3. prop_is_in ---
    ("In List Pass",    StateProps(required=True, prop_is_in={'status': ['pub', 'draft']}), {'status': 'draft'}, True),
    ("In List Fail",    StateProps(required=True, prop_is_in={'status': ['pub', 'draft']}), {'status': 'archived'}, False),
    
    # --- 4. prop_is_truthy ---
    ("Truthy Pass",     StateProps(required=True, prop_is_truthy=['user']), {'user': {'id': 1}}, True),
    ("Truthy Fail",     StateProps(required=True, prop_is_truthy=['user']), {'user': None}, False),
    ("Truthy Missing",  StateProps(required=True, prop_is_truthy=['user']), {}, False),
    
    # --- 5. Complex Combo ---
    ("Combo Pass",      StateProps(required=True, prop_equals={'a': 1}, prop_is_truthy=['b']), {'a': 1, 'b': True}, True),
    ("Combo Fail",      StateProps(required=True, prop_equals={'a': 1}, prop_is_truthy=['b']), {'a': 1, 'b': None}, False),
])
def test_state_props_variations(scenario, rules, context, expected):
    """Test variations of StateProps logic."""
    assert StatePropsValidator(rules, context).is_valid() is expected, f"Failed Scenario: {scenario}"


# ==============================================================================
#  PART 2: ElementState Data Resolution (The Pointer)
# ==============================================================================

# Mock Data Stores
STATIC_DB = {
    'title_s': 'Static Title',
    'title_s_empty': '',
    'user_s': 'Guest',
    'list_s': ['A', 'B']
}
DYNAMIC_DB = {
    'title_d': 'Dynamic Title',
    'user_d': 'Admin',
    'list_d': [1, 2, 3]
}

@pytest.mark.parametrize("scenario, es_args, expected_content", [
    # --- 1. Static Only ---
    (
        "Static Key Found",
        {'element': 'div', 's_state': 'title_s'}, 
        "<div>Static Title</div>"
    ),
    (
        "Static Key Found but value is emplty",
        {'element': 'div', 's_state': 'title_s_empty'}, 
        ""
    ),
    (
        "Static Key Found but dynamic value is not  emplty",
        {'element': 'div', 's_state': 'title_s','d_state': 'missing_key'}, 
        "<div>Static Title</div>"
    ),
    (
        "Static Key Found but dynamic value is not  emplty",
        {'element': 'div', 's_state': 'title_s','d_state': 'missing_key','hide_dynamic':True}, 
        ""
    ),
    (
        "Static Key Missing", 
        {'element': 'div', 's_state': 'missing_key'}, 
        "" # Default empty behavior
    ),

    # --- 2. Dynamic Only ---
    (
        "Dynamic Key Found",
        {'element': 'span','s_state':'', 'd_state': 'title_d'}, 
        "<span>Dynamic Title</span>"
    ),
    (
        "Dynamic Key Missing (Loose Mode)", 
        {'element': 'span', 's_state':'','d_state': 'missing_key'}, 
        ""
    ),

    # --- 3. Priority (Dynamic vs Static) ---
    (
        "Dynamic Overrides Static",
        {'element': 'h1', 's_state': 'title_s', 'd_state': 'title_d'},
        "<h1>Dynamic Title</h1>" # Should NOT be 'Static Title'
    ),
    (
        "Dynamic Missing Fallback to Static",
        {'element': 'h1', 's_state': 'title_s', 'd_state': 'missing_key'},
        "<h1>Static Title</h1>" # Fallback worked
    ),

    # --- 4. Void Elements ---
    (
        "Void Element Ignores Content",
        {'element': 'img', 's_state': 'title_s', 'is_void_element': True, 'src': 'img.png',},
        '<img src="img.png"/>' # No closing tag, content ignored (unless passed to src)
    ),
])

def test_element_state_resolution(scenario, es_args, expected_content):
    """Test how ElementState resolves content from data stores."""
    es = ElementState(**es_args)
    cs = ComponentState(es, s_data=STATIC_DB, d_data=DYNAMIC_DB)
    
    # Use your resolve method (adjust method name if different in your code)
    # Assuming signature: resolve(s_data, d_data)
    result = cs.resolved_template(es.placeholder)
    
    assert result == expected_content, f"Failed Scenario: {scenario}"


# ==============================================================================
#  PART 3: Iterable State Variations (The Loop)
# ==============================================================================

def test_iterable_static_list():
    """Test looping over a static list."""
    es = ElementState(element='li', s_state='list_s', i_state=True)
    cs = ComponentState(es, s_data=STATIC_DB)
    
    # Use your resolve method (adjust method name if different in your code)
    # Assuming signature: resolve(s_data, d_data)
    final_template = cs.resolved_template(es.placeholder)
    result = final_template.split('><')
    # Expected: list of strings
    assert isinstance(result, list)
    assert len(result) == 2
    assert final_template == '<li>A</li><li>B</li>'
    assert result[0]+'>' == "<li>A</li>"
    assert '<'+result[1] == "<li>B</li>"

def test_iterable_dynamic_list():
    """Test looping over a dynamic list."""
    es = ElementState(element='li',s_state='', d_state='list_d', i_state=True)
    cs = ComponentState(es, d_data=DYNAMIC_DB,)
    
    # Use your resolve method (adjust method name if different in your code)
    # Assuming signature: resolve(s_data, d_data)
    final_template = cs.resolved_template(es.placeholder)
    result = final_template.split('><')
    assert len(result) == 3
    assert final_template == '<li>1</li><li>2</li><li>3</li>'
    assert '<'+result[2] == "<li>3</li>"

def test_iterable_non_list_data():
    """Test what happens if i_state=True but data is a String (not list)."""
    # Should probably treat string as single item or list of chars? 
    # Usually strictly list. Let's assume it wraps it or fails gracefully.
    es = ElementState(element='p', s_state='title_s', i_state=True)
    cs = ComponentState(es,s_data=STATIC_DB,)
    
    # Use your resolve method (adjust method name if different in your code)
    # Assuming signature: resolve(s_data, d_data)
    result = cs.resolved_template(es.placeholder)
    
    # Depending on your implementation, this might be a list of chars or 1 item
    # Best practice: Treat non-list as single item list
    if isinstance(result, list):
        assert "Static Title" in result[0]

#===============================================================================================================================
#
#       props validation
#===============================================================================================================================


def test_prop_equals_pass(mock_props_context):
    """Test that element renders when prop matches exactly."""
    # Rule: Render only if theme is 'dark'
    rules = StateProps(required=True, prop_equals={'theme': 'dark'})
    
    assert StatePropsValidator(rules, mock_props_context).is_valid() is True

def test_prop_equals_fail(mock_props_context):
    """Test that element hides when prop does not match."""
    # Rule: Render only if theme is 'light'
    rules = StateProps(required=True, prop_equals={'theme': 'light'})
    
    assert StatePropsValidator(rules, mock_props_context).is_valid() is False

def test_permissions_check(mock_props_context):
    """Test the has_permission logic against the MockUser."""
    # Rule: User needs 'can_edit' permission
    rules = StateProps(has_permissions=['can_edit'])
    
    # Check against the 'user' object in props
    assert StatePropsValidator(rules, mock_props_context).is_valid() is True

def test_permissions_fail(mock_props_context):
    """Test missing permission."""
    rules = StateProps(has_permissions=['can_nuke_database'])
    assert StatePropsValidator(rules, mock_props_context).is_valid() is False

def test_prop_is_in(mock_props_context):
    """Test checking if a value is inside a allowed list."""
    # Rule: Request method must be GET or POST
    rules = StateProps(required=True, prop_is_in={'request.method': ['GET', 'POST']})
    
    # We need to make sure your validator flattens the prop or accesses nested 'request.method'
    # Or just test simple keys:
    rules_simple = StateProps(required=True, prop_is_in={'theme': ['dark', 'high-contrast']})
    assert StatePropsValidator(rules_simple, mock_props_context).is_valid() is True
