from .base_error import ProboError

class ProboComponentError(ProboError):
    """Base exception for component-related errors."""
    pass

class ComponentRenderError(ProboComponentError):
    """Raised when a component fails to render its HTML."""
    pass

class ComponentValidationError(ProboComponentError):
    """Raised when invalid arguments or configuration are passed to a component."""
    pass
class AttributeNotSupported(ProboError):
    """Raised when an attribute is not supported by the component."""
    pass
class RequiredAttributeMissing(ProboError):
    """Raised when a required attribute is missing from the component."""
    pass
class TargetNotFound(ProboError):
    """Raised when the target element is not found in the component."""
    pass
class InvalidPowerNodeState(ProboError):
    """Raised when the state of the power node is invalid."""
    pass
class TargetFetchMismatch(ProboError):
    """Raised when the target fetch does not match the expected result."""
    pass
