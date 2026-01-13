from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element
from probo.styles.frameworks.bs5.comp_enum import Breadcrumb

class BS5Breadcrumb(BS5Component):
    '''
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item active "aria-current="page"><a href="#">Home</a></li>
            <li class="breadcrumb-item"><a href="#">Library</a></li>
            <li class="breadcrumb-item " >Data</li>
        </ol>
    </nav>
    '''
    def __init__(self, *urls,**attrs):
        self.attrs = attrs
        self.urls=urls
        # self.template = self._render_comp()
        self.breadcrum_classes = [Breadcrumb.BASE.value]
        self.tag = 'ol'
        self.nav_attrs={'aria-label': "breadcrumb"}
        super().__init__(name='BS5-breadcrum', props={}, state=None)
    
     
    def element_as_btn(self,tag):
        self.tag = tag
        self.template.tag=tag
        return self
    
    def _render_comp(self):
        if self.urls:
            links = [ BS5Element(
                'li',link,
                classes=[Breadcrumb.ITEM.value],
            ) for link in self.urls]
            links[0].classes.append('active')
            links[0].attrs.update({'aria-current':"page"})
        else:
            links = []
        button = BS5Element(
            self.tag,
            classes=self.breadcrum_classes,**self.attrs
        )
        btn.include(links)
        nav = BS5Element(
            'nav',
            **self.nav_attrs
        )
        return nav.include(button)
