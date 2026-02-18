# from django.core.management import call_command
# from django.utils.text import slugify
from pathlib import Path


def create_hacksoft_structure(app_dir: Path):
    """Services (Write) + Selectors (Read)."""
    for folder in ["services", "selectors"]:
        d = app_dir / folder
        d.mkdir(parents=True, exist_ok=True)
        (d / "__init__.py").touch()
        (d / f"{folder}.py").touch()

def create_probo_dj_structure(app_dir: Path, app_name: str):
    """The Full Enterprise Stack."""
    # 1. Deep Layer Separation
    structure = {
        "services": ["__init__.py", f"{app_name}_service.py", "systems/"],
        "selectors": ["__init__.py", "selectors.py"],
        # Split Views & Forms into Admin/Client
        "forms": ["__init__.py", "admin_forms/", "client_forms/"],
        "views": ["__init__.py", "admin_views/", "client_views/"],
        "urls": ["__init__.py", "admin_urls.py", "client_urls.py"],
        "exceptions": ["__init__.py", "service_exception.py"],
    }

    for folder, files in structure.items():
        folder_path = app_dir / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        for f in files:
            if f.endswith("/"):
                (folder_path / f).mkdir(parents=True, exist_ok=True)
            else:
                (folder_path / f).touch()

    # 2. Root Utilities
    for f in ["signals.py", "dependencies.py", "tasks.py"]:
        (app_dir / f).touch()
