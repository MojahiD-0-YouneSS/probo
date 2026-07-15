import pytest
from collections import deque
from probo.components.tag_classes.block_tags import DIV, SPAN, P
from probo.components.fragment import Frag
from probo.utility import ProboSourceString

# 1. Used Alone - string output
def test_frag_alone_string():
    f = Frag("hello", "world")
    result = f.render()
    assert isinstance(result, ProboSourceString)
    assert result == "hello world"

# 2. Used Alone - list output
def test_frag_alone_list():
    f = Frag("hello", "world")
    f.delegate_render_conditions(use_list=True)
    result = f.render()
    assert isinstance(result, list)
    assert result == ["hello", " ", "world"]

# 3. Used Alone - deque output
def test_frag_alone_deque():
    f = Frag("hello", "world")
    f.delegate_render_conditions(use_list=True, use_deque=True)
    result = f.render()
    assert isinstance(result, deque)
    assert list(result) == ["hello", " ", "world"]

# 4. Used inside other elements - DIV - string
def test_frag_in_div_string():
    d = DIV(Frag("hello", "world"), id="container")
    result = d.render()
    assert isinstance(result, ProboSourceString)
    assert result == '<div id="container">hello world</div>'

# 5. Used inside other elements - DIV - list
def test_frag_in_div_list():
    d = DIV(Frag("hello", "world"), id="container")
    d.delegate_render_conditions(use_list=True)
    result = d.render()
    assert isinstance(result, list)
    assert "".join([str(x) for x in result]) == '<div id="container">hello world</div>'

# 6. Used inside other elements - DIV - deque
def test_frag_in_div_deque():
    d = DIV(Frag("hello", "world"), id="container")
    d.delegate_render_conditions(use_list=True, use_deque=True)
    result = d.render()
    assert isinstance(result, deque)
    assert "".join([str(x) for x in result]) == '<div id="container">hello world</div>'

# 7. Fallback raw testing string (Testing internal EL fallback behavior implicitly)
def test_frag_raw_fallback_string():
    f = Frag("raw_text")
    result = f.render()
    assert isinstance(result, ProboSourceString)
    assert result == "raw_text"

# 8. Nested Frag elements
def test_nested_frag():
    f = Frag(Frag("inner", "text"), "outer")
    result = f.render()
    assert isinstance(result, ProboSourceString)
    assert result == "inner text outer"

# 9. Empty Frag
def test_frag_empty():
    f = Frag()
    result = f.render()
    assert isinstance(result, ProboSourceString)
    assert result == ""

# 10. Frag with numeric and boolean data
def test_frag_numeric_bool():
    f = Frag(1, 2.5, True)
    result = f.render()
    assert isinstance(result, ProboSourceString)
    assert result == "1 2.5 True"

# 11. Stream standard mode
def test_frag_stream_string():
    f = Frag("stream", "test")
    stream_result = list(f.stream())
    assert "".join(stream_result) == "stream test"

# 12. Stream list mode
def test_frag_stream_list_mode():
    f = Frag("stream", "list")
    f.delegate_render_conditions(use_list=True)
    stream_result = list(f.stream())
    assert stream_result == ["stream", " ", "list"]

# 13. Stream deque mode
def test_frag_stream_deque_mode():
    f = Frag("stream", "deque")
    f.delegate_render_conditions(use_list=True, use_deque=True)
    stream_result = list(f.stream())
    assert stream_result == ["stream", " ", "deque"]

# 14. Data pipeline functionality
def test_frag_data_pipeline():
    f = Frag("pipeline", data_pipeline={"key": "value"})
    assert f.get_data_pipeline == {"key": "value"}
    f.provide_data("new_key", "new_value")
    assert f.get_data_pipeline["new_key"] == "new_value"

# 15. Nested inside SPAN and P elements
def test_frag_deeply_nested():
    content = DIV(
        P(Frag("Paragraph", "content")),
        SPAN(Frag("Span", "content"))
    )
    result = content.render()
    assert "<p>Paragraph content</p>" in result
    assert "<span>Span content</span>" in result
    assert result.startswith("<div>")
    assert result.endswith("</div>")

