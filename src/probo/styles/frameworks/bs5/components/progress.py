from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import ProgressBar
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union


class BS5ProgressBar(BS5Component):
    """A manager for Bootstrap 5 Progress Bar components.

    Progress bars are used to show the status of a process to the user. This
    class supports single-bar layouts as well as stacked progress bars (multiple
    bars within one container). It manages utility classes for stripes,
    animations, and accessibility attributes (aria-valuenow, etc.) automatically.

    Attributes:
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Attributes for the outer progress container.
        is_striped (bool): If True, applies a striped gradient to the bar.
        is_animated (bool): If True, animates the stripes from right to left.
        tag (str): The HTML tag for the container (defaults to 'div').
        progress_bars (List[BS5Element]): Collection of individual bar elements.
        progressbar_classes (List[str]): Resolved CSS classes for the outer wrapper.
    """

    def __init__(
        self,
        render_constraints: Optional[Dict[str, Any]] = None,
        is_striped: bool = False,
        is_animated: bool = False,
        **attrs: Any,
    ) -> None:
        """Initializes the progress container with theme and animation logic.

        Args:
            render_constraints (dict, optional): State validation properties.
            is_striped (bool): Enable striped background.
            is_animated (bool): Enable CSS3 animations on stripes.
            **attrs (Any): Additional attributes for the progress container.
        """
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.attrs: Dict[str, Any] = attrs
        self.is_striped: bool = is_striped
        self.is_animated: bool = is_animated
        self.tag: str = "div"
        self.progress_bars: List[BS5Element] = []

        self.progressbar_classes: List[str] = ["progress"]

        super().__init__(name="BS5-ProgressBar", state_props=self.render_constraints)

    def add_progress_bar(
        self,
        width: Union[int, float],
        optional_content: Optional[Any] = None,
        **attr: Any,
    ) -> Self:
        """Constructs and appends an individual bar to the progress container.

        This method facilitates 'Stacked' progress bars by allowing multiple
        calls. Each call adds a segment with its own width and content.

        Args:
            width (int | float): The percentage of the bar (0 to 100).
            optional_content (Any, optional): Text or HTML to display inside the bar.
            **attr (Any): Additional attributes for this specific bar segment.

        Returns:
            Self: Enables fluent method chaining.
        """
        progress_bar: BS5Element = BS5Element(self.tag, classes=["progress-bar"])

        if self.is_striped:
            progress_bar.classes.append("progress-bar-striped")
        if self.is_animated:
            progress_bar.classes.append("progress-bar-animated")

        if optional_content:
            progress_bar.include(optional_content)

        progress_bar.attr_manager.set_bulk_attr(
            role="progressbar",
            aria_valuenow=str(width),
            aria_valuemin="0",
            aria_valuemax="100",
            style=f"width:{width}%;",
        )

        progress_bar.attrs.update(attr)
        self.progress_bars.append(progress_bar)
        return self

    def before_render(self, **props: Any) -> None:
        """Aggregates all registered progress bars into the component template."""
        self.include_content_parts(*self.progress_bars)

    def _render_comp(self, *args: Any, **kwargs: Any) -> BS5Element:
        """Assembles the final progress container SSDOM element.

        Returns:
            BS5Element: The rendered progress root element.
        """
        progress: BS5Element = BS5Element(
            self.tag, classes=self.progressbar_classes, **self.attrs
        )
        return progress
