from abc import ABC, abstractmethod
from collections.abc import Iterable

class BaseHTMLElement(ABC):
    """
    Base class for all HTML elements.
    Provides common initialization for content and attributes.
    """
    def __init__(self, *content, **kwargs):
        """
        Initializes the HTML element.
        Args:
            content: The content of the element. Can be a string, or another
                     BaseHTMLElement instance, or a list of BaseHTMLElement instances.
            **kwargs: Arbitrary keyword arguments representing HTML attributes.
                      (e.g., class_='my-class', id='my-id', style='color: red;').
        """
        self.content = content
        self.attributes = kwargs

    def _get_rendered_content(self):
        """
        Recursively renders content if it consists of other BaseHTMLElement instances.
        """
        is_nested_iter = any([not isinstance(x, (str, bytes)) for x in self.content])
        if not is_nested_iter:

            return ''.join([item.render() if hasattr(item, 'render') else str(item) for item in self.content])
        else:
            results = []
            for sub_item in self.content:
                if hasattr(sub_item, 'render'):
                    results.append(sub_item.render())
                elif isinstance(sub_item, Iterable):
                    results.append(''.join([x.render() if hasattr(x, 'render') else x for x in sub_item]))
                else:
                    results.append(str(sub_item))
            return ''.join(results)
        
    @abstractmethod
    def render(self):
        """
        Abstract method to be implemented by subclasses to render their specific HTML.
        """
        raise NotImplementedError("Subclasses must implement the render method.")
