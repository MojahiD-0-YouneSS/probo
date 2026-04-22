import os
import sys
from types import ModuleType
import pytest
import logging
from probo.router.discovery import (
    ProboRoute,
    route,
    _get_py_files,
    discover_pages,
    discover_routers,
)

# ==========================================
# FIXTURES & MOCKS
# ==========================================


@pytest.fixture(autouse=True)
def mock_template_processor(monkeypatch):
    """
    Mocks the TemplateProcessor module to avoid missing imports
    during isolated testing when probo.context isn't loaded.
    """
    mock_module = type(sys)("probo.context.context_logic")

    class MockTemplateProcessor:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def render_template(self, content):
            return f"RENDERED:{content.strip()}:WITH:{self.kwargs}"

    mock_module.TemplateProcessor = MockTemplateProcessor
    sys.modules["probo.context.context_logic"] = mock_module


@pytest.fixture(autouse=True)
def mock_probo_router(monkeypatch):
    """Mocks the ProboRouter to test Sub-Router discovery."""
    mock_module = type(sys)("probo.router.router")

    class MockProboRouter:
        def __init__(self, app_name):
            self.app_name = app_name

    mock_module.ProboRouter = MockProboRouter
    sys.modules["probo.router.router"] = mock_module


# ==========================================
# TEST 1: Route Helpers
# ==========================================


def test_route_and_probo_route():
    def dummy_func():
        pass

    # Test object wrapper
    r = route("/test", dummy_func, stream=True)
    assert isinstance(r, ProboRoute)
    assert r.path == "/test"
    assert r.component == dummy_func
    assert r.kwargs == {"stream": True}


# ==========================================
# TEST 2: File Discovery Logic
# ==========================================


def test_get_py_files_not_found():
    assert _get_py_files("/does/not/exist/fake_path/") == []


def test_get_py_files_single_file(tmp_path):
    # Test passing an exact python file directly
    test_file = tmp_path / "single.py"
    test_file.write_text("print('hello')")

    files = _get_py_files(str(test_file))
    assert len(files) == 1
    assert files[0] == str(test_file)


def test_get_py_files_directory(tmp_path):
    # Test passing a directory with mixed files
    (tmp_path / "valid.py").write_text("x = 1")
    (tmp_path / "invalid.txt").write_text("text")
    (tmp_path / "__init__.py").write_text("ignore me")

    nested = tmp_path / "nested"
    nested.mkdir()
    (nested / "deep.py").write_text("y = 2")

    files = _get_py_files(str(tmp_path))
    assert len(files) == 2
    assert any("valid.py" in f for f in files)
    assert any("deep.py" in f for f in files)
    assert not any("__init__.py" in f for f in files)


# ==========================================
# TEST 3: Discover Pages (Standard Routes)
# ==========================================


def test_discover_pages_empty(tmp_path, caplog):
    """Test discovering an empty directory throws a warning and continues."""
    with caplog.at_level(logging.WARNING):
        routes = discover_pages(str(tmp_path))
        assert not routes
        assert "not found or empty. Skipping." in caplog.text


def test_discover_pages_explicit_routes(tmp_path):
    """Test discovering standard files containing a 'routes' list."""
    dash_file = tmp_path / "dashboard.py"
    dash_file.write_text(
        """
from probo.router.discovery import route
def my_dash(): return "dash"
app_name = "admin"
routes = [route("/main/", my_dash)]
"""
    )

    routes = discover_pages(str(tmp_path),include_in_path=True)

    # Due to prefix "admin" and path "/main"
    assert "/admin/main/" in routes
    assert isinstance(routes["/admin/main/"], ProboRoute)


def test_discover_pages_url_patterns_fallback(tmp_path):
    """Test discovering files using 'url_patterns' instead of 'routes'."""
    app_file = tmp_path / "app.py"
    app_file.write_text(
        """
from probo.router.discovery import route
def my_app(): return "app"
url_patterns = [route("/settings/", my_app)]
"""
    )

    routes = discover_pages(str(tmp_path))
    assert "/settings/" in routes


def test_discover_pages_slash_cleaning(tmp_path):
    """Tests that double slashes are cleaned up securely."""
    app_file = tmp_path / "app.py"
    app_file.write_text(
        """
from probo.router.discovery import route
def c(): pass
app_name = "/auth/"
routes = [route("/login/", c), route("", c)]
"""
    )

    routes = discover_pages(str(tmp_path),include_in_path=True)
    # /auth/ + /login = //auth/login -> /auth/login
    assert "/auth/login/" in routes
    assert "/auth/" in routes


# ==========================================
# TEST 4: Discover Pages (Magic Templates)
# ==========================================


def test_discover_pages_magic_template(tmp_path):
    """Tests the auto-compiler for __prb_file__ HTML files."""

    html_file = tmp_path / "template.html"
    html_file.write_text("<div>Hello {{ name }}</div>")

    # Name it home.py so it maps to "/" automatically
    home_file = tmp_path / "home.py"
    home_file.write_text(
        f"""
__prb_html__ = r"{html_file}"
__prb_context_dict__ = {{"global": 1}}

def __prb_context__():
    return {{"name": "Probo"}}
"""
    )

    routes = discover_pages(str(tmp_path))
    assert "/" in routes

    # Execute the generated component to verify context was resolved!
    callable_comp = routes["/"]
    result = callable_comp()

    assert (
        "RENDERED:<div>Hello {{ name }}</div>:WITH:{'global': 1, 'name': 'Probo'}"
        in result
    )


def test_discover_pages_with_target_argument(tmp_path):
    """Tests that providing a 'target' argument overrides app_name and skips templates."""
    dash_file = tmp_path / "dashboard.py"
    dash_file.write_text(
        """
from probo.router.discovery import route
def c(): pass
app_name = "wrong_prefix"
__prb_file__ = "skip_me.html" # Should be ignored because target is passed
routes = [route("/panel/", c)]
"""
    )

    routes = discover_pages(str(tmp_path), target="custom_prefix",include_in_path=True)
    assert "/custom_prefix/panel/" in routes
    assert "/wrong_prefix/panel/" not in routes


# ==========================================
# TEST 5: Exceptions & Discovery Routers
# ==========================================


def test_discover_pages_syntax_error(tmp_path, caplog):
    """Ensure bad python files log an error but don't crash the server."""
    bad_file = tmp_path / "bad.py"
    bad_file.write_text("def missing_colon()\n  pass")

    with caplog.at_level(logging.ERROR):
        discover_pages(str(tmp_path))
        assert "Failed to load" in caplog.text


def test_discover_routers(tmp_path):
    """Tests auto-discovering entire sub-applications."""
    router_file = tmp_path / "api.py"
    router_file.write_text(
        """
from probo.router.router import ProboRouter
my_sub_app = ProboRouter("AuthAPI")
"""
    )

    routers = discover_routers(str(tmp_path))
    assert len(routers) == 1
    assert routers[0].app_name == "AuthAPI"


def test_discover_routers_error_handling(tmp_path, caplog):
    """Ensure sub-router discovery safely catches import errors."""
    bad_file = tmp_path / "broken_router.py"
    bad_file.write_text("raise ValueError('Crash!')")

    with caplog.at_level(logging.ERROR):
        discover_routers(str(tmp_path))
        assert "Failed to load Sub-Router" in caplog.text
