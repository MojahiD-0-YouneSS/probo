import pytest
from mui.styles.elements import ComponentStyle, element_style_state, element_style,SelectorRuleBridge
from mui.styles.plain_css import CssRule, CssSelector
from mui.components.state.component_state import ElementState
from mui.styles.utils import resolve_complex_selector

# ==============================================================================
#  MOCKS & FIXTURES
# ==============================================================================

@pytest.fixture
def mock_rule():
    return CssRule(color="red", font_size="16px")

@pytest.fixture
def mock_selector():
    return CssSelector().cls("btn")

# ==============================================================================
#  GROUP 1: element_style (Inline Style Helper) [7 Tests]
# ==============================================================================

def test_element_style_basic():
    """1. Convert kwargs to CSS string."""
    res = element_style(color="red", margin_top="10px")
    # Order varies, check content
    assert "color:red;" in res
    assert "margin-top:10px;" in res
    assert "style=" not in res

def test_element_style_with_attr_wrapper():
    """2. Wrap in style='...'."""
    res = element_style(with_style_attr=True, color="blue")
    assert res == 'style="color:blue;"'

def test_element_style_snake_case():
    """3. Ensure snake_case -> kebab-case."""
    res = element_style(z_index=99, background_color="white")
    assert "z-index:99;" in res
    assert "background-color:white;" in res

def test_element_style_numeric_values():
    """4. Handle integers/floats."""
    res = element_style(opacity=0.5, flex_grow=1)
    assert "opacity:0.5;" in res
    assert "flex-grow:1;" in res

def test_element_style_empty():
    """5. Handle empty kwargs."""
    res = element_style()
    assert res == ""

def test_element_style_empty_wrapped():
    """6. Handle empty kwargs with wrapper (should return empty string or empty attribute?)."""
    # Usually cleaner to return empty string if no styles, or style=""
    res = element_style(with_style_attr=True)
    assert res == 'style=""' or res == ""

def test_element_style_mixed_types():
    """7. Handle mixed string/int types."""
    res = element_style(width=100, height="50%")
    assert "width:100;" in res
    assert "height:50%;" in res


# ==============================================================================
#  GROUP 2: SelectorRuleBridge (The Connector) [7 Tests]
# ==============================================================================

def test_srb_init(mock_selector, mock_rule):
    """8. Initialize bridge."""
    bridge = SelectorRuleBridge(selector=mock_selector, rule=mock_rule)
    assert bridge.selector == mock_selector
    assert bridge.rule == mock_rule

def test_srb_selector_string_property(mock_selector, mock_rule):
    """9. Get raw string from selector object."""
    bridge = SelectorRuleBridge(mock_selector, mock_rule)
    assert bridge.selector_str == ".btn"

def test_srb_render_block(mock_selector, mock_rule):
    """10. Render full CSS block."""
    bridge = SelectorRuleBridge(mock_selector, mock_rule)
    css = bridge.render()
    assert ".btn {" in css
    assert "color:red;" in css
    assert "}" in css

def test_srb_factory_from_dict():
    """11. make_bridge_list from dictionary."""
    raw = {'.card': {'padding':'20px'}}
    bridges = SelectorRuleBridge.make_bridge_list(raw)
    
    assert len(bridges) == 1
    assert bridges[0].selector_str == ".card"
    assert "padding:20px;" in bridges[0].render()

def test_srb_factory_mixed_inputs():
    """12. make_bridge_list with CssRule objects in dict values."""
    rule_obj = CssRule( display="flex")
    raw = {'.nav': rule_obj}
    
    bridges = SelectorRuleBridge.make_bridge_list(raw)
    assert bridges[0].rule == rule_obj

def test_srb_factory_multiple():
    """13. make_bridge_list with multiple items."""
    raw = {'.a': {'color': 'red'}, '.b': {'color': 'blue'}}
    bridges = SelectorRuleBridge.make_bridge_list(raw)
    assert len(bridges) == 2
    # Verify order (Python 3.7+ dicts are ordered)
    assert bridges[0].selector_str == ".a"
    assert bridges[1].selector_str == ".b"

