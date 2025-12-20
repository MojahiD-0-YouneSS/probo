import pytest
from mui.components.state.component_state import ElementState
from mui.components.tag_functions.block_tags import (div, h2, p, )
from mui.components.component import Component

# ==============================================================================
#  SCENARIO: Component Injection via ElementState
# ==============================================================================

class ProductCard(Component):
    """A sub-component we want to repeat."""
    def __init__(self, name, price):
        # Simple template structure
        tmpl = div(
            h2(name, Class="product-title"),
            p(f"${price}", Class="product-price"),
            Class="card"
        )
        # Note: If passing Element object to template, ensure it renders to str
        # or Component handles Element objects in template.
        # Assuming template expects string:
        super().__init__(name="Card", template=tmpl)

def test_es_rendering_components():
    """
    The 'Crazy Feature': 
    ElementState iterates data -> Calls Factory -> Factory returns Component HTML.
    """
    
    # 1. The Data (e.g. from Database)
    db_products = [
        {'name': 'Gaming Laptop', 'price': 1200},
        {'name': 'Mechanical Key', 'price': 150},
    ]
    
    # 2. The Transformer (The Factory)
    # This acts like a React .map() function
    def component_factory(context_tuple):
        index, item = context_tuple
        
        # Instantiate a real Component for this item
        comp = ProductCard(item['name'], item['price'])
        
        # Render it to string so ElementState can append it
        html = comp.render()
        return html

    # 3. The State Configuration
    # We use a 'div' wrapper for the list of cards
    es = ElementState(
        element='div', 
        d_state='products_list',
        i_state=True,               # Enable Looping
        inner_html=component_factory, # Inject the logic
        **{'class': 'product-grid'},
    )
    
    # 4. Execute
    # Simulate ComponentState resolving data
    rendered_html = es.render(**{'products_list': db_products})
    
    # 5. Verify
    # Wrapper
    assert '<div class="product-grid">' in rendered_html
    
    # Card 1
    assert '<div class="card">' in rendered_html
    assert '<h2 class="product-title">Gaming Laptop</h2>' in rendered_html
    assert '<p class="product-price">$1200</p>' in rendered_html
    
    # Card 2
    assert 'Mechanical Key' in rendered_html
    assert '$150' in rendered_html