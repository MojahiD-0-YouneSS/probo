from probo.components import(
    Element,
    BaseHTMLElement,
    ElementNodeMixin,

)
import pytest

class CIRCLE(BaseHTMLElement, ElementNodeMixin):
    def __init__(self, probo_pretty_error=False, probo_custom_attrs=False, **kwargs):
        self.flags = {
            "probo_pretty_error": probo_pretty_error,
            "probo_custom_attrs": probo_custom_attrs
        }
        super().__init__(**kwargs)

    def render(self):
        return (
            Element(**self.flags)  # Pass flags here
            .set_attrs(**self.attributes)
            .circle()
            .element
        )

def test_probo_flags_extraction():
    """
    Test that flags are used by the builder but removed from the tag attributes.
    """
    # Instantiate a CIRCLE with flags passed as kwargs
    circle_inst = CIRCLE(
        r=10, 
        probo_custom_attrs=True, 
        probo_pretty_error=True,
        named_by="test-car" # Custom attribute
    )
    
    rendered = circle_inst.render()
    rendered_str = str(rendered)
    
    # 1. Check that custom attribute was allowed (because flag was True)
    assert 'named-by="test-car"' in rendered_str
    
    # 2. Check that the flags THEMSELVES were stripped and not rendered
    assert 'probo_custom_attrs' not in rendered_str
    assert 'probo_pretty_error' not in rendered_str
    
    # 3. Check standard attributes remain
    assert 'r="10"' in rendered_str

def test_pretty_error_handling_in_class():
    """
    Test that an invalid attribute triggers a custom error string 
    instead of a crash when the flag is passed.
    """
    # Passing an un-renderable dict as an attribute value
    bad_circle = CIRCLE(
        invalid_val={"not": "a string"}, 
        probo_pretty_error=True
    )
    
    result = bad_circle.render()
    
    # Should return a string containing an error message, not raise ValueError
    assert isinstance(result, str)
    assert "Error" in result or "invalid_val" in result

def test_strict_error_without_flag():
    """
    Test that the system still raises a standard error if the flag is omitted.
    """
    with pytest.raises((ValueError, TypeError)):
        bad_circle = CIRCLE(invalid_val={"not": "a string"})
        bad_circle.render()

def test_probo_custom_attrs_flag():
    """
    Verifies that when probo_custom_attrs=True, the Element builder 
    accepts and renders non-standard SVG/HTML attributes.
    """
    # Test with a custom attribute 'named_by'
    # Normally, builders might strip unknown attrs; this flag should prevent that.
    element = (
        Element(probo_custom_attrs=True)
        .set_attrs(named_by="cars", data_test="custom-value")
        .circle()
        .element
    )
    
    rendered = str(element)
    assert 'named-by="cars"' in rendered
    assert 'data-test="custom-value"' in rendered

def test_probo_pretty_error_success():
    """
    Verifies that standard rendering still works when pretty_error is enabled.
    """
    element = (
        Element(probo_pretty_error=True)
        .set_attrs(id="ok")
        .rect()
        .element
    )
    assert 'id="ok"' in str(element)
    assert '<rect' in str(element)

def test_probo_pretty_error_failure_handling():
    """
    Verifies that if an error occurs during rendering (e.g., invalid attribute type),
    the system returns a custom HTML error string instead of crashing the app.
    """
    # Force an error by passing an un-renderable type if your builder validates,
    # or simulate a failure in the set_attrs chain.
    
    # Example: Passing a dictionary as an attribute value which might crash a naive renderer
    result = (
        Element(probo_pretty_error=True)
        .set_attrs(invalid_attr={"this": "should fail"})
        .path()
        .element
    )
    
    # The result should be a string/object containing error info for the UI, 
    # not a Python Traceback.
    assert isinstance(result, str)
    assert "Render Error" in result and "style" in result # Looking for a styled error box
    assert "invalid_attr" in result

def test_default_error_raises_exception():
    """
    Ensures that without the pretty_error flag, the system raises a 
    standard Python exception (Value Error/Attribute Error).
    """
    with pytest.raises((ValueError, TypeError, AttributeError)):
        # Default behavior: probo_pretty_error=False
        (
            Element(probo_pretty_error=False)
            .set_attrs(invalid_attr={"crash": "now"})
            .line()
            .element
        )