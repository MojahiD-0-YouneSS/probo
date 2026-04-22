import os,sys
import importlib.util
import logging
from typing import Dict, Callable, Any

logger = logging.getLogger("probo.discovery")


class ProboRoute:
    """
    The utility object that bundles a path, a component, and routing flags (like stream=True).
    This allows developers to map components without importing the router!
    """

    __slots__ = ("path", "component", "kwargs")

    def __init__(self, path: str, component: Callable, **kwargs):
        self.path = path
        self.component = component
        self.kwargs = kwargs


def route(path: str, component: Callable, **kwargs) -> ProboRoute:
    """
    The 'Take This' utility!
    Maps a URL path to a Probo component cleanly.
    """
    return ProboRoute(path, component, **kwargs)


def _get_py_files(target_path: str) -> list:
    abs_path = os.path.abspath(target_path)
    if not os.path.exists(abs_path):
        return []

    # 1. If the user passed a single file (like 'dashboard.py')
    if os.path.isfile(abs_path) and abs_path.endswith(".py"):
        return [abs_path]

    # 2. If the user passed a folder (like 'pages/')
    py_files = []
    for root, _, files in os.walk(abs_path):
        for f in files:
            if f.endswith(".py") and not f.startswith("__"):
                py_files.append(os.path.join(root, f))
    return py_files


def discover_pages(
    *directories: str, target: str | None = None,include_in_path:bool=False,
) -> Dict[str, Any]:
    """
    Next.js + Django style Auto-Discovery.
    Scans directories OR single files for 'routes' or 'url_patterns'.
    """
    master_routes: Dict[str, Any] = {}

    for directory in directories:
        py_files = _get_py_files(directory)

        if not py_files:
            logger.warning(f"Path '{directory}' not found or empty. Skipping.")
            continue

        for py_file_path in py_files:
            py_file = os.path.basename(py_file_path)
            stem = os.path.splitext(py_file)[0]
            module_name = f"probo_auto_{stem}"

            try:
                # Dynamically import the file
                spec = importlib.util.spec_from_file_location(module_name, py_file_path)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    sys.modules[module_name] = mod

                    prb_callable = None
                    exported_routes = []

                    # Look for Django-style prefix
                    prefix = getattr(mod, "app_name", "")
                    if prefix and not prefix.startswith("/"):
                        prefix = "/" + prefix
                    if prefix and not prefix.endswith("/"):
                        prefix = prefix+"/"

                    # 1. Check for the Parse Magic Variable
                    if not target:
                        prb_file = getattr(mod, "__prb_file__", getattr(mod, "__prb_html__", None))

                        if prb_file:
                            prb_file_str = str(prb_file)
                            if not prefix:
                                prefix = prb_file_str if "." not in prb_file_str else prb_file_str.split('.')[0]
                            # FIX: Isolate the template logic
                            from probo.context.context_logic import TemplateProcessor

                            def resolve_template_context():
                                ctx = getattr(mod, "__prb_context_dict__", {})
                                if not isinstance(ctx, dict): ctx = {}
                                context_func = getattr(mod, "__prb_context__", None)
                                if callable(context_func):
                                    dynamic_ctx = context_func()
                                    if isinstance(dynamic_ctx, dict):
                                        ctx = {**ctx, **dynamic_ctx}
                                return ctx

                            def generated_component():
                                processor = TemplateProcessor(**resolve_template_context())
                                with open(prb_file_str, "r") as f:
                                    return processor.render_template(f.read())

                            prb_callable = generated_component

                    # 2. Grab standard routes if no template magic is found
                    if include_in_path and target:

                        prefix =(f"/{str(target)}/") 
                    if not prb_callable:
                        if target:
                            # If target is provided (e.g., target="xyz"), grab that exact list!
                            exported_routes = getattr(mod, target, [])
                        if not exported_routes:
                            # Default fallback

                            exported_routes = getattr(mod, "routes", getattr(mod, "url_patterns", []))

                        if not exported_routes:
                            continue

                    # 3. Map Magic Template Callable (FIX: Moved outside the for-loop!)
                    if prb_callable:
                        r_path = f"/{stem}/" if stem != "home" else "/"
                        full_path = (
                            f"{prefix}{r_path}".replace("//", "/")
                            if include_in_path
                            else f"{r_path}".replace("//", "/")
                        )
                        master_routes[full_path if full_path else "/"] = prb_callable
                        logger.info(f"Discovered Magic Template Route in {py_file}")
                        continue

                    # 4. Map Explicit Routes List
                    for r in exported_routes:
                        if isinstance(r, ProboRoute):
                            r_path = r.path
                            if not r_path.startswith("/") and not (prefix and r_path == ""):
                                r_path = "/" + r_path
                            if not r_path.endswith("/") and not (prefix and r_path == ""):
                                r_path = r_path+"/"

                            full_path = (
                                f"{prefix}{r_path}".replace("//", "/")
                                if include_in_path
                                else f"{r_path}".replace("//", "/")
                            )
                            master_routes[full_path if full_path else "/"] = r

                    logger.info(f"Discovered {len(exported_routes)} routes in {py_file}")

            except Exception as e:
                logger.error(f"Failed to load {py_file_path}: {e}")

    return master_routes

def discover_routers(*directories: str) -> list:
    """
    Scans directories OR single files for fully instantiated ProboRouter objects.
    """
    # Inline import to prevent circular dependencies
    from probo.router.router import ProboRouter

    found_routers = []

    for directory in directories:
        py_files = _get_py_files(directory)

        for py_file_path in py_files:
            py_file = os.path.basename(py_file_path)
            stem = os.path.splitext(py_file)[0]
            module_name = f"probo_auto_router_{stem}"

            try:
                spec = importlib.util.spec_from_file_location(module_name, py_file_path)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    sys.modules[module_name] = mod

                    for name, obj in vars(mod).items():
                        if isinstance(obj, ProboRouter):
                            found_routers.append(obj)
                            logger.info(
                                f"Discovered Sub-Router '{obj.app_name}' in {py_file}"
                            )
            except Exception as e:
                logger.error(f"Failed to load Sub-Router from {py_file_path}: {e}")

    return found_routers