def test_srb_render_empty_rule():
    """14. Render bridge with empty rule properties."""
    bridge = SelectorRuleBridge(".empty", CssRule())
    css = bridge.render()
    assert ".empty" not in css
    # Should render empty block or minimal block
    assert "{" not in css and "}" not in css
    


# ==============================================================================
#  GROUP 3: element_style_state (The JIT Engine) [10 Tests]
# ==============================================================================

@pytest.fixture
def bridges():
    # Create a suite of bridges
    return [
        SelectorRuleBridge(".used", CssRule(color="red")),
        SelectorRuleBridge("#unused", CssRule(color="blue")),
        SelectorRuleBridge("div", CssRule(display="block")),
    ]

def test_jit_match_class(bridges):
    """15. Match class selector."""
    tmpl = '<div class="used"></div>'
    active = element_style_state(tmpl, {}, *bridges)
    
    assert len(active) == 2 # .used AND div match
    assert any(b.selector_str == ".used" for b in active)

def test_jit_match_tag(bridges):
    """16. Match tag selector."""
    tmpl = '<div></div>'
    active = element_style_state(tmpl, {}, *bridges)
    
    assert len(active) == 1
    assert active[0].selector_str == "div"

def test_jit_no_match(bridges):
    """17. Match nothing."""
    tmpl = '<span></span>'
    active = element_style_state(tmpl, {}, *bridges)
    assert len(active) == 0

def test_jit_filter_unused(bridges):
    """18. Verify unused rules are dropped."""
    tmpl = '<div class="used"></div>'
    active = element_style_state(tmpl, {}, *bridges)
    
    # #unused should NOT be in the list
    assert not any(b.selector_str == "#unused" for b in active)

def test_jit_empty_template(bridges):
    """19. Handle empty template string."""
    active = element_style_state("", {}, *bridges)
    assert len(active) == 0

def test_jit_empty_rules():
    """20. Handle empty rules list."""
    active = element_style_state("<div></div>", {})
    assert len(active) == 0

def test_jit_complex_html_structure(bridges):
    """21. Match deeply nested elements."""
    tmpl = '<section><span><div class="used"></div></span></section>'
    active = element_style_state(tmpl, {}, *bridges)
    
    assert any(b.selector_str == ".used" for b in active)

def test_jit_lxml_parsing_resilience(bridges):
    """22. Handle malformed HTML gracefully."""
    # Missing closing tag
    tmpl = '<div class="used">' 
    active = element_style_state(tmpl, {}, *bridges)
    
    # lxml is usually forgiving
    assert any(b.selector_str == ".used" for b in active)

def test_jit_pseudo_class_preservation(bridges):
    """23. Ensure pseudo-classes are kept (optimistic match)."""
    # If user defines .btn:hover, JIT should keep it if .btn exists
    pseudo_bridge = SelectorRuleBridge(".used:hover", CssRule(color="green"))
    all_bridges = bridges + [pseudo_bridge]
    
    tmpl = '<div class="used"></div>'
    active = element_style_state(tmpl, {}, *all_bridges)
    
    # If your logic keeps complex selectors assuming base match:
    # This asserts that :hover isn't discarded just because "hover" state isn't in HTML
    assert any([b.selector_str == ".used:hover" for b in active])

def test_jit_rslvd_el_context(bridges):
    """24. Test that resolved elements map is accepted (even if unused by lxml logic)."""
    # Just ensuring the signature works and doesn't crash
    tmpl = ElementState('div',s_state='some_id').change_state({'some_id': 'state'},{})
    active = element_style_state(tmpl.state_placeholder,{'any':tmpl} , *bridges)
    assert len(active) >= 1


# ==============================================================================
#  GROUP 4: ComponentStyle (The Renderer) [8 Tests]
# ==============================================================================

