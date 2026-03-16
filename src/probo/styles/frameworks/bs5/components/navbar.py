from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Navbar
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Callable, Union

class BS5NavBar(BS5Component):
    """A manager for Bootstrap 5 Navigation Bar components.

    The Navbar is a powerful, responsive navigation header that includes 
    support for branding, navigation, collapse plugins, and more. This class 
    manages the internal SSDOM structure, ensuring that elements like the 
    brand and toggler are placed correctly within the mandatory container wrapper.

    Attributes:
        attrs (Dict[str, Any]): Attributes for the root <nav> element.
        wraper_func (Optional[Callable]): An optional function to wrap the 
            inner content (usually for container-fluid or container).
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        content (str): Initial inner content provided during instantiation.
        navbar_items (List[str]): Collection of rendered navbar fragments.
        navbar_classes (List[str]): Resolved CSS classes for the nav element.
        tag (str): The HTML tag for the root element (defaults to 'nav').
    """

    def __init__(
        self, 
        *content: Any, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        wraper_func: Optional[Callable[[str], Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the Navbar with theme logic and structural wrappers.

        Args:
            *content (Any): Initial elements or strings to include.
            render_constraints (dict, optional): State validation properties.
            wraper_func (callable, optional): A function used to wrap the 
                rendered content before final output (e.g., a container).
            **attrs (Any): Additional attributes for the <nav> tag.
        """
        self.attrs: Dict[str, Any] = attrs
        self.wraper_func: Optional[Callable[[str], Any]] = wraper_func
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints

        self.content: str = "".join([
            x.render() if hasattr(x, 'render') else str(x) for x in content
        ])

        self.navbar_items: List[str] = []
        self.navbar_classes: List[str] = [Navbar.NAVBAR.value]
        self.tag: str = 'nav'

        super().__init__(name='BS5-NavBar', state_props=self.render_constraints)

        self.attr_manager.root = {}

    def add_navbar_brand(self, content: Any, tag: str = 'a', **attrs: Any) -> Self:
        """Adds a brand element (logo or name) to the navbar.

        Args:
            content (Any): The text or HTML for the brand.
            tag (str): The HTML tag for the brand (defaults to 'a').
            **attrs (Any): Attributes for the brand (e.g., 'href').

        Returns:
            Self: Enables fluent method chaining.
        """
        if tag == 'a' and 'href' not in attrs:
            attrs['href'] = '#'

        item: BS5Element = BS5Element(
            tag,
            content,
            classes=['navbar-brand'],
            **attrs
        )

        container: BS5Element = BS5Element('div', classes=['container-fluid'])
        container.include(item)
        self.navbar_items.append(container.render())
        return self

    def add_navbar_text(self, content: Any, tag: str = 'span', **attrs: Any) -> Self:
        """Adds a localized string of text with vertical centering.

        Args:
            content (Any): The text content to display.
            tag (str): The HTML tag to use (defaults to 'span').
            **attrs (Any): Additional attributes for the text element.

        Returns:
            Self: Enables fluent method chaining.
        """
        item: BS5Element = BS5Element(
            tag,
            content,
            classes=['navbar-text'],
            **attrs
        )

        container: BS5Element = BS5Element('div', classes=['container-fluid'])
        container.include(item)
        self.navbar_items.append(container.render())
        return self

    def add_navbar_toggler(self, target_id: str, **attrs: Any) -> Self:
        """Constructs a responsive toggler button for mobile views.

        Args:
            target_id (str): The ID of the collapsible container to toggle.
            **attrs (Any): Additional attributes for the button.

        Returns:
            Self: Enables fluent method chaining.
        """
        icon: BS5Element = BS5Element('span', classes=['navbar-toggler-icon'])
        toggler: BS5Element = BS5Element(
            'button',
            icon,
            classes=['navbar-toggler'],
            **{
                'type': 'button',
                'data-bs-toggle': 'collapse',
                'data-bs-target': f'#{target_id}',
                'aria-controls': target_id,
                'aria-expanded': 'false',
                'aria-label': 'Toggle navigation'
            }
        )
        toggler.attr_manager.set_bulk_attr(**attrs)
        self.navbar_items.append(toggler.render())
        return self

    def before_render(self, **props: Any) -> None:
        """Aggregates navbar fragments into the component before rendering."""
        self.include_content_parts(*self.navbar_items)

    def _render_comp(self) -> BS5Element:
        """Assembles the final Navbar SSDOM element.

        Returns:
            BS5Element: The fully constructed Navbar root element.
        """
        inner_content: str = (
            self.wraper_func(self.content) 
            if callable(self.wraper_func) 
            else self.content
        )

        nav: BS5Element = BS5Element(
            self.tag,
            inner_content,
            classes=self.navbar_classes,
            **self.attrs
        )
        return nav
