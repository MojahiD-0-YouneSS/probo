from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Offcanvas
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Offcanvas(BS5Component):
    """A manager for Bootstrap 5 Offcanvas components.

    Offcanvas is a sidebar component that can be toggled via JavaScript to 
    appear from the left, right, top, or bottom edge of the viewport. This 
    class manages the structural assembly of the header, body, and trigger 
    elements within the SSDOM.

    Attributes:
        attrs (Dict[str, Any]): Attributes for the root offcanvas container.
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        position (str): The edge from which the offcanvas appears ('start', 'end', 'top', 'bottom').
        content (str): Initial inner content string.
        offcanvas_items (List[BS5Element]): Collection of rendered fragments.
        offcanvas_classes (List[str]): Resolved CSS classes for the container.
        tag (str): The HTML tag for the container (defaults to 'div').
    """

    def __init__(
        self, 
        *content: Any, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        position: str = 'start', 
        **attrs: Any
    ) -> None:
        """Initializes the offcanvas with positional logic and accessibility roles.

        Args:
            *content (Any): Initial elements or strings to include.
            render_constraints (dict, optional): State validation properties.
            position (str): Viewport edge ('start' for left, 'end' for right).
            **attrs (Any): Attributes including the mandatory 'Id' for targeting.
        """
        self.attrs: Dict[str, Any] = attrs
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.position: str = position
        self.content: str = ''.join([str(c) for c in content])
        self.offcanvas_items: List[BS5Element] = []

        self.offcanvas_classes = [
            Offcanvas.OFFCANVAS.value,
            Offcanvas[f"offcanvas_{self.position}".upper()].value,
        ]
        self.tag: str = "div"

        super().__init__(name='BS5-offcanvas', state_props=self.render_constraints)

    def add_trigger(
        self, 
        target: str, 
        content: Any, 
        tag: str = 'button', 
        **attrs: Any
    ) -> Self:
        """Constructs a trigger element to toggle this offcanvas.

        Args:
            target (str): The ID of the offcanvas to toggle.
            content (Any): The text or HTML label for the trigger.
            tag (str): The HTML tag to use (usually 'button' or 'a').
            **attrs (Any): Additional attributes for the trigger.

        Returns:
            Self: Enables fluent method chaining.
        """
        trigger_attrs: Dict[str, Any] = {
            'data-bs-toggle': 'offcanvas',
            'aria-controls': target
        }

        if tag == 'button':
            trigger_attrs.update({'type': 'button'})
        else:
            trigger_attrs.update({'role': 'button', 'href': f'#{target}'})

        trigger: BS5Element = BS5Element(
            tag,
            content,
            **trigger_attrs
        )
        trigger.attr_manager.set_bulk_attr(**attrs)

        return self

    def add_offcanvas_header(
        self, 
        content: Any, 
        tag: str = 'h5', 
        **attrs: Any
    ) -> Self:
        """Constructs and appends the offcanvas header section.

        Args:
            content (Any): The text or HTML for the offcanvas title.
            tag (str): The HTML tag for the title (defaults to 'h5').
            **attrs (Any): Additional attributes for the title element.

        Returns:
            Self: Enables fluent method chaining.
        """
        title: BS5Element = BS5Element(
            tag,
            content,
            classes=[
                Offcanvas.OFFCANVAS_TITLE.value,
            ],
            **attrs,
        )

        if not attrs.get('Id') and self.attrs.get('Id'):
            title.attr_manager.set_attr('Id', f"{self.attrs.get('Id')}Label")

        close_btn: BS5Element = BS5Element(
            'button',
            classes=['btn-close']
        )
        close_btn.attr_manager.set_bulk_attr(
            type='button',
            data_bs_dismiss='offcanvas',
            aria_label="Close"
        )

        header: BS5Element = BS5Element(
            'div',
            classes=['offcanvas-header']
        )
        if attrs.get("Id", None):
            self.template.attr_manager.set_attr("aria_labelledby", attrs["Id"])
        header.include(title, close_btn)

        self.offcanvas_items.append(header)
        return self

    def add_offcanvas_body(self, content: Any, **attrs: Any) -> Self:
        """Constructs and appends the primary offcanvas body section.

        Args:
            content (Any): The HTML or text content for the body.
            **attrs (Any): Additional attributes for the body container.

        Returns:
            Self: Enables fluent method chaining.
        """
        item: BS5Element = BS5Element(
            'div',
            content,
            classes=['offcanvas-body'],
            **attrs
        )
        self.offcanvas_items.append(item)
        return self

    def before_render(self, **props: Any) -> None:
        """Aggregates all offcanvas fragments into the template before rendering."""
        self.include_content_parts(*self.offcanvas_items)

    def _render_comp(self) -> BS5Element:
        """Assembles the final Offcanvas SSDOM element.

        Returns:
            BS5Element: The rendered offcanvas root element.
        """
        offcanvas: BS5Element = BS5Element(
            self.tag,
            self.content,
            classes=self.offcanvas_classes,
            **self.attrs
        )

        # Standard accessibility attribute for hidden off-screen content
        offcanvas.attr_manager.set_bulk_attr(tabindex=-1)

        return offcanvas
