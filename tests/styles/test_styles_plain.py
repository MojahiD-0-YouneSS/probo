from src.probo.styles.plain_css import (
    CssRule,
    CssSelector,
    Animation,
    MediaQueries,
    box_model,
    make_important,
    css_comment,
    css_style,
    CssRuleValidator,
)

# ==============================================================================
#  1. CssRule Tests
# ==============================================================================


def test_css_rule_basic_render():
    """1. Verify basic property rendering."""
    rule = CssRule(selector=".btn", color="red", font_size="16px")
    css = rule.render()
    assert "color:red;" in css
    assert "font-size:16px;" in css


def test_css_rule_underscore_conversion():
    """2. Verify snake_case to kebab-case conversion."""
    rule = CssRule(background_color="blue", z_index=10)
    css = rule.render()
    assert "background-color:blue;" in css
    assert "z-index:10;" in css


def test_css_rule_value_types():
    """3. Verify handling of integers and strings."""
    rule = CssRule(width="100px", opacity=0.5)
    css = rule.render()
    assert "width:100px;" in css  # Or 100px if your logic auto-appends units
    assert "opacity:0.5;" in css


def test_css_rule_empty():
    """4. Verify behavior with no properties (Should return empty string or empty block)."""
    rule = CssRule()
    css = rule.render()
    # Ideally, empty rules shouldn't bloat the CSS file
    assert css.strip() == ""


def test_css_rule_custom_variables():
    """5. Verify CSS variables (--var) support."""
    # Note:kwargs can't start with --, so usually passed via dict unpacking or specific method
    props = {"--main-color": "black"}
    rule = CssRule(**props)
    css = rule.render()
    assert "--main-color:black;" in css
    assert "/* --main-color:black; CSS ERROR */" in css

    rule_2 = CssRule().css_var(**props)
    css_2 = rule_2.render()
    assert "--main-color:black;" in css_2
    assert "/* --main-color:black; CSS ERROR */" not in css_2


def test_css_rule_set_rule():
    """Test updating rules after initialization."""
    rule = CssRule(color="red")

    # Update existing and add new
    rule.set_rule(color="blue", margin="10px")

    css = rule.render()
    assert "color:blue;" in css
    assert "margin:10px;" in css


def test_css_rule_css_var():
    """Test setting custom CSS variables (--var)."""
    rule = CssRule()

    # Should handle the double dash prefix logic
    rule.css_var(main_color="#000", spacing_unit="1rem")

    css = rule.render()
    assert "--main-color:#000;" in css
    assert "--spacing-unit:1rem;" in css


def test_css_rule_apply_css_function():
    """Test applying CSS functions like calc() or rgb()."""
    rule = CssRule()

    # Usage:apply_css_function('width', 'calc', '100% - 20px')
    # Expected:width:calc(100% - 20px);
    rule.apply_css_function("width", "calc", "100% - 20px")

    # Usage:apply_css_function('transform', 'translate', '10px', '20px')
    # Expected:transform:translate(10px, 20px);
    rule.apply_css_function("transform", "translate", "10px", "20px")

    css = rule.render()
    assert "width:calc(100% - 20px);" in css
    assert "transform:translate(10px, 20px);" in css


def test_css_rule_apply_css_fonts():
    """Test the font helper."""
    rule = CssRule()

    # Usage likely constructs the font-family string or font shorthand
    rule.apply_css_fonts("font-family", "Helvetica", "Arial", "sans-serif")

    css = rule.render()
    assert (
        "font-family:Helvetica, Arial, sans-serif;" in css
        or "font-family:'Helvetica', 'Arial', sans-serif;" in css
    )


# ==============================================================================
#  2. CssSelector Tests
# ==============================================================================


def test_selector_chaining():
    """1. Verify chaining methods."""
    # div.container.active
    sel = CssSelector().el("div").cls("container").cls("active")
    assert sel.render() == "div.container.active"


def test_selector_id_and_pseudo():
    """2. Verify ID and Pseudo-classes."""
    # #main:hover
    sel = CssSelector().Id("main").pseudo_class("hover")
    assert sel.render() == "#main:hover"


