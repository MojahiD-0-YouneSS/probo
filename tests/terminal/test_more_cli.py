import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from typer.testing import CliRunner

from probo.terminal.cli import app, VERSION

runner = CliRunner()

# ==========================================
# FIXTURES
# ==========================================


@pytest.fixture
def mock_tcm_file(tmp_path):
    """Creates a temporary probo_tcm.py file for registry testing."""
    tcm_file = tmp_path / "probo_tcm.py"
    tcm_file.write_text(
        """
class MockComponent:
    def render(self): return "<div>UI</div>", ".custom { color: red; }"
    
class MockTCM:
    url_name_comp = {"test_comp": MockComponent}

tcm = MockTCM()
    """
    )
    return tcm_file


# ==========================================
# TESTS
# ==========================================


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert VERSION in result.stdout
    assert "Probo UI" in result.stdout


def test_echo():
    result = runner.invoke(app, ["echo", "Hello_World"])
    assert result.exit_code == 0
    assert "Hello_World" in result.stdout


def test_init(tmp_path):
    """Test standard standalone initialization scaffolding."""
    import os

    # Temporarily switch working directory to our isolated tmp_path
    original_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        result = runner.invoke(app, ["init", "my_new_app"])
        assert result.exit_code == 0
        assert "initialized!" in result.stdout

        # Verify scaffolding
        assert (tmp_path / "my_new_app" / "main.py").exists()
        assert (tmp_path / "my_new_app" / "probo_tcm.py").exists()
        assert (tmp_path / "my_new_app" / "components" / "__init__.py").exists()
    finally:
        os.chdir(original_cwd)


def test_init_already_exists(tmp_path):
    """Ensures it prevents overwriting existing directories."""
    import os

    original_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        (tmp_path / "existing_app").mkdir()
        result = runner.invoke(app, ["init", "existing_app"])

        assert result.exit_code == 1
        assert "already exists!" in result.stdout
    finally:
        os.chdir(original_cwd)


@patch("probo.terminal.cli.subprocess.run")
def test_dj_app_base(mock_subprocess, tmp_path):
    import os

    original_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        result = runner.invoke(app, ["dj-app", "my_django_app"])

        assert result.exit_code == 0
        assert "Created App 'my_django_app' (Base Style)" in result.stdout
        # Django subprocess trigger
        mock_subprocess.assert_called_once()

        # Verify Probo scaffolding was injected into the Django app
        assert (tmp_path / "my_django_app" / "components").exists()
        assert (tmp_path / "my_django_app" / "probo_tcm.py").exists()
    finally:
        os.chdir(original_cwd)


def test_build_css(mock_tcm_file, tmp_path):
    out_file = tmp_path / "styles.css"

    result = runner.invoke(
        app,
        ["build:css", "--registry-path", str(mock_tcm_file), "--output", str(out_file)],
    )

    assert result.exit_code == 0
    assert "unique styles" in result.stdout
    assert ".custom { color: red; }" in out_file.read_text()


def test_build_html(mock_tcm_file, tmp_path):
    out_dir = tmp_path / "dist_html"

    result = runner.invoke(
        app,
        [
            "build:html",
            "--registry-path",
            str(mock_tcm_file),
            "--output-dir",
            str(out_dir),
        ],
    )

    assert result.exit_code == 0
    assert "Generated 1 HTML files" in result.stdout

    html_content = (out_dir / "test_comp.html").read_text()
    assert "<div>UI</div>" in html_content
    assert ".custom { color: red; }" in html_content


@patch("probo.terminal.cli.webbrowser.open_new_tab")
def test_preview(mock_browser, mock_tcm_file):
    result = runner.invoke(
        app, ["preview", "test_comp", "--registry-path", str(mock_tcm_file)]
    )

    assert result.exit_code == 0
    assert "Opening preview for test_comp" in result.stdout
    mock_browser.assert_called_once()


@patch("probo.router.single_file_prototyping.run_file_server")
def test_dev_server(mock_run_server):
    result = runner.invoke(app, ["dev", "app.py", "--port", "5000"])

    assert result.exit_code == 0
    assert "Starting dev server" in result.stdout
    mock_run_server.assert_called_once_with(file="app.py", host="127.0.0.1", port=5000,reload=True)


@patch("probo.router.single_file_prototyping.run_project_server")
def test_run_server(mock_run_server):
    # Testing standard run (WSGI)
    result1 = runner.invoke(app, ["run", "main:app", "--reload"])
    assert result1.exit_code == 0
    mock_run_server.assert_called_with(
        target="main:app",
        port=8000,
        host="localhost",
        reload=False,
        is_uv=False,
        workers=1,
    )

    # Testing Uvicorn Run (ASGI based on :: syntax)
    result2 = runner.invoke(app, ["run", "main::app"])
    assert result2.exit_code == 0
    mock_run_server.assert_called_with(
        target="main::app",
        port=8000,
        host="localhost",
        reload=False,
        is_uv=True,
        workers=1,
    )


def test_build_route(tmp_path):
    """Tests the static site generator targeting explicit route objects."""
    route_file = tmp_path / "routes.py"
    route_file.write_text(
        """
class MockRoute:
    def __init__(self, path): self.path = path
    def component(self): return "<h1>Done</h1>"
    
my_routes = [MockRoute("/index"), MockRoute("/about")]
    """
    )

    out_dir = tmp_path / "dist"

    result = runner.invoke(
        app,
        [
            "build:route",
            str(route_file),
            "--out",
            str(out_dir),
            "--route-name",
            "my_routes",
        ],
    )

    assert result.exit_code == 0
    assert "Built: /index -> index.html" in result.stdout
    assert "Built: /about -> about.html" in result.stdout

    assert "<h1>Done</h1>" in (out_dir / "index.html").read_text()
    assert "<h1>Done</h1>" in (out_dir / "about.html").read_text()

