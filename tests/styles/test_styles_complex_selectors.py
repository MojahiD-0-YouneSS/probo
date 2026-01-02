from src.probo.styles.plain_css import CssRule, CssSelector

# ==============================================================================
#  COMPLEX SELECTOR SCENARIOS
# ==============================================================================


def test_selector_descendant_logic():
    """
    1. Descendant Combinator (Space).
    Scenario: Targeting spans inside a navigation bar.
    Expected: "nav .menu-item span"
    """
    # Assuming your API supports a generic 'descendant' or implied space via chaining
    # If not, testing manual string construction or specific method
    sel = CssSelector().el("nav").cls("menu-item").descendant("span")

    # Result should imply a space
    assert sel.render() == "nav.menu-item span"


def test_selector_direct_child():
    """
    2. Child Combinator (>).
    Scenario: Direct list items of a specific list.
    Expected: "ul.clean-list > li"
    """
    sel = CssSelector().el("ul").cls("clean-list").child("li")
    assert sel.render() == "ul.clean-list > li"


def test_selector_adjacent_sibling():
    """
    3. Adjacent Sibling (+).
    Scenario: Paragraphs immediately following an H1.
    Expected: "h1 + p"
    """
    sel = CssSelector().adjacent("h1", "p")
    assert sel.render() == "h1 + p"


def test_selector_general_sibling():
    """
    4. General Sibling (~).
    Scenario: All images following a break tag.
    Expected: "br ~ img"
    """
    sel = CssSelector().sibling("br", "img")
    assert sel.render() == "br ~ img"


def test_selector_attribute_exact():
    """
    5. Attribute Exact Match.
    Scenario: Inputs with specific type.
    Expected: "input[type='password']"
    """
    sel = CssSelector().el("input").attr("type", "password")
    assert (
        "input[type='password']" in sel.render()
        or 'input[type="password"]' in sel.render()
    )


def test_selector_attribute_partial_match():
    """
    6. Attribute Partial Match (Start/Contains).
    Scenario: Links pointing to secure sites.
    Expected: "a[href^='https']"
    """
    # Assuming API supports op argument
    sel = CssSelector().el("a").attr("href", "https", op="^=")
    assert 'a[href^="https"]' in sel.render()


def test_selector_pseudo_class_chain():
    """
    7. Chaining Pseudo-classes.
    Scenario: Hover state on a non-disabled button.
    Expected: "button:hover:not(:disabled)"
    """
    sel = (
        CssSelector().el("button").pseudo_class("hover").pseudo_class("not(:disabled)")
    )
    assert sel.render() == "button:hover:not(:disabled)"


def test_selector_pseudo_element_double_colon():
    """
    8. Pseudo-elements (Double Colon).
    Scenario: Styling the first line of a paragraph.
    Expected: "p.intro::first-line"
    """
    sel = CssSelector().el("p").cls("intro").pseudo_element("first-line")
    # Ensure double colon is used
    assert "::first-line" in sel.render()
    assert "p.intro" in sel.render()


def test_selector_complex_grouping():
    """
    9. Grouping (Comma Separated).
    Scenario: Applying same style to H1, H2, and specific class.
    Expected: "h1, h2, .display-text"
    """
    # Assuming .group() creates a split point or adds a new selector obj
    sel = CssSelector().group("h1", "h2").group().cls("display-text")

    res = sel.render()
    assert "h1" in res
    assert "h2" in res
    assert ".display-text" in res
    assert "," in res


def test_rule_integration_complex():
    """
    10. Integration: CssRule with a complex Selector object.
    Scenario: Full rule generation for a specific UI state.
    """
    # "div#main > .card:hover"
    complex_sel = (
        CssSelector().el("div").Id("main").child(".card").pseudo_class("hover").render()
    )

    rule = CssRule(box_shadow="0 4px 8px rgba(0,0,0,0.1)", transform="translateY(-2px)")

    css = rule.render()

    # Check Selector
    assert "div#main > .card:hover" in complex_sel
    # Check Properties (snake_case conversion)
    assert "box-shadow:" in css
    assert "transform:" in css
    assert "translateY(-2px)" in css


# ==============================================================================
#  COMPLEX SELECTOR SCENARIOS
# ==============================================================================


def test_selector_fix_tag_collision():
    """
    1. Invalid: divspan (Tag after Tag)
    Scenario: User chains .el('div').el('span')
    Expected Fix: "div span" (Implicit Descendant)
    """
    sel = CssSelector().el("div").el("span")
    assert sel.render() == "div span"


def test_selector_fix_tag_after_class():
    """
    2. Invalid: .btnspan (Tag directly after Class)
    Scenario: User chains .cls('btn').el('span')
    Expected Fix: ".btn span" (Implicit Descendant)
    """
    sel = CssSelector().cls("btn").el("span")
    assert sel.render() == ".btn span"


def test_selector_fix_tag_after_id():
    """
    3. Invalid: #headerdiv (Tag directly after ID)
    Scenario: User chains .id('header').el('div')
    Expected Fix: "#header div" (Implicit Descendant)
    """
    sel = CssSelector().Id("header").el("div")
    assert sel.render() == "#header div"


def test_selector_fix_tag_after_pseudo():
    """
    4. Invalid: :hoverdiv (Tag directly after Pseudo-class)
    Scenario: User chains .pseudo_class('hover').el('div')
    Expected Fix: ":hover div" (Implicit Descendant)
    """
    sel = CssSelector().pseudo_class("hover").el("div")
    assert sel.render() == ":hover div"


def test_selector_pseudo_element_lock():
    """
    5. Logical Invalidity: ::before:hover (Pseudo-class after Pseudo-element)
    Scenario: User tries to add a state to a pseudo-element incorrectly.
    Expected Fix: Implicitly treat it as a new branch (Descendant) or handle gracefully.
    Based on the logic: "::before :hover"
    """
    # If your logic adds a space when appending to a pseudo-element:
    sel = CssSelector().el("div").pseudo_element("before").pseudo_class("hover")

    # This depends on your specific implementation choice for the "Lock" logic.
    # Assuming you insert a combinator to prevent invalid syntax:
    assert (
        sel.render() == "div::before :hover" or sel.render() == "div::before > :hover"
    )


from src.probo.styles.utils import selector_type_identifier


def test_selector_identifier_basic():
    # Element
    assert selector_type_identifier("div") == ("div", "EL")
    assert selector_type_identifier("h1") == ("h1", "EL")

    # Class
    assert selector_type_identifier(".btn") == ("btn", "CLS")
    assert selector_type_identifier(".btn-primary") == ("btn-primary", "CLS")

    # ID
    assert selector_type_identifier("#main") == ("main", "ID")


def test_selector_identifier_pseudos():
    # Pseudo Class
    assert selector_type_identifier(":hover") == ("hover", "PSEUDO_CLASS")
    assert selector_type_identifier(":nth-child(2)") == ("nth-child(2)", "PSEUDO_CLASS")

    # Pseudo Element
    assert selector_type_identifier("::before") == ("before", "PSEUDO_ELEMENT")
    # Legacy single colon pseudo-elements often treated as Class by simple parsers,
    # but :: strictly catches Element.


def test_selector_identifier_attributes():
    # Attribute
    assert selector_type_identifier("[disabled]") == ("disabled", "ATR")
    assert selector_type_identifier('[type="text"]') == ('type="text"', "ATR")


def test_selector_identifier_combinators():
    assert selector_type_identifier(">") == (">", "COMBINATOR >")
    assert selector_type_identifier("+") == ("+", "COMBINATOR +")
    assert selector_type_identifier("~") == ("~", "COMBINATOR ~")
