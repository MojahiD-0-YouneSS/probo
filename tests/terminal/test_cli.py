import pytest
import os
from typer.testing import CliRunner
from probo.terminal.cli import (
    app,
)  # Assuming you named the Enum DjangoStructure or DjangoStructure probo

runner = CliRunner()

# ==============================================================================
#  TEST: probo init (Pure Static Project)
# ==============================================================================


def test_cli_init_pure_project(tmp_path):
    """
    Scenario: User runs 'probo init my_site'.
    Expected: A folder with main.py, dist/, and assets/.
    """
    os.chdir(tmp_path)

    result = runner.invoke(app, ["init", "my_portfolio"])

    # 1. Check Exit Code
    print(result.stdout)

    assert result.exit_code == 0
    assert "Pure PROBO Project" in result.stdout

    # 2. Verify Structure
    project = tmp_path / "my_portfolio"
    assert project.exists()
    assert (project / "main.py").exists()
    assert (project / "probo_tcm.py").exists()
    assert (project / "dist").exists()
    assert (project / "assets").exists()
    assert (project / "components" / "pages.py").exists()


def test_cli_init_duplicate_fails(tmp_path):
    """Scenario: Running init twice should fail gracefully."""
    os.chdir(tmp_path)
    (tmp_path / "dup_site").mkdir()  # Create conflict

    result = runner.invoke(app, ["init", "dup_site"])
    print(result.stdout)

    assert result.exit_code != 0
    assert "Error" in result.stdout


# ==============================================================================
#  TEST: probo dj-app (Django Architectures)
# ==============================================================================


@pytest.fixture
def mock_django_subprocess(monkeypatch):
    """
    Mocks subprocess.run so we don't actually need Django installed
    or to run 'dj-app' (which requires a Django project context).
    """
    import subprocess

    def mock_run(cmd, check=True):
        # We just assume Django succeeded
        return True

    monkeypatch.setattr(subprocess, "run", mock_run)


def test_generate_app_base_structure(tmp_path, mock_django_subprocess):
    """
    Scenario: probo dj-app blog --structure=base
    Expected: Standard Django + components/ folder.
    """
    os.chdir(tmp_path)

    result = runner.invoke(app, ["dj-app", "blog", "--structure=base"])

    assert result.exit_code == 0
    app_dir = tmp_path / "blog"

    # Base PROBO files
    assert (app_dir / "components" / "__init__.py").exists()
    assert (app_dir / "probo_tcm.py").exists()

    # Ensure Advanced folders are NOT created
    assert not (app_dir / "services").exists()
    assert not (app_dir / "forms" / "admin_forms").exists()


def test_generate_app_hacksoft_structure(tmp_path, mock_django_subprocess):
    """
    Scenario: probo dj-app shop --structure=hacksoft
    Expected: Services + Selectors layers.
    """
    os.chdir(tmp_path)

    result = runner.invoke(app, ["dj-app", "shop", "--structure=hacksoft"])

    print(result)

    assert result.exit_code == 0
    app_dir = tmp_path / "shop"

    # Check DDD Layers
    assert (app_dir / "services" / "__init__.py").exists()
    assert (app_dir / "selectors" / "__init__.py").exists()

    # Check standard files
    assert (app_dir / "probo_tcm.py").exists()


def test_generate_app_probo_dj_enterprise(tmp_path, mock_django_subprocess):
    """
    Scenario: probo dj-app core --structure=probo-dj
    Expected: The Full Enterprise Stack (Split Views, Forms, Utils).
    """
    os.chdir(tmp_path)

    result = runner.invoke(app, ["dj-app", "core", "--structure=probo-dj"])

    print(result.stdout)

    assert result.exit_code == 0
    app_dir = tmp_path / "core"

    # 1. Check Deep Splits
    assert (app_dir / "views" / "admin_views").exists()
    assert (app_dir / "views" / "client_views").exists()
    assert (app_dir / "forms" / "admin_forms").exists()
    assert (app_dir / "forms" / "client_forms").exists()

    # 2. Check Service Layer
    assert (app_dir / "services" / "core_service.py").exists()
    assert (app_dir / "services" / "systems").is_dir()

    # 3. Check Root Utils
    assert (app_dir / "signals.py").exists()
    assert (app_dir / "dependencies.py").exists()


# ==============================================================================
#  TEST: Build Commands (Mocked)
# ==============================================================================


def test_build_css_command(tmp_path):
    """
    Test build:css executes correctly.
    We manually create a dummy registry to ensure the command finds what it needs.
    """
    os.chdir(tmp_path)

    # 1. SETUP: Create a valid probo_tcm.py file
    # This ensures the command doesn't fail with "Registry not found"
    registry_code = """
from probo.context import TemplateComponentMap
tcm = TemplateComponentMap()
"""
    (tmp_path / "probo_tcm.py").write_text(registry_code, encoding="utf-8")

    # 2. EXECUTE: Run the build command
    # We output to a custom path to verify path handling
    result = runner.invoke(app, ["build:css", "--output=static/css/test.css"])

    # Debug output if it fails
    if result.exit_code != 0:
        print("STDOUT:", result.stdout)

    # 3. ASSERTIONS
    assert result.exit_code == 0
    assert "Scanning" in result.stdout
    assert "CSS Exported" in result.stdout

    # Verify the file was actually created
    output_file = tmp_path / "static" / "css" / "test.css"
    assert output_file.exists()
