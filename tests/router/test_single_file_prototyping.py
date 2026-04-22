import pytest
import sys
import types
import importlib
from pathlib import Path
from unittest.mock import patch, MagicMock

from probo.router.single_file_prototyping import run_file_server, run_project_server

# ==========================================
# SAFE IMPORT MOCK (PREVENTS PYTEST CRASHES)
# ==========================================
# Pytest uses importlib internally. If we blindly mock it, the test runner crashes.
# This side_effect only mocks our target modules and falls back to real imports.

real_import_module = importlib.import_module


def safe_import_mock(name, package=None):
    if name == "main":
        mock_app = MagicMock()
        mock_app.app_name = "MockApp"
        mock_app.asgi_app = "mock_asgi_app"
        mock_app.wsgi_app = "mock_wsgi_app"

        mock_mod = MagicMock()
        mock_mod.app = mock_app
        mock_mod.my_app = mock_app
        return mock_mod
    elif name == "bad_module":
        raise ImportError("Fake missing dependency")
    return real_import_module(name, package)


# ==========================================
# TESTS: run_file_server (Prototyping)
# ==========================================


def test_run_file_server_file_not_found(capsys):
    """Tests early exit when the target prototyping file doesn't exist."""
    run_file_server("non_existent_file.py")
    captured = capsys.readouterr()
    assert "[X] File not found" in captured.out


@patch("probo.router.single_file_prototyping.ProboRouter")
@patch("probo.router.single_file_prototyping.Path")
def test_run_file_server_success(mock_path_class, mock_router, capsys):
    """Tests successful instantiation and discovery logic for the prototyping server."""
    # 1. Setup Path mock
    mock_file = MagicMock()
    mock_file.exists.return_value = True
    mock_file.parent = Path("/mock/dir")
    mock_file.stem = "prototype"
    mock_path_class.return_value.resolve.return_value = mock_file

    # 2. Setup Router mock
    mock_router_instance = MagicMock()
    mock_router_instance.app_name = "Prototype"
    mock_router.return_value = mock_router_instance

    # 3. Execute
    run_file_server("prototype.py", host="0.0.0.0", port=9000)

    # 4. Assertions
    # Instead of mocking settings, we let the real dataclass instantiate
    # and verify it was passed to the router correctly!
    mock_router.assert_called_once()
    called_settings = mock_router.call_args.kwargs.get("settings")

    assert called_settings is not None
    assert called_settings.HOST == "0.0.0.0"
    assert called_settings.PORT == 9000
    assert called_settings.SECRET_KEY == "PROBO::DEV|||||SECRET"
    assert called_settings.DEBUG is True
    assert called_settings.AUTO_RELOAD is True

    assert mock_router_instance.include_discoveries.call_count == 2
    mock_router_instance.run.assert_called_once()
    assert str(mock_file.parent) in sys.path


# ==========================================
# TESTS: run_project_server (Production)
# ==========================================


def test_run_project_server_invalid_target_wsgi(capsys):
    """Tests target formatting safeguards for WSGI (Gunicorn)."""
    run_project_server(target="invalid_format", is_uv=False)
    captured = capsys.readouterr()
    assert "Target must be in 'module:app' format" in captured.out


def test_run_project_server_invalid_target_asgi(capsys):
    """Tests target formatting safeguards for ASGI (Uvicorn)."""
    run_project_server(target="invalid:format:app", is_uv=True)
    captured = capsys.readouterr()
    assert "Target must be in 'module::app' format" in captured.out


@patch("importlib.import_module", side_effect=safe_import_mock)
def test_run_project_server_import_failure(mock_import, capsys):
    """Tests graceful failure if the user's module fails to import."""
    run_project_server(target="bad_module:app")
    captured = capsys.readouterr()
    assert "[X] Failed to load application 'bad_module:app'" in captured.out


@patch("importlib.import_module", side_effect=safe_import_mock)
@patch("sys.exit")
def test_run_project_server_missing_gunicorn(mock_exit, mock_import, capsys):
    """Tests safeguard when user tries to run WSGI but lacks gunicorn."""
    mock_exit.side_effect = SystemExit(1)

    with patch.dict(
        "sys.modules",
        {"gunicorn": None, "gunicorn.app": None, "gunicorn.app.base": None},
    ):
        with pytest.raises(SystemExit):
            run_project_server(target="main:app", is_uv=False)

    mock_exit.assert_called_once_with(1)
    captured = capsys.readouterr()
    assert "[X] Gunicorn is not installed" in captured.out


@patch("importlib.import_module", side_effect=safe_import_mock)
@patch("sys.exit")
def test_run_project_server_missing_uvicorn(mock_exit, mock_import, capsys):
    """Tests safeguard when user tries to run ASGI but lacks uvicorn."""
    mock_exit.side_effect = SystemExit(1)

    with patch.dict("sys.modules", {"uvicorn": None}):
        with pytest.raises(SystemExit):
            run_project_server(target="main::app", is_uv=True)

    mock_exit.assert_called_once_with(1)
    captured = capsys.readouterr()
    assert "[X] Uvicorn is not installed" in captured.out


@patch("importlib.import_module", side_effect=safe_import_mock)
def test_run_project_server_uvicorn_success(mock_import, capsys):
    """Tests successful Uvicorn initialization and execution."""
    mock_uvicorn = MagicMock()

    with patch.dict("sys.modules", {"uvicorn": mock_uvicorn}):
        run_project_server(
            target="main::my_app",
            host="127.0.0.1",
            port=5000,
            reload=True,
            is_uv=True,
            workers=2,
        )

    # Uvicorn should have been called with our mock's asgi_app property
    mock_uvicorn.run.assert_called_once_with(
        "mock_asgi_app", host="127.0.0.1", port=5000, workers=2
    )


@patch("importlib.import_module", side_effect=safe_import_mock)
def test_run_project_server_gunicorn_success(mock_import, capsys):
    """
    Tests successful Gunicorn initialization by safely mocking the
    inherited BaseApplication class within the scope.
    """
    mock_gunicorn = types.ModuleType("gunicorn")
    mock_gunicorn.__path__ = []
    mock_gunicorn_app = types.ModuleType("gunicorn.app")
    mock_gunicorn_app.__path__ = []
    mock_gunicorn_app_base = types.ModuleType("gunicorn.app.base")

    # Safe mock for BaseApplication to prevent server loops during tests
    class SafeMockBaseApplication:
        def __init__(self, *args, **kwargs):
            pass

        def run(self):
            pass

    mock_gunicorn_app_base.BaseApplication = SafeMockBaseApplication
    mock_gunicorn_app.base = mock_gunicorn_app_base
    mock_gunicorn.app = mock_gunicorn_app

    with patch.dict(
        "sys.modules",
        {
            "gunicorn": mock_gunicorn,
            "gunicorn.app": mock_gunicorn_app,
            "gunicorn.app.base": mock_gunicorn_app_base,
        },
    ):
        run_project_server(
            target="main:my_app",
            host="0.0.0.0",
            port=8080,
            reload=False,
            is_uv=False,
            workers=4,
        )

    captured = capsys.readouterr()
    assert "Starting Gunicorn (WSGI) on 0.0.0.0:8080" in captured.out
