from probo.components.elements import Element
from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin
from typing import Any,Optional

EL = Element()

class A(BaseHTMLElement,ElementNodeMixin,):
    """Represents an A HTML <a> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:a = Element(
        ).set_attrs(**self.attributes).set_content(self.content).a().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .a()
            .element
        )

class ABBR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an ABBR HTML <abbr> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:abbr = Element(
        ).set_attrs(**self.attributes).set_content(self.content).abbr().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .abbr()
            .element
        )

class ADDRESS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an ADDRESS HTML <address> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:address = Element(
        ).set_attrs(**self.attributes).set_content(self.content).address().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .address()
            .element
        )

class ARTICLE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an ARTICLE HTML <article> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:article = Element(
        ).set_attrs(**self.attributes).set_content(self.content).article().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .article()
            .element
        )

class ASIDE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an ASIDE HTML <aside> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:aside = Element(
        ).set_attrs(**self.attributes).set_content(self.content).aside().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .aside()
            .element
        )

class AUDIO(BaseHTMLElement,ElementNodeMixin,):
    """Represents an AUDIO HTML <audio> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:audio = Element(
        ).set_attrs(**self.attributes).set_content(self.content).audio().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .audio()
            .element
        )

class B(BaseHTMLElement,ElementNodeMixin,):
    """Represents an B HTML <b> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:b = Element(
        ).set_attrs(**self.attributes).set_content(self.content).b().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .b()
            .element
        )

class BDI(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BDI HTML <bdi> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:bdi = Element(
        ).set_attrs(**self.attributes).set_content(self.content).bdi().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .bdi()
            .element
        )

class BDO(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BDO HTML <bdo> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:bdo = Element(
        ).set_attrs(**self.attributes).set_content(self.content).bdo().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .bdo()
            .element
        )

class BLOCKQUOTE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BLOCKQUOTE HTML <blockquote> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:blockquote = Element(
        ).set_attrs(**self.attributes).set_content(self.content).blockquote().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .blockquote()
            .element
        )

class BODY(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BODY HTML <body> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:body = Element(
        ).set_attrs(**self.attributes).set_content(self.content).body().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .body()
            .element
        )

class BUTTON(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BUTTON HTML <button> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:button = Element(
        ).set_attrs(**self.attributes).set_content(self.content).button().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .button()
            .element
        )

class CANVAS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an CANVAS HTML <canvas> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:canvas = Element(
        ).set_attrs(**self.attributes).set_content(self.content).canvas().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .canvas()
            .element
        )

class CAPTION(BaseHTMLElement,ElementNodeMixin,):
    """Represents an CAPTION HTML <caption> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:caption = Element(
        ).set_attrs(**self.attributes).set_content(self.content).caption().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .caption()
            .element
        )

class CITE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an CITE HTML <cite> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:cite = Element(
        ).set_attrs(**self.attributes).set_content(self.content).cite().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .cite()
            .element
        )

class CODE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an CODE HTML <code> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:code = Element(
        ).set_attrs(**self.attributes).set_content(self.content).code().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .code()
            .element
        )

class COLGROUP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an COLGROUP HTML <colgroup> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:colgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).colgroup().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .colgroup()
            .element
        )

class DATA(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DATA HTML <data> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:data = Element(
        ).set_attrs(**self.attributes).set_content(self.content).data().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .data()
            .element
        )

class DATALIST(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DATALIST HTML <datalist> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:datalist = Element(
        ).set_attrs(**self.attributes).set_content(self.content).datalist().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .datalist()
            .element
        )

class DD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DD HTML <dd> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:dd = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dd().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dd()
            .element
        )

class DEL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DEL HTML <del> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:del = Element(
        ).set_attrs(**self.attributes).set_content(self.content).del().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .Del()
            .element
        )

class DETAILS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DETAILS HTML <details> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:details = Element(
        ).set_attrs(**self.attributes).set_content(self.content).details().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .details()
            .element
        )

class DFN(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DFN HTML <dfn> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:dfn = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dfn().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dfn()
            .element
        )

class DIALOG(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DIALOG HTML <dialog> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:dialog = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dialog().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dialog()
            .element
        )

