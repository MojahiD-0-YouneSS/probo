from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.utilities import Tooltip
from probo.styles.frameworks.bs5.bs5 import BS5Element

from typing import Any, Dict, List, Optional, Union


class BS5Tooltips(BS5Component):
    """A manager for Bootstrap 5 Tooltip components.

    This component creates the trigger element (typically a button or anchor)
    that displays a tooltip on hover or focus. It manages the injection of
    required data-attributes (`data-bs-toggle`, `data-bs-placement`) and
    accessibility properties into the SSDOM.

    Attributes:
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Additional HTML attributes for the trigger element.
        tag (str): The HTML tag for the trigger element (defaults to 'button').
        content (Any): The visible text or HTML content inside the trigger.
        title (str): The text content to be displayed within the tooltip overlay.
        placement (str): Directional placement ('top', 'bottom', 'left', 'right').
        tooltips_classes (List[str]): Resolved CSS classes for the trigger element.
    """

    def __init__(
        self,
        content: Any,
        title: str,
        placement: str = "top",
        tag: str = "button",
        render_constraints: Optional[Dict[str, Any]] = None,
        **attrs: Any,
    ) -> None:
        """Initializes the tooltip trigger with content and placement logic.

        Args:
            content (Any): The text or element displayed as the trigger.
            title (str): The message displayed inside the tooltip.
            placement (str): Direction of the tooltip.
            tag (str): The HTML tag used for the trigger.
            render_constraints (dict, optional): State validation properties.
            **attrs (Any): Additional attributes for the trigger element.
        """
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.attrs: Dict[str, Any] = attrs
        self.tag: str = tag
        self.content: Any = content
        self.title: str = title
        self.placement: str = placement
        self.tooltips_classes: List[str] = []
        super().__init__(name="BS5-Tooltips", state_props=self.render_constraints)

    def _render_comp(self) -> BS5Element:
        """Assembles the final trigger SSDOM element with tooltip attributes.

        Returns:
            BS5Element: The rendered trigger (button or link) element.
        """
        tooltip_attrs: Dict[str, str] = {
            "data-bs-toggle": "tooltip",
            "data-bs-placement": self.placement,
            "title": self.title,
        }

        if self.tag == "button":
            tooltip_attrs["type"] = "button"

        root: BS5Element = BS5Element(
            self.tag, self.content, classes=self.tooltips_classes, **tooltip_attrs
        )
        root.attr_manager.set_bulk_attr(**self.attrs)
        return root
