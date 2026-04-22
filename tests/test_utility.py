import pytest
import sys
import inspect
from enum import Enum
from collections import deque
from unittest.mock import MagicMock, patch

# Update imports to pull from the newly defined utility module
from probo.utility import (
    StreamManager,
    _resolve_stream,
    ProboSourceString,
    markup_escape,
    exists_in_dict,
    render_attributes,
    EnumLookUPMixin,
)


# ==========================================
# TESTS: ProboSourceString
# ==========================================


def test_probo_source_string_html():
    """Tests the __html__ interface for safe string bypassing."""
    pss = ProboSourceString("<div>safe</div>")
    assert pss.__html__() == "<div>safe</div>"


def test_probo_source_string_add():
    """Tests that appending strings preserves the ProboSourceString type."""
    pss = ProboSourceString("Hello")
    result = pss + " World"

    assert result == "Hello World"
    assert isinstance(result, ProboSourceString)


def test_probo_source_string_radd():
    """Tests that prepending strings preserves the ProboSourceString type."""
    pss = ProboSourceString("World")
    result = "Hello " + pss

    assert result == "Hello World"
    assert isinstance(result, ProboSourceString)


# ==========================================
# TESTS: markup_escape
# ==========================================


def test_markup_escape_basic_strings():
    """Tests standard string and tag escaping."""
    assert (
        markup_escape("<script>alert(1)</script>")
        == "&lt;script&gt;alert(1)&lt;/script&gt;"
    )
    assert markup_escape(12345) == "12345"


def test_markup_escape_renderable_objects():
    """Tests escaping objects that have a native .render() method."""

    class MockRenderable:
        def render(self):
            return "<b>Bold</b>"

    assert markup_escape(MockRenderable()) == "&lt;b&gt;Bold&lt;/b&gt;"


# ==========================================
# TESTS: exists_in_dict
# ==========================================


def test_exists_in_dict(monkeypatch):
    """Tests deep searching for selectors within dictionary keys and values."""

    # Safely mock the internal import to prevent missing dependency crashes
    mock_utils = MagicMock()
    mock_utils.resolve_complex_selector.return_value = [".btn", "#submit"]
    monkeypatch.setitem(sys.modules, "probo.styles.utils", mock_utils)

    # 1. Match top-level key
    data_key = {"btn": "some_value"}
    assert exists_in_dict(data_key, ".btn") is True

    # 2. Match nested key
    data_nested_key = {"wrapper": {"submit": "yes"}}
    assert exists_in_dict(data_nested_key, "#submit") is True

    # 3. Match nested value
    data_nested_val = {"wrapper": {"class": "btn"}}
    assert exists_in_dict(data_nested_val, ".btn") is True

    # 4. No Match
    data_missing = {"wrapper": {"class": "other"}}
    assert exists_in_dict(data_missing, ".btn") is False


# ==========================================
# TESTS: render_attributes
# ==========================================


def test_render_attributes_standard():
    """Tests standard attributes and Python underscore conversions."""
    attrs = {"class": "container", "data_id": 1, "aria_label": "Menu"}
    res = render_attributes("div", attrs)
    assert res == 'class="container" data-id="1" aria-label="Menu"'


def test_render_attributes_booleans():
    """Tests that True yields a key-only attribute, and False/None are omitted."""
    attrs = {"required": True, "disabled": False, "hidden": None}
    res = render_attributes("input", attrs)
    assert res == "required"


def test_render_attributes_lists():
    """Tests that lists are intelligently joined by spaces (great for class lists)."""
    attrs = {"class": ["btn", "btn-primary", "active"]}
    res = render_attributes("button", attrs)
    assert res == 'class="btn btn-primary active"'


def test_render_attributes_html_defaults():
    """Tests that redundant HTML defaults are skipped to keep output clean."""
    # Matches default -> should skip
    res1 = render_attributes("input", {"type": "text", "name": "username"})
    assert res1 == 'name="username"'

    # Overrides default -> should render
    res2 = render_attributes("input", {"type": "password"})
    assert res2 == 'type="password"'

    # Matches form default
    res3 = render_attributes("form", {"method": "get", "action": "/"})
    assert res3 == 'action="/"'


# ==========================================
# TESTS: EnumLookUPMixin
# ==========================================


