from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Cards
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Card(BS5Component):
    """A comprehensive manager for Bootstrap 5 Card components.

    Cards provide a flexible and extensible content container with options 
    for headers, footers, varied display modes, and internal layout sections. 
    This class automates the assignment of 'card-body', 'card-img-top', and 
    'card-title' utility classes while managing structural order based on 
    image placement.

    Attributes:
        attrs (Dict[str, Any]): Additional HTML attributes for the card container.
        is_image_bottom (bool): If True, renders the image at the bottom 
            of the card using 'card-img-bottom' logic.
        card_header (Optional[Any]): Content for the card header section.
        card_body (Optional[Any]): Content for the primary card body.
        card_footer (Optional[Any]): Content for the card footer section.
        card_image (Optional[Any]): Content for the card image section.
        render_constraints (Dict[str, Any]): Schema validation for properties.
        card_classes (List[str]): Resolved CSS classes for the card.
        body_children (List[str]): Collection of rendered body elements.
    """
    
    def __init__(
        self, 
        card_header: Optional[Any] = None,
        card_image: Optional[Any] = None, 
        card_body: Optional[Any] = None,
        card_footer: Optional[Any] = None,
        render_constraints: Optional[Dict[str, Any]] = None,
        is_image_bottom: bool = False, 
        **attrs: Any
    ) -> None:
        """Initializes the card with structural components and state logic."""
        self.attrs: Dict[str, Any] = attrs
        self.is_image_bottom: bool = is_image_bottom
        self.card_header: Optional[Any] = card_header
        self.card_body: Optional[Any] = card_body
        self.card_footer: Optional[Any] = card_footer
        self.render_constraints: Dict[str, Any] = render_constraints or {}
        self.card_image: Optional[Any] = card_image
        self.card_classes: List[str] = ['card']
        self.tag: str = 'div'
        self.body_children: List[str] = []
        
        super().__init__(name='BS5-card', state_props=self.render_constraints)

    def add_card_title(self, title: str, tag: str = 'h1', **attrs: Any) -> Self:
        """Adds a title to the card body with the 'card-title' class.

        Args:
            title (str): The text for the title.
            tag (str): The HTML heading tag to use.
            **attrs (Any): Additional attributes for the title element.

        Returns:
            Self: Enables fluent method chaining.
        """
        card_title: BS5Element = BS5Element(tag, title, classes=['card-title'], **attrs)
        self.body_children.append(card_title.render())
        return self

    def add_card_sub_title(self, sub_title: str, tag: str = 'h1', **attrs: Any) -> Self:
        """Adds a subtitle to the card body with the 'card-subtitle' class.

        Args:
            sub_title (str): The text for the subtitle.
            tag (str): The HTML heading tag to use.
            **attrs (Any): Additional attributes for the subtitle element.

        Returns:
            Self: Enables fluent method chaining.
        """
        card_sub_title: BS5Element = BS5Element(tag, sub_title, classes=['card-subtitle'], **attrs)
        self.body_children.append(card_sub_title.render())
        return self

    def add_card_text(self, text: str, tag: str = 'p', **attrs: Any) -> Self:
        """Adds descriptive text to the card body with the 'card-text' class.

        Args:
            text (str): The paragraph content.
            tag (str): The HTML tag to use (defaults to 'p').
            **attrs (Any): Additional attributes for the text element.

        Returns:
            Self: Enables fluent method chaining.
        """
        card_text: BS5Element = BS5Element(tag, text, classes=['card-text'], **attrs)
        self.body_children.append(card_text.render())
        return self

    def add_card_link(self, link: str, tag: str = 'a', **attrs: Any) -> Self:
        """Adds a link to the card body with the 'card-link' class.

        Args:
            link (str): The link text or label.
            tag (str): The HTML tag to use (defaults to 'a').
            **attrs (Any): Additional attributes for the anchor element.

        Returns:
            Self: Enables fluent method chaining.
        """
        card_link: BS5Element = BS5Element(tag, link, classes=['card-link'], **attrs)
        self.body_children.append(card_link.render())
        return self

    def add_card_body(self, card_body: Any, override: bool = False, **attrs: Any) -> Self:
        """Adds or updates the primary card body container.

        Args:
            card_body (Any): The main content for the body.
            override (bool): If True, replaces existing body content.
            **attrs (Any): Additional attributes for the card-body div.

        Returns:
            Self: Enables fluent method chaining.
        """
        body: BS5Element = BS5Element(
            'div',
            card_body,
            classes=['card-body'], 
            **attrs
        )
        body.include(*self.body_children)
        
        rendered_body: str = body.render()
        if self.card_body and not override:
            self.card_body = str(self.card_body) + rendered_body
        else:
            self.card_body = rendered_body
            
        return self

    def add_card_header(self, card_header: Any, override: bool = False, **attrs: Any) -> Self:
        """Adds or updates the header section of the card.

        Args:
            card_header (Any): The content for the header.
            override (bool): If True, replaces existing header content.
            **attrs (Any): Additional attributes for the card-header div.

        Returns:
            Self: Enables fluent method chaining.
        """
        header: BS5Element = BS5Element(
            'div',
            card_header,
            classes=['card-header'], 
            **attrs
        )
        
        rendered_header: str = header.render()
        if self.card_header and not override:
            self.card_header = str(self.card_header) + rendered_header
        else:
            self.card_header = rendered_header
            
        return self

    def add_card_footer(self, card_footer: Any, override: bool = False, **attrs: Any) -> Self:
        """Adds or updates the footer section of the card.

        Args:
            card_footer (Any): The content for the footer.
            override (bool): If True, replaces existing footer content.
            **attrs (Any): Additional attributes for the card-footer div.

        Returns:
            Self: Enables fluent method chaining.
        """
        footer: BS5Element = BS5Element(
            'div',
            card_footer,
            classes=['card-footer'], 
            **attrs
        )
        
        rendered_footer: str = footer.render()
        if self.card_footer and not override:
            self.card_footer = str(self.card_footer) + rendered_footer
        else:
            self.card_footer = rendered_footer
            
        return self
    
    def add_card_image(self, src_url: str, override: bool = False, **attrs: Any) -> Self:
        """Sets or updates the main card image with appropriate positional classes.

        Args:
            src_url (str): The image source path.
            override (bool): If True, replaces the existing image.
            **attrs (Any): Additional attributes for the img tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        img_class: str = 'card-img-bottom' if self.is_image_bottom else 'card-img-top'
        img: BS5Element = BS5Element(
            'img',
            classes=[img_class], 
            src=src_url,
            **attrs
        )
        
        rendered_img: str = img.render()
        if self.card_image and not override:
            self.card_image = str(self.card_image) + rendered_img
        else:
            self.card_image = rendered_img
            
        return self

    def before_render(self, **props: Any) -> None:
        """Organizes structural parts in correct visual order before rendering.

        Args:
            **props (Any): Rendering properties.
        """
        if self.card_body:
             if not self.body_children:
                 self.body_children.append(str(self.card_body))

        parts: List[Optional[Any]]
        if self.is_image_bottom:
            parts = [self.card_header, *self.body_children, self.card_footer, self.card_image]
        else:
            parts = [self.card_header, self.card_image, *self.body_children, self.card_footer]
            
        filtered_parts: List[str] = [str(x) for x in parts if x is not None]
        self.include_content_parts(*filtered_parts)

    def _render_comp(self) -> BS5Element:
        """Assembles the finalized SSDOM card object.

        Returns:
            BS5Element: The fully constructed card element.
        """
        if self.card_header:
            self.add_card_header(self.card_header, override=True)
        if self.card_image:
            self.add_card_image(str(self.card_image), override=True)
        if self.card_body:
            self.add_card_body(self.card_body, override=True)
        if self.card_footer:
            self.add_card_footer(self.card_footer, override=True)

        parts: List[Optional[Any]]
        if self.is_image_bottom:
            parts = [self.card_header, *self.body_children, self.card_footer, self.card_image]
        else:
            parts = [self.card_header, self.card_image, *self.body_children, self.card_footer]
            
        filtered_parts: List[str] = [str(x) for x in parts if x is not None]
        
        card: BS5Element = BS5Element(
            self.tag,
            ''.join(filtered_parts),
            classes=self.card_classes, 
            **self.attrs
        )
        return card
    
class BS5CardGroup(BS5Component):
    """A layout container for grouping multiple cards with unified sizing.

    In a CardGroup, cards have a constant width and height, and their 
    footers automatically align at the bottom.

    Attributes:
        attrs (Dict[str, Any]): Attributes for the group container.
        cards (List[Any]): Collection of card instances or rendered strings.
        card_classes (List[str]): CSS classes for the group.
        tag (str): HTML tag for the container.
    """
    
    def __init__(
        self, 
        *cards: Any, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the card group with child elements."""
        self.attrs: Dict[str, Any] = attrs
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.cards: List[Any] = list(cards)
        self.card_classes: List[str] = ['card-group']
        self.tag: str = 'div'
        
        super().__init__(name='BS5-card-group', state_props=self.render_constraints)

    def add_card(
        self, 
        card_header: Optional[Any] = None, 
        card_image: Optional[Any] = None, 
        card_body: Optional[Any] = None, 
        card_footer: Optional[Any] = None, 
        **attrs: Any
    ) -> Self:
        """Factory method to create and add a new card directly to the group.

        Args:
            card_header (Any, optional): Header content for the new card.
            card_image (Any, optional): Image content for the new card.
            card_body (Any, optional): Body content for the new card.
            card_footer (Any, optional): Footer content for the new card.
            **attrs (Any): Attributes for the new card container.

        Returns:
            Self: Enables fluent method chaining.
        """
        card: str = BS5Card(
            card_header=card_header, 
            card_image=card_image, 
            card_body=card_body, 
            card_footer=card_footer, 
            **attrs
        ).render()
        self.cards.append(card) 
        return self

    def before_render(self, **props: Any) -> None:
        """Aggregates all cards into the template before rendering."""
        rendered_cards: List[str] = [
            x.render() if hasattr(x, 'render') else str(x) for x in self.cards
        ]
        self.include_content_parts(*rendered_cards)

    def _render_comp(self) -> BS5Element:
        """Final structural assembly of the card group.

        Returns:
            BS5Element: The rendered card group container.
        """
        card_group_content: str = ''.join([
            x.render() if hasattr(x, 'render') else str(x) for x in self.cards
        ])
        
        card_group: BS5Element = BS5Element(
            self.tag,
            card_group_content,
            classes=self.card_classes, 
            **self.attrs
        )
        return card_group
