from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Toast
from probo.styles.frameworks.bs5.bs5 import BS5Element

from typing import Any, Dict, List, Optional, Self, Union

class BS5Toast(BS5Component):
    """A manager for Bootstrap 5 Toast components.

    Toasts are lightweight notifications designed to mimic the push notifications 
    popularized by mobile and desktop operating systems. This class handles 
    the assembly of toast headers and bodies, manages the placement of the 
    close button, and supports wrapping multiple toasts in a dedicated 
    'toast-container' for stacking.

    Attributes:
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Additional HTML attributes for the toast(s).
        btn_position (str): Placement of the close button ('header' or 'body').
        header_content (Optional[Any]): Default content for the toast header.
        body_content (Optional[Any]): Default content for the toast body.
        toast_items (List[BS5Element]): Collection of toasts for container mode.
        toast (Optional[BS5Element]): The single rendered toast element.
        include_container (bool): If True, wraps toasts in a positionable container.
        tag (str): The HTML tag for the container (defaults to 'div').
        close_btn (BS5Element): The reusable dismiss button element.
        toast_classes (List[str]): Resolved CSS classes for the toast elements.
    """

    def __init__(
        self, 
        header_content: Optional[Any] = None,
        body_content: Optional[Any] = None,
        btn_position: str = 'header',
        render_constraints: Optional[Dict[str, Any]] = None,
        include_container: bool = False, 
        **attrs: Any
    ) -> None:
        """Initializes the toast manager with layout and structural logic.

        Args:
            header_content (Any, optional): Text or HTML for the header.
            body_content (Any, optional): Text or HTML for the body.
            btn_position (str): Where to place the 'X' button ('header'|'body').
            render_constraints (dict, optional): State validation properties.
            include_container (bool): Enable stacking container mode.
            **attrs (Any): Attributes for the toast elements.
        """
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.attrs: Dict[str, Any] = attrs
        self.btn_position: str = btn_position
        self.header_content: Optional[Any] = header_content
        self.body_content: Optional[Any] = body_content
        self.toast_items: List[BS5Element] = []
        self.toast: Optional[BS5Element] = None
        self.include_container: bool = include_container
        self.tag: str = 'div'
        
        self.close_btn: BS5Element = self.close_toast_btn()
        self.toast_classes: List[str] = [Toast.TOAST.value]
        
        super().__init__(name='BS5-Toast', state_props=self.render_constraints)

    def close_toast_btn(self) -> BS5Element:
        """Constructs the standard Bootstrap 5 close button for toasts.

        Returns:
            BS5Element: A button configured with 'data-bs-dismiss="toast"'.
        """
        return BS5Element(
            'button',
            classes=['btn-close'],
            Type='button',
            data_bs_dismiss='toast',
            aria_label='close',
        )

    def add_toast(
        self,
        header_content: Optional[Any] = None,
        body_content: Optional[Any] = None,
        btn_position: str = 'header',
        **attrs: Any
    ) -> Self:
        """Constructs a single toast and adds it to the internal state.

        This method handles the conditional logic for including headers, 
        bodies, and the close button based on the provided parameters.

        Args:
            header_content (Any, optional): Local header content override.
            body_content (Any, optional): Local body content override.
            btn_position (str): Local button position override.
            **attrs (Any): Local attribute overrides for this specific toast.

        Returns:
            Self: Enables fluent method chaining.
        """
        toast: BS5Element = BS5Element(
            self.tag,
            classes=self.toast_classes,
            role='alert',
            aria_live='assertive',
            aria_atomic='true',
        )
        toast.attr_manager.set_bulk_attr(**self.attrs)
        toast.attr_manager.set_bulk_attr(**attrs)
        
        header: Optional[BS5Element] = None
        body: Optional[BS5Element] = None

        if header_content:
            header = BS5Element(
                'div', header_content, classes=[Toast.TOAST_HEADER.value],
            )
        if body_content:
            body = BS5Element(
                'div', body_content, classes=[Toast.TOAST_BODY.value],
            )

        if header and btn_position == 'header':
            header.include(self.close_btn)
            toast.include(header)

        if body and btn_position == 'body':
            body.include(self.close_btn)
            toast.include(body)

        if header and not btn_position == 'header':
            toast.include(header)
            
        if body and not btn_position == 'body':
            toast.include(body)

        if self.include_container:
            self.toast_items.append(toast)
        else:
            self.toast = toast
            
        return self

    def before_render(self, **props: Any) -> None:
        """Aggregates all registered toasts into the template before rendering."""
        self.include_content_parts(*self.toast_items)

    def _render_comp(self, *args: Any, **kwargs: Any) -> BS5Element:
        """Assembles the final toast or toast-container SSDOM element.

        Returns:
            BS5Element: The rendered container or single toast element.
        """
        if self.include_container:
            toast_container: BS5Element = BS5Element(
                self.tag,
                classes=[Toast.TOAST_CONTAINER.value],
            )
            toast_container.include(*self.toast_items)
            return toast_container
        else:
            self.add_toast(
                header_content=self.header_content,
                body_content=self.body_content,
                btn_position=self.btn_position,
            )
            return self.toast