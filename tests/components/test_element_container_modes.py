"""
Tests for Element rendering in different container modes:
- Default mode (str): self.element is a string
- List mode (is_list=True): self.element is a list
- Deque mode (use_deque=True): self.element is a deque

These tests validate the fixes for:
1. Correct container initialization (element + content)
2. Operator precedence bug in content init
3. build_tag returning the correct type per mode
4. raw() / set_content() working with deque content
5. Streaming from deque vs list
"""

import pytest
from collections import deque
from src.probo.components.elements import Element


# =====================================================================
# FIXTURES
# =====================================================================

@pytest.fixture
def str_builder():
    """Default string-mode Element."""
    return Element()


@pytest.fixture
def list_builder():
    """List-mode Element (is_list=True, use_deque=False)."""
    return Element(is_list=True)


@pytest.fixture
def deque_builder():
    """Deque-mode Element (is_list=True, use_deque=True)."""
    return Element(is_list=True, use_deque=True)


# =====================================================================
# 1. INITIALIZATION — correct container types
# =====================================================================

class TestInitialization:
    """Verify that element and content are initialized to the correct type."""

    def test_default_mode_types(self, str_builder):
        assert isinstance(str_builder.element, str)
        assert isinstance(str_builder.content, str)
        assert str_builder.is_list is False
        assert str_builder.is_deque is False

    def test_list_mode_types(self, list_builder):
        assert isinstance(list_builder.element, list)
        assert isinstance(list_builder.content, list)
        assert list_builder.is_list is True
        assert list_builder.is_deque is False

    def test_deque_mode_types(self, deque_builder):
        assert isinstance(deque_builder.element, deque)
        assert isinstance(deque_builder.content, deque)
        assert deque_builder.is_list is True
        assert deque_builder.is_deque is True
        assert deque_builder.is_deque is True

    def test_init_with_tag_str_mode(self):
        """When tag is provided in string mode, element is a ProboSourceString."""
        el = Element(tag="div")
        assert isinstance(el.element, str)
        assert "<div>" in el.element
        assert "</div>" in el.element

    def test_init_with_tag_list_mode(self):
        """When tag is provided in list mode, element is a list."""
        el = Element(tag="div", is_list=True)
        assert isinstance(el.element, list)
        joined = "".join(el.element)
        assert "<div>" in joined
        assert "</div>" in joined

    def test_init_with_tag_deque_mode(self):
        """When tag is provided in deque mode, element is a deque."""
        el = Element(tag="div", is_list=True, use_deque=True)
        assert isinstance(el.element, deque)
        joined = "".join(el.element)
        assert "<div>" in joined
        assert "</div>" in joined

    def test_content_not_clobbered_after_build(self):
        """Ensure the use_deque init doesn't erase content set by build_tag."""
        el = Element(tag="div", content="Hello", is_list=True, use_deque=True)
        # Content should have been consumed by build_tag, not wiped after
        assert isinstance(el.element, deque)


# =====================================================================
# 2. BUILD_TAG — output type matches mode
# =====================================================================

