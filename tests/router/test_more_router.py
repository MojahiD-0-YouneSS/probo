import pytest
from unittest.mock import MagicMock
from webtest import TestApp
import json
from probo.router.router import ProboRouter
from probo.router.settings import RouterSettings
from probo.context import TemplateComponentMap
from probo.router.discovery import ProboRoute

# ==========================================
# FIXTURES
# ==========================================


@pytest.fixture
def router():
    """Provides a fresh router with default settings."""
    settings = RouterSettings(DEBUG=True, ENABLE_GZIP=False)
    return ProboRouter(app_name="TestApp", settings=settings)


@pytest.fixture
def client(router):
    """
    Provides a WebTest client for WSGI integration testing.
    This safely simulates real HTTP requests without breaking Bottle proxies!
    """
    return TestApp(router.wsgi_app)


# ==========================================
# TEST 1: Initialization & Settings
# ==========================================


def test_router_initialization():
    settings = RouterSettings(PORT=9999, SECRET_KEY="my-secret")
    router = ProboRouter("MyApp", secret_key="override-secret", settings=settings)

    assert router.app_name == "MyApp"
    assert router.settings.PORT == 9999
    # Explicit secret_key should override the settings fallback
    assert router.secret_key == "override-secret"
    # The config should have been updated with dataclass dict
    assert router.wsgi_app.config["PORT"] == 9999


# ==========================================
# TEST 2: HTML Wrapping & WSGI Normalization
# ==========================================


def test_wrap_in_template(router):
    class MockComponent:
        def render(self):
            return "<div>Component</div>"

    res1 = router._wrap_in_template(MockComponent())
    assert "<div>Component</div>" in res1
    assert "<html" in res1.lower()

    html_string = "<HTML><body>Skip Wrap</body></HTML>"
    res2 = router._wrap_in_template(html_string)
    assert res2 == html_string

    res3 = router._wrap_in_template({"section": "Injected"})
    assert "Injected" in res3


def test_normalize_wsgi_output(router):
    class MockComponent:
        def render(self):
            return "Rendered"

    def wsgi_stream():
        yield b"byte_chunk"
        yield "string_chunk"
        yield MockComponent()
        yield {"section": "dict_chunk"}
        yield 123

    result = list(router._normalize_wsgi_output(wsgi_stream()))

    assert b"byte_chunk" in result
    assert b"string_chunk" in result
    assert b"Rendered" in result
    assert any(
        b"dict_chunk" in r and b"<html" in r.lower()
        for r in result
        if isinstance(r, bytes)
    )
    assert 123 in result


# ==========================================
# TEST 3: GZIP Compression
# ==========================================


def test_maybe_compress(monkeypatch):
    """Uses monkeypatch to verify GZIP compression safely without hitting WSGI iterable edge cases."""
    settings = RouterSettings(ENABLE_GZIP=True)
    router = ProboRouter(settings=settings)

    class MockRequest:
        headers = {"Accept-Encoding": "gzip, deflate"}

    class MockResponse:
        headers = {}

        def set_header(self, k, v):
            self.headers[k] = v

    # Inject our lightweight mocks
    monkeypatch.setattr("probo.router.router.request", MockRequest())
    mock_res = MockResponse()
    monkeypatch.setattr("probo.router.router.response", mock_res)

    # Request compression for string
    compressed = router._maybe_compress("Large HTML Body" * 10)
    assert isinstance(compressed, bytes)
    assert mock_res.headers.get("Content-Encoding") == "gzip"

    # Should safely bypass non-strings
    assert router._maybe_compress(b"binary data") == b"binary data"


# ==========================================
# TEST 4: The @page Routing Decorator
# ==========================================


def test_page_decorator_standard_request(router, client):
    """Tests the standard HTML return flow without HTMX or Cache."""

    @router.page("/hello")
    def hello_route():
        return "Hello World"

    res = client.get("/hello")

    assert "Hello World" in res.text
    assert "<html" in res.text.lower()


