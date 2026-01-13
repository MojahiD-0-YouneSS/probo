from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Nav
from probo.styles.frameworks.bs5.bs5 import BS5Element
class BS5Nav(BS5Component):
    ''' <ul class="nav nav-pills">
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
            </li>
        </ul>
    '''
    
    def __init__(self, *content, **attrs):
        self.attrs = attrs
        self.content=''.join(content)
        self.nav_items=list()
        # self.template = self._render_comp()
        self.btn_classes = [Nav.BASE.value]
        self.tag = 'ul'
        super().__init__(name='BS5-nav', props={}, state=None)

    def add_nav_item(self,content,tag='li',**attrs):
        item = BS5Element(
                tag,
                content,classes=['nav-item'],**attrs)
        self.nav_items.append(item)
        return self
    def add_nav_link(self,content,**attrs):
        item = BS5Element(
                'a',
                content,classes=['nav-link'],**attrs)
        self.nav_items.append(item)
        return self
    
    def _render_comp(self):
        button = BS5Element(
            self.tag,
            self.content,
            classes=self.btn_classes,**self.attrs
        )
        return button
