from probo.components.light_tags.node import LightNode
from probo.components.node import ElementNodeMixin, MutationPipelineMixin,DataPipeLineMixin
from probo.type_hints import GenericSSDOM
from typing import Any, Generator


class Ldoctype(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an DOCTYPE HTML <!> line break element (self-closing)."""

    __slots__ = ("html_doc",)

    def __init__(
        self, content: GenericSSDOM | None = None, **kwargs:Any
    ):
        super().__init__(content, **kwargs)
        self.extract_pipeline_args(self.attributes)
        self.html_doc: GenericSSDOM | None = None
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if (
            content
            and issubclass(content.__class__, ElementNodeMixin)
            and content.tag == "HTML"
        ):
            self.html_doc = content

    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""

        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Larea(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an AREA HTML <area> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):

        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Lbase(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an BASE HTML <base> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Lbr(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an BR HTML <br> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Lcol(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an COL HTML <col> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Lembed(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an EMBED HTML <embed> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Lhr(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an HR HTML <hr> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Limg(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an IMG HTML <img> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Linput(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an INPUT HTML <input> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Llink(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an LINK HTML <link> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Lmeta(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an META HTML <meta> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Lparam(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an PARAM HTML <param> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Lsource(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an SOURCE HTML <source> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)


class Ltrack(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an TRACK HTML <track> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""

        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        yield from super().stream(EL,batch)


class Lwbr(DataPipeLineMixin, ElementNodeMixin, MutationPipelineMixin,LightNode):
    """Represents an WBR HTML <wbr> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs:Any):
        super().__init__(tag=None,**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self,EL,):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)

        yield from super().stream(EL,batch)