class TestBuildTag:
    """Verify build_tag returns the correct container type."""

    def test_build_tag_str_mode(self, str_builder):
        str_builder.div()
        assert isinstance(str_builder.element, str)
        assert str_builder.element == "<div></div>"

    def test_build_tag_list_mode(self, list_builder):
        list_builder.div()
        assert isinstance(list_builder.element, list)
        assert list_builder.element[0] == "<div>"
        assert list_builder.element[-1] == "</div>"

    def test_build_tag_deque_mode(self, deque_builder):
        deque_builder.div()
        assert isinstance(deque_builder.element, deque)
        assert deque_builder.element[0] == "<div>"
        assert deque_builder.element[-1] == "</div>"

    def test_build_tag_with_content_list(self, list_builder):
        list_builder.div("Hello")
        assert isinstance(list_builder.element, list)
        joined = "".join(list_builder.element)
        assert "<div>" in joined
        assert "Hello" in joined
        assert "</div>" in joined

    def test_build_tag_with_content_deque(self, deque_builder):
        deque_builder.div("Hello")
        assert isinstance(deque_builder.element, deque)
        joined = "".join(deque_builder.element)
        assert "<div>" in joined
        assert "Hello" in joined
        assert "</div>" in joined

    def test_build_tag_with_attrs_deque(self, deque_builder):
        deque_builder.set_attrs(id="main", Class="container")
        deque_builder.div("Content")
        assert isinstance(deque_builder.element, deque)
        joined = "".join(deque_builder.element)
        assert 'id="main"' in joined
        assert 'class="container"' in joined
        assert "Content" in joined

    def test_void_tag_list_mode(self, list_builder):
        list_builder.img(src="/logo.png")
        assert isinstance(list_builder.element, list)
        joined = "".join(list_builder.element)
        assert "<img" in joined
        assert "/>" in joined

    def test_void_tag_deque_mode(self, deque_builder):
        deque_builder.img(src="/logo.png")
        assert isinstance(deque_builder.element, deque)
        joined = "".join(deque_builder.element)
        assert "<img" in joined
        assert "/>" in joined


# =====================================================================
# 3. TAG HANDLER CHAIN — type preserved across calls
# =====================================================================

class TestTagHandlerChain:
    """Verify that calling tag methods preserves the correct container type."""

    def test_chained_calls_str_mode(self, str_builder):
        str_builder.set_content("inner")
        str_builder.div()
        assert isinstance(str_builder.element, str)
        assert "inner" in str_builder.element

    def test_chained_calls_list_mode(self, list_builder):
        list_builder.set_content("inner")
        list_builder.div()
        assert isinstance(list_builder.element, list)
        joined = "".join(list_builder.element)
        assert "inner" in joined

    def test_chained_calls_deque_mode(self, deque_builder):
        deque_builder.set_content("inner")
        deque_builder.div()
        assert isinstance(deque_builder.element, deque)
        joined = "".join(deque_builder.element)
        assert "inner" in joined

    def test_attrs_chaining_deque(self, deque_builder):
        res = deque_builder.set_attrs(id="1").set_content("X")
        assert res is deque_builder
        res.div()
        assert isinstance(deque_builder.element, deque)
        joined = "".join(deque_builder.element)
        assert '<div id="1">' in joined
        assert "X" in joined


# =====================================================================
# 4. RAW METHOD — works with all modes
# =====================================================================

class TestRawMethod:
    """Verify raw() works correctly with str, list, and deque modes."""

    def test_raw_str_mode(self, str_builder):
        str_builder.raw("<p>Hello</p>")
        assert "<p>Hello</p>" in str_builder.element

    def test_raw_list_mode(self, list_builder):
        list_builder.raw("<p>Hello</p>")
        joined = "".join(list_builder.element)
        assert "<p>Hello</p>" in joined

    def test_raw_deque_mode(self, deque_builder):
        deque_builder.raw("<p>Hello</p>")
        joined = "".join(deque_builder.element)
        assert "<p>Hello</p>" in joined

    def test_raw_inner_deque_mode(self, deque_builder):
        """raw() with inner=True should append to content without crashing."""
        deque_builder.raw("<p>Hello</p>", inner=True)
        assert isinstance(deque_builder.content, deque)
        joined = "".join(deque_builder.content)
        assert "<p>Hello</p>" in joined

    def test_raw_comment_deque_mode(self, deque_builder):
        """raw() with is_comment=True should wrap in <!-- --> for deque."""
        deque_builder.raw("comment text", is_comment=True)
        joined = "".join(deque_builder.element)
        assert "<!--" in joined
        assert "comment text" in joined
        assert "-->" in joined

    def test_raw_inner_comment_deque_mode(self, deque_builder):
        """raw() with inner=True and is_comment=True for deque content."""
        deque_builder.raw("hidden", inner=True, is_comment=True)
        assert isinstance(deque_builder.content, deque)
        assert "<!--" in list(deque_builder.content)
        assert "hidden" in "".join(deque_builder.content)
        assert "-->" in list(deque_builder.content)


