from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Modal
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Modal(BS5Component):
    """A comprehensive manager for Bootstrap 5 Modal components.

    Modals are positioned over everything else in the document and remove 
    scroll from the <body> so that modal content scrolls instead. This class 
    manages the complex nested structure (Dialog > Content > Header/Body/Footer) 
    and facilitates the creation of external trigger buttons linked via 
    data-attributes.

    Attributes:
        attrs (Dict[str, Any]): Attributes for the root modal container.
        modal_parts (List[str]): Collection of rendered fragments (header, body, footer).
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        modal_classes (List[str]): CSS classes for the root element (defaults to 'modal fade').
        tag (str): The HTML tag for the root container (defaults to 'div').
        triggers (List[BS5Element]): Collection of button elements that toggle this modal.
    """

    def __init__(
        self, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        is_fade: bool = True,
        **attrs: Any
    ) -> None:
        """Initializes the modal with structural placeholders and accessibility roles.

        Args:
            render_constraints (dict, optional): State validation properties.
            is_fade (bool): If True, adds the 'fade' animation class.
            **attrs (Any): Attributes including the mandatory 'Id' for targeting.
        """
        self.attrs: Dict[str, Any] = attrs
        self.attrs.update({
            'tabindex': '-1',
            'aria-hidden': 'true'
        })
        
        self.modal_parts: List[str] = []
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        
        self.modal_classes: List[str] = ['modal']
        if is_fade:
            self.modal_classes.append('fade')
            
        self.tag: str = 'div'
        self.triggers: List[BS5Element] = []
        
        super().__init__(name='BS5-Modal', state_props=self.render_constraints)

    def add_trigger_btn(
        self, 
        content: Any, 
        variant: str = "primary", 
        **attrs: Any
    ) -> Self:
        """Creates a button that targets and toggles this modal instance.

        The modal must have an 'Id' attribute defined in the constructor for 
        the trigger to function correctly.

        Args:
            content (Any): The text or HTML for the button label.
            variant (str): The Bootstrap color variant for the button.
            **attrs (Any): Additional attributes for the trigger button.

        Returns:
            Self: Enables fluent method chaining.
        """
        target_id: str = str(self.attrs.get('Id', ''))
        trigger_btn: BS5Element = BS5Element(
            'button',
            content,
            classes=['btn', f'btn-{variant}'],
            **{
                'type': 'button',
                'data-bs-toggle': 'modal',
                'data-bs-target': f'#{target_id}'
            }
        )
        trigger_btn.attr_manager.set_bulk_attr(**attrs)
        self.triggers.append(trigger_btn)
        return self

    def add_modal_header(
        self, 
        other_content: Any = "", 
        title: Optional[str] = None, 
        **attrs: Any
    ) -> Self:
        """Constructs and appends the modal header section.

        Automatically includes a close button (X) aligned to the right.

        Args:
            other_content (Any): Optional additional HTML content for the header.
            title (str, optional): Text for the 'modal-title' element.
            **attrs (Any): Additional attributes for the header container.

        Returns:
            Self: Enables fluent method chaining.
        """
        header_content: str = ""
        if title:
            title_el = BS5Element('h5', title, classes=['modal-title'])
            header_content += title_el.render()
            
        header_content += str(other_content)
        
        modal_header: BS5Element = BS5Element(
            'div',
            header_content,
            classes=['modal-header'],
            **attrs
        )
        
        btn_close: BS5Element = BS5Element(
            'button',
            classes=['btn-close'],
            **{
                'type': 'button',
                'data-bs-dismiss': 'modal',
                'aria-label': 'Close'
            }
        )
        
        modal_header.include(btn_close)
        self.modal_parts.append(modal_header.render())
        return self 

    def add_modal_body(self, content: Any, **attrs: Any) -> Self:
        """Constructs and appends the primary modal body section.

        Args:
            content (Any): The HTML or text content for the body.
            **attrs (Any): Additional attributes for the body container.

        Returns:
            Self: Enables fluent method chaining.
        """
        modal_body: BS5Element = BS5Element(
            'div',
            content,
            classes=['modal-body'],
            **attrs
        )
        self.modal_parts.append(modal_body.render())
        return self 

    def add_modal_footer(self, content: Any, **attrs: Any) -> Self:
        """Constructs and appends the modal footer section.

        Args:
            content (Any): The HTML or text content for the footer.
            **attrs (Any): Additional attributes for the footer container.

        Returns:
            Self: Enables fluent method chaining.
        """
        modal_footer: BS5Element = BS5Element(
            'div',
            content,
            classes=['modal-footer'],
            **attrs
        )
        self.modal_parts.append(modal_footer.render())
        return self

    def before_render(self, **props: Any) -> None:
        """Assembles the nested modal hierarchy before final rendering.

        This method wraps the collected modal parts (header, body, footer) 
        into the required 'modal-dialog' and 'modal-content' containers.
        """
        modal_content: BS5Element = BS5Element(
            'div',
            ''.join(self.modal_parts),
            classes=['modal-content']
        )
        
        modal_dialog: BS5Element = BS5Element(
            'div',
            modal_content,
            classes=['modal-dialog']
        )
        
        self.include_content_parts(modal_dialog)

    def _render_comp(self) -> BS5Element:
        """Final structural assembly of the root modal container.

        Returns:
            BS5Element: The rendered root modal element.
        """
        modal_root: BS5Element = BS5Element(
            self.tag,
            classes=self.modal_classes,
            **self.attrs
        )
        return modal_root