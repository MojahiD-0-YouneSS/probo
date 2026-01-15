from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Table
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5TableRow(BS5Component):
    def __init__(self,color=None, variant='base',render_constraints=None, **attrs):
        self.render_constraints = render_constraints
        self.attrs = attrs
        self.tag = 'div'
        self.variant=variant
        self.color=color
        self.table_row_classes = []
        if variant.upper() in Table._member_names_:
            self.table_row_classes.append(Table[variant.upper()].value)
        if color and color.upper() in Table._member_names_:
            self.table_row_classes.append(Table[color.upper()].value)
        self.ths=[]
        self.tds=[]

        super().__init__(name='BS5-Table', state_props=self.render_constraints)

    def add_table_head(self,content,colspan=None,**attrs):
        if colspan:
            attrs.update(
            {'colspan': colspan}
        )

        th = BS5Element(
            'th',
            content,
            **attrs)
        self.ths.append(th)
        return self

    def add_table_cel(self,content,colspan=None,**attrs):
        if colspan:
            attrs.update(
            {'colspan': colspan}
        )
        td = BS5Element(
            'td',
            content,
            **attrs)
        self.tds.append(td)
        return self

    def before_render(self, **props):
        self.include_content_parts(*self.ths,*self.tds)

    def _render_comp(self,*args,**kwargs):
        tr = BS5Element(
            'tr',
            classes=self.table_row_classes,
            **self.attrs
        )
        return tr

class BS5Table(BS5Component):
    def __init__(self, caption=None, color=None, variant='base',render_constraints=None, **attrs):
        self.render_constraints = render_constraints
        self.attrs = attrs
        self.caption=caption
        self.tag = 'div'
        self.color=color

        self.variant=variant
        self.table_classes = [Table.TABLE.value]
        if variant.upper() in Table._member_names_:
            self.table_classes.append(Table[variant.upper()].value)
        if color and color.upper() in Table._member_names_:
            self.table_classes.append(Table[color.upper()].value)
        self.thead=None
        self.tbody=None
        self.tfoot=None
        super().__init__(name='BS5-Table', state_props=self.render_constraints)

    def add_table_head(self,*rows:tuple[BS5TableRow],**attrs):
        thead = BS5Element(
            'thead',
            **attrs
        )
        thead.include(*[r.render() for r in rows])
        self.thead=thead
        return self

    def add_table_body(self,*rows:tuple[BS5TableRow],**attrs):
        tbody = BS5Element(
            'tbody',
            **attrs
        )
        tbody.include(*[r.render() for r in rows])
        self.tbody=tbody
        return self

    def add_table_footer(self,*rows:tuple[BS5TableRow],**attrs):
        tfoot = BS5Element(
            'tfoot',
            **attrs
        )
        tfoot.include(*[r.render() for r in rows])
        self.tfoot=tfoot
        return self

    def before_render(self, **props):

        if self.thead:
            self.include_content_parts(self.thead)

        if self.tbody:
            self.include_content_parts(self.tbody)

        if self.tfoot:
            self.include_content_parts(self.tfoot)

    def _render_comp(self,*args,**kwargs):
        table = BS5Element(
            'table',
            classes=self.table_classes,
            **self.attrs
        )
        if self.caption:
            caption=BS5Element(
                'caption',
                self.caption
            )
            table.include(caption)
        return table