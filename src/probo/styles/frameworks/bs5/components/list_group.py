from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Lists
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5ListGroup(BS5Component):
    '''
    
    ''' 
    
    def __init__(self, *items,content, **attrs):
        self.attrs = attrs
        self.content=content
        # self.template = self._render_comp()
        self.items=list(items)
        self.list_classes = [Lists.LIST_GROUP.value]
        self.tag = 'ul'
        super().__init__(name='BS5-button', props={}, state=None)

    def add_list_item(self, content, tag='li', **attrs):
        item = BS5Element(
            tag,
            content,
            classes=[Lists.LIST_GROUP_ITEM.value],
            **attrs
        )
        self.items.append(item.render())
        return self
    def element_as_btn(self,tag):
        self.tag = tag
        self.template.tag=tag
        return self
    
    def _render_comp(self):
        list_group = BS5Element(
            self.tag,
            ''.join(self.items),
            classes=self.list_classes,**self.attrs
        )
        return list_group
