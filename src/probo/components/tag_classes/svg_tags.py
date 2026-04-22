from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin,ElementMutatorMixin
from typing import Any, Generator
from probo.utility import StreamManager

class G(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an G HTML <g> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:g = Element(
        ).set_attrs(**self.attributes).set_content(self.content).g().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .g()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager

class DEFS(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an DEFS HTML <defs> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:defs = Element(
        ).set_attrs(**self.attributes).set_content(self.content).defs().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .defs()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TEXT(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an TEXT HTML <text> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:text = Element(
        ).set_attrs(**self.attributes).set_content(self.content).text().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .text()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class TSPAN(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an TSPAN HTML <tspan> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:tspan = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tspan().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .tspan()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SVG(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an SVG HTML <svg> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:svg = Element(
        ).set_attrs(**self.attributes).set_content(self.content).svg().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .svg()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class SYMBOL(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an SYMBOL HTML <symbol> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:symbol = Element(
        ).set_attrs(**self.attributes).set_content(self.content).symbol().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .symbol()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class MARKER(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an MARKER HTML <marker> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:marker = Element(
        ).set_attrs(**self.attributes).set_content(self.content).marker().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .marker()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class PATTERN(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an PATTERN HTML <pattern> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:pattern = Element(
        ).set_attrs(**self.attributes).set_content(self.content).pattern().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .pattern()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class MASK(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an MASK HTML <mask> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:mask = Element(
        ).set_attrs(**self.attributes).set_content(self.content).mask().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .mask()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class CLIPPATH(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an CLIPPATH HTML <clipPath> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:clipPath = Element(
        ).set_attrs(**self.attributes).set_content(self.content).clipPath().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .clipPath()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class LINEARGRADIENT(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an LINEARGRADIENT HTML <linearGradient> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:linearGradient = Element(
        ).set_attrs(**self.attributes).set_content(self.content).linearGradient().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .linearGradient()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class RADIALGRADIENT(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an RADIALGRADIENT HTML <radialGradient> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:radialGradient = Element(
        ).set_attrs(**self.attributes).set_content(self.content).radialGradient().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .radialGradient()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class FILTER(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FILTER HTML <filter> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:filter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).filter().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .filter()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class FECOMPONENTTRANSFER(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FECOMPONENTTRANSFER HTML <feComponentTransfer> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:feComponentTransfer = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feComponentTransfer().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .feComponentTransfer()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class FEDIFFUSELIGHTING(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEDIFFUSELIGHTING HTML <feDiffuseLighting> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:feDiffuseLighting = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feDiffuseLighting().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .feDiffuseLighting()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class FEMERGE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEMERGE HTML <feMerge> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:feMerge = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feMerge().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .feMerge()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class FESPECULARLIGHTING(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FESPECULARLIGHTING HTML <feSpecularLighting> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:feSpecularLighting = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feSpecularLighting().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .feSpecularLighting()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class ANIMATEMOTION(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an ANIMATEMOTION HTML <animateMotion> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:animateMotion = Element(
        ).set_attrs(**self.attributes).set_content(self.content).animateMotion().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .animateMotion()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


class FOREIGNOBJECT(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FOREIGNOBJECT HTML <foreignObject> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)
    def render(self):
        '''
        Blueprint:foreignObject = Element(
        ).set_attrs(**self.attributes).set_content(self.content).foreignObject().element'''
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

        content_generator = self._get_stream_content(batch=batch)

        elment_info = (
            self.EL.set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .foreignObject()
            .element
        )
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=batch),
            elment_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager


# self closing tags

class PATH(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an PATH HTML <path> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class CIRCLE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an CIRCLE HTML <circle> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class RECT(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an RECT HTML <rect> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class LINE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an LINE HTML <line> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class POLYLINE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an POLYLINE HTML <polyline> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class POLYGON(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an POLYGON HTML <polygon> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class ELLIPSE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an ELLIPSE HTML <ellipse> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class IMAGE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an IMAGE HTML <image> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEBLEND(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEBLEND HTML <feBlend> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FECOLORMATRIX(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FECOLORMATRIX HTML <feColorMatrix> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FECOMPOSITE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FECOMPOSITE HTML <feComposite> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FECONVOLVEMATRIX(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FECONVOLVEMATRIX HTML <feConvolveMatrix> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEDISPLACEMENTMAP(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEDISPLACEMENTMAP HTML <feDisplacementMap> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEDROPSHADOW(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEDROPSHADOW HTML <feDropShadow> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEFLOOD(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEFLOOD HTML <feFlood> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEFUNCA(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEFUNCA HTML <feFuncA> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEFUNCB(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEFUNCB HTML <feFuncB> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEFUNCG(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEFUNCG HTML <feFuncG> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEFUNCR(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEFUNCR HTML <feFuncR> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEGAUSSIANBLUR(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEGAUSSIANBLUR HTML <feGaussianBlur> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEIMAGE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEIMAGE HTML <feImage> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEMERGENODE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEMERGENODE HTML <feMergeNode> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEMORPHOLOGY(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEMORPHOLOGY HTML <feMorphology> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEOFFSET(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEOFFSET HTML <feOffset> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FEPOINTLIGHT(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FEPOINTLIGHT HTML <fePointLight> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FESPOTLIGHT(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FESPOTLIGHT HTML <feSpotLight> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FETILE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FETILE HTML <feTile> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class FETURBULENCE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an FETURBULENCE HTML <feTurbulence> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class ANIMATE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an ANIMATE HTML <animate> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class ANIMATETRANSFORM(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an ANIMATETRANSFORM HTML <animateTransform> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class SET(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an SET HTML <set> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class VIEW(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an VIEW HTML <view> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class USE(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an USE HTML <use> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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


class STOP(BaseHTMLElement, ElementNodeMixin,ElementMutatorMixin):
    """Represents an STOP HTML <stop> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)
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

