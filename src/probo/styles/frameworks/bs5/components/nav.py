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
    
    def __init__(self, *content,render_constraints=None,is_tab=False,is_fill=False,is_pill=False,is_justified=False, **attrs):
        self.attrs = attrs
        self.render_constraints=render_constraints
        self.content=''.join(content)
        self.nav_items=list()
        self.is_tab=is_tab
        # self.template = self._render_comp()
        self.is_fill = is_fill
        self.is_pill = is_pill
        self.is_justified = is_justified
        self.nav_classes = [Nav.NAV.value]
        self.tag = 'ul'
        if self.is_tab:
            self.nav_classes.append(Nav.NAV_TABS.value)
        if self.is_justified:
            self.nav_classes.append(Nav.NAV_JUSTIFYIED.value)
        if self.is_pill:
            self.nav_classes.append(Nav.NAV_PILLS.value)
        if self.is_fill:
            self.nav_classes.append(Nav.NAV_FILL.value)
        super().__init__(name='BS5-nav', state_props=self.render_constraints)

    def add_nav_item(self,content,tag='li',**attrs):
        item = BS5Element(
                tag,
                content,classes=['nav-item'],**attrs)
        self.nav_items.append(item)
        return self
    def add_nav_link(self,content,active=False,**attrs):
        item = BS5Element(
                'a',
                content,classes=['nav-link',],**attrs
        )
        item.attr_manager.set_bulk_attr(

        )
        if active:
            item.classes.append('active')
            item.attr_manager.set_attr('aria-current',"page")
        if attrs.get('Class',None) and 'disabled' in attrs['Class']:
            item.attr_manager.set_attr('aria-disabled',"true")
        self.nav_items.append(item)
        return self
    def before_render(self, **props):
        self.include_content_parts(*self.nav_items)

    def _render_comp(self):
        nav = BS5Element(
            self.tag,
            self.content,
            classes=self.nav_classes,**self.attrs
        )
        return nav
