import pytest
from probo.router.http import (
    RouterRequestdata,
    set_cookie,
    get_cookie,
    hx_redirect,
    get_upload,
    save_upload,
    get_wsgi_environ,
)

# ==========================================
# TEST 1: Request Data Class
# ==========================================


def test_router_request_data(monkeypatch):
    """Tests all the dictionary property accessors in the RouterRequestdata class."""

    # Define a pure Mock Request to completely replace Bottle's proxy object
    class MockRequest:
        params = {"param1": "a"}
        query = {"query1": "b"}
        forms = {"form1": "c"}
        json = {"json1": "d"}
        files = {"file1": "e"}

    # Patch the module namespace directly to bypass Bottle's __setattr__ lock
    monkeypatch.setattr("probo.router.http.request", MockRequest())

    rd = RouterRequestdata()

    assert rd.get_params() == {"param1": "a"}
    assert rd.get_query() == {"query1": "b"}
    assert rd.get_forms() == {"form1": "c"}
    assert rd.get_json() == {"json1": "d"}
    assert rd.get_files() == {"file1": "e"}


# ==========================================
# TEST 2: Environment Accessor
# ==========================================


def test_get_wsgi_environ(monkeypatch):
    """Tests the safe evaluation of the WSGI environment dict."""

    class MockRequest:
        environ = {"HTTP_HOST": "localhost"}

    monkeypatch.setattr("probo.router.http.request", MockRequest())

    env = get_wsgi_environ()
    assert env["HTTP_HOST"] == "localhost"


# ==========================================
# TEST 3: Cookies & Headers
# ==========================================


def test_cookie_helpers(monkeypatch):
    """Tests the cookie setters and getters by mocking the module objects."""

    class MockResponse:
        def __init__(self):
            self.cookies = {}

        def set_cookie(
            self, name, value, secret=None, max_age=None, path=None, **kwargs
        ):
            self.cookies[name] = {
                "value": value,
                "secret": secret,
                "max_age": max_age,
                "path": path,
                **kwargs,
            }

    class MockRequest:
        def get_cookie(self, name, default=None, secret=None):
            if name == "existing_cookie":
                return "real_value"
            return default

    # Instantiate our mocks
    mock_res = MockResponse()
    mock_req = MockRequest()

    # Inject them into the module
    monkeypatch.setattr("probo.router.http.response", mock_res)
    monkeypatch.setattr("probo.router.http.request", mock_req)

    # Test set_cookie writes to our mock response
    set_cookie("session", "abc", secret="my-secret", max_age=500)
    assert mock_res.cookies["session"]["value"] == "abc"
    assert mock_res.cookies["session"]["secret"] == "my-secret"
    assert mock_res.cookies["session"]["max_age"] == 500
    assert mock_res.cookies["session"]["path"] == "/"

    # Test get_cookie reads from our mock request
    assert get_cookie("existing_cookie") == "real_value"
    assert get_cookie("missing_cookie", default="fallback") == "fallback"


def test_hx_redirect(monkeypatch):
    """Tests that HTMX redirects safely modify the response headers."""

    class MockResponse:
        def __init__(self):
            self.headers = {}

        def set_header(self, name, value):
            self.headers[name] = value

    mock_res = MockResponse()
    monkeypatch.setattr("probo.router.http.response", mock_res)

    res = hx_redirect("/dashboard")

    # Must return empty string for HTMX body bypass
    assert res == ""
    assert mock_res.headers["HX-Redirect"] == "/dashboard"


# ==========================================
# TEST 4: File Upload Handling
# ==========================================


def test_file_uploads(monkeypatch):
    """Tests fetching and saving file uploads with a mocked Bottle FileUpload."""

    # Create a fake Bottle FileUpload class
    class MockFileUpload:
        def __init__(self):
            self.saved_path = None
            self.overwrite_flag = None

        def save(self, path, overwrite=False):
            self.saved_path = path
            self.overwrite_flag = overwrite

    # Create an instance to represent our uploaded file
    mock_file = MockFileUpload()

    # Mock request object with nested files dictionary
    class MockRequest:
        class MockFilesDict:
            def get(self, key):
                if key == "avatar":
                    return mock_file
                return None

        files = MockFilesDict()

    monkeypatch.setattr("probo.router.http.request", MockRequest())

    # 1. Test get_upload (Found)
    assert get_upload("avatar") is mock_file

    # 2. Test get_upload (Missing)
    assert get_upload("missing_file") is None

    # 3. Test save_upload (Success)
    success = save_upload("avatar", "/tmp/uploads/avatar.png", overwrite=True)
    assert success is True
    assert mock_file.saved_path == "/tmp/uploads/avatar.png"
    assert mock_file.overwrite_flag is True

    # 4. Test save_upload (Failure - file not found)
    fail = save_upload("missing_file", "/tmp/uploads/missing.png")
    assert fail is False
