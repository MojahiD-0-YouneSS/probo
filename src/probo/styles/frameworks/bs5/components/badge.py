from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element
from probo.styles.frameworks.bs5.utilities import Background


class BS5Badge(BS5Component):
    def __init__(self, content, variant="primary", **attrs):
        self.variant = variant
        self.attrs = attrs
        self.content=content
        # self.template = self._render_comp()
        self.badge_classes = ['badge', Background[self.variant.upper()].value]
        self.tag = 'span'
        super().__init__(name='BS5-badge', props={}, state=None)

    def add_heading_badge(self,heading_content,heading='h1',**attrs):
        '''<h1>Example heading <span class="badge bg-secondary">New</span></h1>'''
        heading_comp = BS5Element(
            heading,heading_content,**attrs
        )
        self.template=heading_comp.include(self.template)
        return self
    def _render_comp(self):
        badge = BS5Element(
            self.tag,
            self.content,
            classes=self.badge_classes,**self.attrs
        )
        return badge