# 16. Data pipeline simple expression (single variable)
def test_frag_data_simple_1():
    f = Frag({'name'})
    f.load_data({'name': 'John Doe'})
    assert f.render() == 'John Doe'

# 17. Data pipeline simple expression (dot notation)
def test_frag_data_simple_2():
    f = Frag({'user.role'})
    f.load_data({'user': {'role': 'Admin'}})
    assert f.render() == 'Admin'

# 18. Data pipeline complex (lambda with multiple variables)
def test_frag_data_complex_1():
    f = Frag({'a', 'b', lambda **kwargs: str(kwargs.get('a', 0) * kwargs.get('b', 0))})
    f.load_data({'a': 4, 'b': 5})
    assert f.render() == '20'

# 19. Data pipeline complex (named function returning element)
def test_frag_data_complex_2():
    def render_status(**kwargs):
        return DIV("Active") if kwargs.get('is_active') else DIV("Inactive")
    
    f = Frag({'is_active', render_status})
    f.load_data({'is_active': False})
    assert f.render() == '<div>Inactive</div>'

# 20. Data pipeline complex (lambda conditionally rendering text)
def test_frag_data_complex_3():
    f1 = Frag(
        "Status:",
        {'code', lambda **kwargs: "OK" if kwargs.get('code') == 200 else "Error"}
    )
    f1.load_data({'code': 200})
    assert f1.render() == "Status: OK"
    
    f2 = Frag(
        "Status:",
        {'code', lambda **kwargs: "OK" if kwargs.get('code') == 200 else "Error"}
    )
    f2.load_data({'code': 500})
    assert f2.render() == "Status: Error"

# 21. Data from direct parent (simple variable)
def test_frag_parent_data_simple_1():
    parent = DIV(Frag({'username'}))
    parent.load_data({'username': 'Alice'})
    assert parent.render() == '<div>Alice</div>'

# 22. Data from grandparent (dot notation)
def test_frag_parent_data_simple_2():
    grandparent = DIV(SPAN(Frag({'settings.theme'})))
    grandparent.load_data({'settings': {'theme': 'dark'}})
    assert grandparent.render() == '<div><span>dark</span></div>'

# 23. Data from parent (lambda with multiple variables)
def test_frag_parent_data_complex_1():
    parent = DIV(Frag({'x', 'y', lambda **kwargs: str(kwargs.get('x', 0) + kwargs.get('y', 0))}))
    parent.load_data({'x': 10, 'y': 20})
    assert parent.render() == '<div>30</div>'

# 24. Data from parent (named function returning element)
def test_frag_parent_data_complex_2():
    def build_profile(**kwargs):
        return SPAN(kwargs.get('role')) if kwargs.get('is_logged_in') else SPAN("Guest")
    
    parent = DIV(Frag({'is_logged_in', 'role', build_profile}))
    parent.load_data({'is_logged_in': True, 'role': 'Moderator'})
    assert parent.render() == '<div><span>Moderator</span></div>'

# 25. Data from parent (conditional lambda, data provided in constructor)
def test_frag_parent_data_complex_3():
    parent = DIV(
        "Welcome",
        Frag({'user', lambda **kwargs: kwargs.get('user') if kwargs.get('user') else "Stranger"}),
        data_pipeline={'user': 'Bob'}
    )
    assert parent.render() == '<div>Welcome Bob</div>'

# 26. Frag with fragments kwarg
def test_frag_fragments_kwarg():
    from probo.components.tag_classes.block_tags import I
    tree = DIV(
        DIV("Header", P('something'), id="h"),
        DIV("Content", I('other thing'), id="c"),
        DIV("Footer", id="f")
    )
    result = Frag(tree, fragments=[lambda n: getattr(n, 'element_tag', None) == 'p', lambda n: getattr(n, 'element_tag', None) == 'i']).render()
    assert '<div id="h">Header</div>' not in result
    assert '<p>something</p>' in result
    assert '<i>other thing</i>' in result
    assert '<div>Content</div>' not in result
    assert '<div>Footer</div>' not in result