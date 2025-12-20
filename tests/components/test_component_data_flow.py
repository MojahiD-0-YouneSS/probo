import pytest
from mui import (
    Component,
    ComponentState,
    ElementState,
    DynamicData,
    div,
    span,
    CssRule,
    CssSelector,
)

# --- FIXTURES ---
@pytest.fixture
def basic_es():
    # <$ s='static_key' d='dynamic_key' ... $>
    return ElementState(element='span', s_state='title', d_state='live_title')
GLOBAL_PROPS ={'is_admin': False,'name':'youness','city':'rabat'}
# --- TESTS ---

def test_render_with_cs_no_es():
    """Test Component with State but NO Elements (Should pass through)."""
    state = ComponentState(s_data={'a': 1})
    comp = Component(name="Stateful", template="<div>Static</div>", state=state)
    
    html = comp.render()
    assert html == "<div>Static</div>"

def test_render_with_es_and_cs():
    """Test full data flow: Data -> CS -> ES -> Template."""
    # 1. Setup Elements
    es = ElementState(element='h1', s_state='header_text')
    
    # 2. Setup State
    cs = ComponentState(
        es, # Register ES with CS
        s_data={'header_text': 'Hello World'},
    )
    
    # 3. Setup Component (Using placeholder in template)
    # Note: Component must know how to find es.placeholder in the template
    comp = Component(name="Main", template=div(es.placeholder), state=cs)
    
    html = comp.render()
    assert "<h1>Hello World</h1>" in html
    assert "<$" not in html # Placeholder replaced

def test_render_override_props():
    """Test render(override_props=...) affecting StateProps logic."""
    from mui import StateProps
    
    # Element requires 'is_admin' to show
    rules = StateProps(required=True, prop_equals={'is_admin': False})
    es = ElementState(element='button', s_state='btn_text', props=rules)
    
    cs = ComponentState(es,s_data={'btn_text': 'Delete'},)
    comp = Component(name="AdminPanel", template=div(es.placeholder), state=cs,props=GLOBAL_PROPS)
    
    # Case A: Render without props -> Hidden
    html_default = comp.render() # Default props empty
    assert "button"in html_default
    
    # Case B: Render WITH override props -> Visible
    html_visible_but_wrong_props = comp.render(override_props={'is_admin': True})
    assert "<button>Delete</button>" not in html_visible_but_wrong_props
    html_visible = comp.render(override_props={'is_admin': False})
    assert "<button>Delete</button>" in html_visible

def test_render_override_props_no_state_props_with_global_prop():
    """Test render(override_props=...) affecting StateProps logic."""
    from mui import StateProps
    
    # Element requires 'is_admin' to show
    rules = StateProps(required=True, prop_equals={'is_admin': True})
    es = ElementState(element='button', s_state='btn_text', props=rules)
    
    cs = ComponentState(es, s_data={'btn_text': 'Delete'},)
    comp = Component(name="AdminPanel", template=div(es.placeholder), state=cs,props=GLOBAL_PROPS)
    
    # Case A: Render without props -> Hidden
    html_hidden = comp.render() # Default props empty
    assert "button" not in html_hidden
    
    # Case B: Render WITH override props -> Visible
    html_visible = comp.render(override_props={'is_admin': True})
    assert "<button>Delete</button>" not in html_visible

def test_render_override_props_no_state_props():
    """Test render(override_props=...) affecting StateProps logic."""
    from mui import StateProps
    
    # Element requires 'is_admin' to show
    rules = StateProps(required=True, prop_equals={'is_admin': True})
    es = ElementState(element='button', s_state='btn_text', props=rules)
    
    cs = ComponentState(es, s_data={'btn_text': 'Delete'},)
    comp = Component(name="AdminPanel", template=div(es.placeholder), state=cs)
    
    # Case A: Render without props -> Hidden
    html_hidden = comp.render() # Default props empty
    assert "button" not in html_hidden
    
    # Case B: Render WITH override props -> Visible
    html_visible = comp.render(override_props={'is_admin': True})
    assert "<button>Delete</button>" not in html_visible

def test_dynamic_data_processor_hook():
    """
    Test the Custom Method Plugin on DynamicData.
    Process: Raw Object -> Processor Function -> CS -> ES -> Render
    """
    # 1. Raw Data (e.g. a Django model or complex dict)
    raw_user = {'first': 'youness', 'last': 'mojahid', 'id': 99}
    
    # 2. The Processor (The Plugin)
    def user_processor(data):
        # Transform: Combine names, capitalize
        return {
            'full_name': f"{data['first']} {data['last']}".upper(),
            'user_id': data['id']
        }
    
    # 3. DynamicData Instance
    dd = DynamicData(data_obj=raw_user, processor=user_processor)
    print('dd.get_data()',dd.dynamic_data)
    # 4. Component Setup
    es = ElementState(element='span', d_state='full_name')
    
    # CS takes the DynamicData object directly (or its result depending on your impl)
    # Assuming CS calls dd.get_data() internally or you pass dd.get_data()
    cs = ComponentState(
        es,
        d_data=dd.dynamic_data, # <--- Processor runs here
    )
    
    comp = Component(name="Profile", template=div(es.placeholder), state=cs)
    
    html = comp.render()
    
    # Assert the PROCESSOR logic worked
    assert "<span>YOUNESS MOJAHID</span>" in html

def test_change_skin_scenarios():
    # Setup
    comp = Component("Test", template=div(Id="main", Class="box"),state=None)
    
    # Case 1: Dictionary Selector
    comp.change_skin({'.box': {'color': 'blue'}})
    _, css = comp.render()

    assert "color:blue" in css

    # Case 2: Component Inheritance
    other = Component("Other",template='',state=None)
    ruels = CssRule(font_size='25px', margin='10px').declarations
    selector = CssSelector().Id('main').render()
    css_rules = {selector[0]:ruels}
    other.load_css_rules(**css_rules)
    comp.change_skin(other)
    with pytest.raises(ValueError) as excinfo:
        _, css = comp.render()
    other.load_css_rules(**css_rules)

    assert "margin:10px" not in css
    # Case 3: Root Kwargs
    # (Assuming s_data has id='main' from template parsing or init)
    # You might need to manually ensure comp knows its root ID for this test
    comp.set_root_element('section',Id='main') 
    
    comp.change_skin(background_color='black') # Root style
    print([x.render() for x in comp.active_css_rules])
    _, css = comp.render()

    assert "background-color:black" in css
    
def test_cs_strict_mode_raises_error():
    """Test that strict=True crashes on missing data."""
    es = ElementState(element='span', s_state='missing_key')
    with pytest.raises(KeyError):
        # Should crash immediately during initialization
        ComponentState(
            es,
            strict=True
        )

def test_cs_strict_mode_props_mismatch():
    """Test that strict=True crashes on wrong props."""
    es = ElementState(element='div')
    
    with pytest.raises(ValueError) as excinfo:
        cs = ComponentState(
            es,
            incoming_props={'theme': 'light'},
            strict=True,
            theme='dark', # We REQUIRE dark
        )
    
        cs.resolved_template("<div>...</div>")
    
    assert "Prop Mismatch" in str(excinfo.value)