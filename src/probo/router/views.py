import inspect
import os
import importlib
from typing import Callable, Any, Dict, Optional


class RouterViewMixin:
    """
    Mixin to resolve and load layouts dynamically (lazy loading).
    Operates directly on the View instance attributes.
    """

    def resolve_layout_callable(self) -> Optional[Callable]:
        # Access via class first to prevent Python from accidentally binding
        # external functions as instance methods.
        layout = getattr(self.__class__, "layout", None) or getattr(
            self, "layout", None
        )

        if layout and callable(layout):
            return layout

        lazy_layout = getattr(self, "lazy_layout", None)
        if not lazy_layout:
            return None

        # 1. Handle HTML file path mapping
        if str(lazy_layout).endswith(".html") or str(lazy_layout).endswith(".htm"):
            from probo.context.context_logic import TemplateProcessor

            def html_layout_wrapper(**context_kwargs):
                if not os.path.exists(lazy_layout):
                    raise FileNotFoundError(
                        f"Lazy layout HTML file not found: {lazy_layout}"
                    )
                with open(str(lazy_layout), "r", encoding="utf-8") as f:
                    content = f.read()
                return TemplateProcessor(**context_kwargs).render_template(content)

            # Cache it so we only read the file once!
            self.layout = html_layout_wrapper
            return self.layout

        # 2. Handle Python module path (e.g., "components.layouts.main_layout")
        try:
            module_name, func_name = lazy_layout.rsplit(".", 1)
            mod = importlib.import_module(module_name)
            func = getattr(mod, func_name)

            if not callable(func):
                raise ValueError(
                    f"Resolved lazy_layout '{lazy_layout}' is not callable."
                )

            self.layout = func
            return self.layout

        except Exception as e:
            raise ImportError(f"Failed to resolve lazy_layout '{lazy_layout}': {e}")


class ProboRouterView(RouterViewMixin):
    """
    Native Class-Based View for Probo.
    Provides layout-awareness and context validation.
    """

    layout: Optional[Callable] = None
    lazy_layout: Optional[str] = None

    def get_context(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Override this to return the context dictionary.
        This data will be validated against the layout signature.
        """
        return {}

    def __call__(self, *args, **kwargs) -> Any:
        """
        Execution entry point. Bridges logic to UI.
        """
        layout_func = self.resolve_layout_callable()

        if not layout_func:
            # If no layout, assume the view returns raw SSDOM nodes directly
            return self.get_context(*args, **kwargs)

        # 1. Fetch logic data
        context = self.get_context(*args, **kwargs)

        if not isinstance(context, dict):
            # Bypass layout wrap if user explicitly returned an HTTP Response, string, or UI component
            return context

        # 2. Signature Inspection (The Validation Layer)
        sig = inspect.signature(layout_func)

        # Fast-path: If the layout accepts **kwargs (like our HTML wrapper), bypass strict filtering
        has_varkw = any(
            p.kind == inspect.Parameter.VAR_KEYWORD for p in sig.parameters.values()
        )
        if has_varkw:
            return layout_func(**context)

        params = sig.parameters

        # Check for missing required arguments
        missing = [
            name
            for name, p in params.items()
            if name not in context and p.default == inspect.Parameter.empty
        ]

        if missing:
            raise ValueError(
                f"View '{self.__class__.__name__}' context missing required layout arguments: {missing}"
            )

        # 3. Filter context to match layout signature (preventing 'unexpected kwarg' errors)
        valid_context = {k: v for k, v in context.items() if k in params}

        # 4. Render through the layout
        return layout_func(**valid_context)
