from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin,ElementMutatorMixin, DataPipeLineMixin, MutationPipelineMixin
from probo.utility import StreamManager
from probo.type_hints import GenericSSDOM
from typing import Any,Generator


class DOCTYPE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DOCTYPE HTML <!> line break element (self-closing)."""

    __slots__ = ('html_doc',)
    def __init__(self, content:GenericSSDOM|None=None, **kwargs:Any):
        super().__init__(content, **kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([], True)
        self.html_doc: GenericSSDOM | None = None
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
        if (
            content
            and issubclass(content.__class__, BaseHTMLElement)
            and content.tag == "HTML"

        ):
            self.html_doc = content
    def render(self):
        content=self._get_rendered_content()
        return self.EL.set_attrs(**self.attributes).set_content(content).doctype().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""

        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.html_doc is not None:        
            content_generator = self.html_doc.stream(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)

        yield from (self.EL.set_attrs(**self.attributes)
        # .set_generator_content((x for x in []))
            .doctype()
            .reset_generator_content()
            .stream(batch=batch))
        stream_manager = StreamManager(
            None,
            content_generator,
            chunk_size=batch,
        )
        yield from stream_manager


class AREA(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an AREA HTML <area> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).area().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .area()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class BASE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an BASE HTML <base> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).base().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .base()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class BR(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an BR HTML <br> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).br().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .br()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class COL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an COL HTML <col> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).col().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .col()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class EMBED(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an EMBED HTML <embed> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).embed().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .embed()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class HR(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an HR HTML <hr> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).hr().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .hr()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class IMG(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an IMG HTML <img> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).img().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .img()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class INPUT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an INPUT HTML <input> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).input().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .input()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class LINK(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an LINK HTML <link> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).link().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .link()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class META(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an META HTML <meta> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).meta().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .meta()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class PARAM(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an PARAM HTML <param> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).param().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .param()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class SOURCE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SOURCE HTML <source> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).source().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .source()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class TRACK(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TRACK HTML <track> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).track().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .track()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager


class WBR(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an WBR HTML <wbr> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:Any):
        super().__init__(**kwargs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children([],True)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        return self.EL.set_attrs(**self.attributes).wbr().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
        if self.has_unresolved_pipeline_vars:
            self.resolve_pipeline_variables(swap_vars=True)
        self.delegate_render_conditions(
            use_list=True,
        )


        stream_manager = StreamManager(
            None,
            (
            self.EL.set_attrs(**self.attributes)
            .wbr()
            .reset_generator_content()
            .stream(batch=batch)
        ),
            chunk_size=batch,
        )
        yield from stream_manager
