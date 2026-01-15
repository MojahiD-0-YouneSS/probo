from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Navbar
from probo.styles.frameworks.bs5.bs5 import BS5Element
class BS5NavBar(BS5Component):
    ''' 

    
    '''
    
    def __init__(self, *content,render_constraints=None, **attrs):
        self.attrs = attrs
        self.render_constraints=render_constraints
        self.content=''.join(content)
        self.navbar_items=list()
        # self.template = self._render_comp()
        self.navbar_classes = [Navbar.NAVBAR.value]
        self.tag = 'nav'
        super().__init__(name='BS5-NavBar', state_props=self.render_constraints)
        self.attr_manager.root = {}

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

    def before_render(self, **props):
        self.include_content_parts(*self.navbar_items)

    def _render_comp(self):
        nav = BS5Element(
            self.tag,
            self.content,
            classes=self.navbar_classes,**self.attrs
        )
        return nav
