from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Collapse
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Collapse(BS5Component):
    
    def __init__(self,content, is_multicollapse=False, render_constraints=None, **attrs):
        self.attrs = attrs
        self.render_constraints=render_constraints
        self.content = content 
        # self.template = self._render_comp()
        self.collapse_classes = [Collapse.COLLAPSE.value,(Collapse.COLLAPSE_MULTI.value if is_multicollapse else '')]
        self.trigger=None
        self.tag = 'div'
        super().__init__(name='BS5-collapse',state_props=self.render_constraints)
    def add_link_trigger(self,content,classes,**attrs):
        link = BS5Element(
            'a',
            content,
            classes=classes,       
            data_bs_toggle="collapse",
            href=f"#{self.attrs.get('Id','')}",
            role="button",
            aria_expanded="false",
            aria_controls=self.attrs.get('Id',''),
            )
        self.trigger=link
        return self
    def add_button_trigger(self,content,classes,**attrs):
        btn = BS5Element(
            'button',
            content,
            classes=classes,       
            data_bs_toggle="collapse",
            Type="button",
            data_bs_target=f"#{self.attrs.get('Id','')}",
            role="button",
            aria_expanded="false",
            aria_controls=self.attrs.get('Id',''),
            )
        self.trigger=btn
        return self
    def _render_comp(self):
        collapse = BS5Element(
            self.tag,
            self.content,
            classes=self.collapse_classes,**self.attrs
        )
        return collapse
