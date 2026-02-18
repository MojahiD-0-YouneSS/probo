import pytest
from src.probo.components.tag_classes import SPAN, DIV, INPUT, BUTTON  # Adjust imports

class TestElementIntegration:

    # 1. Test Inheritance of Manipulator
    def test_element_inherits_methods(self):
        div = DIV().attr_manager
        # Should have methods from ElementAttributeManipulator
        assert hasattr(div, 'add_class')
        assert hasattr(div, 'set_attr')
        assert hasattr(div, 'toggle_class')

    # 2. Test Initial Attributes in Constructor
    def test_element_init_attributes(self):
        btn = BUTTON(Id="submit-btn", Class="btn-primary")
        
        assert btn.attr_manager.get_attr("Id") == "submit-btn"
        assert btn.attr_manager.contains_class("btn-primary")

    # 3. Test Render Output (HTML Generation)
    def test_render_includes_attributes(self):
        """Check if attrs actually appear in the final HTML string."""
        div = DIV(Id="container")
        div.attr_manager.add_class("flex-row")
        
        html = div.render()
        assert 'id="container"' in html
        assert 'class="flex-row"' in html
        assert '<div' in html

    # 4. Test Instance Independence (The "Shared Memory" Bug Check)
    def test_elements_dont_share_classes(self):
        div1 = DIV()
        div2 = DIV()
        
        div1.attr_manager.add_class("red")
        div2.attr_manager.add_class("blue")
        
        assert div1.attr_manager.contains_class("red")
        assert not div1.attr_manager.contains_class("blue")
        assert div2.attr_manager.contains_class("blue")
        assert not div2.attr_manager.contains_class("red")

    # 5. Test ID Setting Helper
    def test_set_id_integration(self):
        div = DIV()
        div.attr_manager.set_id("unique-1")
        assert div.attributes['Id'] == "unique-1"
        
        # Ensure it overrIdes
        div.attr_manager.set_id("unique-2")
        assert div.attributes['Id'] == "unique-2"

    # 6. Test Data Attribute Integration
    def test_data_attribute_integration(self):
        row = DIV()
        row.attr_manager.set_data("row_index", "5")
        
        html = row.render()
        assert 'data-row-index="5"' in html

    # 7. Test Boolean Attribute Rendering
    def test_boolean_attribute_rendering(self):
        inp = INPUT()
        inp.attr_manager.set_attr("required", True)
        inp.attr_manager.set_attr("disabled", True)
        html = inp.render()
        # In HTML, boolean attrs often appear as just the name or name=""
        # Adjust assertion based on your render implementation
        assert 'required' in html
        assert 'disabled' in html

    # 8. Test Style Management on Elements
    def test_style_integration(self):
        box = DIV(style="background: white;")
        box.attr_manager.set_style("color", "black")
        
        html = box.render()
        assert 'background: white' in html
        assert 'color: black' in html

    # 9. Test Chaining on Element Instantiation
    def test_fluent_instantiation(self):
        """Test the pattern: DIV().add_class().set_id()"""
        card = DIV()
        card.attr_manager.add_class("card").set_style("width", "100%")
        
        assert card.attr_manager.contains_class("card")
        assert "width: 100%" in card.attr_manager.get_attr("style")

    # 10. Test Overwriting Attributes via `set_attr` vs `add_class`
    def test_classoverwrite_behavior(self):
        """Ensure set_attr('class') overwrites previous add_class calls."""
        span = SPAN("span is here")
        span.attr_manager.add_class("badge badge-warning")
        
        # Hard overwrite
        span.attr_manager.set_attr("class", "badge-error")
        
        assert span.attr_manager.contains_class("badge-error")
        assert not span.attr_manager.contains_class("badge-warning")