class DIV(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DIV HTML <div> element."""
    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:div = Element(
        ).set_attrs(**self.attributes).set_content(self.content).div().element'''

        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .div()
            .element
        )

class DL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DL HTML <dl> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:dl = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dl().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dl()
            .element
        )

class DT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DT HTML <dt> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:dt = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dt().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .dt()
            .element
        )

class EM(BaseHTMLElement,ElementNodeMixin,):
    """Represents an EM HTML <em> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:em = Element(
        ).set_attrs(**self.attributes).set_content(self.content).em().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .em()
            .element
        )

class FIELDSET(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FIELDSET HTML <fieldset> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:fieldset = Element(
        ).set_attrs(**self.attributes).set_content(self.content).fieldset().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .fieldset()
            .element
        )

class FIGCAPTION(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FIGCAPTION HTML <figcaption> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:figcaption = Element(
        ).set_attrs(**self.attributes).set_content(self.content).figcaption().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .figcaption()
            .element
        )

class FIGURE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FIGURE HTML <figure> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:figure = Element(
        ).set_attrs(**self.attributes).set_content(self.content).figure().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .figure()
            .element
        )

class FOOTER(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FOOTER HTML <footer> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:footer = Element(
        ).set_attrs(**self.attributes).set_content(self.content).footer().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .footer()
            .element
        )

class FORM(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FORM HTML <form> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:form = Element(
        ).set_attrs(**self.attributes).set_content(self.content).form().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .form()
            .element
        )

class H1(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H1 HTML <h1> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:h1 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h1().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h1()
            .element
        )

class H2(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H2 HTML <h2> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:h2 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h2().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h2()
            .element
        )

class H3(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H3 HTML <h3> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:h3 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h3().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h3()
            .element
        )

class H4(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H4 HTML <h4> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:h4 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h4().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h4()
            .element
        )


class H5(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H5 HTML <h5> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:h5 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h5().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h5()
            .element
        )


class H6(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H6 HTML <h6> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:h6 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h6().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .h6()
            .element
        )


class HEAD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HEAD HTML <head> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:head = Element(
        ).set_attrs(**self.attributes).set_content(self.content).head().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .head()
            .element
        )


class HEADER(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HEADER HTML <header> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:header = Element(
        ).set_attrs(**self.attributes).set_content(self.content).header().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .header()
            .element
        )


class HGROUP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HGROUP HTML <hgroup> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:hgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).hgroup().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .hgroup()
            .element
        )


class HTML(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HTML HTML <html> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:html = Element(
        ).set_attrs(**self.attributes).set_content(self.content).html().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .html()
            .element
        )


class I(BaseHTMLElement,ElementNodeMixin,):
    """Represents an I HTML <i> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:i = Element(
        ).set_attrs(**self.attributes).set_content(self.content).i().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .i()
            .element
        )


class IFRAME(BaseHTMLElement,ElementNodeMixin,):
    """Represents an IFRAME HTML <iframe> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:iframe = Element(
        ).set_attrs(**self.attributes).set_content(self.content).iframe().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .iframe()
            .element
        )


class INS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an INS HTML <ins> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:ins = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ins().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .ins()
            .element
        )


class KBD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an KBD HTML <kbd> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:kbd = Element(
        ).set_attrs(**self.attributes).set_content(self.content).kbd().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .kbd()
            .element
        )


class LABEL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an LABEL HTML <label> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:label = Element(
        ).set_attrs(**self.attributes).set_content(self.content).label().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .label()
            .element
        )


class LEGEND(BaseHTMLElement,ElementNodeMixin,):
    """Represents an LEGEND HTML <legend> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:legend = Element(
        ).set_attrs(**self.attributes).set_content(self.content).legend().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .legend()
            .element
        )


class LI(BaseHTMLElement,ElementNodeMixin,):
    """Represents an LI HTML <li> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:li = Element(
        ).set_attrs(**self.attributes).set_content(self.content).li().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .li()
            .element
        )


class MAIN(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MAIN HTML <main> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:main = Element(
        ).set_attrs(**self.attributes).set_content(self.content).main().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .main()
            .element
        )


