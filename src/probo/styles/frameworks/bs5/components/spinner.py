from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Spinner
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union


class BS5Spinner(BS5Component):
    """A manager for Bootstrap 5 Spinner components.

    Spinners are used to indicate the loading state of a component or page.
    This class supports both the 'border' and 'grow' visual variations,
    along with accessibility features like 'role="status"' and hidden
    descriptive text for screen readers.

    Attributes:
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Additional HTML attributes for the spinner.
        variant (str): The visual style ('border' or 'grow').
        content (Optional[str]): Hidden text for accessibility (e.g., 'Loading...').
        spinner_classes (List[str]): Resolved CSS classes for the spinner element.
        tag (str): The HTML tag for the spinner (defaults to 'div').
    """

    def __init__(
        self,
        content: Optional[str] = "Loading...",
        variant: str = "border",
        render_constraints: Optional[Dict[str, Any]] = None,
        **attrs: Any,
    ) -> None:
        """Initializes the spinner with structural and accessibility logic.

        Args:
            content (str, optional): The accessibility text for screen readers.
            variant (str): The spinner type ('border' or 'grow').
            render_constraints (dict, optional): State validation properties.
            **attrs (Any): Additional attributes like color or size utilities.
        """
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.attrs: Dict[str, Any] = attrs
        self.variant: str = variant
        self.content: Optional[str] = content
        self.tag: str = "div"

        spinner_type: str = (
            "spinner-grow" if self.variant == "grow" else "spinner-border"
        )
        self.spinner_classes: List[str] = [spinner_type]

        super().__init__(name="BS5-Spinner", state_props=self.render_constraints)

    def sm(self) -> Self:
        """Downgrades the spinner to the small size variation.

        Returns:
            Self: Enables fluent method chaining.
        """
        size_class: str = f"{self.spinner_classes[0]}-sm"
        self.spinner_classes.append(size_class)
        return self

    def set_color(self, color_variant: str) -> Self:
        """Applies a Bootstrap 5 text color utility to the spinner.

        Args:
            color_variant (str): The color theme (e.g., 'primary', 'success').

        Returns:
            Self: Enables fluent method chaining.
        """
        self.spinner_classes.append(f"text-{color_variant}")
        return self

    def _render_comp(self, *args: Any, **kwargs: Any) -> BS5Element:
        """Assembles the final spinner SSDOM element.

        Returns:
            BS5Element: The rendered spinner root element.
        """
        spinner: BS5Element = BS5Element(
            self.tag, classes=self.spinner_classes, role="status"
        )

        spinner.attr_manager.set_bulk_attr(**self.attrs)

        if self.content:
            spinner_content: BS5Element = BS5Element(
                "span", self.content, classes=["visually-hidden"]
            )
            spinner.include(spinner_content)

        return spinner
