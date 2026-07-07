from .base_error import ProboError

class ProboFormError(ProboError):
    """Base exception for form-related errors."""
    pass

class FormHandlingError(ProboFormError):
    """Raised when there is an issue handling or processing a form submission."""
    pass

class CSRFTokenMissingError(ProboFormError):
    """Raised when a CSRF token is required but missing from the form."""
    pass
