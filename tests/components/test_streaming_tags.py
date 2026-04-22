import pytest
import inspect
from probo.components.elements import Element

# Assuming these are available in your probo namespace
from probo import DIV, IMG, SVG, div, img, svg

# =====================================================================
# 1. FIXTURES & DEFINITIONS
# =====================================================================

# (Category, OOP_Class, tag_name, is_self_closing)
HEAVY_OOP_TAGS = [
    ("block", DIV, "div", False),
    ("self_closing", IMG, "img", True),
    ("svg", SVG, "svg", False),
]

# (Category, Func_Wrapper, tag_name, is_self_closing)
HEAVY_FUNC_TAGS = [
    ("block", div, "div", False),
    ("self_closing", img, "img", True),
    ("svg", svg, "svg", False),
]

# Shared Test Data
TEST_TEXT = "probo-heavy-data"
TEST_ATTRS = {"id": "heavy-id", "class": "heavy-class"}


@pytest.fixture
def shared_el():
    """Provides a fresh Element pipeline, though Heavy nodes might use their own."""
    return Element(is_list=True, use_deque=True)


# =====================================================================
# 2. OOP (HEAVY CLASSES) TESTS
# =====================================================================


@pytest.mark.parametrize(
    "category, TagClass, tag_name, is_self_closing", HEAVY_OOP_TAGS
)
def test_heavy_oop_eager_render(
    shared_el, category, TagClass, tag_name, is_self_closing
):
    """Tests that Heavy OOP classes render eagerly into strings correctly."""

    if is_self_closing:
        node = TagClass(**TEST_ATTRS)
    else:
        node = TagClass(TEST_TEXT, **TEST_ATTRS)

    # Execute render, safely passing EL if the signature requests it
    if hasattr(node, "render"):
        output = (
            node.render(shared_el)
            if "EL" in inspect.signature(node.render).parameters
            else node.render()
        )
    else:
        output = str(node)

    output_str = "".join(output) if isinstance(output, list) else str(output)

    # Assertions
    assert f"<{tag_name}" in output_str
    assert 'id="heavy-id"' in output_str
    assert 'class="heavy-class"' in output_str

    if is_self_closing:
        assert (
            TEST_TEXT not in output_str
        )  # Self-closing tags shouldn't swallow content
    else:
        assert TEST_TEXT in output_str
        assert f"</{tag_name}>" in output_str

    # Heavy nodes typically track parents, let's verify standard Probo Node behavior exists
    assert (
        hasattr(node, "parent") or hasattr(node, "children") or hasattr(node, "content")
    ), "Heavy Node missing structural attributes!"


@pytest.mark.parametrize(
    "category, TagClass, tag_name, is_self_closing", HEAVY_OOP_TAGS
)
def test_heavy_oop_streaming(shared_el, category, TagClass, tag_name, is_self_closing):
    """Tests that Heavy OOP classes correctly yield chunks via .stream()"""

    if is_self_closing:
        node = TagClass(**TEST_ATTRS)
    else:
        node = TagClass(TEST_TEXT, **TEST_ATTRS)

    # Tap into the stream
    stream_gen = (
        node.stream(shared_el, batch=10)
        if "EL" in inspect.signature(node.stream).parameters
        else node.stream(batch=10)
    )

    # Check for __iter__ to support both native generators and custom StreamManager objects
    assert hasattr(
        stream_gen, "__iter__"
    ), f"{TagClass.__name__}.stream() did not return an iterable/StreamManager!"

    chunks = list(stream_gen)
    full_output = "".join(chunks)

    assert len(chunks) > 0, "Stream yielded empty generator"
    assert f"<{tag_name}" in full_output
    assert 'id="heavy-id"' in full_output


# =====================================================================
# 3. FUNCTIONAL (HEAVY FUNC) TESTS
# =====================================================================


@pytest.mark.parametrize(
    "category, tag_func, tag_name, is_self_closing", HEAVY_FUNC_TAGS
)
def test_heavy_func_eager_render(category, tag_func, tag_name, is_self_closing):
    """
    Tests that Heavy Functional wrappers render eagerly.
    Notice we don't pass `shared_el` here, as heavy functions typically instantiate their own.
    """
    if is_self_closing:
        output = tag_func(**TEST_ATTRS)
    else:
        output = tag_func(TEST_TEXT, **TEST_ATTRS)

    output_str = "".join(output) if isinstance(output, list) else str(output)

    assert f"<{tag_name}" in output_str
    assert 'id="heavy-id"' in output_str

    if is_self_closing:
        assert TEST_TEXT not in output_str
    else:
        assert TEST_TEXT in output_str
        assert f"</{tag_name}>" in output_str


@pytest.mark.parametrize(
    "category, tag_func, tag_name, is_self_closing", HEAVY_FUNC_TAGS
)
def test_heavy_func_streaming(category, tag_func, tag_name, is_self_closing):
    """Tests that Heavy Functional wrappers return streams when stream=True."""

    if is_self_closing:
        stream_gen = tag_func(stream=True, batch=10, **TEST_ATTRS)
    else:
        # Wrap content in a generator to prove lazy evaluation works
        lazy_content = (char for char in TEST_TEXT)
        stream_gen = tag_func(
            lazy_content, stream=True, batch=10, **TEST_ATTRS
        )

    # Check for __iter__ to support both native generators and custom StreamManager objects
    assert hasattr(
        stream_gen, "__iter__"
    ), f"{tag_func.__name__}(stream=True) did not return an iterable/StreamManager!"

    chunks = list(stream_gen)
    print(chunks)
    full_output = "".join(chunks)

    assert len(chunks) > 0, "Functional stream yielded empty generator"
    assert f"<{tag_name}" in full_output
    assert 'id="heavy-id"' in full_output

    if not is_self_closing:
        assert (
            TEST_TEXT in full_output
        )  # Ensures the nested lazy_content generator was consumed!
