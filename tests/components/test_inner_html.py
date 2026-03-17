import pytest
from probo import DIV, P, STRONG, H1

def test_basic_replacement():
    """Verify that inner_html replaces existing text content."""
    node = DIV("Original Content")
    node.inner_html("New Content")
    
    assert "New Content" in node.render()
    assert "Original Content" not in node.render()

def test_tag_replacement():
    """Verify that inner_html can replace text with complex Tag structures."""
    node = DIV("Text Only")
    # Swap with a structured tree
    node.inner_html(
        H1("Title"),
        P("Description", STRONG(" - Bolded"))
    )
    
    html = node.render()
    assert "<h1>Title</h1>" in html
    assert "<strong> - Bolded</strong>" in html
    assert "Text Only" not in html

def test_chainability():
    """Ensure inner_html returns  for fluid API usage."""
    node = DIV().inner_html("Chained Content")
    assert "Chained Content" in node.render()

def test_clearing_content():
    """Verify that passing no arguments effectively clears the node."""
    node = DIV("I will disappear")
    node.inner_html()
    
    # Should render an empty tag
    assert node.render() == "<div></div>"

def test_nested_inner_html():
    """Verify inner_html works correctly on nested children."""
    parent = DIV(P("Child 1"), P("Child 2"))
    
    # Target a specific child to change its inner HTML
    first_child = parent.content[0]
    first_child.inner_html(STRONG("Updated Child"))
    
    html = parent.render()
    assert "<p><strong>Updated Child</strong></p>" in html
    assert "<p>Child 2</p>" in html
