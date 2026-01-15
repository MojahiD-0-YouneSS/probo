from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Pagination
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Pagination(BS5Component):

    def __init__(self,*items,position='start',render_constraints=None,**attrs):
        self.render_constraints=render_constraints
        self.attrs=attrs
        self.pagination_items = [self._normalize_bare_items(item) for item in items]
        self.position=position
        self.tag = 'div'
        self.pagination_classes = [Pagination.PAGINATION.value]
        if position == 'end':
            self.pagination_classes.append('justify-content-end')
        if position == 'center':
            self.pagination_classes.append('justify-content-center')
        self.prev_item = None
        self.next_item = None
        super().__init__(name='BS5-Pagination',state_props=self.render_constraints)

    @property
    def lg(self):
        self.pagination_classes.append(Pagination.PAGINATION_LG.value)
        return self

    @property
    def sm(self):
        self.pagination_classes.append(Pagination.PAGINATION_SM.value)
        return self

    def _normalize_bare_items(self,item):
        return BS5Element(
            'li',BS5Element(
                'a',item,classes=[Pagination.PAGE_LINK.value],href='#',
            ) ,classes=[Pagination.PAGE_ITEM.value]
        )

    def add_page_item(self,**content_link):
        items = [BS5Element(
            'li',BS5Element(
                'a',content,classes=[Pagination.PAGE_LINK.value],href=url,
            ) ,classes=[Pagination.PAGE_ITEM.value]
        )for content,url in content_link.items()]
        self.pagination_items.extend(items)
        return self
    def add_controls(self,prev_conten='Previous',prev_link='#',next_conten='Next',next_link='#',):
        prev = BS5Element(
            'li',BS5Element('a',prev_conten,classes=[Pagination.PAGE_LINK.value],href=prev_link)
            , classes=[Pagination.PAGE_ITEM.value]
        )
        nxt = BS5Element(
            'li',BS5Element('a',next_conten,classes=[Pagination.PAGE_LINK.value],href=next_link)
            , classes=[Pagination.PAGE_ITEM.value]
        )
        self.prev_item = prev
        self.next_item = nxt
        return self
    def before_render(self, **props):
        ul = BS5Element(
            'ul',
            classes=self.pagination_classes
        )
        ul.include(self.prev_item, *self.pagination_items, self.next_item)
        self.template.content=''

        self.template.tag='nav'
        self.template.attrs=self.attrs
        self.template.classes.clear()

        self.include_content_parts(ul)

    def _render_comp(self,*args,**kwargs):
        self.add_controls()
        ul = BS5Element(
            'ul',
            classes=self.pagination_classes
        )
        return ul