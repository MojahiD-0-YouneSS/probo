from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Spinner
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Spinner(BS5Component):
    def __init__(self, content,variant='border',render_constraints=None, **attrs):
        self.render_constraints = render_constraints
        self.attrs = attrs
        self.variant=variant
        self.content=content
        self.tag = 'div'
        self.spinner_classes = [(Spinner.SPINNER_GROW.value if self.variant =='grow' else Spinner.SPINNER_BORDER.value)]
        super().__init__(name='BS5-Spinner', state_props=self.render_constraints)

    def _render_comp(self,*args,**kwargs):
        spinner = BS5Element(
            self.tag,
            classes=self.spinner_classes,
           role='status',
        )
        spinner.attr_manager.set_bulk_attr(**self.attrs)
        if self.content:
            spinner_content = BS5Element('span',self.content,classes=['visually-hidden'])
            spinner.include(spinner_content)
        return spinner
