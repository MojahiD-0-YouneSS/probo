from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Pagination
from probo.styles.frameworks.bs5.bs5 import BS5Element
from typing import Any, Dict, List, Optional, Self, Union

class BS5Pagination(BS5Component):
    """A manager for Bootstrap 5 Pagination components.

    Pagination is used to indicate a series of related content exists across
    multiple pages. This class handles the construction of the navigation
    wrapper, the unordered list of page items, and the contextual 'Previous'
    and 'Next' controls.

    Attributes:
        attrs (Dict[str, Any]): Attributes for the root <nav> element.
        pagination_items (List[BS5Element]): Collection of rendered page items.
        position (str): Horizontal alignment ('start', 'center', 'end').
        pagination_classes (List[str]): Resolved CSS classes for the <ul> element.
        prev_item (Optional[BS5Element]): The element for the 'Previous' control.
        next_item (Optional[BS5Element]): The element for the 'Next' control.
        tag (str): The HTML tag for the root container (defaults to 'div').
    """

    def __init__(
        self,
        *items: Any,
        position: str = "start",
        render_constraints: Optional[Dict[str, Any]] = None,
        **attrs: Any,
    ) -> None:
        """Initializes the pagination with items and alignment logic.

        Args:
            *items (Any): Initial labels or elements to be used as page numbers.
            position (str): Alignment of the pagination block.
            render_constraints (dict, optional): State validation properties.
            **attrs (Any): Attributes for the root <nav> tag.
        """
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.attrs: Dict[str, Any] = attrs
        self.pagination_items: List[BS5Element] = [
            self._normalize_bare_items(item) for item in items
        ]
        self.position: str = position
        self.tag: str = "div"

        self.pagination_classes = [Pagination.PAGINATION.value]

        if position == "end":
            self.pagination_classes.append("justify-content-end")
        elif position == "center":
            self.pagination_classes.append("justify-content-center")

        self.prev_item: Optional[BS5Element] = None
        self.next_item: Optional[BS5Element] = None

        super().__init__(name="BS5-Pagination", state_props=self.render_constraints)

    @property
    def lg(self) -> Self:
        """Upgrades the pagination to large size.

        Returns:
            Self: Enables fluent method chaining.
        """
        self.pagination_classes.append(Pagination.PAGINATION_LG.value)
        self.template.classes.append(Pagination.PAGINATION_LG.value)
        return self

    @property
    def sm(self) -> Self:
        """Downgrades the pagination to small size.

        Returns:
            Self: Enables fluent method chaining.
        """
        self.pagination_classes.append(Pagination.PAGINATION_SM.value)
        self.template.classes.append(Pagination.PAGINATION_SM.value)
        return self

    def _normalize_bare_items(self, item: Any,url='#') -> BS5Element:
        """Wraps raw content into a standard BS5 page-item structure.

        Args:
            item (Any): The content (usually a number or string) for the page link.

        Returns:
            BS5Element: A structured <li> containing the <a> page link.
        """
        return BS5Element(
            "li",
            BS5Element(
                "a",
                item,
                classes=[Pagination.PAGE_LINK.value],
                href=url,
            ),
            classes=[Pagination.PAGE_ITEM.value],
        )

    def add_page_item(self, **content_link: str) -> Self:
        """Adds multiple page items via keyword arguments.

        Args:
            **content_link (str): Key-value pairs where key is the label
                and value is the target URL.

        Returns:
            Self: Enables fluent method chaining.
        """
        items: List[BS5Element] = [
            self._normalize_bare_items(content,url)
            for content, url in content_link.items()
        ]
        self.pagination_items.extend(items)
        return self

    def add_controls(
        self,
        prev_content: str = "Previous",
        prev_link: str = "#",
        next_content: str = "Next",
        next_link: str = "#",
    ) -> Self:
        """Defines the navigation controls for the pagination block.

        Args:
            prev_content (str): Label for the previous button.
            prev_link (str): URL for the previous button.
            next_content (str): Label for the next button.
            next_link (str): URL for the next button.

        Returns:
            Self: Enables fluent method chaining.
        """

        prev: BS5Element = BS5Element(
            "li",
            BS5Element("a", prev_content, classes=["page-link"], href=prev_link),
            classes=["page-item"],
        )
        nxt: BS5Element = BS5Element(
            "li",
            BS5Element("a", next_content, classes=["page-link"], href=next_link),
            classes=["page-item"],
        )
        self.prev_item = prev
        self.next_item = nxt
        return self

    def before_render(self, **props: Any) -> None:
        """Pre-processes the component structure before final rendering.

        This method configures the template as a <nav> element and assembles
         the inner <ul> with all items and controls.
        """
        ul: BS5Element = BS5Element("ul", classes=self.pagination_classes)
        ul.include(self.prev_item, *self.pagination_items, self.next_item)
        self.template.content = ""
        self.template.tag = "nav"
        self.template.attrs = self.attrs
        self.template.classes.clear()
        self.include_content_parts(ul)

    def _render_comp(self, *args: Any, **kwargs: Any) -> BS5Element:
        """Assembles the finalized pagination list element.

        Returns:
            BS5Element: The <ul> element containing the pagination items.
        """
        self.add_controls()

        ul: BS5Element = BS5Element("ul", classes=self.pagination_classes)
        return ul
