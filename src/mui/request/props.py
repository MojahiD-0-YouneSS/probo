from dataclasses import dataclass, field
#from django.middleware.csrf import get_token # Import this to get the token string
from typing import Any
@dataclass
class RequestProps:
    # Global: Available to ALL components (User bar, Sidebar, Footer, etc.)
    global_context: dict[str,Any] = field(default_factory=dict)
    
    # Local: Available ONLY to the specific component handling the action (e.g., LoginForm)
    local_context: dict[str,Any] = field(default_factory=dict)
    
    def get_all(self,) -> dict[str,Any]:
        return {**self.global_context,**self.local_context}