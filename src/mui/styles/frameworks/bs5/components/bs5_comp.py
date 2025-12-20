from mui.components.tag_classes import (
    DIV,
    BUTTON,
    BaseHTMLElement,
)

from mui.styles.frameworks.bs5.components.defaults.default_comp import DefaultCompEnums

class Bootstrap5:
    """
    A class to dynamically build Bootstrap 5 CSS class strings.
    Allows for chaining methods to add classes and provides predefined constants
    for common Bootstrap Bs5components and utilities.
    """
    def __init__(self, *initial_classes):
        self._classes = []
        self.add(*initial_classes)

    def add(self, *classes):
        """
        Adds one or more class strings to the builder.
        Can take individual strings or lists of strings.
        Returns self for method chaining.
        """
        for cls in classes:
            if isinstance(cls, str):
                self._classes.extend(cls.split()) # Split space-separated strings
            elif isinstance(cls, (list, tuple)):
                self._classes.extend(cls)
        return self

    def build(self):
        """
        Returns the final space-separated string of all collected Bootstrap classes.
        """
        return " ".join(sorted(list(set(self._classes)))) # Use set to remove duplicates, then sort for consistency

    # --- Nested classes for common Bootstrap 5 Bs5components/utilities ---
class Bs5Component:
    """
    Base class for all UI Bs5components.
    Bs5Components are higher-level abstractions that encapsulate common UI patterns.
    They can accept other Bs5components or raw HTML elements as children.
    """
    def __init__(self, *content , **kwargs):
        self.content = content or []
        self.attrs = kwargs or {}
    def render(self):
        """
        Bs5Components must implement their own render method to define their structure.
        """
        raise NotImplementedError("Bs5Components must implement the render method.")

class Accordion(Bs5Component):
    def __init__(self, *items, **kwargs):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        """
        super().__init__(*items, **kwargs)
        self.items = items or []
        self.adopted_comp = str()
        self.btn_string = items[0] if len(items) > 0 else None or kwargs.get('btn_string',None)
        self.abody_string = items[1] if len(items) > 1 else None or kwargs.get('abody_string',None)
        
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
    def get_default(self):
        
        return DefaultCompEnums.ACCORDION.value(self.btn_string,self.abody_string)
    
    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self
    
class Alert(Bs5Component):
    def __init__(self, *items, **kwargs):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **kwargs)
        self.items = items or []
        self.adopted_comp = str()

        self.content= items[0] if len(items) > 0 else None    or kwargs.get('content', None)
        self.path= items[1] if len(items) > 1 else None   or kwargs.get('path', None)
        self.color= items[2] if len(items) > 2 else None      or kwargs.get('color', None)
        self.link_content= items[3] if len(items) > 3 else None   or kwargs.get('link_content', None)
        self.heading_content= items[4] if len(items) > 4 else None    or kwargs.get('heading_content', None)
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
    def get_default(self):
        
        return DefaultCompEnums.ALERT.value(self.content,self.path,self.color,self.link_content,self.heading_content)
 
    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self

class Badge(Bs5Component):
    def __init__(self, *items, **kwargs):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **kwargs)
        self.items = items or []
        self.adopted_comp = str()
        self.content = items[0] if len(items) > 0 else None  or kwargs.get('content',None)
        self.bg_color = items[1] if len(items) > 1 else None or kwargs.get('color',None)

    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        return DefaultCompEnums.BADGE.value(content=self.content, bg_color=str(self.bg_color))

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self

class Breadcrumb(Bs5Component):
    def __init__(self, *items, **kwargs):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **kwargs)
        self.items = items or []
        self.adopted_comp = str()
        self.url_path_dict = items[0] if len(items) > 0 else None  or kwargs

    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        return DefaultCompEnums.BREADCRUMB.value(self.url_path_dict)

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self

class Button(Bs5Component):
    def __init__(self, *items, **args):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **args)
        self.content = items[0] or []
        self.adopted_comp = str()
        self.args = args
        
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        return DefaultCompEnums.BUTTON.value(self.content, **self.args)

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self

class CloseButton(Bs5Component):
    def __init__(self, state,*items, **args):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **args)
        self.state = state
        self.adopted_comp = str()
        
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        return DefaultCompEnums.CLOSE_BUTTON.value(self.state,)

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self

class ButtonGroup(Bs5Component):
    def __init__(self, *items, **args):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **args)
        self.content = items[0] or []
        self.adopted_comp = str()
        self.args = args
        
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        return DefaultCompEnums.BUTTON_GROUP.value(**self.args)

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self

class Card(Bs5Component):
    def __init__(self, *items, **args):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **args)
        self.is_card_group = bool(items)
        self.adopted_comp = str()
        self.args = args
        
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        return DefaultCompEnums.CARD.value(is_card_group=self.is_card_group, **self.args)

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self
    
class Carousel(Bs5Component):
    def __init__(self, *items, crsl_type=None, **args):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **args)
        self.is_card_group = bool(items)
        self.adopted_comp = str()
        self.args = args
        self.items = items
        self.crsl_type =str(crsl_type or args.get('crsl_type',None))
        
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        return DefaultCompEnums.CAROUSEL.value(self.crsl_type,*self.items, **self.args)

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self

class Collapse(Bs5Component):
    def __init__(self, clps_type=None,*items,  **args):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **args)
        self.is_card_group = bool(items)
        self.adopted_comp = str()
        self.args = args
        self.items = items
        self.clps_type =clps_type or args.get('clps_type','base')
        
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        print('self.clps_type :', self.clps_type)
        return DefaultCompEnums.COLLAPSE.value(self.clps_type, **self.args)

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self

class Dropdown(Bs5Component):
    def __init__(self, drpdwn_type=None,*items,  **args):
        """
        Initializes the Accordion Bs5component.
        
        :param items: A list of tuples, each containing (header, body) for accordion items.
        :param kwargs: Additional HTML attributes for the accordion container.
        content,path,color,link_content, heading_content
        """
        super().__init__(*items, **args)
        self.is_card_group = bool(items)
        self.adopted_comp = str()
        self.args = args
        self.items = items
        self.drpdwn_type =drpdwn_type or args.get('drpdwn_type','base')
        
    def get_adopted_comp(self):
        if self.adopted_comp:
            return self.adopted_comp
        
    def get_default(self):
        print('self.drpdwn_type :', self.drpdwn_type)
        return DefaultCompEnums.DROPDOWN.value(self.drpdwn_type, **self.args)

    def adopt(self,comp_string):
        self.adopted_comp = comp_string
        return self