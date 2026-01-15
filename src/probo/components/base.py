from abc import ABC, abstractmethod
from collections.abc import Iterable

from typing import Dict, Union, Self

class ElementAttributeManipulator:
    def __init__(self, attr_dict=None,**kwargs):
        # 1. Initialize storage per instance (Fixes Shared Memory Bug)
        self.attrs: Dict[str, str] = dict() if attr_dict is None else attr_dict
        self.attrs.update(kwargs)

    def add_class(self, cls_str: str) -> Self:
        """Smartly adds class(es) without duplicating."""
        # Split existing classes into a set to avoid duplicates
        current_classes = set(self.attrs.get("Class", "").split())
        new_classes = cls_str.split()
        # Add new ones
        current_classes.update(set(new_classes))
        
        # Save back as sorted string (cleaner HTML)
        self.attrs["Class"] = " ".join(sorted(current_classes))
        return self

    def remove_class(self, cls_str: str) -> Self:
        current_classes = self.attrs.get("Class", "").split()
        
        # Remove all instances of the class
        if cls_str in current_classes:
            # List comprehension to remove all occurrences safely
            current_classes = [c for c in current_classes if c != cls_str]
            self.attrs["Class"] = " ".join(current_classes)
            
        return self

    def contains_class(self, cls_str: str) -> bool:
        """Checks for exact class match."""
        current_classes = self.attrs.get("Class", "").split()
        return cls_str in current_classes

    def toggle_class(self, class_name: str, condition: bool = None) -> Self:
        # Force Add
        if condition is True:
            return self.add_class(class_name)
        # Force Remove
        if condition is False:
            return self.remove_class(class_name)
            
        # Standard Toggle
        if self.contains_class(class_name):
            return self.remove_class(class_name)
        return self.add_class(class_name)

    def set_attr(self, key: str, value: Union[str, bool]) -> Self:
        if isinstance(value, bool):
            if value is False:
                self.remove_attr(key)
            else:
                self.attrs[key] = "" # Boolean attribute (e.g. disabled="")
        else:
            self.attrs[self._normalize_attr_key(key)] = str(value)
        return self
    def set_bulk_attr(self, **attrs) -> Self:
        for key, value in attrs.items():
            self.set_attr(key,value)
        return self

    def get_attr(self, key: str, default=None) -> str:
        return self.attrs.get(self._normalize_attr_key(key), default)

    def remove_attr(self, key: str) -> Self:
        """Safely removes an attribute if it exists."""
        if key in self.attrs:
            del self.attrs[self._normalize_attr_key(key)]
        return self

    def set_data(self, key: str, value: str) -> Self:
        clean_key = key.replace("_", "-")
        return self.set_attr(f"data-{clean_key}", value)
    
    def set_id(self, unique_id: str) -> Self:
        return self.set_attr("Id", unique_id)

    def merge_attrs(self, **kwargs) -> Self:
        for key, value in kwargs.items():
            if key == "Class":
                self.add_class(value)
            else:
                clean_key = key.replace("_", "-")
                self.set_attr(clean_key, value)
        return self
    def _normalize_attr_key(self,key):
        reserved_attrs = {'id':'Id','class':'Class',}
        return reserved_attrs.get(key.lower(),key)
    def set_style(self, property: str, value: str) -> Self:
        """Updates inline style intelligently."""
        # 1. Parse existing style
        current_style_str = self.attrs.get("style", "")
        style_dict = self._parse_style_string(current_style_str)
        
        # 2. Update the property
        style_dict[property] = value
        
        # 3. Rebuild string
        new_style_str = "; ".join([f"{k}: {v}" for k, v in style_dict.items()])
        self.attrs["style"] = new_style_str
        return self

    def _parse_style_string(self, style_str: str) -> Dict[str, str]:
        """Helper to convert 'color: red; width: 10px' into a dict."""
        if not style_str:
            return {}
        
        result = {}
        # Split by semicolon, then by colon
        items = style_str.split(";")
        for item in items:
            if ":" in item:
                key, val = item.split(":", 1)
                result[key.strip()] = val.strip()
        return result

class ComponentAttrManager(ElementAttributeManipulator):
    """
    Manages the default attributes for a Component's root element.
    """
    # The actual storage
    def __init__(self,**childern):
        self.childern = childern
        self.root={}
        self.attrs = {}

    def add_child(self,name,**attrs):
        self.childern[name]=attrs
        return self

    def update(self,name, **kwargs):
        """
        Bulk update attributes from kwargs.
        Handles class merging intelligently if 'class' is passed.
        """
        for k, v in kwargs.items():
            clean_key = self._normalize_key(k)

            if clean_key == 'class':
                # If updating class, use add_class logic to merge, or overwrite?
                # Usually update() implies overwrite or merge.
                # Let's support space-separated string merging for safety.
                if isinstance(v, str):
                    self.add_class(*v.split())
                elif isinstance(v, (list, tuple)):
                    self.add_class(*v)
            else:
                self.attrs[clean_key] = v
        if self.childern.get(name,None):
            self.childer[name].update(self.attrs)
        else:
            self.childer[name]=self.attrs
        self.clear()
        return self

    def clear(self):
        """Wipes all attributes."""
        self.attrs.clear()
        return self

    def to_dict(self) -> Dict[str, Any]:
        """Returns the raw dictionary for rendering."""
        return self.childern

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
    
    @property
    def attr_manager(self):
        return ElementAttributeManipulator(self.attributes)

    def _get_rendered_content(self):
        """
        Recursively renders content if it consists of other BaseHTMLElement instances.
        """
        is_nested_iter = any([not isinstance(x, (str, bytes)) for x in self.content])
        if not is_nested_iter:
            return "".join(
                [
                    item.render() if hasattr(item, "render") else str(item)
                    for item in self.content
                ]
            )
        else:
            results = []
            for sub_item in self.content:
                if hasattr(sub_item, "render"):
                    results.append(sub_item.render())
                elif isinstance(sub_item, Iterable):
                    results.append(
                        "".join(
                            [
                                x.render() if hasattr(x, "render") else x
                                for x in sub_item
                            ]
                        )
                    )
                else:
                    results.append(str(sub_item))
            return "".join(results)

    @abstractmethod
    def render(self):
        """
        Abstract method to be implemented by subclasses to render their specific HTML.
        """
        raise NotImplementedError("Subclasses must implement the render method.")
