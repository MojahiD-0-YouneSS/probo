import pytest
from mui import ComponentState, ElementState

# --- FIXTURES ---
@pytest.fixture
def setup_cs():
    """Returns a CS with 2 elements and some data."""
    es1 = ElementState(element='div', s_state='title_key') # <$ id='...' $>
    es2 = ElementState(element='span', d_state='user_key')
    s_data = {'title_key': 'Welcome'}
    d_data = {'user_key': 'Youness'}
    
    # Assuming CS takes *elements in init
    return ComponentState(es1, es2, s_data=s_data, d_data=d_data, )

# --- TESTS ---

def test_cs_regex_replacement(setup_cs):
    """
    Scenario: Standard rendering.
    Process: Template has placeholders matching the elements.
    Expected: Placeholders replaced by resolved HTML.
    """
    cs = setup_cs
    # Simulate what TemplateProcessor would output
    raw_template = f"<div>{cs.elements_states[0].placeholder} - {cs.elements_states[1].placeholder}</div>"
    # Render logic (internally calls change_state -> resolve -> regex sub)
    result = cs.resolved_template(raw_template)
    assert "<div>Welcome</div>" in result
    assert "<span>Youness</span>" in result
    assert "<$" not in result # Placeholder gone

def test_cs_final_sweep(setup_cs):
    """
    Scenario: Template has a "dead" placeholder (typo or removed element).
    Process: Render.
    Expected: The valid one renders, the dead one is scrubbed (Empty String).
    """
    cs = setup_cs
    valid_ph = cs.elements_states[0].placeholder
    dead_ph = "<$ s='ghost' d='' i='False'></$>" # Looks like a tag, but matches no object
    
    raw_template = f"{valid_ph} and {dead_ph}"
    
    result = cs.resolved_template(raw_template)
    
    assert "<div>Welcome</div>" in result
    assert dead_ph not in result # Scrubbed!
    assert " and " in result # Surrounding text remains

def test_cs_data_propagation():
    """
    Scenario: Updating Dynamic Data in CS.
    Process: Change d_data, trigger render.
    Expected: Element output changes.
    """
    es = ElementState(element='b', d_state='count')
    cs = ComponentState(es, d_data={'count': 1},)
    
    # Render 1
    assert "<b>1</b>" in cs.resolved_template(es.placeholder)
    
    # Update Data (Simulating a new request context)
    cs.d_data['count'] = 99
    
    # Render 2
    assert "<b>99</b>" in cs.resolved_template(es.placeholder)
