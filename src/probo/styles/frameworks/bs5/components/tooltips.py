from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.utilities import Tooltip
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Tooltips(BS5Component):
    """
    Bootstrap 5 Tooltip component.
    Actually creates the *trigger* element (usually a button or link)
    that displays the tooltip on hover/focus.
    """

    def __init__(self, content, title, placement="top", tag="button", render_constraints=None, **attrs):
        self.render_constraints = render_constraints
        self.attrs = attrs
        self.tag = tag
        self.content=content
        self.title=title
        self.placement = placement
        self.tooltips_classes = []
        super().__init__(name='BS5-Tooltips', state_props=self.render_constraints)

    def _render_comp(self):
        # Base BS5Component logic expects this to return the BS5Element to render
        tooltip_attrs = {
            'data-bs-toggle': 'tooltip',
            'data-bs-placement': self.placement,
            'title': self.title,
            # Accessible name if not provided
        }
        if self.tag == 'button':
            tooltip_attrs['type']= 'button'

        root = BS5Element(self.tag, self.content,classes=self.tooltips_classes, **tooltip_attrs)
        root.attr_manager.set_bulk_attr(**self.attrs)
        return root
