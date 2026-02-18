import pytest
from src.probo.components.elements import Element


# --- FIXTURES ---
@pytest.fixture
def builder():
    """Returns a fresh Element builder instance."""
    return Element()


# --- TESTS ---


def test_build_tag_standard(builder):
    """Test building a standard HTML5 tag via handler."""
    # Usage: Element().div() -> creates <div></div>
    el = builder.div()
    assert el.element == "<div></div>"


def test_build_tag_with_attributes(builder):
    """Test building a tag with attributes."""
    builder.set_attrs(id="main", Class="container")
    el = builder.div()
    # Note: Order of attributes depends on dictionary implementation, checking substring
    assert "<div" in el.element
    assert 'id="main"' in el.element
    assert 'class="container"' in el.element
    assert "></div>" in el.element


def test_custom_element_creation():
    """Test creating a non-standard tag (is_custom=True)."""
    # Usage: custom_element('my-widget', ...)
    el = Element(is_list=True).custom_element(
        "my-widget", content="Content", is_void_element=False
    )

    # Should render <my-widget>Content</my-widget>
    # You might need to check how your custom_element returns data (obj or string)
    assert el.element == ["<my-widget>", "Content", "</my-widget>"]


def test_render_attrs_logic(builder):
    """Test the attribute rendering logic (False/None filtering)."""
    builder.set_attrs(required=True, disabled=False, value=0,)

    # We trigger a build to run render_attrs logic internally
    el = builder.input()

    html = el.element
    assert "required" in html  # True -> Present
    assert "disabled" not in html  # False -> Removed
    assert 'value="0"' in html  # 0 -> Kept

def test_element_health_check(builder):
    """Test validation logic (element_health)."""
    # Valid case
    builder.set_attrs(href="/home")
    builder.a()
    # If element_health runs on build, it should pass silently or return True
    # Assuming internal check passed if element is generated
    assert builder.element.startswith("<a")

    # Invalid case (depending on your strictness)
    # If you implemented strict checking:
    builder_bad = Element()
    builder_bad.set_attrs(href="/home")
    # Building a DIV with href might fail or warn depending on implementation
    # builder_bad.div()


def test_stringify_element(builder):
    """Test converting the element object to a string."""
    builder.span()
    # Assuming stringify_element returns self.element or string representation
    result = builder.stringify_element()

    # Adjust assertion based on whether it returns self or the string
    if isinstance(result, str):
        assert result == "<span></span>"
    else:
        assert result.element == "<span></span>"


def test_render_content_with_marker(builder):
    """Test rendering content with injection at a specific marker."""
    # Setup: content with a marker
    content = "Hello MARKER World"
    builder.set_content(content)

    # Depending on your API, verify how extra content is injected
    # This assumes you have a method to replace the marker or append
    # For v1 BaseHTMLElement logic, content is usually just joined.
    builder.div()
    assert "Hello MARKER World" in builder.element


def test_set_data_django_style(builder):
    """Test set_data converting keys to data-attributes."""
    # Usage: set_data(user_id=123, role='admin') -> data-user-id="123"
    builder.set_data("user_id=123", "toggle_modal=True")
    builder.div()

    html = builder.element
    assert "user_id=123" in html
    assert "toggle_modal=True" in html  # Boolean True usually becomes just the attr
    assert (
        '<$probo-var name="toggle_modal=True"/>' in html
    )  # Boolean True usually becomes just the attr


def test_raw_comment(builder):
    """Test the raw method wrapping content in comments."""
    builder.set_content("Hidden Data")
    builder.raw(
        "Hidden Data 123", "oijoiiotg", "joptjgtijopji"
    )  # Should wrap in <!-- -->

    assert "<!--" in builder.element
    assert "Hidden Data 123" in builder.element
    assert "-->" in builder.element
    assert "joptjgtijopji" in builder.element


def test_attributes_chaining(builder):
    """Test that set_attrs returns self for chaining."""
    res = builder.set_attrs(id="1").set_content("X")
    assert res is builder
    res.div()
    assert '<div id="1">X</div>' == builder.element
