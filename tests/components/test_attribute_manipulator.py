import pytest
from src.probo.components.base import ElementAttributeManipulator

class TestAttributeManipulator:
    
    # 1. Test Initialization & State Isolation
    def test_init_state_isolation(self):
        """Ensure two instances do not share state."""
        m1 = ElementAttributeManipulator(Id="box-1")
        m2 = ElementAttributeManipulator(Id="box-2")
        
        m1.add_class("active")
        
        assert m1.get_attr("class") == "active"
        assert m2.get_attr("class") is None
        assert m1.get_attr("id") == "box-1"

    # 2. Test Smart Class Addition
    def test_add_class_smart_handling(self):
        """Test duplicates are removed and sorting is applied."""
        m = ElementAttributeManipulator()
        m.add_class("btn btn-primary")
        m.add_class("btn")  # Duplicate should be ignored
        
        classes = m.get_attr("class").split()
        assert "btn" in classes
        assert "btn-primary" in classes
        assert len(classes) == 2

    # 3. Test Class Removal
    def test_remove_class(self):
        m = ElementAttributeManipulator(Class="btn btn-danger active")
        m.remove_class("btn-danger")
        
        assert m.contains_class("btn")
        assert m.contains_class("active")
        assert not m.contains_class("btn-danger")

    # 4. Test Toggle Logic
    def test_toggle_class(self):
        m = ElementAttributeManipulator()
        
        # Toggle ON
        m.toggle_class("hidden")
        assert m.contains_class("hidden")
        
        # Toggle OFF
        m.toggle_class("hidden")
        assert not m.contains_class("hidden")

    # 5. Test Toggle with Forcing (True/False)
    def test_toggle_class_forced(self):
        m = ElementAttributeManipulator(Class="visible")
        
        # Force Add (even if present)
        m.toggle_class("visible", condition=True)
        assert m.contains_class("visible")
        
        # Force Remove
        m.toggle_class("visible", condition=False)
        assert not m.contains_class("visible")

    # 6. Test Boolean Attributes (e.g. disabled)
    def test_boolean_attributes(self):
        m = ElementAttributeManipulator()
        
        m.set_attr("disabled", True)
        assert m.get_attr("disabled") == "disabled"  # Standard HTML behavior
        
        m.set_attr("disabled", False)
        assert m.get_attr("disabled") is None  # Should be removed entirely

    # 7. Test Data Attribute Formatting
    def test_set_data_attributes(self):
        m = ElementAttributeManipulator()
        m.set_data("user_id", "123")
        m.set_data("is_active", "true")
        
        assert m.get_attr("data-user-id") == "123"
        assert m.get_attr("data-is-active") == "true"

    # 8. Test Inline Style Parsing & Updating
    def test_set_style_smart_update(self):
        # Start with existing dirty style string
        m = ElementAttributeManipulator(style="color: red; margin: 10px;")
        
        # Update one property, keep the other
        m.set_style("color", "blue")
        m.set_style("padding", "5px")
        
        style = m.get_attr("style")
        assert "color: blue" in style
        assert "margin: 10px" in style
        assert "padding: 5px" in style

    # 9. Test Merge Attributes (Bulk Update)
    def test_merge_attrs(self):
        m = ElementAttributeManipulator(Id="old")
        m.merge_attrs(Id="new", role="alert", aria_hidden="true")
        
        assert m.get_attr("id") == "new"
        assert m.get_attr("role") == "alert"
        assert m.get_attr("aria-hidden") == "true"

    # 10. Test Method Chaining
    def test_method_chaining(self):
        """Ensure methods return 'self' for fluent API."""
        m = ElementAttributeManipulator()
        result = m.add_class("foo").set_id("bar").set_attr("title", "baz")
        
        assert result is m  # The object returned itself
        assert m.contains_class("foo")
        assert m.get_attr("id") == "bar"