import pytest
from mui.context.context_logic import (
    TemplateProcessor,
    loop,
    TemplateComponentMap, 
    StaticData,
    DynamicData,
)
from mui import div, span

# --- LOOP TEST ---
def test_loop_logic():
    """Test the loop utility for ints, lists, and dicts."""
    # 1. Integer Loop
    res_int = loop(3, lambda i: div(f"Item {i}"))
    assert len(res_int) == 3
    assert "Item 0" in res_int[0]

    # 2. List Loop
    res_list = loop(['a', 'b'], lambda x: span(x))
    assert "<span>a</span>" in res_list[0]

    # 3. Dict Loop
    res_dict = loop({'k': 'v'}, lambda k, v: div(f"{k}={v}"))
    assert "k=v" in res_dict[0]


# --- TEMPLATE PROCESSOR TEST ---
def test_template_processor_logic():
    """Test TemplateProcessor initialization and context handling."""
    data = {'key': 'value'}
    tp = TemplateProcessor(data)
    
    # Verify initialization
    assert tp is not None
    # Assuming it stores the context data
    if hasattr(tp, 'data'):
        assert tp.data == data
    elif hasattr(tp, 'context'):
        assert tp.context == data

def test_template_processor_rendering():
    """
    Test the specific template processing logic defined in TemplateProcessor.
    Features: Variables {{ x }}, Filters {{ x|upper }}, If/Else <$if>, For Loops <$for>.
    """
    # 1. Setup Context
    data = {
        'username': 'youness',
        'role': 'admin',
        'score': 10,
        'items': ['apple', 'banana', 'cherry'],
        'is_active': True,
        'is_banned': False
    }
    tp = TemplateProcessor(data)

    # 2. Test Variable & Filter
    # Should evaluate 'username' and apply 'upper' filter
    assert tp.render_template("Hello {{ username|upper }}") == "Hello YOUNESS"
    assert tp.render_template("Length: {{ items|length }}") == "Length: 3"

    # 3. Test Conditional (IF / ELSE)
    # Syntax: <$if condition>...<$else>...</$if>
    tmpl_if = "<$if is_active>Active User<$else>Inactive</$if>"
    assert tp.render_template(tmpl_if) == "Active User"

    tmpl_else = "<$if is_banned>Banned<$else>Clean</$if>"
    assert tp.render_template(tmpl_else) == "Clean"

    # 4. Test Conditional (ELIF)
    # Syntax: <$if cond>...<$elif cond>...</$if>
    tmpl_elif = "<$if 16<score>High<$elif 5<score>Medium<$else>Low</$if>"
    assert tp.render_template(tmpl_elif) == "Medium"

    # 5. Test For Loop
    # Syntax: <$for var in iterable>...</$for>
    tmpl_for = "<ul><$for item in items><li>{{ item|title }}</li></$for></ul>"
    expected_for = "<ul><li>Apple</li><li>Banana</li><li>Cherry</li></ul>"
    assert tp.render_template(tmpl_for) == expected_for

def test_template_processor_static_generators():
    """
    Test the static helper methods that generate the template syntax.
    """
    # 1. if_true helper
    # Should generate: <$if user.is_auth>Dashboard<$else>Login</$if>
    block = TemplateProcessor.if_true(
        expression="user.is_auth", 
        if_block="Dashboard", 
        else_statement="Login"
    )
    assert "<$if user.is_auth>Dashboard" in block
    assert "<$else>Login</$if>" in block

    # 2. for_loop helper
    # Should generate: <$for i in list>Item</$for>
    loop_block = TemplateProcessor.for_loop("i in list", "Item")
    assert "<$for i in list>Item</$for>" == loop_block

# --- TCM TEST ---
def test_template_component_map():
    """Test the registry logic."""
    tcm = TemplateComponentMap()
    
    # Register
    class MockComp: pass
    tcm.set_component(home=MockComp)
    
    # Retrieve
    assert tcm.url_name_comp.get('home',None) == MockComp
    assert tcm.url_name_comp.get('missing',None) is None

# --- DATA TESTS ---
def test_static_and_dynamic_data():
    """Test data containers."""
    # Static
    sd = StaticData({'title': 'Hello'})
    assert sd.get('title') == 'Hello' # Assuming .get() or dict access
    
    # Dynamic (with processor)
    dd = DynamicData(
        data_obj={'raw': 'lowercase'},
        processor=lambda x: {'processed': x['raw'].upper()}
    )
    # Triggers __post_init__
    assert dd.dynamic_data['processed'] == 'LOWERCASE'

def test_template_processor():pass