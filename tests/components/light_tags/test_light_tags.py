from src.probo.components.light_tags import Ldiv, Limg, Lsvg, l_div, l_img, l_svg
import pytest
import inspect
from probo.components.elements import Element


LIGHT_OOP_TAGS = [
    ("block", Ldiv, "div", False),
    ("self_closing", Limg, "img", True),
    ("svg", Lsvg, "svg", False),
]


LIGHT_FUNC_TAGS = [
    ("block", l_div, "div", False),
    ("self_closing", l_img, "img", True),
    ("svg", l_svg, "svg", False),
]


TEST_TEXT = "probo-fast"
TEST_ATTRS = {"id": "test-id", "class": "test-class"}


@pytest.fixture
def shared_el():
    """Provides a fresh Element pipeline for each test."""
    return Element(is_list=True, use_deque=True)


@pytest.mark.parametrize(
    "category, TagClass, tag_name, is_self_closing", LIGHT_OOP_TAGS
)
def test_light_oop_eager_render(
    shared_el, category, TagClass, tag_name, is_self_closing
):
    """Tests that Light OOP classes render eagerly into strings correctly."""

    if is_self_closing:
        node = TagClass(**TEST_ATTRS)
    else:
        node = TagClass(TEST_TEXT, **TEST_ATTRS)

    
    if hasattr(node, "render"):
        output = (
            node.render(shared_el)
            if "EL" in inspect.signature(node.render).parameters
            else node.render()
        )
    else:
        output = str(node)

    output_str = "".join(output) if isinstance(output, list) else str(output)

    
    assert f"<{tag_name}" in output_str
    assert 'id="test-id"' in output_str
    assert 'class="test-class"' in output_str

    if is_self_closing:
        assert (
            TEST_TEXT not in output_str
        )  
    else:
        assert TEST_TEXT in output_str
        assert f"</{tag_name}>" in output_str


@pytest.mark.parametrize(
    "category, TagClass, tag_name, is_self_closing", LIGHT_OOP_TAGS
)
def test_light_oop_streaming(shared_el, category, TagClass, tag_name, is_self_closing):
    """Tests that Light OOP classes correctly yield generators via .stream()"""

    if is_self_closing:
        node = TagClass(**TEST_ATTRS)
    else:
        node = TagClass(TEST_TEXT, **TEST_ATTRS)

    
    stream_gen = (
        node.stream(shared_el, batch=10)
        if "EL" in inspect.signature(node.stream).parameters
        else node.stream(batch=10)
    )

    assert inspect.isgenerator(
        stream_gen
    ), f"{TagClass.__name__}.stream() did not return a generator!"

    chunks = list(stream_gen)
    full_output = "".join(chunks)

    assert len(chunks) > 0, "Stream yielded empty generator"
    assert f"<{tag_name}" in full_output
    assert 'id="test-id"' in full_output


@pytest.mark.parametrize(
    "category, tag_func, tag_name, is_self_closing", LIGHT_FUNC_TAGS
)
def test_light_func_eager_render(
    shared_el, category, tag_func, tag_name, is_self_closing
):
    """Tests that Light Functional wrappers render eagerly."""

    if is_self_closing:
        output = tag_func(shared_el, **TEST_ATTRS)
    else:
        output = tag_func(shared_el, TEST_TEXT, **TEST_ATTRS)

    output_str = "".join(output) if isinstance(output, list) else str(output)

    assert f"<{tag_name}" in output_str
    assert 'id="test-id"' in output_str

    if is_self_closing:
        assert TEST_TEXT not in output_str
    else:
        assert TEST_TEXT in output_str
        assert f"</{tag_name}>" in output_str


@pytest.mark.parametrize(
    "category, tag_func, tag_name, is_self_closing", LIGHT_FUNC_TAGS
)
def test_light_func_streaming(shared_el, category, tag_func, tag_name, is_self_closing):
    """Tests that Light Functional wrappers return streams when stream=True."""

    if is_self_closing:
        stream_gen = tag_func(
            shared_el, stream=True, batch=10, **TEST_ATTRS
        )
    else:
        # Wrap content in a generator to prove lazy evaluation works
        lazy_content = (char for char in TEST_TEXT)
        stream_gen = tag_func(
            shared_el, lazy_content, stream=True, batch=10, **TEST_ATTRS
        )

    # Check for __iter__ to support both native generators and custom StreamManager objects
    assert hasattr(
        stream_gen, "__iter__"
    ), f"{tag_func.__name__}(stream=True) did not return an iterable/StreamManager!"

    chunks = list(stream_gen)
    full_output = "".join(chunks)

    assert len(chunks) > 0, "Functional stream yielded empty generator"
    assert f"<{tag_name}" in full_output
    assert 'id="test-id"' in full_output

    if not is_self_closing:
        assert (
            TEST_TEXT in full_output
        )  # Ensures the nested lazy_content generator was consumed!
