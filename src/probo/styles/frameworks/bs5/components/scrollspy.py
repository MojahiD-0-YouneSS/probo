from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Scrollspy
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Scrollspy(BS5Component):
    """A manager for Bootstrap 5 Scrollspy components.

    Scrollspy automatically updates Bootstrap navigation or list group 
    components based on scroll position to indicate which link is currently 
    active in the viewport. This class manages the scrollable container 
    and the mapping of content IDs to the navigation target.

    Attributes:
        target (str): The CSS selector of the navigation or list group 
            to spy on (e.g., '#navbar-example').
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Additional HTML attributes for the container.
        tag (str): The HTML tag for the container (defaults to 'div').
        scrollpy_items (List[BS5Element]): Collection of content sections.
        scrollpy_classes (List[str]): Resolved CSS classes for the component.
    """

    def __init__(
        self, 
        target: str, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the scrollspy container with target tracking.

        Args:
            target (str): The ID or selector of the nav/list-group component.
            render_constraints (dict, optional): State validation properties.
            **attrs (Any): Attributes for the scrollable element.
        """
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.attrs: Dict[str, Any] = attrs
        self.target: str = target
        self.tag: str = 'div'
        self.scrollpy_items: List[BS5Element] = []
        
        self.scrollpy_classes: List[str] = ['scrollspy-example']
        
        super().__init__(name='BS5-Scrollspy', state_props=self.render_constraints)

    def add_scrollpy_item(
        self, 
        item_id: str, 
        content: Any, 
        tag: str = 'div', 
        **attrs: Any
    ) -> Self:
        """Constructs and appends a content section targeted by the scrollspy.

        Args:
            item_id (str): The unique ID that matches a link in the target nav.
            content (Any): The HTML or text content for the section.
            tag (str): The HTML tag for the section (defaults to 'div').
            **attrs (Any): Additional attributes for the section.

        Returns:
            Self: Enables fluent method chaining.
        """
        scroll: BS5Element = BS5Element(
            tag,
            content,
            Id=item_id,
            **attrs
        )
        self.scrollpy_items.append(scroll)
        return self

    def before_render(self, **props: Any) -> None:
        """Aggregates all registered content sections before rendering."""
        self.include_content_parts(*self.scrollpy_items)

    def _render_comp(self, *args: Any, **kwargs: Any) -> BS5Element:
        """Assembles the final scrollable SSDOM element.

        Returns:
            BS5Element: The rendered scrollspy container.
        """
        scroll: BS5Element = BS5Element(
            self.tag,
            data_bs_spy="scroll",
            data_bs_target=self.target,
            data_bs_offset="0",
            tabindex="0",
        )
        
        scroll.attr_manager.set_bulk_attr(**self.attrs)
        return scroll