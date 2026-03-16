from src.probo import (
    DIV,
    SPAN,
    IMG,
    INPUT,
    FIELDSET,
    LEGEND,
)


def test_basic_block_render():
    """Test a standard block element with content and attributes."""
    element = DIV("Hello World", Id="main", Class="container").render()
    expected = '<div id="main" class="container">Hello World</div>'
    assert element == expected


def test_basic_inline_render():
    """Test inline elements."""
    element = SPAN("Text", style="color: red;").render()
    assert element == '<span style="color: red;">Text</span>'


def test_void_element_render():
    """Test self-closing tags (void elements). Content should be ignored."""
    # img is void, so 'Content' should NOT appear in the output
    element = IMG(src="logo.png", alt="Logo").render()
    assert element == '<img src="logo.png" alt="Logo"/>'


def test_nesting():
    """Test that elements render children correctly recursively."""
    element = DIV(SPAN("Child 1"), DIV("Child 2"), Class="parent").render()
    print(SPAN("Child 1",SPAN("Child 2",Class='2',Id='2'),Class='1',Id='1').render())
    # Note: Your renderer likely produces minified HTML (no newlines)
    expected = '<div class="parent"><span>Child 1</span><div>Child 2</div></div>'
    assert element == expected


def test_attribute_cleaning():
    """Test that False/None attributes are removed, but 0 or empty strings are kept."""
    element = INPUT(
        Type="text",
        required=True,
        disabled=False,  # Should be removed
        value=0,  # Should be kept
        placeholder="",  # Should be kept
    )
    rendered = element.render()

    assert "required" in rendered
    assert "disabled" not in rendered
    assert 'value="0"' in rendered
    assert 'placeholder=""' in rendered


def test_newly_added_tags():
    """Test the tags you added recently (fieldset, legend)."""
    element = FIELDSET(LEGEND("Zone")).render()
    assert element == "<fieldset><legend>Zone</legend></fieldset>"


def test_doctype_render():
    from probo import DOCTYPE

    """Test that doctype renders without a closing slash."""
    el = DOCTYPE().render()
    # Should be exactly this, no "/>"
    assert el == "<!DOCTYPE html>"