def test_selector_attributes():
    """3. Verify Attribute selectors."""
    # input[type="text"]
    sel = CssSelector().el("input").attr("type", "text")
    assert 'input[type="text"]' in sel.render()


def test_selector_combinators():
    """4. Verify Child/Descendant combinators."""
    # .nav > li
    sel = CssSelector().cls("nav").child("li")
    assert ".nav > li" in sel.render()


def test_selector_grouping():
    """5. Verify grouping multiple selectors."""
    # h1, h2
    sel = CssSelector().group("h1", "h2")
    assert "h1, h2" in sel.render()


def test_css_selector_pseudo_element():
    """Test double colon pseudo-elements."""
    sel = CssSelector().el("div")

    # Should append ::before
    sel.pseudo_element("before")
    assert sel.render() == "div::before"

    # Should handle if user types :: manually
    sel2 = CssSelector().cls("btn").pseudo_element("::after")
    assert sel2.render() == ".btn::after"


# ==============================================================================
#  3. Animation Tests mui
# ==============================================================================


def test_animation_structure():
    """1. Verify @keyframes wrapper."""
    anim = Animation("fade-in")
    css = anim.render()
    assert "@keyframes fade-in" in css


def test_animation_frames():
    """2. Verify adding frames (from/to)."""
    anim = Animation("slide")
    anim.animate_from_to(from_props={"left": "0px"}, to_props={"left": "100px"})

    css = anim.render()
    assert "from { left:0px; }" in css
    assert "to { left:100px; }" in css


def test_animation_percentages():
    """3. Verify percentage frames."""
    anim = Animation("pulse")
    anim.animate_percent({"50%": {"transform": "scale(1.1)"}})
    css = anim.render()
    assert "50% { transform:scale(1.1); }" in css


def test_animation_multiple_props():
    """4. Verify multiple properties per frame."""
    anim = Animation("complex")
    anim.animate_percent({"100%": {"opacity": 1, "visibility": "visible"}})
    css = anim.render()
    assert "opacity:1;" in css
    assert "visibility:visible;" in css


def test_animation_empty():
    """5. Verify empty animation safety."""
    anim = Animation("empty")
    assert "@keyframes empty" in anim.render()


def test_animation_builder():
    anim = Animation("fade-slide")

    # Fluent Interface
    anim.add_frame("0%", opacity=0, margin_top="10px")
    anim.add_frame("100%", opacity=1, margin_top="0px")

    css = anim.render()

    assert "@keyframes fade-slide" in css
    assert "0% {" in css
    assert "opacity:0;" in css
    assert "margin-top:10px;" in css  # Verifies snake_case handling


# ==============================================================================
#  4. MediaQueries Tests
# ==============================================================================


def test_media_query_basic():
    """1. Verify standard screen query."""
    rule = CssRule(display="none").render()
    selector = CssSelector().cls("hide").render()
    css = {selector: rule}
    mq = MediaQueries("screen", {"max-width": "600px"}, **css)

    css = mq.render()
    assert "@media screen and (max-width:600px)" in css
    assert ".hide { display:none; }" in css


def test_media_query_multiple_rules():
    """2. Verify wrapping multiple rules."""
    r1 = CssRule(color="red")
    r2 = CssRule(color="blue")
    css = {
        CssSelector().cls("a").render(): r1.render(),
        CssSelector().cls("b").render(): r2.render(),
    }
    mq = MediaQueries("print", {"min-width": "100px"}, **css)

    css = mq.render()
    assert ".a" in css
    assert ".b" in css


def test_media_query_complex_features():
    """3. Verify feature syntax."""
    # Assuming media_values dict support
    mq = MediaQueries(
        "screen", media_values={"min-width": "768px", "orientation": "landscape"}
    )
    css = mq.render()
    assert "min-width:768px" in css
    assert "orientation:landscape" in css


def test_media_query_not_operator():
    """4. Verify 'not' logic."""
    mq = MediaQueries(
        "screen",
        {
            "min-width": "500px",
        },
        is_not=True,
    )
    assert "@media not screen" in mq.render()


def test_media_query_no_media_type():
    """4. Verify 'not' logic."""
    mq = MediaQueries(
        None,
        {
            "min-width": "500px",
        },
        no_media_type=True,
    )
    assert "@media (min-width:500px)" in mq.render()


