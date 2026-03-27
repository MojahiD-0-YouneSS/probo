from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.layout import Button
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Button(BS5Component):
    """A standard Bootstrap 5 Button component.

    This class handles the complexity of Bootstrap button variants and sizing,
    ensuring that the correct CSS classes are applied to the underlying SSDOM
    element. It supports fluent modification for size adjustments.

    Attributes:
        variant (str): The visual style of the button (e.g., 'primary', 'danger').
        size (str): The initial scale of the button ('sm', 'lg', or 'default').
        content (str): The text or HTML content inside the button.
        attrs (Dict[str, Any]): Dictionary of HTML attributes for the button.
        btn_classes (List[str]): List of CSS classes to be applied during render.
        tag (str): The HTML tag name used (always 'button').
    """

    def __init__(
        self, 
        content: str, 
        variant: str = "primary", 
        size: str = 'default', 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the button with theme and size logic.

        Args:
            content (str): The inner content of the button.
            variant (str): BS5 color theme name.
            size (str): Initial size identifier.
            render_constraints (dict, optional): State validation properties.
            **attrs (Any): Additional attributes like 'id' or 'onclick'.
        """
        self.variant: str = variant
        self.size: str = size
        self.attrs: Dict[str, Any] = {'type': 'button'}
        self.attrs.update(attrs)
        self.content: str = content
        self.render_constraints: Dict[str, Any] = render_constraints or {}
        
        self.btn_classes: List[str] = ["btn", f"btn-{self.variant}"]
        self.tag: str = 'button'
        
        if self.size in ['sm', 'lg']:
            self.btn_classes.append(f"btn-{self.size}")
            
        super().__init__(name='BS5-Button', state_props=self.render_constraints)

    @property    
    def lg(self) -> Self:
        """Dynamically upgrades the button to large size.

        Returns:
            Self: The updated button instance for chaining.
        """
        self.btn_classes.append("btn-lg")
        if hasattr(self, 'template'):
            self.template.attr_manager.add_class("btn-lg")
        return self

    @property
    def sm(self) -> Self:
        """Dynamically downgrades the button to small size.

        Returns:
            Self: The updated button instance for chaining.
        """
        self.btn_classes.append("btn-sm")
        if hasattr(self, 'template'):
            self.template.attr_manager.add_class("btn-sm")
        return self

    def _render_comp(self) -> BS5Element:
        """Constructs the final SSDOM button element.

        Returns:
            BS5Element: The rendered button object.
        """
        button: BS5Element = BS5Element(
            self.tag,
            self.content,
            classes=self.btn_classes,
            **self.attrs
        )
        return button

class BS5CloseButton(BS5Component):
    """A specialized generic close button for dismissible content.

    Specifically designed for Modals, Alerts, and Offcanvas components.
    It supports the 'white' variant to ensure visibility on dark backgrounds.

    Attributes:
        variant (str): Use 'white' for dark backgrounds, otherwise 'base'.
        btn_classes (List[str]): Resolved classes for the close button.
    """

    def __init__(
        self, 
        variant: str = "base", 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the close button with accessibility defaults."""
        self.variant: str = variant
        self.attrs: Dict[str, Any] = attrs
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.btn_classes: List[str] = ['btn-close']
        
        self.attrs.update({"type": "button", "aria-label": "Close"})
        
        if variant == 'white':
            self.btn_classes.append('btn-close-white')
            
        self.tag: str = 'button'
        super().__init__(name='BS5-close-button', state_props=self.render_constraints)

    def _render_comp(self) -> BS5Element:
        """Assembles the close button SSDOM element.

        Returns:
            BS5Element: The button ready for DOM injection.
        """
        button: BS5Element = BS5Element(
            self.tag,
            classes=self.btn_classes,
            **self.attrs
        )
        return button

class BS5ButtonGroup(BS5Component):
    """A container for grouping multiple buttons into a cohesive unit.

    Facilitates horizontal or vertical button stacking and allows for
    group-wide sizing constraints.

    Attributes:
        btns (List[str]): Collection of rendered button strings.
        variant (str): The layout orientation ('horizontal' or 'vertical').
    """

    def __init__(
        self, 
        *btns: Any, 
        variant: str = 'horizontal', 
        size: str = 'default', 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the group with orientation and roles."""
        self.attrs: Dict[str, Any] = attrs
        self.attrs.update({'role': "group"})
        self.size: str = size
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.tag: str = 'div'
        
        group_type: str = "btn-group-vertical" if variant == "vertical" else "btn-group"
        self.btn_group_classes: List[str] = [group_type]
        self.variant: str = variant
        self.btns: List[str] = [b.render() if hasattr(b, 'render') else str(b) for b in btns]
        
        if self.size in ['sm', 'lg']:
            self.btn_group_classes.append(f"btn-group-{self.size}")

        super().__init__(name='BS5-button-group', state_props=self.render_constraints)

    @property
    def lg(self) -> Self:
        """Applies large scaling to the entire button group."""
        self.btn_group_classes.append("btn-group-lg")
        if hasattr(self, 'template'):
            self.template.attr_manager.add_class("btn-group-lg")
        return self

    @property
    def sm(self) -> Self:
        """Applies small scaling to the entire button group."""
        self.btn_group_classes.append("btn-group-sm")
        if hasattr(self, 'template'):
            self.template.attr_manager.add_class("btn-group-sm")
        return self

    def before_render(self, *args: Any, **kwargs: Any) -> Self:
        """Pre-processes buttons into the component template."""
        self.include_content_parts(*self.btns)
        return self

    def add_btn(self, content: str, variant: str = "primary", size: str = 'default', **attrs: Any) -> Self:
        """Appends a new BS5Button to the internal collection.

        Args:
            content (str): Text for the new button.
            variant (str): Theme color.
            size (str): Local button size.
            **attrs (Any): Button HTML attributes.

        Returns:
            Self: For fluent chaining.
        """
        btn: BS5Button = BS5Button(content, variant=variant, size=size, **attrs)
        self.btns.append(btn.render())
        return self

    def add_check_box_btn(
        self, 
        content: str, 
        variant: str = "primary", 
        size: str = 'default', 
        override_input_attr: Optional[Dict[str, str]] = None, 
        **attrs: Any
    ) -> Self:
        """Adds a toggleable checkbox styled as a button.

        Args:
            content (str): Label for the checkbox.
            variant (str): Color of the active state.
            size (str): Size of the checkbox button.
            override_input_attr (dict, optional): Overrides for the hidden input tag.
            **attrs (Any): Attributes for the label tag.

        Returns:
            Self: For fluent chaining.
        """
        input_id: str = attrs.get('for', f"check-{len(self.btns)}")
        input_attrs: Dict[str, str] = {
            "type": "checkbox", 
            "id": input_id, 
            "autocomplete": "off"
        }
        
        if override_input_attr:
            input_attrs.update(override_input_attr)

        bs5_input: BS5Element = BS5Element('input', classes=["btn-check"], **input_attrs)
        btn_label: BS5Element = BS5Element('label', content, classes=["btn", f"btn-{variant}"], **attrs)
        
        if size in ['sm', 'lg']:
            btn_label.attr_manager.add_class(f"btn-{size}")
            
        self.btns.append(f'{bs5_input.render()}{btn_label.render()}')
        return self

    def _render_comp(self) -> BS5Element:
        """Renders the outer button group container."""
        btn_grp: BS5Element = BS5Element(
            self.tag,
            ''.join(self.btns),
            classes=self.btn_group_classes,
            **self.attrs
        )
        return btn_grp

class BS5ButtonToolbar(BS5Component):
    """A high-level container for grouping multiple ButtonGroups.

    Ideal for complex interfaces like text editors or paginated lists.

    Attributes:
        btn_grps (List[str]): List of rendered button group strings.
    """

    def __init__(self, *btn_grps: Any, render_constraints: Optional[Dict[str, Any]] = None, **attrs: Any) -> None:
        """Initializes the toolbar with accessibility attributes."""
        self.btn_grps: List[str] = [
            bg.render() if hasattr(bg, 'render') else str(bg) for bg in btn_grps
        ]
        self.attrs: Dict[str, Any] = attrs
        self.attrs.update({'role': "toolbar"})
        self.tag: str = 'div'
        self.btn_toolbar_classes: List[str] = ['btn-toolbar']
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        super().__init__(name='BS5-button-toolbar', state_props=self.render_constraints)

    def add_btn_grp(self, btn_grp: BS5ButtonGroup) -> Self:
        """Injects a new ButtonGroup into the toolbar."""
        self.btn_grps.append(btn_grp.render())
        return self

    def before_render(self, *args: Any, **kwargs: Any) -> Self:
        """Aggregates all groups before rendering the toolbar."""
        self.include_content_parts(*self.btn_grps)
        return self

    def _render_comp(self) -> BS5Element:
        """Finalizes the toolbar structure."""
        btn_toolbar: BS5Element = BS5Element(
            self.tag,
            ''.join(self.btn_grps),
            classes=self.btn_toolbar_classes,
            **self.attrs
        )
        return btn_toolbar