import pytest
import json
import hashlib
from probo.router.payload import RouterPayload # Adjust import based on your actual structure

# Mock component for testing .render() behavior
class MockComponent:
    def __init__(self, content):
        self.content = content
    def render(self):
        return self.content

@pytest.fixture(autouse=True)
def clear_cache():
    """Clears the global state cache before every test to ensure isolation."""
    RouterPayload._state_cache = {}

def test_initial_payload_processing():
    """1. Test that initialization correctly processes and hashes a new component."""
    comp = MockComponent("<h1>Hello</h1>")
    payload = RouterPayload(header=comp)
    
    expected_hash = hashlib.md5("<h1>Hello</h1>".encode()).hexdigest()
    assert "header" in payload.diff
    assert payload.diff["header"]["hash"] == expected_hash
    assert payload.diff["header"]["content"] == "<h1>Hello</h1>"

def test_cache_skips_unchanged_content():
    """2. Test that unchanged content results in an empty diff and 'no-change' status."""
    comp = "static content"
    # First run caches it
    RouterPayload(sidebar=comp)
    
    # Second run with same content
    payload2 = RouterPayload(sidebar=comp)
    assert payload2.diff == {}
    assert "no-change" in payload2.get_json_response()

def test_diff_detects_changes():
    """3. Test that changing component content triggers a diff update."""
    # Cache initial state
    RouterPayload(main="Version 1")
    
    # Update content
    payload = RouterPayload(main="Version 2")
    assert "main" in payload.diff
    assert payload.diff["main"]["content"] == "Version 2"
    assert "update" in payload.get_json_response()

def test_json_response_structure():
    """4. Verify the JSON output format matches SSDOM requirements."""
    payload = RouterPayload(btn=MockComponent("<button>Click</button>"))
    data = json.loads(payload.get_json_response())
    
    assert data["status"] == "update"
    assert "btn" in data["payload"]
    assert "content" in data["payload"]["btn"]
    assert "hash" in data["payload"]["btn"]

def test_xml_response_structure():
    """5. Verify the XML output format correctly wraps fragments."""
    payload = RouterPayload(nav="<nav></nav>")
    xml = payload.get_xml_response()
    
    assert xml.startswith("<ssdom_update>")
    assert '<component id="nav"' in xml
    assert "</ssdom_update>" in xml

def test_multiple_payload_diffing():
    """6. Test processing multiple components where only one changes."""
    RouterPayload(a="fixed", b="old")
    
    # Only 'b' changes
    payload = RouterPayload(a="fixed", b="new")
    
    assert "a" not in payload.diff
    assert "b" in payload.diff

def test_load_method_functionality():
    """7. Test the .load() method for late-binding additional payloads."""
    payload = RouterPayload(initial="data")
    payload.load(late="arrival")
    
    assert "late" in payload.diff
    assert RouterPayload._state_cache["late"] is not None

def test_get_response_dispatcher():
    """8. Test the universal get_response dispatcher for both formats."""
    payload = RouterPayload(test="val")
    
    json_res = payload.get_response("json")
    xml_res = payload.get_response("xml")
    
    assert '"status": "update"' in json_res
    assert "<ssdom_update>" in xml_res

def test_non_renderable_fallback():
    """9. Test that non-renderable objects (integers/floats) are cast to strings correctly."""
    payload = RouterPayload(count=123)
    assert payload.diff["count"]["content"] == "123"

def test_state_cache_persistence_across_instances():
    """10. Verify that the class-level cache persists across different instances."""
    # Instance 1 caches 'key1'
    RouterPayload(key1="content1")
    
    # Instance 2 should see 'key1' as unchanged even if not passed in init
    payload2 = RouterPayload(key1="content1")
    assert "key1" not in payload2.diff
    assert "key1" in RouterPayload._state_cache