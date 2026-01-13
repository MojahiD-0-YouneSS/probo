from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Navbar
from probo.styles.frameworks.bs5.bs5 import BS5Element
class BS5NavBar(BS5Component):
    ''' 

    
    '''
    
    def __init__(self, *content, **attrs):
        self.attrs = attrs
        self.content=''.join(content)
        self.navbar_items=list()
        # self.template = self._render_comp()
        self.btn_classes = [Navbar.BASE.value]
        self.tag = 'nav'
        super().__init__(name='BS5-Nav', props={}, state=None)

    def add_navbar_brand(self,content,tag='div',**attrs):
        
        item = BS5Element(
                tag,
                content,classes=['navbar-brand'],**attrs)
        self.navbar_items.append(BS5Element('div',classes=['container-fluid']).include(item,).render())
        return self
    def add_navbar_text(self,content,tag='span',**attrs):
        item = BS5Element(
                tag,
                content,classes=['navbar-text'],**attrs)
        self.navbar_items.append(BS5Element('div',classes=['container-fluid']).include(item,).render())
        return self
    
    def _render_comp(self):
        button = BS5Element(
            self.tag,
            self.content,
            classes=self.btn_classes,**self.attrs
        )
        return button