# =====================================================================
# 5. CUSTOM ELEMENT — type matches mode
# =====================================================================

class TestCustomElement:
    """Verify custom_element returns the correct container type."""

    def test_custom_element_str_mode(self, str_builder):
        str_builder.custom_element("my-widget", content="Hi")
        assert isinstance(str_builder.element, str)
        assert "<my-widget>" in str_builder.element
        assert "Hi" in str_builder.element

    def test_custom_element_list_mode(self, list_builder):
        list_builder.custom_element("my-widget", content="Hi")
        assert isinstance(list_builder.element, list)
        joined = "".join(list_builder.element)
        assert "<my-widget>" in joined
        assert "Hi" in joined

    def test_custom_element_deque_mode(self, deque_builder):
        deque_builder.custom_element("my-widget", content="Hi")
        assert isinstance(deque_builder.element, deque)
        joined = "".join(deque_builder.element)
        assert "<my-widget>" in joined
        assert "Hi" in joined


# =====================================================================
# 6. STREAMING — list vs deque behavior
# =====================================================================

class TestStreaming:
    """Verify stream() works correctly for both list and deque modes."""

    def test_stream_from_str_yields_once(self, str_builder):
        """String mode should yield the full element as a single chunk."""
        str_builder.div("Hello")
        chunks = list(str_builder.stream())
        assert len(chunks) == 1
        assert "Hello" in chunks[0]

    def test_stream_from_list(self, list_builder):
        list_builder.div("Hello")
        chunks = list(list_builder.stream(batch=1))
        full = "".join(chunks)
        assert "<div>" in full
        assert "Hello" in full
        assert "</div>" in full

    def test_stream_from_deque(self, deque_builder):
        deque_builder.div("Hello")
        chunks = list(deque_builder.stream(batch=1))
        full = "".join(chunks)
        assert "<div>" in full
        assert "Hello" in full
        assert "</div>" in full

    def test_stream_deque_clears_on_consume(self, deque_builder):
        """Deque stream popleft() should empty the deque after consuming."""
        deque_builder.div("Hello")
        _ = list(deque_builder.stream(batch=1))
        # After streaming, deque should be empty (popleft consumed everything)
        assert len(deque_builder.element) == 0

    def test_stream_list_clears_on_consume(self, list_builder):
        """List stream should clear after consuming."""
        list_builder.div("Hello")
        assert len(list_builder.element) > 0
        _ = list(list_builder.stream(batch=1))
        assert len(list_builder.element) == 0

    def test_stream_batching_list(self, list_builder):
        """With batch=2, fragments should be joined in groups of 2."""
        for i in range(6):
            list_builder.span(f"Item {i}", set_as_content=True)
        list_builder.div()
        chunks = list(list_builder.stream(batch=3))
        # Each chunk (except possibly the last) should contain ~3 fragments joined
        assert len(chunks) >= 1

    def test_stream_batching_deque(self, deque_builder):
        """With batch=2, deque fragments should be joined in groups of 2."""
        for i in range(6):
            deque_builder.span(f"Item {i}", set_as_content=True)
        deque_builder.div()
        chunks = list(deque_builder.stream(batch=3))
        assert len(chunks) >= 1


# =====================================================================
# 7. RENDER_CONTENT — resets to correct container type
# =====================================================================

class TestRenderContent:
    """Verify render_content drains content and resets to the correct type."""

    def test_render_content_resets_str(self, str_builder):
        str_builder.content = "hello"
        _ = str_builder.render_content()
        assert str_builder.content == ""
        assert isinstance(str_builder.content, str)

    def test_render_content_resets_list(self, list_builder):
        list_builder.content = ["hello"]
        _ = list_builder.render_content()
        assert list_builder.content == []
        assert isinstance(list_builder.content, list)

    def test_render_content_resets_deque(self, deque_builder):
        deque_builder.content = deque(["hello"])
        _ = deque_builder.render_content()
        assert list(deque_builder.content) == []
        assert isinstance(deque_builder.content, deque)

    def test_render_content_returns_original(self, deque_builder):
        original = deque(["a", "b"])
        deque_builder.content = original
        result = deque_builder.render_content()
        assert result is original


