from pathlib import Path
import sys
from probo.router.router import ProboRouter
from probo.router.settings import RouterSettings
import importlib


def run_file_server(
    file: str,
    host: str = "localhost",
    port: int = 8000,
    reload:bool=True,
) -> None:
    """
    Rapid Prototyping Server.
    Loads a single file, spins up an isolated Router, discovers its routes,
    and runs it with automatic Live Reloading.
    """
    file_path = Path(file).resolve()
    if not file_path.exists():
        print(f"❌ [X] File not found: {file_path}")
        return

    # Add file's parent to sys.path so its local imports work smoothly
    sys.path.insert(0, str(file_path.parent))

    # Configure Isolated Dev Settings
    SECRET_KEY = "PROBO::DEV|||||SECRET"
    settings = RouterSettings(
        HOST=host,
        PORT=port,
        SECRET_KEY=SECRET_KEY,
        DEBUG=True,  # Enables native Live Reload pinging and error traces
        AUTO_RELOAD=True if reload else False,  # Restarts server on file save
    )

    # Instantiate the prototyping Router
    router = ProboRouter(app_name=file_path.stem.capitalize(), settings=settings)
    # MAGIC: Let the router discover itself!
    # We pass the exact file path to map both standard pages and sub-routers
    router.include_discoveries(str(file_path), for_router=True)
    router.include_discoveries(str(file_path), for_router=False)

    print(f"✅ [V] Running Single-File Prototype: {router.app_name}")
    if sys.argv and not sys.argv[0].endswith('.py') and "-m" not in sys.argv:
        import probo.terminal.cli
        sys.argv[0] = probo.terminal.cli.__file__
    router.run()


def run_project_server(
    target: str = "main:app",
    host: str = "localhost",
    port: int = 8000,
    reload: bool = False,
    is_uv: bool = False,
    workers: int = 1,
):
    """
    Production/Project Server.
    Loads an entire Probo project (like main:app) and runs it with
    either Gunicorn (WSGI) or Uvicorn (ASGI) based on the target flag.
    """
    try:
        if not is_uv:
            module_name, app_var = target.split(":")
        else:
            module_name, app_var = target.split("::")
    except ValueError:
        format_hint = "'module::app'" if is_uv else "'module:app'"
        print(
            f"❌ [X] Error: Target must be in {format_hint} format (e.g., 'main{'::' if is_uv else ':'}app')"
        )
        return

    # Add the current working directory so imports like 'from pages import ...' work globally
    sys.path.insert(0, str(Path.cwd()))

    try:
        # Dynamically import the user's Python module and extract the ProboRouter instance
        mod = importlib.import_module(module_name)
        app = getattr(mod, app_var)
    except Exception as e:
        print(f"❌ [X] Failed to load application '{target}': {e}")
        return

    # Enforce development settings if reload is True (overriding any hardcoded production limits in the file)
    if reload:
        app.settings.DEBUG = True
        app.settings.AUTO_RELOAD = True

    app.settings.HOST = host
    app.settings.PORT = port
    print(f"✅ [V] Running Project: {app.app_name} on http://{host}:{port}")

    if not is_uv:
        # ==========================================
        # GUNICORN WSGI ENGINE (Default)
        # ==========================================
        try:
            from gunicorn.app.base import BaseApplication
        except ImportError as e:
            print("❌ [X] Gunicorn is not installed. Please run: pip install gunicorn",e)
            sys.exit(1)

        # We must wrap Gunicorn's BaseApplication to run it dynamically inside our Python script
        class StandaloneApplication(BaseApplication):
            def __init__(self, application_instance, options=None):
                self.options = options or {}
                self.application = application_instance
                super().__init__()

            def load_config(self):
                config = {
                    key: value
                    for key, value in self.options.items()
                    if key in self.cfg.settings and value is not None
                }
                for key, value in config.items():
                    self.cfg.set(key.lower(), value)

            def load(self):
                # Pass the raw Bottle WSGI application to Gunicorn
                return self.application.wsgi_app

        print(f"🚀 Starting Gunicorn (WSGI) on {host}:{port} with {workers} workers...")
        options = {"bind": f"{host}:{port}", "workers": workers}
        StandaloneApplication(app, options).run()

    else:
        # ==========================================
        # UVICORN ASGI ENGINE
        # ==========================================
        try:
            import uvicorn
        except ImportError:
            print(
                "❌ [X] Uvicorn is not installed. Please run: pip install uvicorn asgiref"
            )
            sys.exit(1)

        print(f"🚀 Starting Uvicorn (ASGI) on {host}:{port} with {workers} workers...")
        # Pass the asgi_app bridge property to Uvicorn
        uvicorn.run(app.asgi_app, host=host, port=port, workers=workers)
