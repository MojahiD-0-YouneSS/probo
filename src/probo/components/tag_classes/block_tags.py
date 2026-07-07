from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin, ElementMutatorMixin, DataPipeLineMixin,MutationPipelineMixin
from probo.utility import StreamManager

from typing import Any,Generator


class A(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):

    """Represents an A HTML <a> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str | Any, **attrs:Any):
        # DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)

    def render(self)->str:
        '''
        Blueprint:a = Element(
        ).set_attrs(**self.attributes).set_content(self.content).a().element'''

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .a()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks. 
        Note: The builder's .a() method must support returning a generator.
        """
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .a()
            .element
        )
        stream_manager = StreamManager(elment_info[0], self.EL.stream(batch=batch), elment_info[-1], chunk_size=batch)
        yield from stream_manager

class ABBR(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an ABBR HTML <abbr> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:abbr = Element(
            ).set_attrs(**self.attributes).set_content(self.content).abbr().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content = self._get_rendered_content()
        else:
            content = self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .abbr()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:abbr = Element(
        ).set_attrs(**self.attributes).set_content(self.content).abbr().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .abbr()
            .element
        )
        stream_manager = StreamManager(elment_info[0], self.EL.stream(batch=batch), elment_info[-1], chunk_size=batch)
        yield from stream_manager


