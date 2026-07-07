from .base_error import ProboError

class ProboTemplateError(ProboError):
    """Base exception for template-related errors."""
    pass

class TemplateResolutionError(ProboTemplateError):
    """Raised when a template file or node cannot be found or resolved."""
    pass
