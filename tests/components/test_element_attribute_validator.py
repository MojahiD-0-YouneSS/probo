from probo.components.attributes import ElementAttributeValidator

def test_validator_success_path():
    """Test standard validation with valid attributes."""
    attrs = {'cx': 50, 'r': 10}
    validator = ElementAttributeValidator(element_tag='<circle>', **attrs)
    
    assert validator.validate() is True
    assert validator.valid_attrs == attrs
    assert validator.error_attrs == []

def test_validator_error_path():
    """Test validator when invalid attributes are passed."""
    attrs = {'cx': 50, 'unknown_attr': 'value'}
    validator = ElementAttributeValidator(element_tag='<circle>', **attrs)
    
    assert validator.validate() is False
    assert "unknown-attr='value'" in validator.error_attrs
    assert 'cx' in validator.valid_attrs
