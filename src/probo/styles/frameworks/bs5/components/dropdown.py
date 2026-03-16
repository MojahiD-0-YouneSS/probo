from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Dropdowns
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union


class BS5Dropdown(BS5Component):
    """A manager for Bootstrap 5 Dropdown components.

    Dropdowns are toggleable, contextual overlays for displaying lists of links
    and more. This class manages the relationship between the toggle element
    (button or link) and the menu container, supporting standard dropdowns,
    button groups, and split-button variations.

    Attributes:
        attrs (Dict[str, Any]): Attributes for the dropdown container.
        is_btn_group (bool): If True, uses 'btn-group' class instead of 'dropdown'.
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        dropdown_btn (Optional[str]): Rendered string of the toggle button.
        escape_btn (bool): If True, prevents automatic inclusion of the button
            in the before_render cycle.
        dropdown_menu (Optional[str]): Rendered string of the menu container.
        tag (str): The HTML tag for the container (defaults to 'div').
    """

    def __init__(
        self,
        render_constraints: Optional[Dict[str, Any]] = None,
        is_btn_group: bool = False,
        escape_btn: bool = False,
        **attrs: Any,
    ) -> None:
        """Initializes the dropdown container with behavioral logic."""
        self.attrs: Dict[str, Any] = attrs
        self.is_btn_group: bool = is_btn_group
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.dropdown_btn: Optional[str] = None
        self.escape_btn: bool = escape_btn
        self.dropdown_menu: Optional[str] = None
        self.tag: str = "div"

        super().__init__(name="BS5-dropdown", state_props=self.render_constraints)

    def add_btn(self, content: Any, **attrs: Any) -> Self:
        """Creates and assigns the dropdown toggle button.

        Args:
            content (Any): The text or HTML to display inside the button.
            **attrs (Any): Additional attributes for the button element.

        Returns:
            Self: Enables fluent method chaining.
        """
        btn_attrs={
            "type": "button",
            "data-bs-toggle": "dropdown",
            "aria-expanded": "false",
        }
        btn_attrs.update(attrs)
        btn: BS5Element = BS5Element(
            "button",
            content,
            classes=["dropdown-toggle"],
            **btn_attrs,
        )
        self.dropdown_btn = btn.render()
        return self

    def add_menu(
        self,
        *items_content: Any,
        items_attrs: Optional[Dict[int, Dict[str, Any]]] = None,
        **attrs: Any,
    ) -> Self:
        """Constructs the dropdown menu and its child items.

        Args:
            *items_content (Any): Variadic list of contents for each menu item.
            items_attrs (Dict[int, Dict[str, Any]], optional): Attribute mappings
                where the key is the index of the item.
            **attrs (Any): Attributes for the 'ul' menu container.

        Returns:
            Self: Enables fluent method chaining.
        """
        menu: BS5Element = BS5Element("ul", classes=["dropdown-menu"], **attrs)

        items: List[BS5Element] = []
        for indx, content in enumerate(items_content):
            specific_attrs: Dict[str, Any] = {}
            if items_attrs and indx in items_attrs:
                specific_attrs = items_attrs[indx]

            item: BS5Element = BS5Element(
                "li", content, classes=["dropdown-item"], **specific_attrs
            )
            items.append(item)

        menu.include(*items)
        self.dropdown_menu = menu.render()
        return self

    def before_render(self, **props: Any) -> None:
        """Handles structural inclusion before the component is finalized.

        Args:
            **props (Any): Rendering properties passed from the engine.
        """
        if self.dropdown_btn and not self.escape_btn:
            self.include_content_parts(self.dropdown_btn, first=True)

        if self.dropdown_menu:
            self.include_content_parts(self.dropdown_menu)

    def _render_comp(self) -> BS5Element:
        """Assembles the final dropdown SSDOM element.

        Returns:
            BS5Element: The fully constructed dropdown container.
        """
        container_class: str = "btn-group" if self.is_btn_group else "dropdown"

        dropdown: BS5Element = BS5Element(
            self.tag, classes=[container_class], **self.attrs
        )

        if self.dropdown_btn:
            dropdown.include(self.dropdown_btn)

        if self.dropdown_menu:
            dropdown.include(self.dropdown_menu)

        return dropdown