class ADDRESS(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an ADDRESS HTML <address> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:address = Element(
            ).set_attrs(**self.attributes).set_content(self.content).address().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .address()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:address = Element(
        ).set_attrs(**self.attributes).set_content(self.content).address().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .address()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class ARTICLE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an ARTICLE HTML <article> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:article = Element(
            ).set_attrs(**self.attributes).set_content(self.content).article().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .article()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:article = Element(
        ).set_attrs(**self.attributes).set_content(self.content).article().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .article()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class ASIDE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an ASIDE HTML <aside> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:aside = Element(
            ).set_attrs(**self.attributes).set_content(self.content).aside().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .aside()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:aside = Element(
        ).set_attrs(**self.attributes).set_content(self.content).aside().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .aside()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class AUDIO(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an AUDIO HTML <audio> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:audio = Element(
            ).set_attrs(**self.attributes).set_content(self.content).audio().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .audio()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:audio = Element(
        ).set_attrs(**self.attributes).set_content(self.content).audio().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .audio()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class B(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an B HTML <b> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:b = Element(
            ).set_attrs(**self.attributes).set_content(self.content).b().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .b()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:b = Element(
        ).set_attrs(**self.attributes).set_content(self.content).b().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .b()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class BDI(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an BDI HTML <bdi> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:bdi = Element(
            ).set_attrs(**self.attributes).set_content(self.content).bdi().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .bdi()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:bdi = Element(
        ).set_attrs(**self.attributes).set_content(self.content).bdi().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .bdi()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class BDO(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an BDO HTML <bdo> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:bdo = Element(
            ).set_attrs(**self.attributes).set_content(self.content).bdo().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .bdo()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:bdo = Element(
        ).set_attrs(**self.attributes).set_content(self.content).bdo().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .bdo()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class BLOCKQUOTE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an BLOCKQUOTE HTML <blockquote> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:blockquote = Element(
            ).set_attrs(**self.attributes).set_content(self.content).blockquote().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .blockquote()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:blockquote = Element(
        ).set_attrs(**self.attributes).set_content(self.content).blockquote().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .blockquote()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class BODY(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an BODY HTML <body> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:body = Element(
            ).set_attrs(**self.attributes).set_content(self.content).body().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .body()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:body = Element(
        ).set_attrs(**self.attributes).set_content(self.content).body().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .body()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class BUTTON(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an BUTTON HTML <button> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:button = Element(
            ).set_attrs(**self.attributes).set_content(self.content).button().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .button()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:button = Element(
        ).set_attrs(**self.attributes).set_content(self.content).button().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .button()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class CANVAS(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an CANVAS HTML <canvas> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:canvas = Element(
            ).set_attrs(**self.attributes).set_content(self.content).canvas().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .canvas()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:canvas = Element(
        ).set_attrs(**self.attributes).set_content(self.content).canvas().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .canvas()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class CAPTION(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an CAPTION HTML <caption> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:caption = Element(
            ).set_attrs(**self.attributes).set_content(self.content).caption().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .caption()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:caption = Element(
        ).set_attrs(**self.attributes).set_content(self.content).caption().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .caption()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class CITE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an CITE HTML <cite> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:cite = Element(
            ).set_attrs(**self.attributes).set_content(self.content).cite().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .cite()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:cite = Element(
        ).set_attrs(**self.attributes).set_content(self.content).cite().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .cite()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class CODE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an CODE HTML <code> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:code = Element(
            ).set_attrs(**self.attributes).set_content(self.content).code().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .code()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:code = Element(
        ).set_attrs(**self.attributes).set_content(self.content).code().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .code()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class COLGROUP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an COLGROUP HTML <colgroup> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:colgroup = Element(
            ).set_attrs(**self.attributes).set_content(self.content).colgroup().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .colgroup()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:colgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).colgroup().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .colgroup()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DATA(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DATA HTML <data> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:data = Element(
            ).set_attrs(**self.attributes).set_content(self.content).data().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .data()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:data = Element(
        ).set_attrs(**self.attributes).set_content(self.content).data().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .data()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DATALIST(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DATALIST HTML <datalist> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:datalist = Element(
            ).set_attrs(**self.attributes).set_content(self.content).datalist().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .datalist()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:datalist = Element(
        ).set_attrs(**self.attributes).set_content(self.content).datalist().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .datalist()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DD(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DD HTML <dd> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:dd = Element(
            ).set_attrs(**self.attributes).set_content(self.content).dd().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dd()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:dd = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dd().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .dd()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DEL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DEL HTML <del> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:del = Element(
            ).set_attrs(**self.attributes).set_content(self.content).del().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .Del()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:del = Element(
        ).set_attrs(**self.attributes).set_content(self.content).del().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .Del()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DETAILS(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DETAILS HTML <details> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:details = Element(
            ).set_attrs(**self.attributes).set_content(self.content).details().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .details()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:details = Element(
        ).set_attrs(**self.attributes).set_content(self.content).details().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .details()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DFN(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DFN HTML <dfn> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:dfn = Element(
            ).set_attrs(**self.attributes).set_content(self.content).dfn().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dfn()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:dfn = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dfn().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .dfn()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DIALOG(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DIALOG HTML <dialog> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:dialog = Element(
            ).set_attrs(**self.attributes).set_content(self.content).dialog().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dialog()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:dialog = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dialog().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .dialog()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class DIV(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DIV HTML <div> element."""
    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        #         ElementNodeMixin.self.__init__(self)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
        Blueprint:div = Element(
        ).set_attrs(**self.attributes).set_content(self.content).div().element'''

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .div()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:div = Element(
        ).set_attrs(**self.attributes).set_content(self.content).div().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .div()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class DL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DL HTML <dl> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:dl = Element(
            ).set_attrs(**self.attributes).set_content(self.content).dl().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dl()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:dl = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dl().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .dl()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an DT HTML <dt> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:dt = Element(
            ).set_attrs(**self.attributes).set_content(self.content).dt().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dt()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:dt = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dt().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .dt()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class EM(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an EM HTML <em> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:em = Element(
            ).set_attrs(**self.attributes).set_content(self.content).em().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .em()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:em = Element(
        ).set_attrs(**self.attributes).set_content(self.content).em().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .em()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FIELDSET(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an FIELDSET HTML <fieldset> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:fieldset = Element(
            ).set_attrs(**self.attributes).set_content(self.content).fieldset().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .fieldset()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:fieldset = Element(
        ).set_attrs(**self.attributes).set_content(self.content).fieldset().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .fieldset()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FIGCAPTION(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an FIGCAPTION HTML <figcaption> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:figcaption = Element(
            ).set_attrs(**self.attributes).set_content(self.content).figcaption().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .figcaption()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:figcaption = Element(
        ).set_attrs(**self.attributes).set_content(self.content).figcaption().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .figcaption()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FIGURE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an FIGURE HTML <figure> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:figure = Element(
            ).set_attrs(**self.attributes).set_content(self.content).figure().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .figure()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:figure = Element(
        ).set_attrs(**self.attributes).set_content(self.content).figure().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .figure()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FOOTER(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an FOOTER HTML <footer> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:footer = Element(
            ).set_attrs(**self.attributes).set_content(self.content).footer().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .footer()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:footer = Element(
        ).set_attrs(**self.attributes).set_content(self.content).footer().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .footer()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FORM(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an FORM HTML <form> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:form = Element(
            ).set_attrs(**self.attributes).set_content(self.content).form().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .form()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:form = Element(
        ).set_attrs(**self.attributes).set_content(self.content).form().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .form()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class H1(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an H1 HTML <h1> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:h1 = Element(
            ).set_attrs(**self.attributes).set_content(self.content).h1().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h1()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:h1 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h1().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .h1()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class H2(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an H2 HTML <h2> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:h2 = Element(
            ).set_attrs(**self.attributes).set_content(self.content).h2().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h2()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:h2 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h2().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .h2()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class H3(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an H3 HTML <h3> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:h3 = Element(
            ).set_attrs(**self.attributes).set_content(self.content).h3().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h3()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:h3 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h3().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .h3()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class H4(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an H4 HTML <h4> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:h4 = Element(
            ).set_attrs(**self.attributes).set_content(self.content).h4().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h4()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:h4 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h4().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .h4()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class H5(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an H5 HTML <h5> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:h5 = Element(
            ).set_attrs(**self.attributes).set_content(self.content).h5().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h5()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:h5 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h5().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .h5()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class H6(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an H6 HTML <h6> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:h6 = Element(
            ).set_attrs(**self.attributes).set_content(self.content).h6().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h6()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:h6 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h6().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .h6()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class HEAD(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an HEAD HTML <head> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:head = Element(
            ).set_attrs(**self.attributes).set_content(self.content).head().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .head()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:head = Element(
        ).set_attrs(**self.attributes).set_content(self.content).head().element'''
        self.delegate_render_conditions(
            use_list=True,
        )
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .head()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class HEADER(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an HEADER HTML <header> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:header = Element(
            ).set_attrs(**self.attributes).set_content(self.content).header().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .header()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:header = Element(
        ).set_attrs(**self.attributes).set_content(self.content).header().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .header()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class HGROUP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an HGROUP HTML <hgroup> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:hgroup = Element(
            ).set_attrs(**self.attributes).set_content(self.content).hgroup().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .hgroup()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:hgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).hgroup().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .hgroup()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class HTML(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an HTML HTML <html> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:html = Element(
            ).set_attrs(**self.attributes).set_content(self.content).html().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .html()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:html = Element(
        ).set_attrs(**self.attributes).set_content(self.content).html().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .html()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class I(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an I HTML <i> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:i = Element(
            ).set_attrs(**self.attributes).set_content(self.content).i().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .i()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:i = Element(
        ).set_attrs(**self.attributes).set_content(self.content).i().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .i()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class IFRAME(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an IFRAME HTML <iframe> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:iframe = Element(
            ).set_attrs(**self.attributes).set_content(self.content).iframe().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .iframe()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:iframe = Element(
        ).set_attrs(**self.attributes).set_content(self.content).iframe().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .iframe()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class INS(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an INS HTML <ins> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:ins = Element(
            ).set_attrs(**self.attributes).set_content(self.content).ins().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .ins()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:ins = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ins().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .ins()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class KBD(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an KBD HTML <kbd> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:kbd = Element(
            ).set_attrs(**self.attributes).set_content(self.content).kbd().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .kbd()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:kbd = Element(
        ).set_attrs(**self.attributes).set_content(self.content).kbd().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .kbd()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class LABEL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an LABEL HTML <label> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:label = Element(
            ).set_attrs(**self.attributes).set_content(self.content).label().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .label()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:label = Element(
        ).set_attrs(**self.attributes).set_content(self.content).label().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .label()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class LEGEND(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an LEGEND HTML <legend> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:legend = Element(
            ).set_attrs(**self.attributes).set_content(self.content).legend().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .legend()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:legend = Element(
        ).set_attrs(**self.attributes).set_content(self.content).legend().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .legend()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class LI(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an LI HTML <li> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:li = Element(
            ).set_attrs(**self.attributes).set_content(self.content).li().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .li()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:li = Element(
        ).set_attrs(**self.attributes).set_content(self.content).li().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .li()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class MAIN(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an MAIN HTML <main> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:main = Element(
            ).set_attrs(**self.attributes).set_content(self.content).main().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .main()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:main = Element(
        ).set_attrs(**self.attributes).set_content(self.content).main().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .main()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class MATH(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an MATH HTML <math> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:math = Element(
            ).set_attrs(**self.attributes).set_content(self.content).math().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .math()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:math = Element(
        ).set_attrs(**self.attributes).set_content(self.content).math().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .math()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class MAP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an MAP HTML <map> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:map = Element(
            ).set_attrs(**self.attributes).set_content(self.content).map().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .Map()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:map = Element(
        ).set_attrs(**self.attributes).set_content(self.content).map().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .Map()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class MARK(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an MARK HTML <mark> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:mark = Element(
            ).set_attrs(**self.attributes).set_content(self.content).mark().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .mark()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:mark = Element(
        ).set_attrs(**self.attributes).set_content(self.content).mark().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .mark()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class MENU(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an MENU HTML <menu> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:menu = Element(
            ).set_attrs(**self.attributes).set_content(self.content).menu().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .menu()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:menu = Element(
        ).set_attrs(**self.attributes).set_content(self.content).menu().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .menu()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class METER(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an METER HTML <meter> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:meter = Element(
            ).set_attrs(**self.attributes).set_content(self.content).meter().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .meter()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .meter()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class NAV(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an NAV HTML <nav> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:nav = Element(
            ).set_attrs(**self.attributes).set_content(self.content).nav().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .nav()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:nav = Element(
        ).set_attrs(**self.attributes).set_content(self.content).nav().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .nav()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class NOSCRIPT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an NOSCRIPT HTML <noscript> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:noscript = Element(
            ).set_attrs(**self.attributes).set_content(self.content).noscript().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .noscript()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:noscript = Element(
        ).set_attrs(**self.attributes).set_content(self.content).noscript().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .noscript()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class OBJECT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an OBJECT HTML <object> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:object = Element(
            ).set_attrs(**self.attributes).set_content(self.content).object().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .object()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:object = Element(
        ).set_attrs(**self.attributes).set_content(self.content).object().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .object()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class OL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an OL HTML <ol> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:ol = Element(
            ).set_attrs(**self.attributes).set_content(self.content).ol().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .ol()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:ol = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ol().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .ol()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class OPTGROUP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an OPTGROUP HTML <optgroup> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:optgroup = Element(
            ).set_attrs(**self.attributes).set_content(self.content).optgroup().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .optgroup()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:optgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).optgroup().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .optgroup()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class OPTION(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an OPTION HTML <option> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:option = Element(
            ).set_attrs(**self.attributes).set_content(self.content).option().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .option()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:option = Element(
        ).set_attrs(**self.attributes).set_content(self.content).option().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .option()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class OUTPUT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an OUTPUT HTML <output> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:output = Element(
            ).set_attrs(**self.attributes).set_content(self.content).output().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .output()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:output = Element(
        ).set_attrs(**self.attributes).set_content(self.content).output().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .output()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class P(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an P HTML <p> element."""
    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:p = Element(
            ).set_attrs(**self.attributes).set_content(self.content).p().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .p()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:p = Element(
        ).set_attrs(**self.attributes).set_content(self.content).p().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .p()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class PORTAL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an PORTAL HTML <portal> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:portal = Element(
            ).set_attrs(**self.attributes).set_content(self.content).portal().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .portal()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:portal = Element(
        ).set_attrs(**self.attributes).set_content(self.content).portal().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .portal()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class PICTURE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an PICTURE HTML <picture> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:picture = Element(
            ).set_attrs(**self.attributes).set_content(self.content).picture().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .picture()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:picture = Element(
        ).set_attrs(**self.attributes).set_content(self.content).picture().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .picture()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class PRE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an PRE HTML <pre> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:pre = Element(
            ).set_attrs(**self.attributes).set_content(self.content).pre().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .pre()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:pre = Element(
        ).set_attrs(**self.attributes).set_content(self.content).pre().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .pre()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class PROGRESS(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an PROGRESS HTML <progress> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:progress = Element(
            ).set_attrs(**self.attributes).set_content(self.content).progress().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .progress()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:progress = Element(
        ).set_attrs(**self.attributes).set_content(self.content).progress().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .progress()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class Q(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an Q HTML <q> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:q = Element(
            ).set_attrs(**self.attributes).set_content(self.content).q().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .q()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:q = Element(
        ).set_attrs(**self.attributes).set_content(self.content).q().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .q()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class RP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an RP HTML <rp> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:rp = Element(
            ).set_attrs(**self.attributes).set_content(self.content).rp().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .rp()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:rp = Element(
        ).set_attrs(**self.attributes).set_content(self.content).rp().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .rp()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class RT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an RT HTML <rt> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:rt = Element(
            ).set_attrs(**self.attributes).set_content(self.content).rt().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .rt()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:rt = Element(
        ).set_attrs(**self.attributes).set_content(self.content).rt().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .rt()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class RUBY(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an RUBY HTML <ruby> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:ruby = Element(
            ).set_attrs(**self.attributes).set_content(self.content).ruby().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .ruby()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:ruby = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ruby().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .ruby()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class S(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an S HTML <s> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:s = Element(
            ).set_attrs(**self.attributes).set_content(self.content).s().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .s()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:s = Element(
        ).set_attrs(**self.attributes).set_content(self.content).s().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .s()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SAMP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SAMP HTML <samp> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:samp = Element(
            ).set_attrs(**self.attributes).set_content(self.content).samp().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .samp()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:samp = Element(
        ).set_attrs(**self.attributes).set_content(self.content).samp().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .samp()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SCRIPT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SCRIPT HTML <script> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:script = Element(
            ).set_attrs(**self.attributes).set_content(self.content).script().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .script()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:script = Element(
        ).set_attrs(**self.attributes).set_content(self.content).script().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .script()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SEARCH(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SEARCH HTML <search> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:search = Element(
            ).set_attrs(**self.attributes).set_content(self.content).search().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .search()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:search = Element(
        ).set_attrs(**self.attributes).set_content(self.content).search().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .search()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SECTION(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SECTION HTML <section> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:section = Element(
            ).set_attrs(**self.attributes).set_content(self.content).section().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .section()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:section = Element(
        ).set_attrs(**self.attributes).set_content(self.content).section().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .section()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SELECT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SELECT HTML <select> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:select = Element(
            ).set_attrs(**self.attributes).set_content(self.content).select().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .select()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:select = Element(
        ).set_attrs(**self.attributes).set_content(self.content).select().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .select()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SLOT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SLOT HTML <slot> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:slot = Element(
            ).set_attrs(**self.attributes).set_content(self.content).slot().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .slot()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:slot = Element(
        ).set_attrs(**self.attributes).set_content(self.content).slot().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .slot()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SMALL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SMALL HTML <small> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:small = Element(
            ).set_attrs(**self.attributes).set_content(self.content).small().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .small()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:small = Element(
        ).set_attrs(**self.attributes).set_content(self.content).small().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .small()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SPAN(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SPAN HTML <span> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:span = Element(
            ).set_attrs(**self.attributes).set_content(self.content).span().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .span()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:span = Element(
        ).set_attrs(**self.attributes).set_content(self.content).span().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .span()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class STRONG(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an STRONG HTML <strong> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:strong = Element(
            ).set_attrs(**self.attributes).set_content(self.content).strong().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .strong()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:strong = Element(
        ).set_attrs(**self.attributes).set_content(self.content).strong().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .strong()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class STYLE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an STYLE HTML <style> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:style = Element(
            ).set_attrs(**self.attributes).set_content(self.content).style().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .style()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:style = Element(
        ).set_attrs(**self.attributes).set_content(self.content).style().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .style()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SUB(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SUB HTML <sub> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:sub = Element(
            ).set_attrs(**self.attributes).set_content(self.content).sub().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .sub()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:sub = Element(
        ).set_attrs(**self.attributes).set_content(self.content).sub().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .sub()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SUMMARY(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SUMMARY HTML <summary> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:summary = Element(
            ).set_attrs(**self.attributes).set_content(self.content).summary().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .summary()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:summary = Element(
        ).set_attrs(**self.attributes).set_content(self.content).summary().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .summary()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SUP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SUP HTML <sup> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:sup = Element(
            ).set_attrs(**self.attributes).set_content(self.content).sup().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .sup()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:sup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).sup().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .sup()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class TABLE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TABLE HTML <table> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:table = Element(
            ).set_attrs(**self.attributes).set_content(self.content).table().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .table()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:table = Element(
        ).set_attrs(**self.attributes).set_content(self.content).table().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .table()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TBODY(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TBODY HTML <tbody> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:tbody = Element(
            ).set_attrs(**self.attributes).set_content(self.content).tbody().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .tbody()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:tbody = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tbody().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .tbody()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TD(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TD HTML <td> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:td = Element(
            ).set_attrs(**self.attributes).set_content(self.content).td().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .td()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:td = Element(
        ).set_attrs(**self.attributes).set_content(self.content).td().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .td()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TEMPLATE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TEMPLATE HTML <template> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:template = Element(
            ).set_attrs(**self.attributes).set_content(self.content).template().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .template()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:template = Element(
        ).set_attrs(**self.attributes).set_content(self.content).template().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .template()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TEXTAREA(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TEXTAREA HTML <textarea> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:textarea = Element(
            ).set_attrs(**self.attributes).set_content(self.content).textarea().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .textarea()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:textarea = Element(
        ).set_attrs(**self.attributes).set_content(self.content).textarea().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .textarea()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TFOOT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TFOOT HTML <tfoot> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:tfoot = Element(
            ).set_attrs(**self.attributes).set_content(self.content).tfoot().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .tfoot()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:tfoot = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tfoot().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .tfoot()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TH(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TH HTML <th> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:th = Element(
            ).set_attrs(**self.attributes).set_content(self.content).th().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .th()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:th = Element(
        ).set_attrs(**self.attributes).set_content(self.content).th().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .th()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class THEAD(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an THEAD HTML <thead> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:thead = Element(
            ).set_attrs(**self.attributes).set_content(self.content).thead().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .thead()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:thead = Element(
        ).set_attrs(**self.attributes).set_content(self.content).thead().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .thead()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TIME(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TIME HTML <time> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:time = Element(
            ).set_attrs(**self.attributes).set_content(self.content).time().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .time()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:time = Element(
        ).set_attrs(**self.attributes).set_content(self.content).time().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .time()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TITLE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TITLE HTML <title> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:title = Element(
            ).set_attrs(**self.attributes).set_content(self.content).title().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .title()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:title = Element(
        ).set_attrs(**self.attributes).set_content(self.content).title().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .title()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TR(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an TR HTML <tr> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:tr = Element(
            ).set_attrs(**self.attributes).set_content(self.content).tr().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .tr()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:tr = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tr().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .tr()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class U(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an U HTML <u> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:u = Element(
            ).set_attrs(**self.attributes).set_content(self.content).u().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .u()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:u = Element(
        ).set_attrs(**self.attributes).set_content(self.content).u().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .u()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class UL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an UL HTML <ul> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:ul = Element(
            ).set_attrs(**self.attributes).set_content(self.content).ul().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .ul()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:ul = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ul().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .ul()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class VAR(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an VAR HTML <var> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:var = Element(
            ).set_attrs(**self.attributes).set_content(self.content).var().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .var()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:var = Element(
        ).set_attrs(**self.attributes).set_content(self.content).var().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)


        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .var()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class VIDEO(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an VIDEO HTML <video> element."""

    __slots__ = ()
    def __init__(self, *content:str | Any, **attrs:Any):
        #         DataPipeLineMixin.__init__(self)
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs
        super().__init__(*content, **attrs)
        #         ElementNodeMixin.__init__(self)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        #         ElementMutatorMixin.__init__(self)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self)->str:
        '''
            Blueprint:video = Element(
            ).set_attrs(**self.attributes).set_content(self.content).video().element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .video()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        '''
        Blueprint:video = Element(
        ).set_attrs(**self.attributes).set_content(self.content).video().element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))

            else:
                content_generator = self._get_stream_content(batch=batch)

        else:
            content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .video()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager
