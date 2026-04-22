from probo.components.light_tags.node import LightNode
from probo.components.node import ElementNodeMixin, ElementMutatorMixin

from typing import Any,Generator


class La(LightNode,ElementNodeMixin):

    """Represents an A HTML <a> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]: 
        yield from super().stream(EL,batch)       

class Labbr(LightNode,ElementNodeMixin):
    """Represents an ABBR HTML <abbr> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
        
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Laddress(LightNode,ElementNodeMixin):
    """Represents an ADDRESS HTML <address> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Larticle(LightNode,ElementNodeMixin):
    """Represents an ARTICLE HTML <article> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Laside(LightNode,ElementNodeMixin):
    """Represents an ASIDE HTML <aside> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Laudio(LightNode,ElementNodeMixin):
    """Represents an AUDIO HTML <audio> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lb(LightNode,ElementNodeMixin):
    """Represents an B HTML <b> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lbdi(LightNode,ElementNodeMixin):
    """Represents an BDI HTML <bdi> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lbdo(LightNode,ElementNodeMixin):
    """Represents an BDO HTML <bdo> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lblockquote(LightNode,ElementNodeMixin):
    """Represents an BLOCKQUOTE HTML <blockquote> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lbody(LightNode,ElementNodeMixin):
    """Represents an BODY HTML <body> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lbutton(LightNode,ElementNodeMixin):
    """Represents an BUTTON HTML <button> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lcanvas(LightNode,ElementNodeMixin):
    """Represents an CANVAS HTML <canvas> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lcaption(LightNode,ElementNodeMixin):
    """Represents an CAPTION HTML <caption> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lcite(LightNode,ElementNodeMixin):
    """Represents an CITE HTML <cite> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lcode(LightNode,ElementNodeMixin):
    """Represents an CODE HTML <code> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lcolgroup(LightNode,ElementNodeMixin):
    """Represents an COLGROUP HTML <colgroup> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ldata(LightNode,ElementNodeMixin):
    """Represents an DATA HTML <data> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ldatalist(LightNode,ElementNodeMixin):
    """Represents an DATALIST HTML <datalist> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ldd(LightNode,ElementNodeMixin):
    """Represents an DD HTML <dd> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ldel(LightNode,ElementNodeMixin):
    """Represents an DEL HTML <del> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ldetails(LightNode,ElementNodeMixin):
    """Represents an DETAILS HTML <details> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ldfn(LightNode,ElementNodeMixin):
    """Represents an DFN HTML <dfn> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ldialog(LightNode,ElementNodeMixin):
    """Represents an DIALOG HTML <dialog> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ldiv(LightNode,ElementNodeMixin):
    """Represents an DIV HTML <div> element."""
    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ldl(LightNode,ElementNodeMixin):
    """Represents an DL HTML <dl> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ldt(LightNode,ElementNodeMixin):
    """Represents an DT HTML <dt> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lem(LightNode,ElementNodeMixin):
    """Represents an EM HTML <em> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lfieldset(LightNode,ElementNodeMixin):
    """Represents an FIELDSET HTML <fieldset> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lfigcaption(LightNode,ElementNodeMixin):
    """Represents an FIGCAPTION HTML <figcaption> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lfigure(LightNode,ElementNodeMixin):
    """Represents an FIGURE HTML <figure> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lfooter(LightNode,ElementNodeMixin):
    """Represents an FOOTER HTML <footer> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lform(LightNode,ElementNodeMixin):
    """Represents an FORM HTML <form> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lh1(LightNode,ElementNodeMixin):
    """Represents an H1 HTML <h1> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lh2(LightNode,ElementNodeMixin):
    """Represents an H2 HTML <h2> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lh3(LightNode,ElementNodeMixin):
    """Represents an H3 HTML <h3> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Lh4(LightNode,ElementNodeMixin):
    """Represents an H4 HTML <h4> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lh5(LightNode,ElementNodeMixin):
    """Represents an H5 HTML <h5> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lh6(LightNode,ElementNodeMixin):
    """Represents an H6 HTML <h6> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lhead(LightNode,ElementNodeMixin):
    """Represents an HEAD HTML <head> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lheader(LightNode,ElementNodeMixin):
    """Represents an HEADER HTML <header> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lhgroup(LightNode,ElementNodeMixin):
    """Represents an HGROUP HTML <hgroup> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lhtml(LightNode,ElementNodeMixin):
    """Represents an HTML HTML <html> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Li(LightNode,ElementNodeMixin):
    """Represents an I HTML <i> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Liframe(LightNode,ElementNodeMixin):
    """Represents an IFRAME HTML <iframe> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lins(LightNode,ElementNodeMixin):
    """Represents an INS HTML <ins> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lkbd(LightNode,ElementNodeMixin):
    """Represents an KBD HTML <kbd> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Llabel(LightNode,ElementNodeMixin):
    """Represents an LABEL HTML <label> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Llegend(LightNode,ElementNodeMixin):
    """Represents an LEGEND HTML <legend> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lli(LightNode,ElementNodeMixin):
    """Represents an LI HTML <li> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lmain(LightNode,ElementNodeMixin):
    """Represents an MAIN HTML <main> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lmath(LightNode,ElementNodeMixin):
    """Represents an MATH HTML <math> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lmap(LightNode,ElementNodeMixin):
    """Represents an MAP HTML <map> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lmark(LightNode,ElementNodeMixin):
    """Represents an MARK HTML <mark> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lmenu(LightNode,ElementNodeMixin):
    """Represents an MENU HTML <menu> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lmeter(LightNode,ElementNodeMixin):
    """Represents an METER HTML <meter> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lnav(LightNode,ElementNodeMixin):
    """Represents an NAV HTML <nav> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lnoscript(LightNode,ElementNodeMixin):
    """Represents an NOSCRIPT HTML <noscript> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lobject(LightNode,ElementNodeMixin):
    """Represents an OBJECT HTML <object> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lol(LightNode,ElementNodeMixin):
    """Represents an OL HTML <ol> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Loptgroup(LightNode,ElementNodeMixin):
    """Represents an OPTGROUP HTML <optgroup> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Loption(LightNode,ElementNodeMixin):
    """Represents an OPTION HTML <option> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Loutput(LightNode,ElementNodeMixin):
    """Represents an OUTPUT HTML <output> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lp(LightNode,ElementNodeMixin):
    """Represents an P HTML <p> element."""
    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lportal(LightNode,ElementNodeMixin):
    """Represents an PORTAL HTML <portal> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lpicture(LightNode,ElementNodeMixin):
    """Represents an PICTURE HTML <picture> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lpre(LightNode,ElementNodeMixin):
    """Represents an PRE HTML <pre> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lprogress(LightNode,ElementNodeMixin):
    """Represents an PROGRESS HTML <progress> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lq(LightNode,ElementNodeMixin):
    """Represents an Q HTML <q> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lrp(LightNode,ElementNodeMixin):
    """Represents an RP HTML <rp> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lrt(LightNode,ElementNodeMixin):
    """Represents an RT HTML <rt> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lruby(LightNode,ElementNodeMixin):
    """Represents an RUBY HTML <ruby> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ls(LightNode,ElementNodeMixin):
    """Represents an S HTML <s> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lsamp(LightNode,ElementNodeMixin):
    """Represents an SAMP HTML <samp> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lscript(LightNode,ElementNodeMixin):
    """Represents an SCRIPT HTML <script> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lsearch(LightNode,ElementNodeMixin):
    """Represents an SEARCH HTML <search> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lsection(LightNode,ElementNodeMixin):
    """Represents an SECTION HTML <section> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lselect(LightNode,ElementNodeMixin):
    """Represents an SELECT HTML <select> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lslot(LightNode,ElementNodeMixin):
    """Represents an SLOT HTML <slot> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lsmall(LightNode,ElementNodeMixin):
    """Represents an SMALL HTML <small> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lspan(LightNode,ElementNodeMixin):
    """Represents an SPAN HTML <span> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lstrong(LightNode,ElementNodeMixin):
    """Represents an STRONG HTML <strong> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lstyle(LightNode,ElementNodeMixin):
    """Represents an STYLE HTML <style> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lsub(LightNode,ElementNodeMixin):
    """Represents an SUB HTML <sub> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lsummary(LightNode,ElementNodeMixin):
    """Represents an SUMMARY HTML <summary> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lsup(LightNode,ElementNodeMixin):
    """Represents an SUP HTML <sup> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)

