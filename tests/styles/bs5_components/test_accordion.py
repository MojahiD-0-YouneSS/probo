from probo.styles.frameworks.bs5.components.accordion import (
    BS5Accordion,
)

# ==============================================================================
#  BS5Accordion Tests
# ==============================================================================

def test_bs5_accordion_render_basic_structure():
    """1. Render basic accordion container."""
    acc = BS5Accordion(Id="myAccordion")
    html = acc.render()
    
    assert '<div id="myAccordion" class="accordion"' in html
    assert 'id="myAccordion"' in html

def test_bs5_accordion_add_item_render():
    """2. Render accordion with added items (Header + Body)."""
    acc = BS5Accordion(Id="faqAccordion")
    
    # Add Item 1
    acc.add_accordion_item(
        accordion_header="Question 1",
        header_id="headingOne",
        accordion_body="Answer 1",
        body_id="collapseOne"
    )
    
    html = acc.render()
    
    # Check Item Structure
    assert '<div class="accordion-item">' in html
    assert '<h2 id="headingOne" class="accordion-header"' in html
    assert 'id="headingOne"' in html
    assert '<button type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne" class="accordion-button"' in html
    assert 'Question 1' in html
    # Check Body
    assert '<div id="collapseOne"' in html
    assert 'class="accordion-collapse collapse"' in html
    assert '<div class="accordion-body">Answer 1</div>' in html

def test_bs5_accordion_render_flush_variant():
    """3. Render flush variant (removes borders)."""
    # Assuming 'flush' variant adds .accordion-flush class
    acc = BS5Accordion(variant='flush', Id="flushAcc")
    acc.add_accordion_item("Head", "h1", "Body", "b1")
    
    html = acc.render()
    
    assert 'class="accordion accordion-flush"' in html

def test_bs5_accordion_render_attributes():
    """4. Render with custom attributes passed to constructor."""
    acc = BS5Accordion(data_bs_always_open="true", style="width: 50%;")
    html = acc.render()
    
    assert 'data-bs-always-open="true"' in html
    assert 'style="width: 50%;"' in html

def test_bs5_accordion_state_constraints_blocking():
    """5. State: Accordion hidden when constraints not met."""
    # Logic: Only show FAQ if user has permission
    acc = BS5Accordion(
        id="secretFAQ",
        render_constraints={"can_view_faq": True}
    )
    acc.add_accordion_item("Secret Q", "h_sec", "Secret A", "b_sec")
    
    # Render without props (or with False) -> Should be hidden
    html = acc.render(override_props={"can_view_faq": False})
    
    assert not html

def test_bs5_accordion_state_constraints_passing():
    """6. State: Accordion visible when constraints met."""
    acc = BS5Accordion(
        id="publicFAQ",
        render_constraints={"is_public": True}
    )
    acc.add_accordion_item("Public Q", "h_pub", "Public A", "b_pub")
    
    # Render with matching props
    html = acc.render(override_props={"is_public": True},add_to_global=True)
    
    assert '<div id="publicFAQ" class="accordion"' in html
    assert "Public Q" in html

def test_bs5_accordion_state_constraints_not_passing_global():
    """6. State: Accordion visible when constraints met."""
    acc = BS5Accordion(
        id="publicFAQ",
        render_constraints={"is_public": True}
    )
    acc.add_accordion_item("Public Q", "h_pub", "Public A", "b_pub")
    
    # Render with matching props
    html = acc.render(override_props={"is_public": True})
    
    assert '<div class="accordion"' not in html
    assert "Public Q" not in html