from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Collapse
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Collapse(BS5Component):
    """A manager for Bootstrap 5 Collapse components.

    The Collapse component allows for toggling the visibility of content 
    across the page. This class handles the complexity of linking triggers 
    (links or buttons) to the collapsible container using unique IDs and 
    data-attributes, ensuring the accessibility state (aria-expanded) is 
    correctly initialized.

    Attributes:
        content (Any): The HTML or text content inside the collapsible area.
        collapse_classes (List[str]): Resolved CSS classes for the component.
        trigger (Optional[BS5Element]): The element assigned to toggle the collapse.
        attrs (Dict[str, Any]): Additional HTML attributes for the collapse container.
        tag (str): The HTML tag for the container (defaults to 'div').
    """

    def __init__(
        self, 
        content: Any, 
        is_multicollapse: bool = False, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the collapse container with theme and multi-target logic.

        Args:
            content (Any): The inner content of the collapsible element.
            is_multicollapse (bool): If True, enables multi-target toggle behavior.
            render_constraints (dict, optional): State validation properties.
            **attrs (Any): Attributes including the mandatory 'Id' for targeting.
        """
        self.attrs: Dict[str, Any] = attrs
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.content: Any = content 
        
        multi_class: str = 'multi-collapse' if is_multicollapse else ''
        self.collapse_classes: List[str] = ['collapse', multi_class]
        
        self.trigger: Optional[BS5Element] = None
        self.tag: str = 'div'
        
        super().__init__(name='BS5-collapse', state_props=self.render_constraints)

    def add_link_trigger(self, content: Any, classes: List[str], **attrs: Any) -> Self:
        """Assigns an anchor tag (<a>) as the toggle trigger.

        Bootstrap 5 supports using the 'href' attribute of a link to target 
        a collapsible element by its ID.

        Args:
            content (Any): The text or HTML inside the link.
            classes (List[str]): CSS classes for the link (e.g., ['btn', 'btn-primary']).
            **attrs (Any): Additional attributes for the link tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        target_id: str = str(self.attrs.get('Id', ''))
        link: BS5Element = BS5Element(
            'a',
            content,
            classes=classes,       
            data_bs_toggle="collapse",
            href=f"#{target_id}",
            role="button",
            aria_expanded="false",
            aria_controls=target_id,
            **attrs
        )
        self.trigger = link
        return self

    def add_button_trigger(self, content: Any, classes: List[str], **attrs: Any) -> Self:
        """Assigns a button tag (<button>) as the toggle trigger.

        Unlike links, buttons use the 'data-bs-target' attribute to 
        identify the collapsible container.

        Args:
            content (Any): The text or HTML inside the button.
            classes (List[str]): CSS classes for the button.
            **attrs (Any): Additional attributes for the button tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        target_id: str = str(self.attrs.get('Id', ''))
        btn: BS5Element = BS5Element(
            'button',
            content,
            classes=classes,       
            data_bs_toggle="collapse",
            type="button",
            data_bs_target=f"#{target_id}",
            aria_expanded="false",
            aria_controls=target_id,
            **attrs
        )
        self.trigger = btn
        return self

    def get_trigger_html(self) -> str:
        """Returns the rendered HTML of the assigned trigger.

        Returns:
            str: The rendered HTML string of the trigger element.
        """
        if self.trigger:
            return self.trigger.render()
        return ""

    def _render_comp(self) -> BS5Element:
        """Assembles the final collapsible SSDOM element.

        Returns:
            BS5Element: The rendered collapse object ready for the DOM.
        """
        collapse: BS5Element = BS5Element(
            self.tag,
            self.content,
            classes=self.collapse_classes,
            **self.attrs
        )
        return collapse