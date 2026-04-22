from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin,ElementMutatorMixin
from probo.utility import StreamManager
from typing import Any,Generator,Self


class DOCTYPE(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an DOCTYPE HTML <!> line break element (self-closing)."""

    __slots__ = ('html_doc',)
    def __init__(self, content:ElementNodeMixin|None=None, **kwargs:dict[str,Any]):
        super().__init__(content, **kwargs)
        ElementMutatorMixin.__init__(self)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)
        self.html_doc: ElementNodeMixin | None = None
        if (
            content
            and isinstance(content, BaseHTMLElement)
            and content.element_tag == "html"
            or isinstance(content, ElementNodeMixin)
            and hasattr(content, "light_tag")
            and content.light_tag == "html"
        ):
            self.html_doc = content
    def render(self):
        content=self._get_rendered_content()
        return self.EL.set_attrs(**self.attributes).set_content(content).doctype().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""

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


class AREA(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an AREA HTML <area> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):

        return self.EL.set_attrs(**self.attributes).area().element

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class BASE(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an BASE HTML <base> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).base().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class BR(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an BR HTML <br> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).br().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class COL(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an COL HTML <col> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).col().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class EMBED(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an EMBED HTML <embed> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).embed().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class HR(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an HR HTML <hr> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).hr().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class IMG(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an IMG HTML <img> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).img().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class INPUT(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an INPUT HTML <input> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).input().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class LINK(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an LINK HTML <link> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).link().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class META(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an META HTML <meta> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).meta().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class PARAM(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an PARAM HTML <param> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).param().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class SOURCE(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an SOURCE HTML <source> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).source().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class TRACK(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an TRACK HTML <track> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).track().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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


class WBR(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    """Represents an WBR HTML <wbr> line break element (self-closing)."""

    __slots__ = ()
    def __init__(self, **kwargs:dict[str,Any]):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
        ElementMutatorMixin.__init__(self)

    def render(self):
        return self.EL.set_attrs(**self.attributes).wbr().element
    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).meter().element"""
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
