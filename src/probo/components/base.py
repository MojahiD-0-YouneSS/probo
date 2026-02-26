from abc import ABC, abstractmethod
from collections.abc import Iterable
from collections import deque
from typing import Dict, Union, Self,Any
class ElementAttributeManipulator:
    """
    ElementAttributeManipulator handles the core logic for attribute and class manipulation.
    Args: 
        attr_dict: the attributes the element recieves.
        kwargs: extra attributes the element recieves.
    Note: 
        **kwargs often passed as copy of the variable itself that's why we passed them as dict literal.
    """
    __slots__ = ('attrs',)
    def __init__(self, attr_dict:dict=None,**kwargs:dict[str,Any]):
        # 1. Initialize storage per instance (Fixes Shared Memory Bug)
        self.attrs: Dict[str, str] = dict() if attr_dict is None else attr_dict
        self.attrs.update(kwargs)

    def add_class(self, cls_str: str,*classes:tuple[str]) -> Self:
        """            
        Adds one or more classes to attr_dict's "Class" key and if not found then it woud be created.

        Args:
            cls_str (str): A class name string  to add.
            classes (tuple[str]): a tuple of classes for better developer experience.
        
        Returns:
            Self: The current instance for method chaining.
        """
        # Split existing classes into a set to avoid duplicates
        current_classes = set(self.attrs.get("Class", "").split())
        new_classes = cls_str.split()
        new_classes.extend(list(classes))
        # Add new ones
        current_classes.update(set(new_classes))
        
        # Save back as sorted string (cleaner HTML)
        self.attrs["Class"] = " ".join(sorted(current_classes))
        return self

    def remove_class(self, cls_str: str) -> Self:
        """
        Removes class name from the element.

        Args:
            cls_str (str): A class name string to remove.

        Returns:
            Self: The current instance for method chaining.
        """
        current_classes = self.attrs.get("Class", "").split()
        
        # Remove all instances of the class
        if cls_str in current_classes:
            # List comprehension to remove all occurrences safely
            current_classes = [c for c in current_classes if c != cls_str]
            self.attrs["Class"] = " ".join(current_classes)
            
        return self

    def contains_class(self, cls_str: str) -> bool:
        """ Checks if the element has the specified class.

        Args:
            cls_str (str): The class name to search for.

        Returns:
            bool: True if the class exists in the element, False otherwise.
        """
        current_classes = self.attrs.get("Class", "").split()
        return cls_str in current_classes

    def toggle_class(self, class_name: str, condition: bool = None) -> Self:
        """
        Toggles a class on or off.

        Args:
            class_name (str): The name of the class to toggle.
            condition (bool, optional): If True, adds the class. If False, removes it. 
                If None, flips the current state of the class.

        Returns:
            Self: The current instance for method chaining.
        """
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
        """
        Sets a single attribute on the element.

        Args:
            key (str): The attribute name.
            value (Union[str, bool]): The value to assign. Booleans are handled 
                as HTML boolean attributes.

        Returns:
            Self: The current instance for method chaining.
        """
        if isinstance(value, bool):
            if value is False:
                self.remove_attr(key)
            else:
                self.attrs[key] = str(key) # Boolean attribute (e.g. disabled="")
        else:
            self.attrs[self._normalize_attr_key(key)] = str(value)
        return self
    
    def set_bulk_attr(self, **attrs:dict[str,Any]) -> Self:
        """
        Sets multiple attributes at once using keyword arguments.

        Args:
            **attrs: Arbitrary keyword arguments representing attribute key-value pairs.

        Returns:
            Self: The current instance for method chaining.
        """
        for key, value in attrs.items():
            self.set_attr(key,value)
        return self

    def get_attr(self, key: str, default=None) -> str:
        """
        Retrieves an attribute's value.

        Args:
            key (str): The attribute name to look up.
            default (any, optional): The value to return if the attribute is missing.

        Returns:
            str: The attribute value or the provided default.
        """
            
        return self.attrs.get(self._normalize_attr_key(key), default)

    def remove_attr(self, key: str) -> Self:
        """
        Removes an attribute from the element.

        Args:
            key (str): The attribute name to delete.

        Returns:
            Self: The current instance for method chaining.
        """

        if key in self.attrs:
            del self.attrs[self._normalize_attr_key(key)]
        return self

    def set_data(self, key: str, value: str) -> Self:
        """
        Helper method to set 'data-*' attributes.

        Args:
            key (str): The key suffix (e.g., 'id' results in 'data-id').
            value (str): The value to assign.

        Returns:
            Self: The current instance for method chaining.
        """
        clean_key = key.replace("_", "-")
        return self.set_attr(f"data-{clean_key}", value)
    
    def set_id(self, unique_id: str) -> Self:
        """
        Shorthand method to set the 'id' attribute.

        Args:
            unique_id (str): The unique identifier for the element.

        Returns:
            Self: The current instance for method chaining.
        """
        return self.set_attr("Id", unique_id)

    def merge_attrs(self, **kwargs:dict[str,str]) -> Self:
        """
        Merges a new set of attributes with existing ones.

        Args:
            **kwargs: Attributes to merge into the current set.

        Returns:
            Self: The current instance for method chaining.
        """
        for key, value in kwargs.items():
            if key == "Class":
                self.add_class(value)
            else:
                clean_key = key.replace("_", "-")
                self.set_attr(clean_key, value)
        return self
    
    def _normalize_attr_key(self,key:str):
        """
        Internal utility to convert Pythonic keys to valid HTML/SVG attributes.
        For example: 'stroke_width' -> 'stroke-width' and 'Class' -> 'class'.

        Args:
            key (str): The key string to normalize.

        Returns:
            str: The normalized, hyphenated, or lowercased attribute key.
        """

        reserved_attrs = {'id':'Id','class':'Class',}
        return reserved_attrs.get(key.lower(),key)
    
    def set_style(self, property: str, value: str) -> Self:
        """
        Sets a specific CSS property on the element's style attribute.

        Args:
            property (str): The CSS property name (e.g., 'background-color').
            value (str): The CSS property value.

        Returns:
            Self: The current instance for method chaining.
        """
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
        """
        Internal utility to convert a raw CSS string into a dictionary of properties.

        Args:
            style_str (str): A standard CSS string (e.g., "color: red; opacity: 1;").

        Returns:
            Dict[str, str]: A dictionary mapping CSS properties to values.
        """
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
    """Manages attribute storage and delegation for Component elements.

    This class serves as a staging area for HTML attributes. It allows for 
    the incremental building and updating of attributes (including smart 
    CSS class merging) before committing them to specific child elements 
    within the component's registry.

    Attributes:
        children (dict): Storage for resolved attributes indexed by child name.
        attrs (dict): Temporary buffer for attributes being processed 
            during an `update` call.
    """
    __slots__ = ('attrs','root','children')

    def __init__(self,**children:dict[str,Any]) -> None:
        self.children = children
        self.root={}
        self.attrs = {}

    def add_child(self,name:str,**attrs:dict[str,Any]) -> Self:
        """Registers a new child element or overwrites an existing one.

        Args:
            name: The unique identifier for the child element.
            **attrs: Initial attributes for the child.

        Returns:
            self: The instance of ComponentAttrManager (for chaining).
        """
        self.children[name]=attrs
        return self

    def update(self,name:str, **kwargs:dict[str,Any]) -> Self:
        """Bulk updates attributes for a specific child with intelligent merging.

        Normalizes keys (e.g., converting 'data_id' to 'data-id') and handles 
        CSS classes by merging them rather than overwriting. After processing, 
        the attributes are committed to the specified child and the 
        temporary buffer is cleared.

        Args:
            name: The name of the child element to update.
            **kwargs: Attribute key-value pairs to apply.

        Returns:
            The instance of ComponentAttrManager (for chaining).

        Examples:
            >>> manager = ComponentAttrManager()
            >>> manager.add_child("button", class_="btn")
            >>> # Update with a string class and a new attribute
            >>> manager.update("button", class_="btn-primary", id="submit-main")
            >>> manager.to_dict()["button"]
            {'class': 'btn btn-primary', 'id': 'submit-main'}
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
        if self.children.get(name,None):
            self.children[name].update(self.attrs)
        else:
            self.children[name]=self.attrs
        self.clear()
        return self

    def clear(self) -> Self:
        """Wipes the temporary attribute buffer.

        Returns:
            The instance of ComponentAttrManager (for chaining).
        """
        self.attrs.clear()
        return self

    def to_dict(self) -> Dict[str, Any]:
        """Returns the dictionary containing all registered children and their attributes.

        Returns:
            A dictionary where keys are child names and values are 
            dictionaries of HTML attributes.
        """
        return self.children

class BaseHTMLElement(ABC):
    """The abstract base class for all ProboUI HTML elements.

    Provides a unified initialization for element content and attributes. 
    It facilitates a fluent, chainable interface for managing HTML/SVG 
    attributes, CSS classes, and inline styles by delegating to 
    `ElementAttributeManipulator`.

    Attributes:
        content (tuple): The positional arguments representing inner HTML/text.
        attributes (dict): The keyword arguments representing HTML attributes.
    """
    __slots__ = ('attributes', 'content','node_children', 'parent','_ElementNodeMixin__void_node')

    def __init__(self, *content:tuple[str], **kwargs:dict[str,Any]):
        """
        Initializes the HTML element.
        Args:
            content: The content of the element. Can be a string, or another
                     BaseHTMLElement instance, or a list of BaseHTMLElement instances.
            **kwargs: Arbitrary keyword arguments representing HTML attributes.
                      (e.g., class_='my-class', id='my-id', style='color: red;').
        """
        self.content = deque(content)
        self.attributes = kwargs
    
    @property
    def attr_manager(self) -> ElementAttributeManipulator:
        """Accesses the attribute manipulator for this element.

        Returns:
            An instance of ElementAttributeManipulator initialized with 
            the element's current attributes, allowing for chainable updates.
        """
        return ElementAttributeManipulator(self.attributes)

    def _get_rendered_content(self) -> str:
        """Recursively renders all nested content into a single HTML string.

        This internal helper iterates through `self.content`, checking for 
        objects with a `.render()` method (like other components) or nested 
        iterables (like lists of elements), converting everything to its 
        final string representation.

        Returns:
            A string containing the concatenated HTML of all child items.
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
            results = [
                sub_item.render()
                if hasattr(sub_item, "render") else
                    
                    "".join(
                        [
                            x.render() if hasattr(x, "render") else x
                            for x in sub_item
                        ]
                    )
                
                if isinstance(sub_item, Iterable) else
                    str(sub_item)
                for sub_item in self.content
                ]
            return "".join(results)

    @abstractmethod
    def render(self) -> str:
        """Abstract method to generate the final HTML string for the element.

        This must be implemented by concrete subclasses (e.g., `Div`, `Span`).

        Returns:
            The complete HTML representation of the element.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("Subclasses must implement the render method.")


