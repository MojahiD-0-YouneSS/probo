from src.probo import (
    div,
    span,
    img,
    Input,
    fieldset,
    legend,
DIV,

)


def test_basic_block_render():
    """Test a standard block element with content and attributes."""
    element = div("Hello World", Id="main", Class="container")
    expected = '<div id="main" class="container">Hello World</div>'
    assert element == expected


def test_basic_inline_render():
    """Test inline elements."""
    element = span("Text", style="color: red;")
    assert element == '<span style="color: red;">Text</span>'


def test_void_element_render():
    """Test self-closing tags (void elements). Content should be ignored."""
    # img is void, so 'Content' should NOT appear in the output
    element = img(src="logo.png", alt="Logo")
    assert element == '<img src="logo.png" alt="Logo"/>'


def test_nesting():
    """Test that elements render children correctly recursively."""
    element = div(span("Child 1"), div("Child 2"), Class="parent")
    # Note: Your renderer likely produces minified HTML (no newlines)
    expected = '<div class="parent"><span>Child 1</span><div>Child 2</div></div>'
    assert element == expected


def test_attribute_cleaning():
    """Test that False/None attributes are removed, but 0 or empty strings are kept."""
    element = Input(
        Type="text",
        required=True,
        disabled=False,  # Should be removed
        value=0,  # Should be kept
        placeholder="",  # Should be kept
    )
    rendered = element

    assert "required" in rendered
    assert "disabled" not in rendered
    assert 'value="0"' in rendered
    assert 'placeholder=""' in rendered


def test_newly_added_tags():
    """Test the tags you added recently (fieldset, legend)."""
    element = fieldset(legend("Zone"))
    assert element == "<fieldset><legend>Zone</legend></fieldset>"


def test_doctype_render():
    from probo import doctype

    """Test that doctype renders without a closing slash."""
    el = doctype()
    # Should be exactly this, no "/>"
    assert el == "<!DOCTYPE html>"

def test_render_constraints_kwarg():
    """Test that render_constraints kwarg is parsed and evaluated correctly."""
    # Create an element with a render constraint
    element = DIV("Content", render_constraints={"user_logged_in": True})
    # Should be recorded in _render_conditions
    assert element._render_conditions == {"user_logged_in": True}
    
    # Simulate data pipeline where condition is met
    element.load_data({"user_logged_in": True})
    assert element.render() == "<div>Content</div>"
    
    # Simulate data pipeline where condition is not met
    element_fail = DIV("Content", render_constraints={"user_logged_in": True})
    element_fail.load_data({"user_logged_in": False})
    # When constraints fail, element renders as empty
    assert element_fail.render() == "<div></div>"

