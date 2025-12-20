import pytest
from dataclasses import asdict
from mui.shortcuts.configs import (
    ElementStateConfig, StateConfig, StyleConfig, ComponentConfig
)
from mui.styles.plain_css import CssRule
from mui.components.state.props import StateProps

# ==============================================================================
#  1. CONFIGURATION TESTS (2 Tests Per Config)
# ==============================================================================

# --- ElementStateConfig ---

def test_element_state_config_defaults():
    """Test 1: Default initialization and ID generation."""
    esc = ElementStateConfig(tag="div")
    
    assert esc.tag == "div"
    # Verify ID was generated (UUID hex is 32 chars, plus 'div==')
    assert "div==" in esc.config_id 
    assert esc.s_state == ""
    assert esc.d_state == ""
    assert esc.i_state is False

def test_element_state_config_full():
    """Test 2: Full initialization with binding and props."""
    props = StateProps(required=True)
    esc = ElementStateConfig(
        tag="span",
        s_state="static_val",
        d_state="dynamic_val",
        bind_to="class",
        props=props,
        attrs={'id': 'my-span'}
    )
    
    assert esc.tag == "span"
    assert esc.s_state == "static_val"
    assert esc.bind_to == "class"
    assert esc.props.required is True
    assert esc.attrs['id'] == "my-span"


# --- StateConfig ---

def test_state_config_data_storage():
    """Test 1: Holding static and dynamic data."""
    sc = StateConfig(
        s_data={'title': 'Hello'},
        d_data={'user': 'Admin'}
    )
    assert sc.s_data['title'] == 'Hello'
    assert sc.d_data['user'] == 'Admin'
    assert sc.strict is False # Default check

def test_state_config_flags_and_elements():
    """Test 2: Strict mode flags and element list."""
    # Create child config
    esc = ElementStateConfig(tag="b", d_state="count")
    
    sc = StateConfig(
        strict=True,
        require_props=True,
        elements_state_config=[esc]
    )
    
    assert sc.strict is True
    assert sc.require_props is True
    assert len(sc.elements_state_config) == 1
    assert sc.elements_state_config[0].tag == "b"


# --- StyleConfig ---

def test_style_config_jit_rules():
    """Test 1: holding JIT CSS rules."""
    # Can accept Dict or List[CssRule]
    rule_dict = {'.btn': {'color': 'red'}}
    
    sc = StyleConfig(css=rule_dict)
    assert sc.css['.btn']['color'] == 'red'

def test_style_config_frameworks():
    """Test 2: Root styles and Bootstrap classes."""
    sc = StyleConfig(
        root_css={'margin': '10px'},
        root_bs5_classes=['card', 'p-3']
    )
    
    assert sc.root_css['margin'] == '10px'
    assert 'card' in sc.root_bs5_classes
    assert 'p-3' in sc.root_bs5_classes


# --- ComponentConfig ---

def test_component_config_structure():
    """Test 1: Basic hierarchy."""
    cc = ComponentConfig(name="MyCard", template="<div></div>")
    
    assert cc.name == "MyCard"
    assert cc.template == "<div></div>"
    # Ensure sub-configs are initialized by default
    assert isinstance(cc.state_config, StateConfig)
    assert isinstance(cc.style_config, StyleConfig)

def test_component_config_composition():
    """Test 2: Injecting sub-configs manually."""
    my_style = StyleConfig(root_bs5_classes=['alert'])
    my_state = StateConfig(s_data={'msg': 'Error'})
    
    cc = ComponentConfig(
        name="Alert", 
        template="<div></div>",
        style_config=my_style,
        state_config=my_state
    )
    
    assert cc.style_config.root_bs5_classes == ['alert']
    assert cc.state_config.s_data['msg'] == 'Error'
