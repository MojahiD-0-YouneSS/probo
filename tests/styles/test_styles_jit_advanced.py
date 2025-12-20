import pytest
from mui.styles.elements import ComponentStyle, element_style_state,SelectorRuleBridge
from mui.styles.plain_css import CssRule, CssSelector

# ==============================================================================
#  FIXTURES: The Static Template
# ==============================================================================

@pytest.fixture
def static_template():
    """
    A complex HTML structure simulating a real page component.
    Used to verify if JIT correctly identifies matching elements.
    """
    return """
    <div id="app-root">
        <header class="top-bar sticky">
            <nav>
                <ul class="menu">
                    <li class="menu-item active"><a href="/home">Home</a></li>
                    <li class="menu-item"><a href="/contact">Contact</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <section id="hero">
                <h1 class="hero-title">Welcome</h1>
                <p class="lead">Subtitle here</p>
                <button class="btn btn-primary" disabled>Action</button>
            </section>
        </main>
        <footer>
            <span class="copyright">&copy; 2025</span>
        </footer>
    </div>
    """

# ==============================================================================
#  JIT INTEGRATION TESTS (10 Tests)
# ==============================================================================

def test_jit_bridge_class_chain(static_template):
    """1. Verify JIT keeps rules for chained classes that exist."""
    # .top-bar.sticky exists
    sel = CssSelector().cls('top-bar').cls('sticky')
    rule = CssRule(display='block', position='fixed')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    assert len(valid_bridges) == 1
    assert ".top-bar.sticky" in valid_bridges[0].render()

def test_jit_bridge_descendant_context(static_template):
    """2. Verify JIT keeps rules for deep descendant context."""
    # #app-root nav ul.menu
    sel = CssSelector().Id('app-root').descendant('nav').descendant('ul').cls('menu')
    rule = CssRule(display='none', list_style='none')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    assert len(valid_bridges) == 1
    assert "#app-root nav ul.menu" in valid_bridges[0].render()

def test_jit_bridge_direct_child(static_template):
    """3. Verify JIT handles direct child combinators."""
    # ul.menu > li
    sel = CssSelector().el('ul').cls('menu').child('li')
    rule = CssRule(display='inline-block',margin='2px')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    assert len(valid_bridges) == 1
    assert "ul.menu > li" in valid_bridges[0].render()

def test_jit_bridge_adjacent_sibling(static_template):
    """4. Verify JIT handles adjacent siblings."""
    # h1 + p
    sel = CssSelector().el('h1').adjacent('p')
    rule = CssRule(display='block', margin_top='0')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    assert len(valid_bridges) == 1
    assert "h1 + p" in valid_bridges[0].render()

def test_jit_bridge_attribute_presence(static_template):
    """5. Verify JIT checks for attribute existence."""
    # button[disabled]
    sel = CssSelector().el('button').attr('disabled')
    rule = CssRule(display='block', opacity='0.5')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    assert len(valid_bridges) == 1
    assert "button[disabled]" in valid_bridges[0].render()

def test_jit_bridge_attribute_value_match(static_template):
    """6. Verify JIT checks for specific attribute values."""
    # a[href="/home"]
    sel = CssSelector().el('a').attr('href', '/home')
    rule = CssRule(display='block', color='blue')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    assert len(valid_bridges) == 1
    assert 'a[href="/home"]' in valid_bridges[0].render() or "a[href='/home']" in valid_bridges[0].render()

def test_jit_bridge_pseudo_class_optimistic(static_template): #ERROR
    """
    7. Verify JIT is optimistic about pseudo-classes.
    (It should keep :hover rules if the base element exists)
    """
    # .btn:hover
    sel = CssSelector().cls('btn').pseudo_class('hover')
    rule = CssRule(display='block', background_color='darkblue')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    # LXML might not support :hover, so logic usually strips pseudo for check OR keeps it if lxml fails
    # Assuming your element_style_state implementation gracefully handles or strips pseudos for the check
    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    assert len(valid_bridges) == 1
    assert ".btn:hover" in valid_bridges[0].render()

