from .base_error import ProboError

class ProboStyleError(ProboError):
    """Base exception for style-related errors."""
    pass

class StyleCompilationError(ProboStyleError):
    """Raised when an error occurs during style generation or compilation."""
    pass
