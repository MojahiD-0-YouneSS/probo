from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Lists
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5ListGroup(BS5Component):
    """A manager for Bootstrap 5 List Group components.

    List groups are flexible and powerful components for displaying a series 
    of content. This class supports basic unordered lists, linked lists, 
    and button-based list items, ensuring that 'list-group-item-action' 
    is applied correctly for interactive elements.

    Attributes:
        items (List[str]): Collection of rendered list item strings.
        list_classes (List[str]): Resolved CSS classes for the container.
        tag (str): The HTML tag for the container (defaults to 'ul').
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Additional HTML attributes for the list group.
    """

    def __init__(
        self, 
        *items: Any, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        is_flush: bool = False,
        is_numbered: bool = False,
        is_horizontal: bool = False,
        **attrs: Any
    ) -> None:
        """Initializes the list group with structural logic.

        Args:
            *items (Any): Initial items to populate the list.
            render_constraints (dict, optional): State validation properties.
            is_flush: If True, removes borders and rounded corners.
            is_numbered: If True, uses 'list-group-numbered' and 'ol' tag.
            is_horizontal: If True, changes layout to horizontal across breakpoints.
            **attrs (Any): Attributes for the container (e.g., 'Id').
        """
        self.attrs: Dict[str, Any] = attrs
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.items: List[str] = [
            i.render() if hasattr(i, 'render') else str(i) for i in items
        ]
        
        self.list_classes: List[str] = ['list-group']
        self.tag: str = 'ul'
        
        if is_flush:
            self.list_classes.append('list-group-flush')
        if is_numbered:
            self.list_classes.append('list-group-numbered')
            self.tag = 'ol'
        if is_horizontal:
            self.list_classes.append('list-group-horizontal')

        super().__init__(name='BS5-list-group', state_props=self.render_constraints)

    def add_list_item(
        self, 
        content: Any, 
        tag: str = 'li', 
        variant: Optional[str] = None,
        is_active: bool = False,
        is_disabled: bool = False,
        return_item: bool = False, 
        **attrs: Any
    ) -> Union[Self, BS5Element]:
        """Creates and appends a new item to the list group.

        Args:
            content (Any): The text or HTML for the item.
            tag (str): HTML tag (usually 'li', 'a', or 'button').
            variant (str, optional): BS5 contextual color (e.g., 'primary').
            is_active (bool): Whether to apply the 'active' class.
            is_disabled (bool): Whether to apply the 'disabled' class.
            return_item (bool): If True, returns the BS5Element instead of Self.
            **attrs (Any): Additional attributes for the item tag.

        Returns:
            Union[Self, BS5Element]: The component instance or the item element.
        """
        classes: List[str] = ['list-group-item']
        
        if tag in ['a', 'button']:
            classes.append('list-group-item-action')
            
        if variant:
            classes.append(f'list-group-item-{variant}')
            
        if is_active:
            classes.append('active')
            attrs.update({'aria-current': 'true'})
            
        if is_disabled:
            classes.append('disabled')
            attrs.update({'aria-disabled': 'true', 'tabindex': '-1'})

        item: BS5Element = BS5Element(
            tag,
            content,
            classes=classes,
            **attrs
        )
        
        if return_item:
            return item
            
        self.items.append(item.render())
        return self

    def add_link_item(self, content: Any, url: str = "#", **attrs: Any) -> Self:
        """Shorthand for adding a linked (anchor) list item.

        Args:
            content (Any): Text/HTML for the link.
            url (str): Target href.
            **attrs (Any): Attributes for the <a> tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        return self.add_list_item(content, tag='a', href=url, **attrs)

    def before_render(self, **prop: Any) -> Self:
        """Aggregates all registered items into the component template."""
        self.include_content_parts(*self.items)
        return self
    
    def _render_comp(self) -> BS5Element:
        """Assembles the final list group SSDOM element.

        Returns:
            BS5Element: The rendered list group container.
        """
        items=[]
        if self.items:
            items = [
                self.add_list_item(item, return_item=True).render()
                for item in self.items
            ]
        list_group: BS5Element = BS5Element(
            self.tag,
            ''.join(items),
            classes=self.list_classes,
            **self.attrs
        )
        return list_group

