import pytest
import gzip
import io
import json
from typing import Iterator
from unittest.mock import MagicMock, patch
from probo.streaming import (
GzipStreamer,
stream_render,
to_django_response,
)
from probo.components.elements import Element
# For testing purposes, we define/import the logic provided in the prompt
import sys


# Mocking Django for the integration test
class MockStreamingHttpResponse:
    def __init__(self, streaming_content, **kwargs):
        self.streaming_content = streaming_content
        self.headers = kwargs
        self.status_code = 200


def decompress_stream(byte_iterator: Iterator[bytes]) -> str:
    """Helper to verify GzipStreamer output by decompressing it."""
    bio = io.BytesIO()
    for chunk in byte_iterator:
        bio.write(chunk)
    bio.seek(0)
    with gzip.GzipFile(fileobj=bio, mode='rb') as f:
        return f.read().decode('utf-8')


# --- TEST SUITE ---

def test_gzip_streamer_integrity():
    """Hard Test 1: Verify that compressed output matches original input exactly."""
    fragments = ["<div>", "Hello ", "World", "</div>"]
    streamer = GzipStreamer(iter(fragments))

    decompressed_result = decompress_stream(streamer)
    assert decompressed_result == "<div>Hello World</div>"


def test_stream_render_mixed_types():
    """Hard Test 2: Verify handling of callables, raw strings, and renderable objects."""

    class MockElement:
        def render(self): return "<span>Element</span>"

    def my_tag(): return "<div>Tag</div>"

    def my_obj_tag(): return MockElement()

    # Mixture of callable strings, callable objects, and raw strings
    elements = [my_tag, "raw_text", my_obj_tag]

    result = list(stream_render(elements))
    assert result == ["<div>Tag</div>", "raw_text", "<span>Element</span>"]


def test_gzip_empty_stream():
    """Hard Test 3: Ensure empty generators don't crash the compressor."""
    streamer = GzipStreamer(iter([]))
    # Gzip of empty still produces a small header/footer
    result = b"".join(list(streamer))
    assert len(result) > 0
    assert decompress_stream(iter([result])) == ""


def test_large_payload_chunking():
    """Hard Test 4: Test streaming of massive fragments (Memory Pressure Test)."""
    # 1MB string
    large_string = "A" * 1024 * 1024
    fragments = [large_string for _ in range(5)]  # 5MB total

    streamer = GzipStreamer(iter(fragments))

    # We consume it chunk by chunk
    total_size = 0
    for chunk in streamer:
        total_size += len(chunk)

    # Compression should make it much smaller than 5MB
    assert total_size < (5 * 1024 * 1024)


def test_gzip_flushing_logic():
    """Hard Test 5: Ensure that every yielded chunk from GzipStreamer is usable."""
    fragments = ["part1", "part2"]
    streamer = GzipStreamer(iter(fragments))

    chunks = list(streamer)
    # GzipStreamer flushes every fragment, so we should have at least 2 chunks
    assert len(chunks) >= 2

    # Combined they should form a valid gzip file
    assert decompress_stream(iter(chunks)) == "part1part2"


def test_stream_render_exception_handling():
    """Hard Test 6: Verify behavior when a generator element raises an error."""

    def broken_el():
        raise ValueError("Simulated Error")

    gen = stream_render(["valid", broken_el])

    assert next(gen) == "valid"
    with pytest.raises(ValueError, match="Simulated Error"):
        next(gen)


@patch('sys.modules', {'django.http': MagicMock()})
def test_django_integration_mock():
    """Integration Test: Simulating the full flow into a Django Response."""
    from django.http import StreamingHttpResponse

    # Custom Mock for the specific class requested
    class MockNode:
        def render_stream(self):
            yield "<html>"
            yield "<body>"
            yield "Hello"
            yield "</body>"
            yield "</html>"

    node = MockNode()

    # We manually simulate to_django_response logic since we can't easily
    # import a real Django env here
    stream = node.render_stream()
    response_stream = GzipStreamer(stream)

    # Verify the final assembled result
    final_html = decompress_stream(response_stream)
    assert "<html><body>Hello</body></html>" == final_html


def test_probo_element_integration():
    """Hard Test 7: Integration with the actual Element class provided."""
    el = Element(is_natural=False)

    def lazy_div():
        # Using the monolith logic
        return el.div("Inner Content", id="test-id")

    # Pass the callable to stream_render
    stream = stream_render([lazy_div])
    result = "".join(list(stream))

    assert '<div id="test-id">Inner Content</div>' in result


def test_nested_stream_render():
    """Hard Test 8: Deep nesting of callables."""

    def level3(): return "depth"

    def level2(): return level3  # stream_render logic handles callables

    def level1(): return level2

    # Current stream_render implementation only calls once: content=el()
    # If level1() returns level2 (a callable), it will yield level2 as str()
    # unless logic is recursive. Let's test current behavior:
    res = list(stream_render([level1]))
    # Based on: content=el() -> level2. then yields content (level2)
    assert "function" in str(res[0])