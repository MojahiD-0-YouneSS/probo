from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Lists
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5ListGroup(BS5Component):
    '''
    
    ''' 
    
    def __init__(self, *items,content,render_constraints=None, **attrs):
        self.attrs = attrs
        self.content=content
        self.render_constraints=render_constraints
        # self.template = self._render_comp()
        self.items=list(items)
        self.list_classes = [Lists.LIST_GROUP.value]
        self.tag = 'ul'
        super().__init__(name='BS5-button', state_props=self.render_constraints)

    def add_list_item(self, content, tag='li',return_item=False, **attrs):
        item = BS5Element(
            tag,
            content,
            classes=[Lists.LIST_GROUP_ITEM.value,('list-group-item-action' if tag=='a' else '')],
            **attrs
        )
        if return_item:
            return item
        else:
            self.items.append(item.render())
        return self
    def before_render(self,**prop):
        self.include_content_parts(*self.items)
        return self
    
    def _render_comp(self):
        if self.items:
            self.items = [self.add_list_item(item,return_item=True).render() for item in self.items]
        list_group = BS5Element(
            self.tag,
            ''.join(self.items),
            classes=self.list_classes,**self.attrs
        )
        return list_group
