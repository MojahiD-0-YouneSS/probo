import pytest
from unittest.mock import MagicMock
from probo.components.node import ProxyElement, ProboSourceString
from probo import DIV,P

# --- Fixtures ---

@pytest.fixture
def proxy():
    """Returns a basic ProxyElement instance for testing."""
    return ProxyElement("div", "Initial Content", id="main")


# --- Tests ---

def test_basic_tag_rendering(proxy):
    """Ensures fallback to standard Element rendering works."""
    rendered = proxy.render()
    assert isinstance(rendered, str)
    assert "<div" in rendered
    assert 'id="main"' in rendered
    assert "Initial Content" in rendered


def test_render_callable_no_logic():
    """Tests rendering when only a callable is provided."""
    pe = ProxyElement("section")
    pe.load_render_logic(lambda: "<span>Logic Only</span>")
    result = pe.render()
    assert isinstance(result, ProboSourceString)
    assert result == "<span>Logic Only</span>"


def test_render_callable_with_logic():
    """Tests rendering when logic_obj is passed to the callable."""
    pe = ProxyElement("article")
    mock_data = {"title": "ProboUI Rocks"}
    pe.load_logic(mock_data)
    pe.load_render_logic(lambda data: f"<h1>{data['title']}</h1>")
    assert pe.render() == "<h1>ProboUI Rocks</h1>"


def test_logic_obj_render_method():
    """Tests delegation to the logic object's own .render() method."""

    class Component:
        def render(self): return "Component Output"

    pe = ProxyElement("div")
    pe.load_logic(Component())
    assert pe.render() == "Component Output"


def test_precedence_callable_vs_method():
    """Verifies that render_callable takes priority over logic_obj.render()."""

    class Component:
        def render(self): return "Method"

    pe = ProxyElement("div")
    pe.load_logic(Component())
    pe.load_render_logic(lambda obj: "Callable")
    assert pe.render() == "Callable"


@pytest.mark.parametrize("input_val, expected", [
    ("test", "test"),
    (123, "123"),
    ("<b>Safe</b>", "<b>Safe</b>")
])
def test_probo_source_string_wrapping(input_val, expected):
    """Ensures all logic-based branches return the special container."""
    pe = ProxyElement("div")
    pe.load_render_logic(lambda: input_val)
    result = pe.render()
    assert isinstance(result, ProboSourceString)
    assert result == expected


def test_attribute_persistence(proxy):
    """Checks if attributes from __init__ survive the render process."""
    proxy.attributes['class'] = 'container'
    rendered = proxy.render()
    assert 'class="container"' in rendered

def test_tree_proxy_rendering():
    """Tests recursive rendering of ProboUI nodes."""
    inner = ProxyElement("span", "Inner")
    outer = DIV(Class='container')
    outer.add(inner)
    outer.add(P('hello'))
    rendered = outer.render()
    print(rendered)
    assert "<div><span>Inner</span><p>hello</p></div>" in rendered

def test_logic_reload_efficiency():
    """Ensures logic can be swapped without re-instantiating the node."""
    pe = ProxyElement("p")
    pe.load_render_logic(lambda val: f"Count: {val}")

    pe.load_logic(1)
    assert pe.render() == "Count: 1"

    pe.load_logic(2)
    assert pe.render() == "Count: 2"


def test_render_without_tag_or_logic():
    """Edge case: What happens if everything is None?"""
    pe = ProxyElement(None)
    # This tests your 'if self.tag' fallback branch
    result = pe.render()
    assert result is None