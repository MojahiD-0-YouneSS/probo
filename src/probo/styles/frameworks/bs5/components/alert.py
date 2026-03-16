from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element
from probo.styles.frameworks.bs5.comp_enum import Alert
from typing import Any, Dict, List, Optional, Self, Union

class BS5Alert(BS5Component):
    """A comprehensive manager for Bootstrap 5 Alert components.

    This class automates the creation of alert boxes, supporting various 
    color themes, dismissible states, and multiple icon types including 
    inline SVGs, Symbol-based sprites, or Icon Fonts. It utilizes the 
    internal SSDOM to handle content injection dynamically.

    Attributes:
        variant (str): The Bootstrap color utility name.
        is_dismissible (bool): Whether the alert can be closed by the user.
        has_icon (bool): Flag to enable internal layout adjustments for icons.
        alert_classes (List[str]): Resolved CSS classes for the component.
    """

    def __init__(
        self, 
        content: str, 
        color_variant: str = "primary", 
        is_dismissible: bool = False, 
        has_icon: bool = False, 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the alert with theme logic and state properties."""
        self.variant: str = color_variant
        self.attrs: Dict[str, Any] = attrs
        self.attrs.update({'role': 'alert'})
        self.content: str = content
        self.is_dismissible: bool = is_dismissible
        self.has_icon: bool = has_icon
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        
        self.alert_classes: List[str] = ['alert', f'alert-{self.variant}']
        self.tag: str = 'div'
        
        if is_dismissible:
            self.alert_classes.append('alert-dismissible')
            
        if has_icon:
            self.content = f'<div>{self.content}</div>'
            
        super().__init__(name='BS5-alert', state_props=render_constraints)
        
        self.attr_manager.root = {'role': 'alert'}
        self.attr_manager.root.update(self.attrs)

    def add_svg_icon(
        self, 
        bs_icon_id: str, 
        path_d: Optional[str] = None, 
        **svg_attrs: Any
    ) -> Self:
        """Injects a raw inline SVG icon into the alert.

        Args:
            bs_icon_id (str): The ID to assign to the SVG element or 
                the reference ID for the sprite sheet.
            path_d (str, optional): The SVG path data. If omitted, the 
                method assumes a reference to an external sprite sheet.
            **svg_attrs (Any): Additional SVG attributes such as viewbox.

        Returns:
            Self: Enables fluent method chaining.
        """
        path_element: Optional[BS5Element] = None
        
        if not path_d:
            svg_attrs.update({
                'width': '24',
                'height': '24',
                'role': 'img',
                'aria-label': f'{self.variant.capitalize()}',
                'class': 'flex-shrink-0 me-2',
            })
            
        if path_d:
            svg_attrs.update({
                'xmlns': "http://www.w3.org/2000/svg", 
                'class': f'{bs_icon_id} flex-shrink-0 me-2'
            })
            path_element = BS5Element('path', d=path_d)
            icon_svg = BS5Element('svg', classes=['bi'], **svg_attrs)
            icon_svg.include(path_element)
        else:
            use_element = BS5Element('use', href=f'bootstrap-icons.svg#{bs_icon_id}')
            icon_svg = BS5Element('svg', classes=['bi'], **svg_attrs)
            icon_svg.include(use_element)
            
        self.template.include(icon_svg, first=True)
        return self

    def add_svg_symbol_icon(
        self, 
        symbol_attrs: Optional[Dict[str, Any]] = None, 
        **symbol_data: str
    ) -> Self:
        """Adds an icon using the SVG <symbol> definition pattern.

        Args:
            symbol_attrs (dict, optional): Attributes applied to the symbol tag.
            **symbol_data (str): Key-value pairs where key is the symbol ID 
                and value is the path 'd' string.

        Returns:
            Self: Enables fluent method chaining.
        """
        svg_items: List[BS5Element] = []
        default_attrs: Dict[str, str] = {
            'fill': "currentColor", 
            'viewBox': "0 0 16 16"
        }
        
        if symbol_attrs:
            default_attrs.update(symbol_attrs)
            
        icon_svg: BS5Element = BS5Element(
            'svg',
            classes=['bi', 'flex-shrink-0', 'me-2'],
            xmlns="http://www.w3.org/2000/svg",
            style="display: none;",
        )
        
        for symbol_id, path_d in symbol_data.items():
            symbol_element = BS5Element('symbol', Id=symbol_id, **default_attrs)
            path_element = BS5Element('path', d=path_d)
            symbol_element.include(path_element)
            svg_items.append(symbol_element)
            
        icon_svg.include(*svg_items)
        self.template.include(icon_svg, first=True)
        return self

    def add_alert_link(self, content: str, url: str = "#") -> Self:
        """Wraps text in an 'alert-link' class for consistent anchor styling.

        Args:
            content (str): The text to display for the link.
            url (str): The destination URL.

        Returns:
            Self: Enables fluent method chaining.
        """
        link: BS5Element = BS5Element('a', content, href=url)
        link.attr_manager.add_class('alert-link')
        self.template.include(link)
        return self

    def add_font_icon(self, icon_class: str, **attr: Any) -> Self:
        """Adds an icon from a font library (e.g., FontAwesome, Bootstrap Icons).

        Args:
            icon_class (str): The CSS class for the icon (e.g., 'bi-check-circle').
            **attr (Any): Additional attributes for the <i> tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        icon_element: BS5Element = BS5Element('i', classes=[icon_class], **attr)
        self.template.include(icon_element, first=True)
        return self

    def add_additional_content(
        self, 
        content: str, 
        override: bool = False, 
        alert_heading: str = ''
    ) -> Self:
        """Appends secondary content, headings, and horizontal rules.

        Args:
            content (str): The HTML or text content to append.
            override (bool): If True, replaces existing content entirely.
            alert_heading (str): Optional text for a stylized heading.

        Returns:
            Self: Enables fluent method chaining.
        """
        processed_content: str = ""
        
        if alert_heading:
            heading = BS5Element('h4', alert_heading, classes=["alert-heading"])
            processed_content += heading.render()
            
        processed_content += content
        
        if override:
            self.template.content = processed_content
        else:
            self.template.content += processed_content
            
        return self

    def before_render(self, **props: Any) -> None:
        """Finalizes the attribute state before the render cycle begins."""
        self.template.attrs = self.attr_manager.root

    def _render_comp(self) -> BS5Element:
        """Assembles the final BS5Element for string conversion."""
        alert: BS5Element = BS5Element(
            self.tag,
            self.content,
            classes=self.alert_classes,
            **self.attrs
        )
        
        if self.is_dismissible:
            close_btn = BS5Element('button', '', classes=['btn-close'])
            close_btn.attr_manager.set_bulk_attr(
                type='button',
                data_bs_dismiss='alert',
                aria_label='Close'
            )
            alert.include(close_btn)
            
        return alert