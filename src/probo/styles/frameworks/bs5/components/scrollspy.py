from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Scrollspy
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Scrollspy(BS5Component):
    def __init__(self, target,render_constraints=None, **attrs):
        self.render_constraints = render_constraints
        self.attrs = attrs
        self.target=target
        self.tag = 'div'
        self.scrollpy_items = []
        self.scrollpy_classes = [Scrollspy.SCROLLSPY.value]
        super().__init__(name='BS5-Scrollspy', state_props=self.render_constraints)

    def add_scrollpy_item(self,item_id,content,tag='div',**attrs):
        scroll = BS5Element(
            tag,content,Id=item_id,**attrs)
        self.scrollpy_items.append(scroll)
        return self

    def before_render(self, **props):
        self.include_content_parts(*self.scrollpy_items)

    def _render_comp(self,*args,**kwargs):
        scroll = BS5Element(
            self.tag,
            data_bs_spy="scroll",
            data_bs_target=self.target,
            data_bs_offset=0,
            tabindex=0,
        )
        scroll.attr_manager.set_bulk_attr(**self.attrs)
        return scroll
