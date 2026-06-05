import pytest
from probo.components.custom_element import CustomElement
from probo.components.tag_classes.block_tags import DIV

def test_custom_element_basic_render():
    """Tests whether a custom tag with content generates the correct opening and closing HTML."""
    elem = CustomElement('MY-TAG', 'Internal Text', id='test-id')
    html = elem.render()
    
    assert '<my-tag' in html
    assert 'id="test-id"' in html
    assert 'Internal Text' in html
    assert '</my-tag>' in html

def test_custom_element_self_closing():
    """Test that the is_self_closing parameter generates an empty, self-closing tag."""
    elem = CustomElement('GITHUB', is_self_closing=True, url="https://github.com")
    html = elem.render()
    
    assert '<github' in html
    assert 'url="https://github.com"' in html

def test_custom_element_ssdom_find():
    """
    Verify that the CustomElement is a real SSDOM node 
    and that it can be found using the .find() method.
    """
    template = DIV(
        CustomElement('GITHUB', is_self_closing=True)
    )
    
    custom = template.find(lambda n: hasattr(n, 'tag') and n.tag == 'GITHUB')
    
    assert custom is not None
    assert custom.tag == 'GITHUB'
    assert custom.is_self_closing is True

def test_custom_element_stream():
    """Test that the custom tag supports streaming via generators."""
    elem = CustomElement('STREAM-TAG', 'Async Content')
    stream_generator = elem.stream()
    html = "".join(list(stream_generator))
    
    assert '<stream-tag' in html
    assert 'Async Content' in html
    assert '</stream-tag>' in html