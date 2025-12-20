from mui import (
    span,
)
from mui.styles.frameworks.bs5.utilities import Background


class DefaultBadge:
    def __init__(self, content=None, bg_color='primary'):
        self.content = content
        self.bg_color = bg_color.upper()
    
    
    def render(self,):
        return span(
            self.content,
            Class=f'badge {Background[self.bg_color].value}'
        )

DefaultBadgeObject = DefaultBadge

