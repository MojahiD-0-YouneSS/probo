from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin,ElementMutatorMixin,DataPipeLineMixin, MutationPipelineMixin
from typing import Any, Generator
from probo.utility import StreamManager

class G(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an G HTML <g> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:g = Element(
        ).set_attrs(**self.attributes).set_content(self.content).g().element'''
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
            .g()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .g() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .g()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DEFS(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an DEFS HTML <defs> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:defs = Element(
        ).set_attrs(**self.attributes).set_content(self.content).defs().element'''
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
            .defs()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .defs() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .defs()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class TEXT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an TEXT HTML <text> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:text = Element(
        ).set_attrs(**self.attributes).set_content(self.content).text().element'''
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
            .text()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .text() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .text()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class TSPAN(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an TSPAN HTML <tspan> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:tspan = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tspan().element'''
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
            .tspan()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .tspan() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .tspan()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class SVG(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,MutationPipelineMixin,BaseHTMLElement):
    """Represents an SVG HTML <svg> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)

        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:svg = Element(
        ).set_attrs(**self.attributes).set_content(self.content).svg().element'''
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
            .svg()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .svg() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .svg()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class SYMBOL(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an SYMBOL HTML <symbol> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:symbol = Element(
        ).set_attrs(**self.attributes).set_content(self.content).symbol().element'''
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
            .symbol()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .symbol() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .symbol()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class MARKER(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an MARKER HTML <marker> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:marker = Element(
        ).set_attrs(**self.attributes).set_content(self.content).marker().element'''
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
            .marker()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .marker() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .marker()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class PATTERN(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an PATTERN HTML <pattern> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:pattern = Element(
        ).set_attrs(**self.attributes).set_content(self.content).pattern().element'''
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
            .pattern()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .pattern() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .pattern()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class MASK(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an MASK HTML <mask> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:mask = Element(
        ).set_attrs(**self.attributes).set_content(self.content).mask().element'''
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
            .mask()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .mask() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .mask()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class CLIPPATH(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an CLIPPATH HTML <clipPath> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:clipPath = Element(
        ).set_attrs(**self.attributes).set_content(self.content).clipPath().element'''
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
            .clipPath()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .clipPath() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .clipPath()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class LINEARGRADIENT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an LINEARGRADIENT HTML <linearGradient> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:linearGradient = Element(
        ).set_attrs(**self.attributes).set_content(self.content).linearGradient().element'''
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
            .linearGradient()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .linearGradient() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .linearGradient()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class RADIALGRADIENT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an RADIALGRADIENT HTML <radialGradient> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:radialGradient = Element(
        ).set_attrs(**self.attributes).set_content(self.content).radialGradient().element'''
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
            .radialGradient()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .radialGradient() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .radialGradient()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FILTER(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FILTER HTML <filter> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:filter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).filter().element'''
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
            .filter()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .filter() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .filter()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FECOMPONENTTRANSFER(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FECOMPONENTTRANSFER HTML <feComponentTransfer> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:feComponentTransfer = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feComponentTransfer().element'''
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
            .feComponentTransfer()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .feComponentTransfer() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .feComponentTransfer()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FEDIFFUSELIGHTING(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEDIFFUSELIGHTING HTML <feDiffuseLighting> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:feDiffuseLighting = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feDiffuseLighting().element'''
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
            .feDiffuseLighting()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .feDiffuseLighting() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .feDiffuseLighting()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FEMERGE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEMERGE HTML <feMerge> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:feMerge = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feMerge().element'''
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
            .feMerge()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .feMerge() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .feMerge()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FESPECULARLIGHTING(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FESPECULARLIGHTING HTML <feSpecularLighting> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:feSpecularLighting = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feSpecularLighting().element'''
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
            .feSpecularLighting()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .feSpecularLighting() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .feSpecularLighting()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class ANIMATEMOTION(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an ANIMATEMOTION HTML <animateMotion> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:animateMotion = Element(
        ).set_attrs(**self.attributes).set_content(self.content).animateMotion().element'''
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
            .animateMotion()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .animateMotion() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .animateMotion()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class FOREIGNOBJECT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FOREIGNOBJECT HTML <foreignObject> element."""

    __slots__ = ()
    def __init__(self, *content:str|Any, **attrs:Any):
        super().__init__(*content, **attrs)
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)
    def render(self):
        '''
        Blueprint:foreignObject = Element(
        ).set_attrs(**self.attributes).set_content(self.content).foreignObject().element'''
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
            .foreignObject()
            .element
        )

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .foreignObject() method must support returning a generator.
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


        element_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .foreignObject()
            .element
        )
        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

