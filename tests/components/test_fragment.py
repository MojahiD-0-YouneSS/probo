from probo.components.fragment import frag
from probo import div
def test_fragment_coverage():
    """Specifically targets the 0% fragment.py file."""
    # Test Eager Fragment
    f = frag("A", "B")
    assert f == "AB"

    # Test Streaming Fragment
    f_stream = frag("A", "B", stream=True)
    assert list(f_stream) == ["A", "B"]

def test_fragment_deep_resolution():
    """Hits the recursive streaming paths in fragment.py."""

    # Test nested fragments and generators
    def gen_content():
        yield "Chunk 1"
        yield "Chunk 2"

    f = frag(div("Parent"), frag(gen_content(), stream=True), stream=True)

    output = list(f)
    assert "<div>Parent</div>" in output
    assert "Chunk 1" in output
    assert "Chunk 2" in output