def test_enum_lookup_mixin():
    """Tests the high-speed O(1) caching features on the Enum mixin."""

    class MockEnum(EnumLookUPMixin, Enum):
        DIV = ("div", {"void": False})
        IMG = ("img", {"void": True})

    # Thaw it
    MockEnum.thaw()

    # Verify cached sets
    assert MockEnum.keys_set == {"DIV", "IMG"}
    assert MockEnum.values_map["div"] == MockEnum.DIV
    assert MockEnum.values_map["img"] == MockEnum.IMG
    assert MockEnum.void_set == {"img"}

    # Verify custom iterator override logic
    instance = MockEnum.DIV
    assert set(instance.keys_set) == {"DIV", "IMG"}


# ==========================================
# TESTS: StreamManager
# ==========================================


def test_stream_manager_basic_tags():
    """Tests that opening and closing tags wrap the generator properly."""

    def simple_gen():
        yield "Content"

    sm = StreamManager(
        opening="<div>", content_gen=simple_gen(), closing="</div>", chunk_size=5
    )
    results = list(sm)

    assert results == ["<div>", "Content", "</div>"]


def test_stream_manager_chunking():
    """Tests that the buffer correctly flushes when it hits the exact chunk size."""

    def num_gen():
        for i in range(5):  # 0, 1, 2, 3, 4
            yield str(i)

    # Chunk size 2 should result in: "01", "23", "4"
    sm = StreamManager(opening=None, content_gen=num_gen(), closing=None, chunk_size=2)
    results = list(sm)

    assert results == ["01", "23", "4"]


def test_stream_manager_complex_fragments():
    """Tests the specific branch that handles nested lists and deques."""

    def complex_gen():
        yield ["list", "_", "item"]
        yield deque(["deque", "_", "item"])
        yield 42  # Int fallback branch

    sm = StreamManager(
        opening="<p>", content_gen=complex_gen(), closing="</p>", chunk_size=10
    )
    results = list(sm)

    # "list_item", "deque_item", and "42" should all be joined into chunks
    assert results == ["<p>", "list_itemdeque_item42", "</p>"]


def test_stream_manager_empty_gen():
    """Tests behavior when the generator yields absolutely nothing."""

    def empty_gen():
        yield from []

    sm = StreamManager(opening="<empty>", content_gen=empty_gen(), closing="</empty>")
    results = list(sm)

    # Should yield opening and closing without crashing or yielding empty strings
    assert results == ["<empty>", "</empty>"]


def test_stream_manager_no_wrappers():
    """Tests the manager without opening or closing tags."""

    def gen():
        yield "naked"

    sm = StreamManager(opening=None, content_gen=gen(), closing=None)
    results = list(sm)

    assert results == ["naked"]


# ==========================================
# TESTS: _resolve_stream
# ==========================================


def test_resolve_stream_with_generator():
    """Tests the inspect.isgenerator() branch."""

    def nested_gen():
        yield "A"
        yield "B"

    content_tuple = (nested_gen(),)
    results = list(_resolve_stream(content_tuple))

    assert results == ["A", "B"]


def test_resolve_stream_standard_object():
    """Tests the fallback branch that wraps primitive types in the REAL ProboSourceString."""
    content_tuple = ("Hello", 123)
    results = list(_resolve_stream(content_tuple))

    assert len(results) == 2
    # Verify outputs equal string evaluations but are securely typed
    assert results[0] == "Hello"
    assert isinstance(results[0], ProboSourceString)
    assert results[1] == "123"
    assert isinstance(results[1], ProboSourceString)


def test_resolve_stream_streamable_class():
    """Tests delegating to standard components that have a .stream() method."""

    class MockComponent:
        def stream(self, batch):
            yield f"Streamed with batch={batch}"

    content_tuple = (MockComponent(),)
    results = list(_resolve_stream(content_tuple, chunk_size=99))

    assert results == ["Streamed with batch=99"]


def test_resolve_stream_light_tag_class():
    """Tests the highly specific branch for 'light_tag' components requiring an EL context."""

    class MockLightComponent:
        light_tag = True

        def stream(self, batch, EL):
            yield f"Light stream batch={batch} EL={EL}"

    content_tuple = (MockLightComponent(),)

    # 1. With EL provided (Hits the light_tag branch)
    results_with_el = list(_resolve_stream(content_tuple, chunk_size=10, EL="LI"))
    assert results_with_el == ["Light stream batch=10 EL=LI"]

    # 2. Without EL provided (Falls back to standard stream branch because EL is None)
    class MockLightComponentFallback:
        light_tag = True

        def stream(self, batch):
            yield "Fallback stream"

    results_without_el = list(
        _resolve_stream((MockLightComponentFallback(),), chunk_size=10, EL=None)
    )
    assert results_without_el == ["Fallback stream"]
