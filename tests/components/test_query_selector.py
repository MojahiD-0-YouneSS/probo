from probo import DIV, SPAN, P
from probo.components import Component

def test_css_selector_by_tag():
    comp = DIV(SPAN("hello"), P("world"))
    
    # css_selector
    span_node = comp.css_selector("span")
    assert span_node is not None
    assert span_node.tag == "SPAN"
    assert span_node.text == "hello"

def test_css_selector_by_class():
    comp = DIV(SPAN("hello", Class="greeting"), P("world", Class="greeting info"))
    
    # css_selector
    first_greeting = comp.css_selector(".greeting")
    assert first_greeting is not None
    assert first_greeting.tag == "SPAN"

    # css_selector_all
    greetings = comp.css_selector_all(".greeting")
    assert len(greetings) == 2
    assert greetings[0].tag == "SPAN"
    assert greetings[1].tag == "P"
    
def test_css_selector_by_id():
    comp = DIV(SPAN("hello", Id="main-span"))
    
    node = comp.css_selector("#main-span")
    assert node is not None
    assert node.tag == "SPAN"
    assert node.text == "hello"

def test_css_selector_not_found():
    comp = DIV(SPAN("hello"))
    
    node = comp.css_selector(".non-existent")
    assert node is None
    
    nodes = comp.css_selector_all(".non-existent")
    assert len(nodes) == 0
