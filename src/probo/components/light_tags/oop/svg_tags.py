from probo.components.light_tags.node import LightNode
from probo.components.node import ElementNodeMixin,MutationPipelineMixin,DataPipeLineMixin
from typing import Any

class Lg(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an G HTML <g> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="g".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class Ldefs(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an DEFS HTML <defs> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="defs".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class Ltext(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an TEXT HTML <text> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="text".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class Ltspan(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an TSPAN HTML <tspan> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="tspan".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)


class Lsvg(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode,):
    """Represents an SVG HTML <svg> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)


class Lsymbol(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an SYMBOL HTML <symbol> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="symbol".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class Lmarker(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an MARKER HTML <marker> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="marker".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class Lpattern(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an PATTERN HTML <pattern> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="pattern".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class Lmask(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an MASK HTML <mask> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="mask".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LclipPath(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an CLIPPATH HTML <clipPath> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="clipPath".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LlinearGradient(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an LINEARGRADIENT HTML <linearGradient> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="linearGradient".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LradialGradient(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an RADIALGRADIENT HTML <radialGradient> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="radialGradient".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class Lfilter(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FILTER HTML <filter> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="filter".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LfeComponentTransfer(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FECOMPONENTTRANSFER HTML <feComponentTransfer> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="feComponentTransfer".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LfeDiffuseLighting(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEDIFFUSELIGHTING HTML <feDiffuseLighting> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="feDiffuseLighting".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LfeMerge(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEMERGE HTML <feMerge> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="feMerge".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LfeSpecularLighting(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FESPECULARLIGHTING HTML <feSpecularLighting> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="feSpecularLighting".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LanimateMotion(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an ANIMATEMOTION HTML <animateMotion> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="animateMotion".lower(),**attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

class LforeignObject(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FOREIGNOBJECT HTML <foreignObject> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content,tag="foreignObject".lower(), **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content=[]
        yield from super().stream(EL,batch)

# self closing tags

class Lpath(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an PATH HTML <path> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="path".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lcircle(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an CIRCLE HTML <circle> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="circle".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lrect(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an RECT HTML <rect> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="rect".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lline(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an LINE HTML <line> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="line".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lpolyline(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an POLYLINE HTML <polyline> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="polyline".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lpolygon(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an POLYGON HTML <polygon> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="polygon".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lellipse(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an ELLIPSE HTML <ellipse> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="ellipse".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Limage(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an IMAGE HTML <image> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="image".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeBlend(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEBLEND HTML <feBlend> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feBlend".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeColorMatrix(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FECOLORMATRIX HTML <feColorMatrix> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feColorMatrix".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeComposite(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FECOMPOSITE HTML <feComposite> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feComposite".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeConvolveMatrix(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FECONVOLVEMATRIX HTML <feConvolveMatrix> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feConvolveMatrix".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeDisplacementMap(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEDISPLACEMENTMAP HTML <feDisplacementMap> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feDisplacementMap".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeDropShadow(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEDROPSHADOW HTML <feDropShadow> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feDropShadow".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeFlood(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEFLOOD HTML <feFlood> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feFlood".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeFuncA(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEFUNCA HTML <feFuncA> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feFuncA".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeFuncB(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEFUNCB HTML <feFuncB> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feFuncB".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeFuncG(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEFUNCG HTML <feFuncG> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feFuncG".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeFuncR(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEFUNCR HTML <feFuncR> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feFuncR".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeGaussianBlur(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEGAUSSIANBLUR HTML <feGaussianBlur> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feGaussianBlur".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeImage(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEIMAGE HTML <feImage> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feImage".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeMergeNode(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEMERGENODE HTML <feMergeNode> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feMergeNode".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeMorphology(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEMORPHOLOGY HTML <feMorphology> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feMorphology".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeOffset(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEOFFSET HTML <feOffset> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feOffset".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfePointLight(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FEPOINTLIGHT HTML <fePointLight> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="fePointLight".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeSpotLight(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FESPOTLIGHT HTML <feSpotLight> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feSpotLight".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeTile(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FETILE HTML <feTile> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feTile".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LfeTurbulence(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an FETURBULENCE HTML <feTurbulence> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="feTurbulence".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lanimate(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an ANIMATE HTML <animate> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="animate".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class LanimateTransform(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an ANIMATETRANSFORM HTML <animateTransform> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="animateTransform".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lset(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an SET HTML <set> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="set".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Lview(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an VIEW HTML <view> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="view".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
class Luse(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an USE HTML <use> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="use".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)

class Lstop(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin, LightNode):
    """Represents an STOP HTML <stop> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs:Any):
        super().__init__(tag="stop".lower(),**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL)

    def stream(self, EL,batch=50):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