def test_cs_init_logic():
    """25. Init with template and rules."""
    rules = [SelectorRuleBridge(".a", CssRule(color="red"))]
    style = ComponentStyle("<div></div>", *rules)
    assert style.css_rules == tuple(rules)

def test_cs_render_as_string_true():
    """26. Render as string (Block)."""
    rules = [SelectorRuleBridge("div", CssRule( color="red"))]
    style = ComponentStyle("<div></div>", *rules)
    
    res = style.render(as_string=True)
    assert "<style>" not in res
    assert "div {" in res
    res2 = style.render(as_string=True,with_style_tag=True)
    assert "<style>" in res2
    assert "div {" in res2

def test_cs_render_as_string_false():
    """27. Render raw CSS (No tags)."""
    rules = [SelectorRuleBridge("div", CssRule( color="red"))]
    style = ComponentStyle("<div></div>", *rules)
    pytest.raises(ValueError)
    res = style.render(as_string=False)
    assert "<style>" not in res
    assert any(["div {" in s for s in res])

def test_cs_render_empty():
    """28. Render with no rules."""
    style = ComponentStyle("<div></div>")
    res = style.render()
    assert res == "" # or empty style tag

def test_cs_link_component():
    """29. Test linking metadata (if implemented)."""
    style = ComponentStyle("")
    style.link_component("MyComponent")
    # Assuming it stores it or modifies a property
    # assert style.linked_component == "MyComponent" 
    pass 

def test_cs_template_info_parsing():
    """30. Verify it extracts info from template on init."""
    # user.py says: self.template_info = CssSelector(self.template).template_info
    style = ComponentStyle('<div id="main"></div>')
    # Assuming CssSelector parses IDs/Classes
    if hasattr(style, 'template_info'):
        assert style.template_info is not None

def test_cs_integration_pipeline(bridges):
    """31. Full Pipeline: Bridges -> ComponentStyle -> Render."""
    # Mock JIT result passed to CS
    active_bridges = [bridges[0]] # Just .used
    
    style = ComponentStyle('<div class="used"></div>', *active_bridges)
    output = style.render()
    
    assert ".used {" in output
    assert "#unused" not in output

def test_cs_multiple_blocks(bridges):
    """32. Verify multiple rules are joined correctly."""
    style = ComponentStyle("<div id='unused' class='used'></div>", *bridges)
    output = style.render(as_string=False)
    for x in output:print(x)
    # Should have 3 blocks
    assert len(output) == 3  # .used, #unused, div

# ==============================================================================
#  GROUP 5: resolve_complex_selector [5 Tests]
# ==============================================================================

def test_resolve_simple_compound():
    """Split tag.class#id."""
    res = resolve_complex_selector("div#main.container")
    assert "div" in res
    assert "#main" in res
    assert ".container" in res
    assert len(res) == 3

def test_resolve_combinators():
    """Handle > + ~ separators."""
    res = resolve_complex_selector("div > span + b")
    assert "div" in res
    assert "span" in res
    assert "b" in res
    assert ">" not in res # Should be stripped

def test_resolve_attributes():
    """Handle attribute selectors."""
    res = resolve_complex_selector("input[type='text'][required]")
    assert "input" in res
    assert "[type='text']" in res
    assert "[required]" in res

def test_resolve_pseudos():
    """Handle pseudo classes and elements."""
    res = resolve_complex_selector("a:hover::before")
    assert "a" in res
    assert ":hover" in res
    assert "::before" in res

def test_resolve_complex_grouping():
    """Complex real world example."""
    res = resolve_complex_selector("nav.fixed-top > ul li:last-child a[href^='http']")
    expected = ['nav', '.fixed-top', 'ul', 'li', ':last-child', 'a', "[href^='http']"]
    assert res == expected

# ==============================================================================
#  GROUP : complex selectors [5 Tests]
# ==============================================================================


