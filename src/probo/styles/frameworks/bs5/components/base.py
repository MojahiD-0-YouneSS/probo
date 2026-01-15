from probo.components.component import Component
from probo.components.state.component_state import ComponentState
from typing import List, Union, Dict

class BaseComponent(Component):
    """
    The Single Source of Truth.
    Handles:
    1. HTML Generation (render)
    2. Attribute Management (id, class, data-*)
    3. Content Nesting (children)
    """
     
    def __init__(self,name: str, state: 'ComponentState' = None, template: str = str(), props: dict = None,):
        # 1. Set the Tag (Allow override, fallback to default)
        super().__init__(name=name, state=state, template=template, props=props)

class BS5Component(BaseComponent):
    """
    Base class for all Bootstrap 5 components.
    """

    def __init__(self,name: str, state_props: dict = None,  props: dict = None,):

        # 1. Set the Tag (Allow override, fallback to default)
        self.DEFAULT_BS5_VARIANTS=[]
        self.STATE=None
        self.children=[]
        self.DEFAULT_ATTRS = {}
        if self.STATE == 'dynamic':
            raise ValueError("Dynamic components require a state object.")
        self.template = self._render_comp()
        if self.children:
            self.template.content += ''.join(self.children)
        state=None
        if isinstance(state_props,dict):
            state=ComponentState(**state_props)
        super().__init__(name=name, state=state, template=self.template, props=props)

    def include_env_props(self,**props):
        self.props.update(props)
        return self
    
    def add_child(self,child):
        self.children.append((child.render() if hasattr(child,'render') else str(child)))
        return self
    def swap_element(self,tag):
        self.tag = tag
        self.template.tag=tag
        return self
    def include_content_parts(self,*parts,first=False):
        self.template.include(*parts,first=first)
        return self
    def _render_comp(self,*args,**kwargs):
        """
        Override in subclasses to provide component-specific rendering logic.
        """
        raise NotImplementedError("_render_comp must be implemented in subclasses.")
'''
bs5 comp:
1. bs5 comp <=>Component
2. template is defaulted out in bs5 comp
3. bs5 comp <=> bs5 element
3. bs5 comp <=> content kwargs and attrs as variants
4. bs5 comp <=> static and dynamic variant (DynamicBS5Button(C,CS,ES,SP),StaticBS5Button(C))
5. bs5 comp <=> Suported Variants variable

'''
