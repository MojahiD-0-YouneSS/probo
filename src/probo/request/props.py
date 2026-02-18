from dataclasses import dataclass, field

# from django.middleware.csrf import get_token # Import this to get the token string
from typing import Any


@dataclass
class RequestProps:
    """Manages data flow and context scoping for ProboUI components.

    This dataclass separates data into two tiers: Global context, which is 
    accessible by every component in the document tree (e.g., user sessions, 
    site settings), and Local context, which is restricted to the specific 
    component handling an immediate action or fragment.

    Attributes:
        global_context (Dict[str, Any]): Data shared across all components 
            rendered in the current request.
        local_context (Dict[str, Any]): Data specific to a single component 
            instance or a targeted HTMX swap.
    """
    # Global: Available to ALL components (User bar, Sidebar, Footer, etc.)
    global_context: dict[str, Any] = field(default_factory=dict)

    # Local: Available ONLY to the specific component handling the action (e.g., LoginForm)
    local_context: dict[str, Any] = field(default_factory=dict)

    def get_all(
        self,
    ) -> dict[str, Any]:
        return {**self.global_context, **self.local_context}
