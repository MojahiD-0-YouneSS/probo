from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Popover
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Popover(BS5Component):
    """A manager for Bootstrap 5 Popover components.

    Popovers are similar to tooltips but provide a more robust overlay for 
    secondary information. This class handles the specific attribute 
    requirements for both button-based and anchor-based popovers, including 
    automatic accessibility handling (role, tabindex) and the 'wrapper' 
    pattern required for triggering popovers on disabled elements.

    Attributes:
        content (str): The HTML or text content to display inside the popover.
        position (str): The placement of the popover ('top', 'bottom', 'left', 'right').
        tag (str): The HTML tag for the toggle element ('button' or 'a').
        wraper_content (Optional[str]): Content to display in the popover specifically 
            when a wrapper is used (defaults to primary content if None).
        is_wraped (bool): If True, wraps the toggle in a container to allow 
            triggers on disabled or block-level elements.
        wraper_tag (str): The HTML tag for the wrapper container (defaults to 'span').
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Additional HTML attributes for the toggle element.
        wraper (Optional[BS5Element]): The assigned wrapper element if applicable.
    """

    def __init__(
        self, 
        content: str, 
        position: str = 'right', 
        tag: str = 'button', 
        wraper_content: Optional[str] = None, 
        is_wraped: bool = False, 
        wraper_tag: str = 'span', 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the popover with specific trigger and placement logic.

        Args:
            content (str): Text or HTML for the popover body.
            position (str): Directional placement.
            tag (str): Toggle element tag.
            wraper_content (str, optional): Alternative content for wrapped mode.
            is_wraped (bool): Enable wrapper container logic.
            wraper_tag (str): Wrapper container tag.
            render_constraints (dict, optional): Validation properties.
            **attrs (Any): Attributes for the core toggle element.
        """
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.wraper_content: Optional[str] = wraper_content
        self.attrs: Dict[str, Any] = attrs
        self.wraper_tag: str = wraper_tag
        self.is_wraped: bool = is_wraped
        self.content: str = content
        self.tag: str = tag
        self.position: str = position
        self.wraper: Optional[BS5Element] = None
        
        super().__init__(name='BS5-Popover', state_props=self.render_constraints)
        
        if self.tag == 'button':
            self.attr_manager.root = {
                'type': 'button',
                'data-bs-container': 'body',
                'data-bs-toggle': 'popover',
                'data-bs-placement': self.position,
                'data-bs-content': self.content
            }
            
        if self.tag == 'a':
            self.attr_manager.root = {
                'tabindex': '0',
                'role': 'button',
                'data-bs-container': 'body',
                'data-bs-toggle': 'popover',
                'data-bs-placement': self.position,
                'data-bs-content': self.content,
                'data-bs-trigger': 'focus',
            }

    def _add_wraper(self, tag: str = 'span') -> Self:
        """Internal helper to construct the interactive wrapper container.

        This is used to circumvent browser limitations where disabled elements 
        do not trigger mouse events. By wrapping the element in a focusable 
        span/div, the popover remains functional even if the child is disabled.

        Args:
            tag (str): HTML tag for the wrapper.

        Returns:
            Self: Enables fluent method chaining.
        """
        wraper: BS5Element = BS5Element(
            tag,
            classes=['d-inline-block'],
            tabindex=0,
            **{
                'data-bs-trigger': 'hover focus',
                'data-bs-toggle': 'popover',
                'data-bs-content': (self.wraper_content if self.wraper_content else self.content),
            }
        )
        self.wraper = wraper
        return self

    def before_render(self, **props: Any) -> None:
        """Adjusts the SSDOM hierarchy before final rendering.

        If a wrapper is present, the core template is moved inside the wrapper 
        and the wrapper becomes the primary render target. Otherwise, the 
        standard popover attributes are applied to the base template.

        Args:
            **props (Any): Rendering properties.
        """
        if self.wraper:
            self.template = self.wraper.include(self.template)
            self.template.include(self.wraper, override=True)
        else:
            self.template.attrs.update(self.attr_manager.root)

    def _render_comp(self, *args: Any, **kwargs: Any) -> BS5Element:
        """Assembles the final Popover toggle or wrapper element.

        Returns:
            BS5Element: The rendered toggle button, link, or wrapper.
        """
        btn: BS5Element = BS5Element(
            self.tag,
            **self.attrs
        )
        
        if self.is_wraped:
            self._add_wraper(self.wraper_tag if self.wraper_tag else 'span')
            if self.wraper:
                self.wraper.include(btn)
                return self.wraper
                
        return btn