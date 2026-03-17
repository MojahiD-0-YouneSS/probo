from typing import Any, Dict, Optional
from probo.styles import element_style
from probo.styles.css_enum import CssPropertyEnum, CssFunctionsEnum

class StyleManager:
    """
    A lightweight, slot-based proxy for element styling.

    Optimized for v1.4.0 to handle bi-directional synchronization
    between Python object attributes and the underlying SSDOM attribute dict.
    """

    # __slots__ keeps memory usage flat on low-spec hardware (Celeron N4020)
    __slots__ = ["_owner_attrs", "_styles", "_override_style"]

    def __init__(self, owner_attrs: Dict[str, Any],_override_style: bool = False):
        # Use super().__setattr__ to bypass our custom logic during initialization
        super().__setattr__("_owner_attrs", owner_attrs)
        super().__setattr__("_styles", {})
        super().__setattr__("_override_style", _override_style)

        # Load existing styles from the owner's 'style' attribute if present
        self._read_style_attr()

    def __setattr__(self, name: str, value: Any):
        """
        Intercepts attribute setting to route CSS properties to the buffer.
        Converts Pythonic underscores to CSS hyphens.
        """
        # 1. Route internal members to standard storage
        if name in self.__slots__:
            super().__setattr__(name, value)
            return

        # 2. Convert background_color -> background-color
        css_prop = CssPropertyEnum.get(name) or CssFunctionsEnum.get(name)

        # 3. Store in the CSS buffer
        if css_prop:
            self._styles[css_prop.value.split(':')[0]] = str(value)
            self.render

    def __getattr__(self, name: str) -> Optional[str]:
        """Allows access to styles via dot notation."""
        css_prop = name.lower().replace("_", "-")
        self._read_style_attr()  # Ensure we have the latest from the owner
        return self._styles.get(css_prop)

    def _read_style_attr(self):
        """
        Parses the existing 'style' string from the owner attributes
        into the managed dictionary.
        """
        style_string = self._owner_attrs.get("style")
        if not style_string or not isinstance(style_string, str):
            return

        # Defensive parsing: handles trailing semicolons and extra whitespace
        pairs = [p.strip() for p in style_string.split(";") if ":" in p]
        for prop in pairs:
            try:
                k, v = prop.split(":", 1)
                self._styles[k.strip().lower()] = v.strip()
            except ValueError:
                continue

    def add(self, name: str, value: str):
        """Adds a style property to the buffer."""
        css_prop = name.lower().replace("_", "-")
        self._read_style_attr()
        self._styles[css_prop] = str(value)
        self.render
        return self  # Allow chaining
    def remove(self, name: str):
        """Removes a style property from the buffer."""
        self._read_style_attr()
        css_prop = name.lower().replace("_", "-")
        if css_prop in self._styles:
            del self._styles[css_prop]
            self.render
        return self  # Allow chaining

    @property
    def render(self) -> str:
        """
        Serializes the styles and synchronizes the owner's attribute dictionary.
        """
        if not self._styles:
            # If styles were cleared, ensure the owner attr is updated
            if "style" in self._owner_attrs:
                self._owner_attrs["style"] = ""
            return ""

        # Logic: We use the existing element_style engine for consistency
        # Note: element_style is expected to return a formatted string
        inline_style = element_style(**self._styles)

        # Bi-directional sync: Update the owner element's attribute dict
        self._owner_attrs["style"] = inline_style
        return inline_style
