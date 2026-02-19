# attributes

::: probo.components.attributes

#examples:
```python
attrs = {'cx': 50, 'unknown_attr': 'value'}
validator = ElementAttributeValidator(element_tag='<circle>', **attrs)

assert validator.validate() is False # True
assert "unknown-attr='value'" in validator.error_attrs # True ["unknown-attr='value'",]
assert 'cx' in validator.valid_attrs # True , {'cx':50,}
```
