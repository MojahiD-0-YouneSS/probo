import pytest
from probo.components.elements import Element
from probo.styles.plain_css import CssRule

def test_element_none_content():
    """11. Element with None content."""
    el = Element('div',content=None)
    assert el.render() == "<div></div>"

def test_element_int_attributes():
    """12. Integer attributes."""
    el = Element("div", tabindex=0, role='status')
    assert 'tabindex="0"' in el.render()
    assert 'role="status"' in el.render()

def test_css_rule_empty_selector():
    """13. Rule with empty selector."""
    # Should technically be valid syntax even if useless
    rule = CssRule(selector="", color="red")
    css = rule.render()
    assert "{" in css # Should just render block

def test_css_rule_none_value():
    """14. Property with None value."""
    rule = CssRule(color=None)
    # Should skip the property
    assert "/* color:... ERROR */;" not in rule.render()

def test_element_nested_empty_list():
    """15. Element with empty list content."""
    el = Element('div',content=[])
    assert "<div></div>" == el.render()