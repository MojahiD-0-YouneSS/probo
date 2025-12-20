import pytest
from mui.htmx.htmx import HTMX, HTMXElement

# ==============================================================================
#  TEST 1: HTMXElement as Full HTML Element
# ==============================================================================
def test_htmx_element_full_render():
    """
    Scenario: User defines a specific button with HTMX behavior.
    Expected: <button hx-post="/save">Save</button>
    """
    # Mode A: Tag is provided
    save_btn = HTMXElement(
        element_tag="button",
        content="Save",
        hx_post="/api/save",
        hx_swap="outerHTML"
    )
    
    html = save_btn.render()
    
    assert "<button" in html
    assert 'hx-post="/api/save"' in html
    assert 'hx-swap="outerHTML"' in html
    assert ">Save</button>" in html

# ==============================================================================
#  TEST 2: HTMXElement as Attributes Renderer (Attribute Bag)
# ==============================================================================
def test_htmx_element_attributes_only():
    """
    Scenario: User wants just the attribute string to inject manually later.
    Expected: hx-get="/search" hx-trigger="keyup"
    """
    # Mode B: Tag is None
    search_attrs = HTMXElement(
        name="search_logic",
        hx_get="/api/search",
        hx_trigger="keyup delay:500ms"
    )
    
    attr_string = search_attrs.render()
    
    # Should NOT contain brackets <>
    assert "<" not in attr_string
    assert ">" not in attr_string
    
    # Should contain attributes
    assert 'hx-get="/api/search"' in attr_string
    assert 'hx-trigger="keyup delay:500ms"' in attr_string

# ==============================================================================
#  TEST 3: The HTMX Bucket (Registry)
# ==============================================================================
def test_htmx_bucket_logic():
    """
    Scenario: Storing multiple configs and retrieving them.
    """
    # 1. Create Elements
    btn = HTMXElement("button","btn", hx_post="/submit")
    logic = HTMXElement(name="logic", hx_swap="none")
    
    # 2. Initialize Bucket
    bucket = HTMX(hx_btn=btn, hx_logic=logic)
    
    # 3. Get Specific
    assert "<button" in bucket.render("hx_btn")
    assert 'hx-post="/submit"' in bucket.render("hx_btn")
    
    assert "<" not in bucket.render("hx_logic")
    assert 'hx-swap="none"' in bucket.render("hx_logic")
    
    # 4. Render All (Dump)
    all_html = bucket.render(all_elements=True)
    assert "<button" in all_html
    assert 'hx-swap="none"' in all_html
    assert "\n" not in all_html # Separator check