# self closing tags

class PATH(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an PATH HTML <path> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).path().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).path().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .path()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class CIRCLE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an CIRCLE HTML <circle> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).circle().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).circle().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .circle()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class RECT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an RECT HTML <rect> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).rect().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).rect().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .rect()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class LINE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an LINE HTML <line> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).line().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).line().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .line()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class POLYLINE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an POLYLINE HTML <polyline> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).polyline().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).polyline().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .polyline()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class POLYGON(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an POLYGON HTML <polygon> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).polygon().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).polygon().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .polygon()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class ELLIPSE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an ELLIPSE HTML <ellipse> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).ellipse().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).ellipse().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .ellipse()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class IMAGE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an IMAGE HTML <image> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).image().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).image().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .image()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEBLEND(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEBLEND HTML <feBlend> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feBlend().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feBlend().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feBlend()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FECOLORMATRIX(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FECOLORMATRIX HTML <feColorMatrix> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feColorMatrix().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feColorMatrix().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feColorMatrix()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FECOMPOSITE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FECOMPOSITE HTML <feComposite> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feComposite().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feComposite().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feComposite()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FECONVOLVEMATRIX(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FECONVOLVEMATRIX HTML <feConvolveMatrix> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feConvolveMatrix().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feConvolveMatrix().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feConvolveMatrix()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEDISPLACEMENTMAP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEDISPLACEMENTMAP HTML <feDisplacementMap> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feDisplacementMap().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feDisplacementMap().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feDisplacementMap()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEDROPSHADOW(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEDROPSHADOW HTML <feDropShadow> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feDropShadow().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feDropShadow().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feDropShadow()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEFLOOD(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEFLOOD HTML <feFlood> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feFlood().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feFlood().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feFlood()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEFUNCA(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEFUNCA HTML <feFuncA> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feFuncA().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feFuncA().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feFuncA()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEFUNCB(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEFUNCB HTML <feFuncB> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feFuncB().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feFuncB().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feFuncB()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEFUNCG(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEFUNCG HTML <feFuncG> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feFuncG().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feFuncG().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feFuncG()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEFUNCR(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEFUNCR HTML <feFuncR> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feFuncR().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feFuncR().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feFuncR()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEGAUSSIANBLUR(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEGAUSSIANBLUR HTML <feGaussianBlur> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feGaussianBlur().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feGaussianBlur().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feGaussianBlur()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEIMAGE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEIMAGE HTML <feImage> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feImage().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feImage().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feImage()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEMERGENODE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEMERGENODE HTML <feMergeNode> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feMergeNode().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feMergeNode().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feMergeNode()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEMORPHOLOGY(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEMORPHOLOGY HTML <feMorphology> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feMorphology().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feMorphology().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feMorphology()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEOFFSET(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEOFFSET HTML <feOffset> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feOffset().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feOffset().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feOffset()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FEPOINTLIGHT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FEPOINTLIGHT HTML <fePointLight> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).fePointLight().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).fePointLight().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .fePointLight()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FESPOTLIGHT(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FESPOTLIGHT HTML <feSpotLight> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feSpotLight().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feSpotLight().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feSpotLight()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FETILE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FETILE HTML <feTile> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feTile().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feTile().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feTile()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class FETURBULENCE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an FETURBULENCE HTML <feTurbulence> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).feTurbulence().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).feTurbulence().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .feTurbulence()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class ANIMATE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an ANIMATE HTML <animate> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).animate().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).animate().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .animate()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class ANIMATETRANSFORM(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an ANIMATETRANSFORM HTML <animateTransform> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).animateTransform().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).animateTransform().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .animateTransform()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class SET(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an SET HTML <set> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).set().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .set()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class VIEW(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an VIEW HTML <view> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).view().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).view().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .view()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class USE(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an USE HTML <use> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).use().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).use().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .use()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager


class STOP(DataPipeLineMixin, ElementNodeMixin,ElementMutatorMixin,  MutationPipelineMixin, BaseHTMLElement,):
    """Represents an STOP HTML <stop> line break element (self-closing)."""

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
        return self.EL.set_attrs(**self.attributes).stop().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).stop().element"""
        self.delegate_render_conditions(
            use_list=True,
        )

        stream_manager = StreamManager(
            None,
            (
                self.EL.set_attrs(**self.attributes)
                .stop()
                .reset_generator_content()
                .stream(batch=batch)
            ),
            chunk_size=batch,
        )
        yield from stream_manager

