from probo.router.views import ProboRouterView
from probo import div, h1
import pytest

#
class UserProfileView(ProboRouterView):
    """A Class-Based View to test the View rendering engine."""

    def get(self, uid):
        return div(h1(f"User {uid}"), id="profile")


def test_cbv_engine():
    view = UserProfileView()
    # Exercise the internal rendering call that the router usually makes
    res = view.get("99")
    rendered = res
    assert 'id="profile"' in rendered
    assert "User 99" in rendered


# ==========================================
# TEST 1: Standard Execution & Filtering
# ==========================================


def test_standard_layout_filtering():
    """Tests that a standard callable layout correctly receives filtered context."""

    def user_layout(name, age):
        return f"User: {name}, Age: {age}"

    class DashboardView(ProboRouterView):
        layout = user_layout

        def get_context(self):
            # 'status' is an extra variable. Probo should filter it out
            # to prevent Python from throwing an unexpected kwarg TypeError!
            return {"name": "Alice", "age": 28, "status": "active"}

    view = DashboardView()
    assert view() == "User: Alice, Age: 28"


def test_layout_missing_kwargs():
    """Tests that missing required layout arguments throws a clear validation error."""

    def strict_layout(title, content):
        pass

    class BadView(ProboRouterView):
        layout = strict_layout

        def get_context(self):
            return {"title": "Only Title Provided"}

    view = BadView()
    with pytest.raises(
        ValueError, match="missing required layout arguments: \\['content'\\]"
    ):
        view()


def test_no_layout_bypass():
    """If no layout is provided, the raw context should be returned directly."""

    class ApiView(ProboRouterView):
        def get_context(self):
            return {"json_data": 123}

    view = ApiView()
    assert view() == {"json_data": 123}


def test_non_dict_bypass():
    """If get_context returns a string/component instead of a dict, bypass the layout."""

    def never_called_layout(data):
        return "Fail"

    class OverrideView(ProboRouterView):
        layout = never_called_layout

        def get_context(self):
            return "<div>Explicit Override</div>"

    view = OverrideView()
    assert view() == "<div>Explicit Override</div>"


# ==========================================
# TEST 2: Lazy Layouts (Dynamic HTML)
# ==========================================


def test_lazy_layout_html_file(tmp_path, monkeypatch):
    """Tests that string paths to HTML files are automatically compiled."""

    # 1. Create a fake HTML template
    html_file = tmp_path / "dashboard.html"
    html_file.write_text("<h1>Welcome {{ user }}</h1>")

    # 2. Mock TemplateProcessor to prevent dependency errors during isolated testing
    class MockTemplateProcessor:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def render_template(self, content):
            return content.replace("{{ user }}", self.kwargs.get("user", ""))

    monkeypatch.setattr(
        "probo.context.context_logic.TemplateProcessor", MockTemplateProcessor, raising=False
    )

    # 3. Create the View
    class HtmlView(ProboRouterView):
        lazy_layout = str(html_file)

        def get_context(self):
            return {"user": "ProboDev"}

    view = HtmlView()

    # 4. Assert it rendered perfectly using **kwargs
    assert view() == "<h1>Welcome ProboDev</h1>"

    # Verify the layout function was cached to prevent re-reading the hard drive
    assert callable(view.layout)


def test_lazy_layout_missing_html():
    """Ensures a missing HTML file triggers a FileNotFoundError."""

    class MissingView(ProboRouterView):
        lazy_layout = "does_not_exist_xyz.html"

        def get_context(self):
            return {}

    view = MissingView()
    with pytest.raises(FileNotFoundError):
        view()


# ==========================================
# TEST 3: Lazy Layouts (Python Modules)
# ==========================================


def test_lazy_layout_python_module(tmp_path, monkeypatch):
    """Tests dynamically importing a layout function from a string path."""

    # 1. Write a real python file
    py_file = tmp_path / "mock_components.py"
    py_file.write_text(
        """
def external_layout(title):
    return f"External Title: {title}"
"""
    )

    # Add to sys.path so importlib can find it
    import sys

    sys.path.insert(0, str(tmp_path))

    # 2. Create the View referencing the python function string
    class ModuleView(ProboRouterView):
        lazy_layout = "mock_components.external_layout"

        def get_context(self):
            return {"title": "Imported"}

    view = ModuleView()
    assert view() == "External Title: Imported"


def test_lazy_layout_bad_import():
    """Tests graceful failure if the user provides a bad import string."""

    class BadModuleView(ProboRouterView):
        lazy_layout = "missing_module.some_function"

    view = BadModuleView()
    with pytest.raises(ImportError):
        view()