# =====================================================================
# 8. CONTENT ACCUMULATION — prepend/append in both modes
# =====================================================================

class TestContentAccumulation:
    """Verify content is correctly appended/prepended in list and deque modes."""

    def test_append_content_list(self, list_builder):
        list_builder.span("A", set_as_content=True)
        list_builder.span("B", set_as_content=True)
        assert isinstance(list_builder.content, list)
        joined = "".join(list_builder.content)
        assert "A" in joined
        assert "B" in joined

    def test_append_content_deque(self, deque_builder):
        deque_builder.span("A", set_as_content=True)
        deque_builder.span("B", set_as_content=True)
        assert isinstance(deque_builder.content, deque)
        joined = "".join(deque_builder.content)
        assert "A" in joined
        assert "B" in joined

    def test_prepend_content_list_with_history(self):
        """With collect_history=True, previous element output feeds into the next tag."""
        builder = Element(is_list=True, collect_history=True)
        builder.span("A")  # builds <span>A</span>, stored in element
        builder.div()      # previous element is collected into content, then wrapped in <div>
        assert isinstance(builder.element, list)
        joined = "".join(builder.element)
        assert "<span>" in joined
        assert "A" in joined
        assert "<div>" in joined

    def test_prepend_content_deque_with_history(self):
        """With collect_history=True, previous element output feeds into the next tag."""
        builder = Element(is_list=True, use_deque=True, collect_history=True)
        builder.span("A")  # builds <span>A</span>, stored in element
        builder.div()      # previous element is collected into content, then wrapped in <div>
        assert isinstance(builder.element, deque)
        joined = "".join(builder.element)
        assert "<span>" in joined
        assert "A" in joined
        assert "<div>" in joined


# =====================================================================
# 9. EDGE CASES
# =====================================================================

class TestEdgeCases:
    """Boundary conditions and regression tests."""

    def test_empty_deque_element_renders_empty_tag(self, deque_builder):
        """An empty deque builder should still produce valid HTML."""
        deque_builder.div()
        assert isinstance(deque_builder.element, deque)
        joined = "".join(deque_builder.element)
        assert joined == "<div></div>"

    def test_empty_list_element_renders_empty_tag(self, list_builder):
        list_builder.div()
        assert isinstance(list_builder.element, list)
        joined = "".join(list_builder.element)
        assert joined == "<div></div>"

    def test_stringify_element_deque(self, deque_builder):
        """stringify_element should convert deque to a ProboSourceString."""
        deque_builder.div("Hello")
        deque_builder.stringify_element()
        assert isinstance(deque_builder.element, str)
        assert "<div>" in deque_builder.element

    def test_use_deque_method(self):
        """Calling use_deque() on an existing Element should switch content to deque."""
        el = Element(is_list=True)
        assert isinstance(el.content, list)
        el.use_deque()
        assert isinstance(el.content, deque)
        assert el.is_deque is True

    def test_nested_elements_deque(self, deque_builder):
        """Building nested elements should preserve deque type."""
        deque_builder.set_content("<span>inner</span>")
        deque_builder.div()
        assert isinstance(deque_builder.element, deque)
        joined = "".join(deque_builder.element)
        assert "<div>" in joined
        assert "<span>inner</span>" in joined
        assert "</div>" in joined

    def test_multiple_tag_calls_deque(self, deque_builder):
        """Multiple sequential tag calls should each produce a deque."""
        deque_builder.div("First")
        assert isinstance(deque_builder.element, deque)
        first = "".join(deque_builder.element)

        deque_builder.span("Second")
        assert isinstance(deque_builder.element, deque)
        second = "".join(deque_builder.element)

        assert "<div>" in first
        assert "<span>" in second
