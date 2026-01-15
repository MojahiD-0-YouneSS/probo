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
    def __init__(self, *urls,url_dict=None,render_constraints=None,**attrs):
        self.url_dict:dict=url_dict or {}
        self.attrs = attrs
        self.urls=urls
        self.render_constraints=render_constraints or {}
        # self.template = self._render_comp()
        self.breadcrum_classes = [Breadcrumb.BASE.value]
        self.tag = 'ol'
        self.nav_attrs={'aria-label': "breadcrumb"}
        super().__init__(name='BS5-breadcrum', state_props=self.render_constraints)

    def _render_comp(self):
        links_dict = {}
        if self.urls:
            links_dict = {link:'#' for link in self.urls[0:-1]}
        if self.url_dict:
            links_dict = self.url_dict
        if links_dict:

            links = [ BS5Element(
                'li',BS5Element(
                    'a',link_name,href=link_url).render(),
                classes=[Breadcrumb.ITEM.value],
            ) for link_name,link_url in links_dict.items()]
            links.append(
                BS5Element(
                    'li', self.urls[-1],
                    classes=[Breadcrumb.ITEM.value],
                )
            )
            links[-1].classes.append('active')
            links[-1].attrs.update({'aria-current': "page"})
        else:
            links = []
        breadcrum = BS5Element(
            self.tag,
            classes=self.breadcrum_classes, **self.attrs
        )
        breadcrum.include(*links)
        nav = BS5Element(
            'nav',
            **self.nav_attrs
        )
        return nav.include(breadcrum)
