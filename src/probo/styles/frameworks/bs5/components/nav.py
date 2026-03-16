from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Nav
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Nav(BS5Component):
    """A manager for Bootstrap 5 Navigation components.

    The Nav component provides a flexible foundation for building tabbed, 
    pilled, or justified navigation menus. This class handles the logic 
    for applying structural utility classes like 'nav-tabs' and 'nav-pills', 
    while managing the lifecycle of child nav-items and nav-links within 
    the SSDOM.

    Attributes:
        attrs (Dict[str, Any]): HTML attributes for the root navigation tag.
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        content (str): The primary inner content string.
        nav_items (List[BS5Element]): Collection of child navigation elements.
        is_tab (bool): If True, applies the 'nav-tabs' visual style.
        is_fill (bool): If True, forces items to fill all available space.
        is_pill (bool): If True, applies the 'nav-pills' visual style.
        is_justified (bool): If True, ensures items have equal widths.
        nav_classes (List[str]): Resolved CSS classes for the container.
        tag (str): The HTML tag for the container (defaults to 'ul').
    """
    
    def __init__(
        self, 
        *content: Any, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        is_tab: bool = False, 
        is_fill: bool = False, 
        is_pill: bool = False, 
        is_justified: bool = False, 
        **attrs: Any
    ) -> None:
        """Initializes the navigation container with structural variant logic."""
        self.attrs: Dict[str, Any] = attrs
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.content: str = ''.join([str(c) for c in content])
        self.nav_items: List[BS5Element] = []
        
        self.is_tab: bool = is_tab
        self.is_fill: bool = is_fill
        self.is_pill: bool = is_pill
        self.is_justified: bool = is_justified
        
        self.nav_classes: List[str] = ['nav']
        self.tag: str = 'ul'
        
        if self.is_tab:
            self.nav_classes.append('nav-tabs')
        if self.is_justified:
            self.nav_classes.append('nav-justified')
        if self.is_pill:
            self.nav_classes.append('nav-pills')
        if self.is_fill:
            self.nav_classes.append('nav-fill')
            
        super().__init__(name='BS5-nav', state_props=self.render_constraints)

    def add_nav_item(
        self, 
        content: Any, 
        tag: str = 'li', 
        **attrs: Any
    ) -> Self:
        """Constructs and appends a standard 'nav-item' to the list.

        Args:
            content (Any): The HTML or text to place inside the item.
            tag (str): The HTML tag for the item (usually 'li').
            **attrs (Any): Additional attributes for the item tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        item: BS5Element = BS5Element(
            tag,
            content,
            classes=['nav-item'],
            **attrs
        )
        self.nav_items.append(item)
        return self

    def add_nav_link(
        self, 
        content: Any, 
        active: bool = False, 
        disabled: bool = False,
        url: str = "#",
        **attrs: Any
    ) -> Self:
        """Constructs and appends a 'nav-link' specifically for anchor-based navigation.
        
        Args:
            content (Any): The text or HTML for the link label.
            active (bool): If True, applies the 'active' state and accessibility tags.
            disabled (bool): If True, applies the 'disabled' state and accessibility tags.
            url (str): The destination URL for the link.
            **attrs (Any): Additional attributes for the anchor tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        link_classes: List[str] = ['nav-link']
        
        if active:
            link_classes.append('active')
            attrs.update({'aria-current': 'page'})
            
        if disabled or 'disabled' in attrs.get('Class',[]):
            if disabled:
                link_classes.append('disabled')
            attrs.update({
                'aria-disabled': 'true',
                'tabindex': '-1'
            })

        item: BS5Element = BS5Element(
            'a',
            content,
            classes=link_classes,
            href=url,
            **attrs
        )
        
        self.nav_items.append(item)
        return self

    def before_render(self, **props: Any) -> None:
        """Aggregates all registered navigation items into the component template."""
        self.include_content_parts(*self.nav_items)

    def _render_comp(self) -> BS5Element:
        """Assembles the final navigation SSDOM element.

        Returns:
            BS5Element: The rendered navigation root element.
        """
        nav: BS5Element = BS5Element(
            self.tag,
            self.content,
            classes=self.nav_classes,
            **self.attrs
        )
        return nav