def test_page_decorator_htmx_request():
    """Tests that HTMX requests bypass the template wrapper and hit the payload tracker."""
    # Must explicitly set respond_format to trigger the payload diffing engine!
    router = ProboRouter(app_name="TestApp", respond_format="json")
    client = TestApp(router.wsgi_app)

    @router.page("/htmx-part")
    def htmx_route():
        return "<div>Chunk</div>"

    # Inject the HX-Request header normally via WebTest
    res = client.get("/htmx-part", headers={"HX-Request": "true"})

    # Parse the resulting JSON payload response
    data = json.loads(res.text)

    assert data["status"] == "update"
    assert "/htmx-part" in data["payload"]
    assert data["payload"]["/htmx-part"]["content"] == "<div>Chunk</div>"

    # Verify the internal tracker stored it
    assert "/htmx-part" in router.payload.diff


def test_page_decorator_caching(router, client, monkeypatch):
    """Tests the new cache_ttl integration."""
    mock_cache = MagicMock()
    mock_cache.get.return_value = None
    monkeypatch.setattr("probo.router.router.global_cache", mock_cache)

    @router.page("/cached", cache_ttl=60)
    def cached_route():
        return "Expensive Data"

    # Call it (Cache Miss -> Renders -> Sets Cache)
    client.get("/cached")
    mock_cache.set.assert_called_once()

    # Simulate Cache Hit
    mock_cache.get.return_value = "Cached HTML"
    res_hit = client.get("/cached")
    assert res_hit.text == "Cached HTML"


# ==========================================
# TEST 5: Discovery & Sub-Routers
# ==========================================


def test_load_discovered_routes(router):
    def comp1():
        return "1"

    def comp2():
        return "2"

    discovered = {
        "/route1": ProboRoute("/route1", comp1, stream=True),
        "/route2": ProboRoute("/route2", comp2),
    }

    router.load_discovered_routes(**discovered)
    assert "/route1" in router.routes
    assert "/route2" in router.routes


def test_include_router(router):
    # Added trailing slash '/api/' to fix Bottle's DeprecationWarning
    sub_router = ProboRouter("API", prefix="/api/")
    sub_router.tcm.url_name_comp = {"/api/test/": "comp"}

    router.include_router(sub_router)

    assert "/api/test/" in router.tcm.url_name_comp
    assert "/api/test/" in router.payload.diff


# ==========================================
# TEST 6: TCM Error Interception & 404s
# ==========================================


def test_404_handling(client):
    """Test that non-existent routes return 404 cleanly."""
    res = client.get("/non-existent", status=404)

    assert res.status_code == 404
    assert "404 - Page Not Found" in res.text
    # Now it safely reads the real request.path!
    assert "The path (/non-existent) does not exist" in res.text


def test_tcm_fallback():
    """Test that the router correctly falls back to TCM if a route isn't found."""
    router = ProboRouter(app_name="TCMApp", secret_key="secret")

    # Safely seed the TCM dictionary instead of mocking
    router.tcm.url_name_comp["/tcm-page"] = "TCM Content"

    # Mock get_component safely on the CLASS, not the instance, to avoid __slots__ conflict
    def mock_get_comp(self, path):
        return "TCM Content" if path == "/tcm-page" else None

    # Apply to class definition temporarily for this test scope
    original_method = TemplateComponentMap.get_component
    TemplateComponentMap.get_component = mock_get_comp

    try:
        tcm_client = TestApp(router.wsgi_app)
        res = tcm_client.get("/tcm-page")

        assert res.status_code == 200
        assert "TCM Content" in res.text
    finally:
        # Restore original class method
        TemplateComponentMap.get_component = original_method


def test_tcm_catch_all_404(router, client, monkeypatch):
    """Tests that a 404 is intercepted and handled dynamically by TCM."""

    # Safely patch the method on the class to bypass __slots__ restrictions
    def mock_get_comp(self, path):
        return "Dynamic Content" if path == "/auto-route" else None

    monkeypatch.setattr(TemplateComponentMap, "get_component", mock_get_comp)

    res = client.get("/auto-route")

    assert "Dynamic Content" in res.text
    assert res.status_code == 200
    assert "/auto-route" in router.routes  # Confirms dynamic registration

