from probo.components.light_tags.node import LightNode
from probo.components.node import ElementNodeMixin, ElementMutatorMixin
from probo.utility import StreamManager
from typing import Any, Generator, Self


class Ldoctype(LightNode, ElementNodeMixin):
    """Represents an DOCTYPE HTML <!> line break element (self-closing)."""

    __slots__ = ("html_doc",)

    def __init__(
        self, content: ElementNodeMixin | None = None, **kwargs: dict[str, Any]
    ):
        super().__init__(content, **kwargs)
        self.html_doc: ElementNodeMixin | None = None
        ElementNodeMixin.__init__(self)

        if (
            content
            and isinstance(content, ElementNodeMixin)
            and content.light_tag == "html"
            or isinstance(content, ElementNodeMixin)
            and hasattr(content, "element_tag")
            and content.element_tag == "html"
        ):
            self.html_doc = content

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""

        yield from super().stream(EL,batch)


class Larea(LightNode, ElementNodeMixin):
    """Represents an AREA HTML <area> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):

        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lbase(LightNode, ElementNodeMixin):
    """Represents an BASE HTML <base> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lbr(LightNode, ElementNodeMixin):
    """Represents an BR HTML <br> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lcol(LightNode, ElementNodeMixin):
    """Represents an COL HTML <col> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lembed(LightNode, ElementNodeMixin):
    """Represents an EMBED HTML <embed> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lhr(LightNode, ElementNodeMixin):
    """Represents an HR HTML <hr> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Limg(LightNode, ElementNodeMixin):
    """Represents an IMG HTML <img> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Linput(LightNode, ElementNodeMixin):
    """Represents an INPUT HTML <input> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Llink(LightNode, ElementNodeMixin):
    """Represents an LINK HTML <link> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lmeta(LightNode, ElementNodeMixin):
    """Represents an META HTML <meta> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lparam(LightNode, ElementNodeMixin):
    """Represents an PARAM HTML <param> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lsource(LightNode, ElementNodeMixin):
    """Represents an SOURCE HTML <source> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Ltrack(LightNode, ElementNodeMixin):
    """Represents an TRACK HTML <track> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)


class Lwbr(LightNode, ElementNodeMixin):
    """Represents an WBR HTML <wbr> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(tag=None,**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([], True)

    def render(self,EL,):
        return super().render(EL,)

    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        """
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element"""
        yield from super().stream(EL,batch)
