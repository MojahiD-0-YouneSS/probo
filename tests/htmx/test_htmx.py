import pytest
from mui.htmx.htmx import HTMX, HTMXElement 
# Assuming these classes wrap elements or generate attr dicts

def test_htmx_element_attributes():
    """Test generating hx attributes via helper."""
    # Usage might be: HTMXElement(tag='div', hx_get='/api', hx_swap='outerHTML')
    # Or a helper that returns attributes
    
    # Example usage based on typical patterns:
    el = HTMXElement(
        'button', 
        'Click Me', 
        hx_get="/clicked", 
        hx_target="#result"
    )
    
    html = el.render()
    print(html)
    assert 'hx-get="/clicked"' in str(html)
    assert 'hx-target="#result"' in str(html)

def test_htmx_enums_integration():
    """
    Test that Enums (like HxSwap) resolve to strings.
    """
    # Assuming you allow passing Enum or String
    from mui.htmx.htmx_enum import HxSwap
    
    el = HTMXElement('div', hx_swap=HxSwap.OUTER_HTML.value) # or however enum is named
    html = el.render()
    
    # Should convert Enum -> "outerHTML"
    assert 'hx-swap="outerHTML"' in str(html) or 'hx-swap="outerHTML"' in str(html).replace("'", '"')
    

def test_fluent_api_chaining():
    """
    Scenario: Building an HTMX button using method chaining.
    Expected: <button hx-post="/save" hx-target="#status">Save</button>
    """
    btn = HTMXElement( element_tag="button", content="Save",Class="save_btn",)
    
    # Chaining methods (The "Ajax" logic)
    btn.hx_post("/api/save").hx_target("#status").hx_swap("outerHTML")
    
    html = btn.render()
    
    assert '<button' in html
    assert 'hx-post="/api/save"' in html
    assert 'hx-target="#status"' in html
    assert 'hx-swap="outerHTML"' in html
    assert '>Save</button>' in html

def test_fluent_attributes_only():
    """
    Scenario: Using fluent API to build an attribute string.
    """
    logic = HTMXElement(element_tag=None, name="search_logic",)
    
    # Configure
    logic.hx_get("/search").hx_trigger("keyup delay:500ms").hx_indicator(".spinner")
    
    attr_str = logic.render()
    
    assert 'hx-get="/search"' in attr_str
    assert 'hx-trigger="keyup delay:500ms"' in attr_str
    assert 'hx-indicator=".spinner"' in attr_str
    assert "<" not in attr_str # Ensure no tags generated
