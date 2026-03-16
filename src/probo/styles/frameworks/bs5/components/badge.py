from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element
from probo.styles.frameworks.bs5.utilities import Background
from typing import Any, Dict, List, Optional, Self, Union

class BS5Badge(BS5Component):
    """A comprehensive manager for Bootstrap 5 Badge components.

    Badges are small count and labeling components typically used to display 
    notifications, counts, or status indicators. This class provides specific 
    factory methods to integrate badges into larger interactive elements like 
    headings or buttons, ensuring the scaling and positioning follow 
    Bootstrap's typography rules.

    Attributes:
        variant (str): The Bootstrap background color utility name.
        content (str): The textual or numerical content of the badge.
        badge_classes (List[str]): Resolved CSS classes for the component.
        tag (str): The HTML tag used for rendering (defaults to 'span').
    """

    def __init__(
        self, 
        content: str, 
        variant: str = "primary", 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the badge with theme logic and state properties.

        Args:
            content (str): The text or number to display.
            variant (str): BS5 theme color (e.g., 'primary', 'success').
            render_constraints (dict, optional): Schema validation for props.
            **attrs (Any): Additional HTML attributes for the badge tag.
        """
        self.variant: str = variant
        self.attrs: Dict[str, Any] = attrs
        self.render_constraints: Dict[str, Any] = render_constraints or {}
        self.content: str = content
        
        self.badge_classes: List[str] = ['badge', f'bg-{self.variant}']
        self.tag: str = 'span'
        
        super().__init__(name='BS5-badge', state_props=self.render_constraints)

    def _add_parent_badge(
        self, 
        content: str, 
        tag: str, 
        **attrs: Any
    ) -> Self:
        """Internal helper to wrap the badge in a parent container.

        This method facilitates patterns like '<h1>Text <span class="badge">New</span></h1>'
        by nesting the badge within the provided tag and overriding the 
        template root.

        Args:
            content (str): The leading text for the parent container.
            tag (str): The HTML tag for the wrapper (e.g., 'h1', 'button').
            **attrs (Any): Attributes to apply to the parent container.

        Returns:
            Self: Enables fluent method chaining.
        """
        comp: BS5Element = BS5Element(tag, content, **attrs)
        comp.include(self.template)
        self.template.include(comp, override=True)
        return self
   
    def add_heading_badge(
        self, 
        heading_content: str, 
        heading: str = 'h1', 
        **attrs: Any
    ) -> Self:
        """Wraps the badge inside a heading element.

        Bootstrap badges scale to match the size of the immediate parent 
        heading by using relative font sizing (em units).

        Args:
            heading_content (str): The main text of the heading.
            heading (str): The heading level (h1 through h6).
            **attrs (Any): Additional attributes for the heading tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        return self._add_parent_badge(heading_content, tag=heading, **attrs)
   
    def add_button_badge(
        self, 
        button_content: str, 
        tag: str = 'button', 
        **attrs: Any
    ) -> Self:
        """Integrates the badge into a button or anchor tag.

        Commonly used for notification counts (e.g., 'Inbox <span class="badge">4</span>').
        If the tag is 'button', it automatically ensures the type is set.

        Args:
            button_content (str): The label for the button.
            tag (str): The clickable tag (usually 'button' or 'a').
            **attrs (Any): Additional attributes like 'type="button"'.

        Returns:
            Self: Enables fluent method chaining.
        """
        if tag == 'button' and 'type' not in attrs:
            attrs['type'] = 'button'
            
        return self._add_parent_badge(button_content, tag=tag, **attrs)
    
    def _render_comp(self) -> BS5Element:
        """Assembles the final badge structure.

        Returns:
            BS5Element: The rendered badge object ready for SSDOM placement.
        """
        badge: BS5Element = BS5Element(
            self.tag,
            self.content,
            classes=self.badge_classes,
            **self.attrs
        )
        return badge