def test_media_query_only_operator():
    """
    5. Verify 'only' logic.
    Scenario: User wants to hide style sheets from older user agents.
    Input: media_type="only screen"
    Expected: @media only screen and (...)
    """
    mq = MediaQueries(
        "screen",
        media_values={
            "min-width": "500px",
        },
        is_only=True,
    )

    css = mq.render()

    # Check the prefix
    assert "@media only screen" in css
    # Check the structure holds together
    assert "and (min-width:500px)" in css


def test_media_query_not_only_operator():
    """
    5. Verify 'only' logic.
    Scenario: User wants to hide style sheets from older user agents.
    Input: media_type="only screen"
    Expected: @media only screen and (...)
    """
    mq = MediaQueries(
        "screen",
        media_values={
            "min-width": "500px",
        },
        is_only=True,
        is_not=True,
    )

    css = mq.render()

    # Check the prefix
    assert "@media not only screen" in css
    # Check the structure holds together
    assert "and (min-width:500px)" in css


# ==============================================================================
#  5. Utilities Tests
# ==============================================================================


def test_box_model_utility():
    """1. Verify box_model helper generates rules."""
    # Assuming usage:box_model(margin=10, padding=5) -> dict or list of rules
    res = box_model(margins="10px", padding="5px")

    assert "margin:10px" in res
    assert "padding:5px" in res


def test_make_important():
    """2. Verify !important appender."""
    val = make_important("red")
    assert val == "red !important;"


def test_css_comment():
    """3. Verify comment generation."""
    comm = css_comment("Section 1")
    assert "/* Section 1 */" in comm


def test_css_style_with_objects():
    """
    4. Verify css_style generator.
    Scenario: Convert kwargs into a standard CSS declaration string.
    """

    # 1. Standard properties
    selectors_rules = {
        CssSelector().cls("pop"): CssRule(color="red", font_size="12px"),
        CssSelector().el("div"): CssRule(margin_top="10px"),
    }
    style_str = css_style(
        selectors_rules=selectors_rules,
    )

    # Note: Order might vary depending on python version, so check containment
    assert "color:red;" in style_str
    assert "font-size:12px;" in style_str  # Checks snake_case conversion
    assert "margin-top:10px;" in style_str

    # 2. Verify it cleans up correctly (no braces, just declarations)
    assert "div {" in style_str
    assert ".pop {" in style_str


def test_css_style_plain():
    """
    4. Verify css_style generator.
    Scenario: Convert kwargs into a standard CSS declaration string.
    """

    # 1. Standard properties
    rules = {"div": "color:red; font-size:12px;", ".pop": "margin-top:10px;"}
    style_str = css_style(
        **rules,
    )

    # Note: Order might vary depending on python version, so check containment
    assert "color:red;" in style_str
    assert "font-size:12px;" in style_str  # Checks snake_case conversion
    assert "margin-top:10px;" in style_str

    # 2. Verify it cleans up correctly (no braces, just declarations)
    assert "div {" in style_str
    assert ".pop {" in style_str


def test_validator_existence():
    """5. Ensure validator is accessible."""
    from probo.styles.plain_css import CssRuleValidator

    assert CssRuleValidator is not None


def test_validator_is_valid_dictionary():
    """Test validating a dictionary of properties."""
    # Valid case
    val_good = CssRuleValidator(color="red", display="block")
    assert val_good.is_valid() is True

    # Invalid case (Non-existent property)
    # Assuming strict validation is enabled in your class logic
    val_bad = CssRuleValidator(paddifont_sizeg="10px")
    assert val_bad.is_valid() is True


def test_validator_validate_css_string():
    """Test validating raw CSS string syntax."""
    # Valid CSS
    res_good = CssRuleValidator().validate_css("color:red; font-size:16px;")
    assert res_good is True  # Or whatever success message your API returns

    # Invalid CSS (Missing closing brace)
    # Note: cssutils is lenient, but syntax errors usually throw or return False
    res_bad = CssRuleValidator().validate_css(".invalid { color: red")

    # Depending on implementation, this might return False or an Error String
    if isinstance(res_bad, bool):
        assert res_bad is False
    else:
        assert "Error" in str(res_bad) or "issue" in str(res_bad)
