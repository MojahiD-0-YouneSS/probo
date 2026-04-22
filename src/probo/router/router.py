import os
import inspect
import importlib.util
from functools import wraps
from typing import Callable, Dict, Any, Union, Iterable
import dataclasses

from bottle import Bottle, request, response, run, static_file
from asgiref.wsgi import WsgiToAsgi
from typing import Self

from probo.components.elements import Template
from probo.context import TemplateComponentMap
from probo.router.payload import RouterPayload
from probo.router.global_cache import global_cache
from probo.router.settings import RouterSettings
from probo.router.responses import gzip_response


class ProboRouter:
    """The Routing Engine for ProboUI.

    This class manages URL mapping to Probo Page objects and handles
    dynamic scaffolding discovery. It integrates with TemplateComponentMapper (TCM)
    to resolve component-based routes and uses the Probo Template object
    to ensure full HTML document delivery.
    """

    __slots__ = (
        "__app",
        "secret_key",
        "respond_type",
        "app_name",
        "pages_dir",
        "routes",
        "tcm",
        "document_template",
        "payload",
        "settings",
        "error_pages",
        "prefix",
    )

    def __init__(
        self,
        app_name: str = "ProboApp",
        pages_dir: str = "pages",
        secret_key: str | None = None,
        prefix: str | None = None,
        respond_format: str = "txt",
        base_template: Template | None = None,
        settings: RouterSettings | None = None,
    ):
        """Initializes the ProboRouter."""
        self.settings = settings or RouterSettings()
        self.__app = Bottle()
        # Load Settings into Bottle Config safely using dataclasses.asdict
        self.__app.config.update(dataclasses.asdict(self.settings))

        # Prioritize explicitly passed secret_key, fallback to Settings
        self.secret_key = secret_key or self.settings.SECRET_KEY

        self.respond_type = respond_format
        self.app_name = app_name
        self.pages_dir = pages_dir
        self.routes: Dict[str, Any] = {}
        self.tcm: TemplateComponentMap = TemplateComponentMap()
        self.error_pages = {}
        self.document_template = base_template or Template()

        self.payload = (
            RouterPayload(**self.tcm.url_name_comp)
            if self.tcm.url_name_comp
            else RouterPayload()
        )
        self.prefix = "/" + prefix.strip("/") + "/" if prefix else ""

        self._setup_static_routes()
        self._setup_tcm_handler()

    def is_htmx(self) -> bool:
        """Checks if the current request was triggered by HTMX."""
        return request.headers.get("HX-Request") == "true"

    def __call__(
        self, environ: Dict[str, Any], start_response: Callable
    ) -> Iterable[bytes]:
        """
        WSGI Entry Point for Gunicorn.
        Delegates the request to the internal Bottle app but ensures
        the output is refined into the WSGI-compliant byte-stream format.
        """
        result = self._maybe_compress(self.__app(environ, start_response))
        return self._normalize_wsgi_output(result)

    def set_error_page(self, code: int, component_func):
        """Allows developers to set a beautiful Probo UI for ANY HTTP error code."""
        self.error_pages[code] = component_func

        if code != 404:

            @self.__app.error(code)
            def generic_error_handler(error):
                response.status = code
                return self._wrap_in_template(component_func(request.path, error))

    def _normalize_wsgi_output(self, result: Any) -> Iterable[bytes]:
        """Hyper-optimized WSGI normalizer."""
        for chunk in result:
            if isinstance(chunk, bytes):
                yield chunk
                continue

            if hasattr(chunk, "render"):
                chunk = chunk.render()

            if isinstance(chunk, dict):
                chunk = self.document_template.swap_component(**chunk).render()

            if isinstance(chunk, str):
                yield chunk.encode("utf-8")
            else:
                yield chunk

    def _maybe_compress(self, body: Any) -> Union[Any, bytes]:
        if not self.settings.ENABLE_GZIP or "gzip" not in request.headers.get(
            "Accept-Encoding", ""
        ):
            return body

        if isinstance(body, str):
            return gzip_response(body, response)
        return body

    def _setup_tcm_handler(self) -> None:
        """
        Injects a hook into Bottle to check the TemplateComponentMap before
        failing with a 404. This avoids manual route registration overhead.
        """

        @self.__app.error(404)
        def catch_all_tcm(error) -> str:
            if self.tcm:
                path = request.path
                try:
                    component_data = self.tcm.get_component(path)
                except Exception:
                    component_data = None

                if component_data:
                    self.routes[path] = lambda: component_data
                    response.status = 200
                    if isinstance(component_data, tuple):
                        component_data = component_data[0]
                    return self._wrap_in_template(component_data)

            response.status = 404

            # If the developer set a custom 404 UI, render it!
            if 404 in self.error_pages:
                return self._wrap_in_template(
                    self.error_pages[404](request.path, error)
                )

            # Otherwise, return a clean, generic Probo default
            from probo.components.tag_functions.block_tags import div, h1, p

            default_404 = div(
                h1("404 - Page Not Found", style="color: #ef4444;"),
                p(f"The path ({str(request.path)}) does not exist."),
                style="text-align: center; margin-top: 50vh; transform: translateY(-50%); font-family: sans-serif;",
            )
            return self._wrap_in_template(default_404)

    def _setup_static_routes(self) -> None:
        """Standard routes for Probo-generated assets, integrated with Settings."""
        # Use settings to define where static assets live
        static_url = f"{self.settings.STATIC_URL.rstrip('/')}/<filename:path>"

        @self.__app.get(static_url)
        def send_static(filename):
            return static_file(filename, root=f"./{self.settings.STATIC_FOLDER}")

    def _wrap_in_template(self, content: Any) -> str:
        """Optimized HTML wrapper. Avoids scanning massive strings."""
        rendered_content = content.render() if hasattr(content, "render") else content

        if not isinstance(rendered_content, dict):
            content_str = str(rendered_content)

            if "<html" in content_str[:100].lower():
                return content_str
            rendered_content = {"section": content_str}

        return self.document_template.swap_component(**rendered_content).render()

    def mount(self, prefix: str, sub_app):
        wsgi_target = getattr(sub_app, "wsgi_app", sub_app)
        self.__app.mount(prefix, wsgi_target)

    def install(self, plugin):
        self.__app.install(plugin)

    def uninstall(self, plugin):
        self.__app.uninstall(plugin)

    def hook(self, name: str):
        def decorator(func):
            self.__app.add_hook(name, func)
            return func

        return decorator

    def serve_static(self, url_path: str | None = None, directory: str | None = None):
        """Serves static files, gracefully defaulting to the RouterSettings."""
        safe_dir = directory or self.settings.STATIC_FOLDER
        safe_url = url_path or f"{self.settings.STATIC_URL.rstrip('/')}/<filepath:path>"

        os.makedirs(safe_dir, exist_ok=True)

        @self.__app.get(safe_url)
        def _serve_static_files(filepath):
            return static_file(filepath, root=safe_dir)

    def error_page(self, code: int):
        def decorator(func):
            @self.__app.error(code)
            def wrapper(error_obj):
                result = func(error_obj)
                if hasattr(result, "render"):
                    return result.render()
                if isinstance(result, list):
                    return "".join(str(n) for n in result)
                return str(result)

            return decorator

    def page(
        self, path: str, stream: bool = False, batch_size: int = 50, cache_ttl: int = 0
    ) -> Any:
        """
        Hyper-Optimized Decorator.
        Now supports Page-Level Caching via `cache_ttl` (in seconds).
        """

        def decorator(func):
            self.routes[path] = func
            sig = inspect.signature(func)
            pass_response = "response" in sig.parameters
            pass_request = "request" in sig.parameters

            @self.__app.get(path)
            @wraps(func)
            def wrapper(*args, **kwargs):
                if pass_response:
                    kwargs["response"] = response
                if pass_request:
                    kwargs["request"] = request

                cache_key = f"route:{path}"
                if cache_ttl > 0:
                    cached_html = global_cache.get(cache_key)
                    if cached_html:
                        response.content_type = "text/html; charset=UTF-8"
                        return cached_html

                result = func(*args, **kwargs)

                if stream and hasattr(result, "stream") and cache_ttl == 0:
                    response.content_type = "text/html; charset=UTF-8"
                    return result.stream(batch_size=batch_size)

                is_htmx = self.is_htmx()
                if is_htmx:
                    html_output = (
                        result.render() if hasattr(result, "render") else str(result)
                    )
                else:
                    html_output = self._wrap_in_template(result)

                if self.respond_type != "txt":
                    # BUGFIX: We dynamically unpack the string `path` as the dictionary key
                    # so payload tracking correctly recognizes the URL route ID.
                    self.payload.load(**{path: html_output})
                    html_output = self.payload.get_response(self.respond_type)

                if cache_ttl > 0:
                    global_cache.set(cache_key, html_output, ttl=cache_ttl)

                return html_output

            return wrapper

        return decorator

    def load_discovered_routes(self, **routes) -> Self:
        """BUGFIX: Corrected spelling to `load_discovered_routes`."""
        for path, route_obj in routes.items():
            self.page(path, **route_obj.kwargs)(route_obj.component)
        return self

    def load_tcm(
        self, url: str = ".", renamed_obj_to: str = None, renamed_file_to: str = None
    ) -> None | TemplateComponentMap:
        """Automatically loads the tcm object from url."""
        if not os.path.exists(url):
            return

        file_name = renamed_file_to or "probo_tcm.py"
        obj_name = renamed_obj_to or "tcm"

        for root, dirs, files in os.walk(url):
            for file in files:
                if file.endswith(".py") and not file.startswith("_"):
                    if file == str(file_name):
                        module_name = file.replace(".py", "")
                        spec = importlib.util.spec_from_file_location(
                            module_name, os.path.join(root, file)
                        )
                        if spec and spec.loader:
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)
                            if hasattr(module, "tcm"):
                                obj = getattr(module, obj_name)
                                if not isinstance(obj, TemplateComponentMap):
                                    obj = TemplateComponentMap()
                                self.tcm = obj
                                return obj

    def register_tcm(self, tcm: TemplateComponentMap) -> None:
        if not isinstance(tcm, TemplateComponentMap):
            return
        self.tcm = tcm

    def include_router(self, router: "ProboRouter") -> Self:
        """Mounts or merges a Sub-Router into this main application."""
        if router.prefix:
            # Mounts as an isolated app under the prefix (e.g. /auth)
            self.__app.mount(router.prefix, router.wsgi_app)
        else:
            # Merges routes directly into the root level
            self.__app.merge(router.wsgi_app)

        # Merge the TCMs so payload diffing works across sub-routers
        if router.tcm and router.tcm.url_name_comp:
            self.tcm.url_name_comp.update(router.tcm.url_name_comp)
            from probo.router.payload import RouterPayload

            self.payload = RouterPayload(**self.tcm.url_name_comp)

        return self

    def include_discoveries(self, *directories: str, for_router: bool = True) -> Self:
        """Scans folders for exported ProboRouters and automatically mounts them."""
        from probo.router.discovery import discover_routers, discover_pages

        if for_router:
            routers = discover_routers(*directories)
            for r in routers:
                self.include_router(r)
        else:
            if directories:
                routes = discover_pages(*directories)
            else:
                routes = discover_pages(self.pages_dir or "pages")
            self.load_discovered_routes(**routes)

        return self

    @property
    def wsgi_app(self) -> Bottle:
        return self.__app

    @property
    def asgi_app(self) -> WsgiToAsgi:
        return WsgiToAsgi(self.__app)

    def run(self) -> None:
        """Launch the Probo Development Server."""
        self.settings.freeze()

        if os.environ.get("BOTTLE_CHILD") != "true":
            print(
                f"🚀 {self.app_name} starting on http://{self.settings.HOST}:{self.settings.PORT} "
            )
            if self.settings.DEBUG:
                print(
                    "🐛 Debug mode is ON. Detailed error messages and auto-reloading enabled."
                )

        run(
            self.__app,
            host=self.settings.HOST,
            port=self.settings.PORT,
            debug=self.settings.DEBUG,
            reloader=self.settings.AUTO_RELOAD,
        )