class MATH(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MATH HTML <math> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:math = Element(
        ).set_attrs(**self.attributes).set_content(self.content).math().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .math()
            .element
        )


class MAP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MAP HTML <map> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:map = Element(
        ).set_attrs(**self.attributes).set_content(self.content).map().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .Map()
            .element
        )


class MARK(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MARK HTML <mark> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:mark = Element(
        ).set_attrs(**self.attributes).set_content(self.content).mark().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .mark()
            .element
        )


class MENU(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MENU HTML <menu> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:menu = Element(
        ).set_attrs(**self.attributes).set_content(self.content).menu().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .menu()
            .element
        )


class METER(BaseHTMLElement,ElementNodeMixin,):
    """Represents an METER HTML <meter> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .meter()
            .element
        )


class NAV(BaseHTMLElement,ElementNodeMixin,):
    """Represents an NAV HTML <nav> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:nav = Element(
        ).set_attrs(**self.attributes).set_content(self.content).nav().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .nav()
            .element
        )


class NOSCRIPT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an NOSCRIPT HTML <noscript> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:noscript = Element(
        ).set_attrs(**self.attributes).set_content(self.content).noscript().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .noscript()
            .element
        )


class OBJECT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OBJECT HTML <object> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:object = Element(
        ).set_attrs(**self.attributes).set_content(self.content).object().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .object()
            .element
        )


class OL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OL HTML <ol> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:ol = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ol().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .ol()
            .element
        )


class OPTGROUP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OPTGROUP HTML <optgroup> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:optgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).optgroup().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .optgroup()
            .element
        )


class OPTION(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OPTION HTML <option> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:option = Element(
        ).set_attrs(**self.attributes).set_content(self.content).option().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .option()
            .element
        )


class OUTPUT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OUTPUT HTML <output> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:output = Element(
        ).set_attrs(**self.attributes).set_content(self.content).output().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .output()
            .element
        )


class P(BaseHTMLElement,ElementNodeMixin,):
    """Represents an P HTML <p> element."""
    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:p = Element(
        ).set_attrs(**self.attributes).set_content(self.content).p().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .p()
            .element
        )


class PORTAL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PORTAL HTML <portal> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:portal = Element(
        ).set_attrs(**self.attributes).set_content(self.content).portal().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .portal()
            .element
        )


class PICTURE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PICTURE HTML <picture> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:picture = Element(
        ).set_attrs(**self.attributes).set_content(self.content).picture().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .picture()
            .element
        )


class PRE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PRE HTML <pre> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:pre = Element(
        ).set_attrs(**self.attributes).set_content(self.content).pre().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .pre()
            .element
        )


class PROGRESS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PROGRESS HTML <progress> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:progress = Element(
        ).set_attrs(**self.attributes).set_content(self.content).progress().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .progress()
            .element
        )


class Q(BaseHTMLElement,ElementNodeMixin,):
    """Represents an Q HTML <q> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:q = Element(
        ).set_attrs(**self.attributes).set_content(self.content).q().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .q()
            .element
        )


class RP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an RP HTML <rp> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:rp = Element(
        ).set_attrs(**self.attributes).set_content(self.content).rp().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .rp()
            .element
        )


class RT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an RT HTML <rt> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:rt = Element(
        ).set_attrs(**self.attributes).set_content(self.content).rt().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .rt()
            .element
        )


class RUBY(BaseHTMLElement,ElementNodeMixin,):
    """Represents an RUBY HTML <ruby> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:ruby = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ruby().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .ruby()
            .element
        )


