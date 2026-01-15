from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Popover
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Popover(BS5Component):
    def __init__(self,content,position='right',tag='button',wraper_content=None,is_wraped=False,wraper_tag='span', render_constraints=None, **attrs):
        self.render_constraints = render_constraints
        self.wraper_content=wraper_content
        self.attrs = attrs
        self.wraper_tag=wraper_tag
        self.is_wraped=is_wraped
        self.content=content
        self.tag = tag
        self.position=position
        self.wraper=None
        self.progressbar_classes = []
        super().__init__(name='BS5-Popover', state_props=self.render_constraints)
        if self.tag == 'button':
            self.attr_manager.root ={
                'type':'button',
                'data-bs-container':'body',
                'data-bs-toggle':'popover',
                'data-bs-placement':self.position,
                'data-bs-content':self.content
            }
        if self.tag =='a':
            self.attr_manager.root = {
                'tabindex': '0',
                'role':'button',
                'data-bs-container': 'body',
                'data-bs-toggle': 'popover',
                'data-bs-placement': self.position,
                'data-bs-content': self.content,
                'data-bs-trigger':'focus',
            }

    def _add_wraper(self,tag='span',):
        wraper = BS5Element(
            tag,
            classes=['d-inline-block'],
            tabindex=0,
            data_bs_trigger='hover focus',
            data_bs_toggle='popover',
            data_bs_content=(self.wraper_content if self.wraper_content else self.content),

        )
        # wraper.include(self.template)
        # self.template=wraper
        self.wraper = wraper
        return self
    def before_render(self, **props):
        if self.wraper:
            self.template = self.wraper.include(self.template)
            self.template.include(self.wraper,override=True)
        else:
            self.template.attrs.update(self.attr_manager.root)

    def _render_comp(self,*args,**kwargs):
        btn = BS5Element(
            self.tag,**self.attrs
        )
        if self.is_wraped:
            if self.wraper_tag:
                self._add_wraper(self.wraper_tag)
            else:
                self._add_wraper()
            self.wraper.include(btn)
            return self.wraper
        return btn
