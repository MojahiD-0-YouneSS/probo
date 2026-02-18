from probo.components.component import Component
from probo.components.state.component_state import ComponentState
from typing import List, Union, Dict

class BaseComponent(Component):
    """The Single Source of Truth for the ProboUI Component Tree.

    BaseComponent handles the fundamental responsibilities of an HTML node: 
    generating valid markup, managing attributes (IDs, classes, data-attributes), 
    and maintaining the nesting hierarchy of child elements.

    Attributes:
        name (str): A unique identifier for the component instance.
        state (ComponentState): The reactive data object associated with the component.
        template (str/BS5Element): The underlying HTML structure.
        props (dict): Configuration properties passed during initialization.
    """
     
    def __init__(self,name: str, state: 'ComponentState' = None, template: str = str(), props: dict = None,):
        # 1. Set the Tag (Allow override, fallback to default)
        super().__init__(name=name, state=state, template=template, props=props)

class BS5Component(BaseComponent):
    """The foundation for all Bootstrap 5-specific UI components.

    This class introduces the 'dynamic' state lifecycle. It manages the 
    transformation of raw data into Bootstrap-styled elements and provides 
    methods for child injection and element swapping.

    Attributes:
        DEFAULT_BS5_VARIANTS (list): Default style variants (e.g., 'primary', 'dark').
        STATE (str): Defines if the component is 'static' or 'dynamic'.
        children (list): A list of rendered strings representing child nodes.
        DEFAULT_ATTRS (dict): Default HTML attributes for the component.
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
        """Merges environment-specific properties into the component's property dictionary.

        Returns:
            self: Enables fluent method chaining.
        """
        self.props.update(props)
        return self
    
    def add_child(self,child):
        """Appends a child component or raw HTML string to the children list.

        Args:
            child (Any): A component instance (with a .render() method) or a string.

        Returns:
            self: Enables fluent method chaining.
        """
        self.children.append((child.render() if hasattr(child,'render') else str(child)))
        return self
    def swap_element(self,tag):
        """Dynamically changes the HTML tag of the rendered component.

        Useful for changing a <div> to a <section> or a <button> to an <a> 
        without rebuilding the entire component logic.

        Args:
            tag (str): The new HTML tag name.
        """
        self.tag = tag
        self.template.tag=tag
        return self
    def include_content_parts(self,*parts,first=False):
        """Injects content directly into the underlying BS5Element template.

        Args:
            *parts: Content segments to include.
            first (bool): If True, prepends the content to the template.
        """
        self.template.include(*parts,first=first)
        return self
    def _render_comp(self,*args,**kwargs):
        """The primary rendering hook for subclasses.

        This method MUST be overridden in subclasses (e.g., BS5Card, BS5Navbar). 
        It defines the initial structural 'skeleton' of the component.

        Returns:
            BS5Element: The root element of the component.
        """
       
        raise NotImplementedError("_render_comp must be implemented in subclasses.")