class S(BaseHTMLElement,ElementNodeMixin,):
    """Represents an S HTML <s> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:s = Element(
        ).set_attrs(**self.attributes).set_content(self.content).s().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .s()
            .element
        )


class SAMP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SAMP HTML <samp> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:samp = Element(
        ).set_attrs(**self.attributes).set_content(self.content).samp().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .samp()
            .element
        )


class SCRIPT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SCRIPT HTML <script> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:script = Element(
        ).set_attrs(**self.attributes).set_content(self.content).script().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .script()
            .element
        )


class SEARCH(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SEARCH HTML <search> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:search = Element(
        ).set_attrs(**self.attributes).set_content(self.content).search().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .search()
            .element
        )


class SECTION(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SECTION HTML <section> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:section = Element(
        ).set_attrs(**self.attributes).set_content(self.content).section().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .section()
            .element
        )


class SELECT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SELECT HTML <select> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:select = Element(
        ).set_attrs(**self.attributes).set_content(self.content).select().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .select()
            .element
        )


class SLOT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SLOT HTML <slot> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:slot = Element(
        ).set_attrs(**self.attributes).set_content(self.content).slot().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .slot()
            .element
        )


class SMALL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SMALL HTML <small> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:small = Element(
        ).set_attrs(**self.attributes).set_content(self.content).small().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .small()
            .element
        )


class SPAN(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SPAN HTML <span> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:span = Element(
        ).set_attrs(**self.attributes).set_content(self.content).span().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .span()
            .element
        )


class STRONG(BaseHTMLElement,ElementNodeMixin,):
    """Represents an STRONG HTML <strong> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:strong = Element(
        ).set_attrs(**self.attributes).set_content(self.content).strong().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .strong()
            .element
        )


class STYLE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an STYLE HTML <style> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:style = Element(
        ).set_attrs(**self.attributes).set_content(self.content).style().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .style()
            .element
        )


class SUB(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SUB HTML <sub> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:sub = Element(
        ).set_attrs(**self.attributes).set_content(self.content).sub().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .sub()
            .element
        )


class SUMMARY(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SUMMARY HTML <summary> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:summary = Element(
        ).set_attrs(**self.attributes).set_content(self.content).summary().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .summary()
            .element
        )


class SUP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SUP HTML <sup> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:sup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).sup().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .sup()
            .element
        )

class TABLE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TABLE HTML <table> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:table = Element(
        ).set_attrs(**self.attributes).set_content(self.content).table().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .table()
            .element
        )


class TBODY(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TBODY HTML <tbody> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:tbody = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tbody().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .tbody()
            .element
        )


class TD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TD HTML <td> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:td = Element(
        ).set_attrs(**self.attributes).set_content(self.content).td().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .td()
            .element
        )


class TEMPLATE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TEMPLATE HTML <template> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:template = Element(
        ).set_attrs(**self.attributes).set_content(self.content).template().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .template()
            .element
        )


class TEXTAREA(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TEXTAREA HTML <textarea> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:textarea = Element(
        ).set_attrs(**self.attributes).set_content(self.content).textarea().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .textarea()
            .element
        )


class TFOOT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TFOOT HTML <tfoot> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:tfoot = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tfoot().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .tfoot()
            .element
        )


class TH(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TH HTML <th> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:th = Element(
        ).set_attrs(**self.attributes).set_content(self.content).th().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .th()
            .element
        )


class THEAD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an THEAD HTML <thead> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:thead = Element(
        ).set_attrs(**self.attributes).set_content(self.content).thead().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .thead()
            .element
        )


class TIME(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TIME HTML <time> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:time = Element(
        ).set_attrs(**self.attributes).set_content(self.content).time().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .time()
            .element
        )


class TITLE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TITLE HTML <title> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:title = Element(
        ).set_attrs(**self.attributes).set_content(self.content).title().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .title()
            .element
        )


class TR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TR HTML <tr> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:tr = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tr().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .tr()
            .element
        )


class U(BaseHTMLElement,ElementNodeMixin,):
    """Represents an U HTML <u> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:u = Element(
        ).set_attrs(**self.attributes).set_content(self.content).u().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .u()
            .element
        )


class UL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an UL HTML <ul> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:ul = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ul().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .ul()
            .element
        )


class VAR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an VAR HTML <var> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:var = Element(
        ).set_attrs(**self.attributes).set_content(self.content).var().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .var()
            .element
        )


class VIDEO(BaseHTMLElement,ElementNodeMixin,):
    """Represents an VIDEO HTML <video> element."""

    __slots__ = ()
    def __init__(self, *content:tuple[str | ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self)->str:
        '''
        Blueprint:video = Element(
        ).set_attrs(**self.attributes).set_content(self.content).video().element'''
        content=self._get_rendered_content()
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .video()
            .element
        )
