from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element
from probo.styles.frameworks.bs5.utilities import Background


class BS5Badge(BS5Component):
    def __init__(self, content, variant="primary",render_constraints=None, **attrs):
        self.variant = variant
        self.attrs = attrs
        self.render_constraints=render_constraints or{}
        self.content=content
        # self.template = self._render_comp()
        self.badge_classes = ['badge', Background[self.variant.upper()].value]
        self.tag = 'span'
        super().__init__(name='BS5-badge', state_props=self.render_constraints)

    def _add_parent_badge(self,content,tag,**attrs):
        '''<h1>Example heading <span class="badge bg-secondary">New</span></h1>'''
        comp = BS5Element(
            tag,content,**attrs
        )
        comp.include(self.template)
        self.template.include(comp,override=True)
        return self
    def add_heading_badge(self,heading_content,heading='h1',**attrs):
        '''<h1>Example heading <span class="badge bg-secondary">New</span></h1>'''
        self._add_parent_badge(heading_content,tag=heading,**attrs)
        return self
    def add_button_badge(self,button_content,tag='button',**attrs):
        '''<h1>Example heading <span class="badge bg-secondary">New</span></h1>'''
        self._add_parent_badge(button_content, tag=tag, **attrs)
        return self
    def _render_comp(self):
        badge = BS5Element(
            self.tag,
            self.content,
            classes=self.badge_classes,**self.attrs
        )
        return badge
