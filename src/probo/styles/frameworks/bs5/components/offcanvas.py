from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import offcanvas
from probo.styles.frameworks.bs5.bs5 import BS5Element
class BS5Offcanvas(BS5Component):
    ''' <ul class="offcanvas offcanvas-pills">
            <li class="offcanvas-item">
                <a class="offcanvas-link active" aria-current="page" href="#">Active</a>
            </li>
        </ul>
    '''
    
    def __init__(self, *content, **attrs):
        self.attrs = attrs
        self.content=''.join(content)
        self.offcanvas_items=list()
        # self.template = self._render_comp()
        self.btn_classes = [offcanvas.BASE.value]
        self.tag = 'ul'
        super().__init__(name='BS5-offcanvas', props={}, state=None)

    def add_offcanvas_header(self,content,tag='li',**attrs):
        item = BS5Element(
                tag,
                content,classes=['offcanvas-item'],**attrs)
        self.offcanvas_items.append(item)
        return self
    def add_offcanvas_body(self,content,**attrs):
        item = BS5Element(
                'a',
                content,classes=['offcanvas-link'],**attrs)
        self.offcanvas_items.append(item)
        return self
    
    def _render_comp(self):
        button = BS5Element(
            self.tag,
            self.content,
            classes=self.btn_classes,**self.attrs
        )
        return button

