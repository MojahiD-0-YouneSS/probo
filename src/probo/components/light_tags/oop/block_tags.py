from probo.components.light_tags.node import LightNode
from probo.components.node import ElementNodeMixin, MutationPipelineMixin,DataPipeLineMixin

from typing import Any,Generator


class La(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):

    """Represents an A HTML <a> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]: 
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Labbr(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an ABBR HTML <abbr> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
        
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Laddress(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an ADDRESS HTML <address> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Larticle(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an ARTICLE HTML <article> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Laside(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an ASIDE HTML <aside> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Laudio(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an AUDIO HTML <audio> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lb(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an B HTML <b> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lbdi(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an BDI HTML <bdi> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lbdo(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an BDO HTML <bdo> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lblockquote(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an BLOCKQUOTE HTML <blockquote> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lbody(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an BODY HTML <body> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lbutton(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an BUTTON HTML <button> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lcanvas(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an CANVAS HTML <canvas> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lcaption(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an CAPTION HTML <caption> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lcite(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an CITE HTML <cite> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lcode(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an CODE HTML <code> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lcolgroup(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an COLGROUP HTML <colgroup> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ldata(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DATA HTML <data> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ldatalist(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DATALIST HTML <datalist> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ldd(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DD HTML <dd> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ldel(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DEL HTML <del> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ldetails(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DETAILS HTML <details> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ldfn(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DFN HTML <dfn> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ldialog(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DIALOG HTML <dialog> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ldiv(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DIV HTML <div> element."""
    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ldl(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DL HTML <dl> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ldt(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an DT HTML <dt> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lem(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an EM HTML <em> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lfieldset(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an FIELDSET HTML <fieldset> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lfigcaption(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an FIGCAPTION HTML <figcaption> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lfigure(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an FIGURE HTML <figure> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lfooter(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an FOOTER HTML <footer> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lform(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an FORM HTML <form> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lh1(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an H1 HTML <h1> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lh2(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an H2 HTML <h2> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lh3(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an H3 HTML <h3> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Lh4(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an H4 HTML <h4> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lh5(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an H5 HTML <h5> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lh6(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an H6 HTML <h6> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lhead(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an HEAD HTML <head> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lheader(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an HEADER HTML <header> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lhgroup(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an HGROUP HTML <hgroup> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lhtml(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an HTML HTML <html> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Li(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an I HTML <i> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Liframe(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an IFRAME HTML <iframe> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lins(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an INS HTML <ins> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lkbd(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an KBD HTML <kbd> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Llabel(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an LABEL HTML <label> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Llegend(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an LEGEND HTML <legend> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lli(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an LI HTML <li> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lmain(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an MAIN HTML <main> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lmath(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an MATH HTML <math> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lmap(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an MAP HTML <map> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lmark(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an MARK HTML <mark> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lmenu(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an MENU HTML <menu> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lmeter(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an METER HTML <meter> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lnav(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an NAV HTML <nav> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lnoscript(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an NOSCRIPT HTML <noscript> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lobject(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an OBJECT HTML <object> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lol(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an OL HTML <ol> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Loptgroup(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an OPTGROUP HTML <optgroup> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Loption(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an OPTION HTML <option> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Loutput(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an OUTPUT HTML <output> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lp(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an P HTML <p> element."""
    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lportal(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an PORTAL HTML <portal> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lpicture(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an PICTURE HTML <picture> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lpre(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an PRE HTML <pre> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lprogress(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an PROGRESS HTML <progress> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lq(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an Q HTML <q> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lrp(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an RP HTML <rp> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lrt(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an RT HTML <rt> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lruby(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an RUBY HTML <ruby> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ls(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an S HTML <s> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lsamp(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SAMP HTML <samp> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lscript(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SCRIPT HTML <script> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lsearch(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SEARCH HTML <search> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lsection(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SECTION HTML <section> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lselect(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SELECT HTML <select> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lslot(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SLOT HTML <slot> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lsmall(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SMALL HTML <small> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lspan(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SPAN HTML <span> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lstrong(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an STRONG HTML <strong> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lstyle(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an STYLE HTML <style> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lsub(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SUB HTML <sub> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lsummary(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SUMMARY HTML <summary> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lsup(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an SUP HTML <sup> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)

class Ltable(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TABLE HTML <table> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ltbody(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TBODY HTML <tbody> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ltd(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TD HTML <td> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ltemplate(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TEMPLATE HTML <template> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ltextarea(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TEXTAREA HTML <textarea> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ltfoot(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TFOOT HTML <tfoot> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lth(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TH HTML <th> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lthead(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an THEAD HTML <thead> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ltime(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TIME HTML <time> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ltitle(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TITLE HTML <title> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Ltr(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an TR HTML <tr> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lu(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an U HTML <u> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lul(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an UL HTML <ul> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lvar(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an VAR HTML <var> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)


class Lvideo(DataPipeLineMixin,ElementNodeMixin,MutationPipelineMixin,LightNode):
    """Represents an VIDEO HTML <video> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        super().__init__(*content,tag=None, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL)->str:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                self.content = []
        yield from super().stream(EL,batch)