class Ltable(LightNode,ElementNodeMixin):
    """Represents an TABLE HTML <table> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ltbody(LightNode,ElementNodeMixin):
    """Represents an TBODY HTML <tbody> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ltd(LightNode,ElementNodeMixin):
    """Represents an TD HTML <td> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ltemplate(LightNode,ElementNodeMixin):
    """Represents an TEMPLATE HTML <template> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ltextarea(LightNode,ElementNodeMixin):
    """Represents an TEXTAREA HTML <textarea> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ltfoot(LightNode,ElementNodeMixin):
    """Represents an TFOOT HTML <tfoot> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lth(LightNode,ElementNodeMixin):
    """Represents an TH HTML <th> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lthead(LightNode,ElementNodeMixin):
    """Represents an THEAD HTML <thead> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ltime(LightNode,ElementNodeMixin):
    """Represents an TIME HTML <time> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ltitle(LightNode,ElementNodeMixin):
    """Represents an TITLE HTML <title> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Ltr(LightNode,ElementNodeMixin):
    """Represents an TR HTML <tr> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lu(LightNode,ElementNodeMixin):
    """Represents an U HTML <u> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lul(LightNode,ElementNodeMixin):
    """Represents an UL HTML <ul> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lvar(LightNode,ElementNodeMixin):
    """Represents an VAR HTML <var> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)


class Lvideo(LightNode,ElementNodeMixin):
    """Represents an VIDEO HTML <video> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag=None, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)
    def stream(self, EL,batch: int = 50) -> Generator[str, None, None]:
        yield from super().stream(EL,batch)