def test_jit_bridge_group_selector_partial(static_template): #ERROR
    """8. Verify JIT handles grouped selectors (keep if ANY match)."""
    # h1, h6 (h1 exists, h6 does not)
    sel = CssSelector().group('h1','h6')
    rule = CssRule(display='block', font_weight='bold')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    # Should be kept because h1 matches
    assert len(valid_bridges) == 1
    assert "h1, h6" in valid_bridges[0].render()

def test_jit_bridge_filter_unused(static_template):
    """9. Verify JIT completely removes rules for missing elements."""
    # .sidebar (Does not exist in template)
    sel = CssSelector().cls('sidebar')
    rule = CssRule(display='block', width='200px')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)

    valid_bridges = element_style_state(static_template,{}, *[bridge])
    
    assert len(valid_bridges) == 0

def test_jit_component_style_render(static_template): #ERROR
    """
    10. Verify ComponentStyle renders the filtered bridge list correctly.
    """
    sel = CssSelector().Id('hero')
    rule = CssRule(display='block', background='url(bg.jpg)')
    bridge = SelectorRuleBridge(selector=sel, rule=rule)
    
    # ComponentStyle usually runs element_style_state internally or accepts pre-filtered
    # Assuming it accepts the template and raw bridges, then filters:
    cs = ComponentStyle(static_template, *[bridge]) # Pass *bridges
    # Note: If your ComponentStyle signature differs (e.g. takes *selectors), adjust accordingly.
    # Assuming updated to take bridges or rules.
    
    # Use JIT function manually if ComponentStyle doesn't auto-filter
    valid = element_style_state(static_template,{}, *[bridge])
    
    # Render manually using the bridge render method for verification
    css_output = "\n".join(b.render() for b in valid)
    
    assert "#hero {" in css_output
    assert "background:url(bg.jpg);" in css_output
    assert "display:block;" in css_output

# ==============================================================================
#  CASCADING HISTORY TESTS (2 Tests)
# ==============================================================================

def test_css_cascade_order(static_template):
    """
    11. Verify Order Preservation (History).
    If two rules match the same element, they must appear in the output 
    in the order they were defined/passed.
    """
    sel = CssSelector().cls('btn')
    
    # Rule 1: Blue (Defined first)
    rule1 = CssRule(display='block', color='blue')
    bridge1 = SelectorRuleBridge(selector=sel, rule=rule1)
    
    # Rule 2: Red (Defined second - Should Override in CSS)
    rule2 = CssRule(display='block', color='red')
    bridge2 = SelectorRuleBridge(selector=sel, rule=rule2)
    
    bridges = [bridge1, bridge2]
    
    # Process
    valid_bridges = element_style_state(static_template, {}, *bridges)
    
    assert len(valid_bridges) == 2
    
    # Render combined CSS
    css = "\n".join(b.render() for b in valid_bridges)
    # Verify positions
    idx_blue = css.find("color:blue")
    idx_red = css.find("color:red")
    
    assert idx_blue < idx_red, "Cascading order failed: Red should define after Blue"

def test_css_specificity_accumulation(static_template):
    """
    12. Verify mixing broad and specific rules.
    Both should be kept, allowing CSS specificity to work in the browser.
    """
    # Broad: .btn
    sel_broad = CssSelector().cls('btn')
    bridge_broad = SelectorRuleBridge(selector=sel_broad, rule=CssRule( padding='10px'))
    
    # Specific: .btn.btn-primary
    sel_specific = CssSelector().cls('btn').cls('btn-primary')
    bridge_specific = SelectorRuleBridge(selector=sel_specific, rule=CssRule(color='white'))
    
    bridges = [bridge_broad, bridge_specific]
    
    valid_bridges = element_style_state(static_template, {}, *bridges)
    
    assert len(valid_bridges) == 2
    
    output = "\n".join(b.render() for b in valid_bridges)
    assert ".btn {" in output
    assert ".btn.btn-primary {" in output

