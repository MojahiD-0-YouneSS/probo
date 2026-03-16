from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Table
from probo.styles.frameworks.bs5.bs5 import BS5Element

from typing import Any, Dict, List, Optional, Self, Union, Iterable

class BS5TableRow(BS5Component):
    """A manager for Bootstrap 5 Table Row (<tr>) components.

    This class facilitates the construction of table rows by managing a 
    collection of header cells (<th>) and data cells (<td>). It supports 
    contextual coloring and variants via the internal Table enum registry 
    and ensures structural integrity during the SSDOM render cycle.

    Attributes:
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Additional HTML attributes for the <tr> element.
        tag (str): The internal placeholder tag (defaults to 'div').
        variant (str): The table variant identifier.
        color (Optional[str]): Contextual color utility name.
        table_row_classes (List[str]): Resolved CSS classes for the row.
        ths (List[BS5Element]): Collection of header cell elements.
        tds (List[BS5Element]): Collection of data cell elements.
    """

    def __init__(
        self, 
        color: Optional[str] = None, 
        variant: str = 'base', 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the table row with variant and color logic.

        Args:
            color (str, optional): BS5 contextual color (e.g., 'primary').
            variant (str): Table variant style (e.g., 'striped').
            render_constraints (dict, optional): State validation properties.
            **attrs (Any): Additional attributes for the row element.
        """
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.attrs: Dict[str, Any] = attrs
        self.tag: str = 'div'
        self.variant: str = variant
        self.color: Optional[str] = color
        self.table_row_classes: List[str] = []
        
        if variant.upper() in Table._member_names_:
            self.table_row_classes.append(Table[variant.upper()].value)
            
        if color and color.upper() in Table._member_names_:
            self.table_row_classes.append(Table[color.upper()].value)
            
        self.ths: List[BS5Element] = []
        self.tds: List[BS5Element] = []

        super().__init__(name='BS5-Table', state_props=self.render_constraints)

    def add_table_head(
        self, 
        content: Any, 
        colspan: Optional[Union[int, str]] = None, 
        **attrs: Any
    ) -> Self:
        """Constructs and appends a header cell (<th>) to the row.

        Args:
            content (Any): The text or HTML content for the cell.
            colspan (int | str, optional): Number of columns the cell should span.
            **attrs (Any): Additional attributes for the <th> element.

        Returns:
            Self: Enables fluent method chaining.
        """
        if colspan:
            attrs.update({'colspan': colspan})

        th: BS5Element = BS5Element(
            'th',
            content,
            **attrs
        )
        self.ths.append(th)
        return self

    def add_table_cel(
        self, 
        content: Any, 
        colspan: Optional[Union[int, str]] = None, 
        **attrs: Any
    ) -> Self:
        """Constructs and appends a data cell (<td>) to the row.

        Args:
            content (Any): The text or HTML content for the cell.
            colspan (int | str, optional): Number of columns the cell should span.
            **attrs (Any): Additional attributes for the <td> element.

        Returns:
            Self: Enables fluent method chaining.
        """
        if colspan:
            attrs.update({'colspan': colspan})
            
        td: BS5Element = BS5Element(
            'td',
            content,
            **attrs
        )
        self.tds.append(td)
        return self

    def before_render(self, **props: Any) -> None:
        """Aggregates all cells into the component before rendering."""
        self.include_content_parts(*self.ths, *self.tds)

    def _render_comp(self, *args: Any, **kwargs: Any) -> BS5Element:
        """Assembles the final <tr> SSDOM element.

        Returns:
            BS5Element: The rendered table row element.
        """
        tr: BS5Element = BS5Element(
            'tr',
            classes=self.table_row_classes,
            **self.attrs
        )
        return tr

class BS5Table(BS5Component):
    """A high-level manager for Bootstrap 5 Table components.

    This class coordinates the assembly of a full HTML table, including 
    captions, headers (<thead>), bodies (<tbody>), and footers (<tfoot>). 
    It enforces Bootstrap 5 utility patterns for striped, hovered, and 
    bordered variations.

    Attributes:
        render_constraints (Optional[Dict[str, Any]]): State validation schema.
        attrs (Dict[str, Any]): Attributes for the root <table> element.
        caption (Optional[str]): Table caption text.
        tag (str): Internal placeholder tag (defaults to 'div').
        color (Optional[str]): Contextual color utility for the table.
        variant (str): Table variant style.
        table_classes (List[str]): Resolved CSS classes for the table.
        thead (Optional[BS5Element]): The rendered header section.
        tbody (Optional[BS5Element]): The rendered body section.
        tfoot (Optional[BS5Element]): The rendered footer section.
    """

    def __init__(
        self, 
        caption: Optional[str] = None, 
        color: Optional[str] = None, 
        variant: str = 'base', 
        render_constraints: Optional[Dict[str, Any]] = None, 
        **attrs: Any
    ) -> None:
        """Initializes the table with global styling and captions."""
        self.render_constraints: Optional[Dict[str, Any]] = render_constraints
        self.attrs: Dict[str, Any] = attrs
        self.caption: Optional[str] = caption
        self.tag: str = 'div'
        self.color: Optional[str] = color

        self.variant: str = variant
        self.table_classes: List[str] = [Table.TABLE.value]
        
        if variant.upper() in Table._member_names_:
            self.table_classes.append(Table[variant.upper()].value)
            
        if color and color.upper() in Table._member_names_:
            self.table_classes.append(Table[color.upper()].value)
            
        self.thead: Optional[BS5Element] = None
        self.tbody: Optional[BS5Element] = None
        self.tfoot: Optional[BS5Element] = None
        
        super().__init__(name='BS5-Table', state_props=self.render_constraints)

    def add_table_head(self, *rows: BS5TableRow, **attrs: Any) -> Self:
        """Constructs and assigns the <thead> section.

        Args:
            *rows (BS5TableRow): Variadic list of row components for the header.
            **attrs (Any): Additional attributes for the <thead> tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        thead: BS5Element = BS5Element(
            'thead',
            **attrs
        )
        thead.include(*[r.render() for r in rows])
        self.thead = thead
        return self

    def add_table_body(self, *rows: BS5TableRow, **attrs: Any) -> Self:
        """Constructs and assigns the <tbody> section.

        Args:
            *rows (BS5TableRow): Variadic list of row components for the body.
            **attrs (Any): Additional attributes for the <tbody> tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        tbody: BS5Element = BS5Element(
            'tbody',
            **attrs
        )
        tbody.include(*[r.render() for r in rows])
        self.tbody = tbody
        return self

    def add_table_footer(self, *rows: BS5TableRow, **attrs: Any) -> Self:
        """Constructs and assigns the <tfoot> section.

        Args:
            *rows (BS5TableRow): Variadic list of row components for the footer.
            **attrs (Any): Additional attributes for the <tfoot> tag.

        Returns:
            Self: Enables fluent method chaining.
        """
        tfoot: BS5Element = BS5Element(
            'tfoot',
            **attrs
        )
        tfoot.include(*[r.render() for r in rows])
        self.tfoot = tfoot
        return self

    def before_render(self, **props: Any) -> None:
        """Organizes table sections (head, body, foot) before final rendering."""
        if self.thead:
            self.include_content_parts(self.thead)

        if self.tbody:
            self.include_content_parts(self.tbody)

        if self.tfoot:
            self.include_content_parts(self.tfoot)

    def _render_comp(self, *args: Any, **kwargs: Any) -> BS5Element:
        """Assembles the final <table> SSDOM element.

        Returns:
            BS5Element: The rendered table element.
        """
        table: BS5Element = BS5Element(
            'table',
            classes=self.table_classes,
            **self.attrs
        )
        
        if self.caption:
            caption_el: BS5Element = BS5Element(
                'caption',
                self.caption
            )
            table.include(caption_el)
            
        return table