import pytest
from src.probo import div, span
from src.probo.components.component import Component
from src.probo.styles.plain_css import CssRule, CssSelector


# --- FIXTURES ---
@pytest.fixture
def empty_comp():
    return Component(name="TestComp", template="<div>Original</div>", state=None)


# --- TESTS ---


def test_registry_lifecycle():
    """Test Component.register and Component.get."""
    # 1. Register
    Component.register("MyPage", div("Hello"), props={"auth": True})

    # 2. Get
    comp_class = Component.get("MyPage")

    # 3. Verify it returns a class/instance we can use
    # Note: Depending on your implementation, get() might return the class or instance
    assert comp_class is not None
    assert comp_class.name == "MyPage"


def test_render_pure_html_no_mutation():
    """Test rendering simple HTML string without state/props."""
    raw_html = '<div class="fixed">Static Content</div>'
    comp = Component(name="Static", template=raw_html, state=None)

    html = comp.render()

    assert html == raw_html


def test_add_child_and_nesting(empty_comp):
    """Test add_child appending content."""
    # 1. Add string child
    empty_comp.add_child("<span>Appended</span>", name="span")

    html = empty_comp.render()
    assert "<div>Original</div>" in html
    assert "<span>Appended</span>" in html


def test_sub_component_nesting():
    """Test embedding a Component inside another Component."""
    child = Component(name="Child", template=span("I am child"), state=None)
    parent = Component(name="Parent", template=div(child), state=None)
    html = parent.render()

    # Parent should render itself AND the child
    assert "<div>" in html
    assert "<span>I am child</span>" in html


def test_set_root_element(empty_comp):
    """Test wrapping the template in a root element."""
    # Wrap the existing "<div>Original</div>" in a <main> tag
    empty_comp.set_root_element(root="main", id="root-node")

    html = empty_comp.render()

    # Expected: <main id='root-node'><div>Original</div></main>
    assert '<main id="root-node">' in html
    assert "<div>Original</div>" in html
    assert "</main>" in html


def test_load_css_rules():
    """Test JIT CSS generation."""
    comp = Component(name="Styled", template=div("Text", Class="box"), state=None)

    # Load rule matching .box
    selector = CssSelector().cls("box").render()
    rule = CssRule(color="red").declarations
    rules = {selector: rule}
    print(selector, rules)
    comp.load_css_rules(**rules)

    html, css = comp.render()

    assert 'class="box"' in html
    assert ".box" in css
    assert "color:red" in css
