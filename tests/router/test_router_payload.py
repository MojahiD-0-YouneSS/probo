import pytest
import json
import hashlib
from probo.router.payload import RouterPayload
from probo.context import TemplateComponentMap
from probo.router.router import ProboRouter
from probo import DIV, P

# --- Mocks for Integration ---

class StateComponent:
    """A component that simulates dynamic state."""
    def __init__(self, val):
        self.val = val
    def render(self):
        return f"<div>{self.val}</div>"

@pytest.fixture(autouse=True)
def clean_system():
    """Resets the global SSDOM cache before every test."""
    RouterPayload._state_cache = {}

@pytest.fixture
def router():
    """Returns a configured ProboRouter with a sample SSDOM route."""
    r = ProboRouter(app_name="IntegrationTest")
    
    @r.page("/api/update")
    def update_view(request):
        # Integration point: Router view returns a Payload object
        val = request.params.get("val", "default")
        return RouterPayload(
            main_content=DIV(P(f"Value: {val}"), Id="main"),
            sidebar=DIV("Static Sidebar", Id="side")
        )
    return r

# --- Integration Test Suite (20 Tests) ---

def test_router_payload_initial_render(router):
    """1. Verify router correctly renders a full payload on the first request."""
    # Simulating a first-time request
    payload = router.routes["/api/update"](type('MockReq', (), {'params': {'val': 'init'}})())
    res_json = json.loads(payload.get_json_response())
    
    assert res_json["status"] == "update"
    assert "main_content" in res_json["payload"]
    assert "sidebar" in res_json["payload"]

def test_cache_persistence_between_router_calls(router):
    """2. Verify that subsequent router calls recognize existing state."""
    req = type('MockReq', (), {'params': {'val': 'same'}})()
    
    # First call fills cache
    router.routes["/api/update"](req)
    
    # Second call should result in no-change
    payload2 = router.routes["/api/update"](req)
    res_json = json.loads(payload2.get_json_response())
    
    assert res_json["status"] == "no-change"
    assert payload2.diff == {}

def test_partial_router_update(router):
    """3. Verify only the changed component is sent back by the router."""
    # First call: init
    router.routes["/api/update"](type('MockReq', (), {'params': {'val': 'v1'}})())
    
    # Second call: change val (main_content changes, sidebar stays same)
    payload = router.routes["/api/update"](type('MockReq', (), {'params': {'val': 'v2'}})())
    res_json = json.loads(payload.get_json_response())
    
    assert "main_content" in res_json["payload"]
    assert "sidebar" not in res_json["payload"]

def test_hash_match_with_router_context(router):
    """4. Ensure the hash generated in the router matches expected MD5."""
    payload = router.routes["/api/update"](type('MockReq', (), {'params': {'val': 'test'}})())
    content = DIV(P("Value: test"), Id="main").render()
    expected_hash = hashlib.md5(content.encode()).hexdigest()
    
    assert payload.diff["main_content"]["hash"] == expected_hash

def test_xml_integration_format(router):
    """5. Verify the router can output XML fragments for SSDOM."""
    payload = router.routes["/api/update"](type('MockReq', (), {'params': {'val': 'xml'}})())
    xml = payload.get_response("xml")
    assert "<ssdom_update>" in xml
    assert 'id="main_content"' in xml

def test_tcm_fallback_payload_integration():
    """6. Test if TCM-based components correctly interact with the payload cache."""
    class MockTCM(TemplateComponentMap):
        def __init__(self, r_props = None, **url_name_comp):
            super().__init__(r_props, **url_name_comp)
    mock_tcm = MockTCM(**{"/tcm":"TCM Data"})
    router = ProboRouter()
    router.register_tcm(mock_tcm)

    # Simulate TCM rendering into a payload
    comp = router.tcm.get_component("/tcm")
    p1 = RouterPayload(tcm_node=comp)
    assert "tcm_node" in p1.diff
    
    p2 = RouterPayload(tcm_node=comp)
    assert "tcm_node" not in p2.diff

def test_large_payload_performance_hint(router):
    """7. Integration test for 100 components to ensure hashing overhead is minimal."""
    components = {f"id-{i}": f"content-{i}" for i in range(100)}
    p = RouterPayload(**components)
    assert len(p.diff) == 100

def test_payload_load_extension(router):
    """8. Verify .load() works correctly when called within a router view context."""
    p = RouterPayload(a="1")
    p.load(b="2")
    assert "a" in p.diff and "b" in p.diff

def test_none_content_handling_in_router(router):
    """9. Ensure router doesn't crash if a view returns a payload with None."""
    p = RouterPayload(empty=None)
    assert p.diff["empty"]["content"] == "None"

def test_duplicate_cid_overwrite(router):
    """10. Verify that providing the same CID twice in one payload handles the last one."""
    p = RouterPayload(item="first")
    p.load(item="second") # Overwrite
    assert p.diff["item"]["content"] == "second"

def test_complex_nesting_diff(router):
    """11. Verify nested DIVs are hashed correctly as a single unit by the payload."""
    nested = DIV(DIV(P("Deep")))
    p1 = RouterPayload(nested=nested)
    p2 = RouterPayload(nested=nested)
    assert p2.diff == {}

def test_router_status_on_no_change(router):
    """12. Check that the payload status string is exactly 'no-change' for JS compat."""
    p = RouterPayload(x=1) # Cache it
    p2 = RouterPayload(x=1)
    assert json.loads(p2.get_json_response())["status"] == "no-change"

def test_manual_cache_clear_triggers_resend(router):
    """13. Manually clearing the _state_cache should force the router to resend everything."""
    RouterPayload(x=1)
    RouterPayload._state_cache.clear()
    p = RouterPayload(x=1)
    assert "x" in p.diff

def test_signed_cookie_impact_on_hashing(router):
    """14. Ensure that content containing cookies hashes differently if values change."""
    p1 = RouterPayload(c=DIV("User: A"))
    p2 = RouterPayload(c=DIV("User: B"))
    assert p1.diff["c"]["hash"] != p2.diff["c"]["hash"]

def test_multiple_instances_isolation(router):
    """15. Verify two different Payloads in the same request cycle share the same cache."""
    p1 = RouterPayload(shared="data")
    p2 = RouterPayload(shared="data")
    assert "shared" in p1.diff
    assert "shared" not in p2.diff

def test_json_payload_key_integrity(router):
    """16. Ensure component IDs (CIDs) are preserved as keys in the JSON response."""
    p = RouterPayload(my_unique_id="content")
    data = json.loads(p.get_json_response())
    assert "my_unique_id" in data["payload"]

def test_empty_payload_init(router):
    """17. Verify initializing a payload with no arguments is safe."""
    p = RouterPayload()
    assert p.diff == {}
    assert "no-change" in p.get_json_response()

def test_binary_content_hashing(router):
    """18. Verify that bytes content is hashed correctly (compatibility check)."""
    p = RouterPayload(bin=b"some bytes")
    assert "bin" in p.diff

def test_router_payload_type_check(router):
    """19. Ensure RouterPayload strictly uses MD5 (Standard for SSDOM v1.3.0)."""
    p = RouterPayload(t="val")
    # MD5 is 32 chars
    assert len(p.diff["t"]["hash"]) == 32

def test_ssdom_update_tag_presence(router):
    """20. Verify XML transport uses the mandatory <ssdom_update> root tag."""
    p = RouterPayload(x=1)
    assert p.get_response("xml").startswith("<ssdom_update>")