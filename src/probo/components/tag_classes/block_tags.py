from probo.components.elements import Element
from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin

# --- Specific HTML Block Element Classes (accepting content and attributes) ---
# These classes now use the `Element` helper class as per your blueprint.


class A(BaseHTMLElement,ElementNodeMixin,):
    """Represents an A HTML <a> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:a = Element(
        ).set_attrs(**self.attributes).set_content(self.content).a().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .a()
            .element
        )


class ABBR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an ABBR HTML <abbr> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:abbr = Element(
        ).set_attrs(**self.attributes).set_content(self.content).abbr().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .abbr()
            .element
        )


class ADDRESS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an ADDRESS HTML <address> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:address = Element(
        ).set_attrs(**self.attributes).set_content(self.content).address().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .address()
            .element
        )


class ARTICLE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an ARTICLE HTML <article> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:article = Element(
        ).set_attrs(**self.attributes).set_content(self.content).article().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .article()
            .element
        )


class ASIDE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an ASIDE HTML <aside> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:aside = Element(
        ).set_attrs(**self.attributes).set_content(self.content).aside().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .aside()
            .element
        )


class AUDIO(BaseHTMLElement,ElementNodeMixin,):
    """Represents an AUDIO HTML <audio> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:audio = Element(
        ).set_attrs(**self.attributes).set_content(self.content).audio().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .audio()
            .element
        )


class B(BaseHTMLElement,ElementNodeMixin,):
    """Represents an B HTML <b> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:b = Element(
        ).set_attrs(**self.attributes).set_content(self.content).b().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .b()
            .element
        )


class BDI(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BDI HTML <bdi> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:bdi = Element(
        ).set_attrs(**self.attributes).set_content(self.content).bdi().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .bdi()
            .element
        )


class BDO(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BDO HTML <bdo> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:bdo = Element(
        ).set_attrs(**self.attributes).set_content(self.content).bdo().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .bdo()
            .element
        )


class BLOCKQUOTE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BLOCKQUOTE HTML <blockquote> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:blockquote = Element(
        ).set_attrs(**self.attributes).set_content(self.content).blockquote().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .blockquote()
            .element
        )


class BODY(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BODY HTML <body> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:body = Element(
        ).set_attrs(**self.attributes).set_content(self.content).body().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .body()
            .element
        )


class BUTTON(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BUTTON HTML <button> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:button = Element(
        ).set_attrs(**self.attributes).set_content(self.content).button().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .button()
            .element
        )


class CANVAS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an CANVAS HTML <canvas> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:canvas = Element(
        ).set_attrs(**self.attributes).set_content(self.content).canvas().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .canvas()
            .element
        )


class CAPTION(BaseHTMLElement,ElementNodeMixin,):
    """Represents an CAPTION HTML <caption> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:caption = Element(
        ).set_attrs(**self.attributes).set_content(self.content).caption().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .caption()
            .element
        )


class CITE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an CITE HTML <cite> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:cite = Element(
        ).set_attrs(**self.attributes).set_content(self.content).cite().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .cite()
            .element
        )


class CODE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an CODE HTML <code> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:code = Element(
        ).set_attrs(**self.attributes).set_content(self.content).code().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .code()
            .element
        )


class COLGROUP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an COLGROUP HTML <colgroup> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:colgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).colgroup().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .colgroup()
            .element
        )


class DATA(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DATA HTML <data> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:data = Element(
        ).set_attrs(**self.attributes).set_content(self.content).data().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .data()
            .element
        )


class DATALIST(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DATALIST HTML <datalist> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:datalist = Element(
        ).set_attrs(**self.attributes).set_content(self.content).datalist().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .datalist()
            .element
        )


class DD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DD HTML <dd> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:dd = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dd().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .dd()
            .element
        )


class DEL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DEL HTML <del> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:del = Element(
        ).set_attrs(**self.attributes).set_content(self.content).del().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .Del()
            .element
        )


class DETAILS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DETAILS HTML <details> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:details = Element(
        ).set_attrs(**self.attributes).set_content(self.content).details().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .details()
            .element
        )


class DFN(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DFN HTML <dfn> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:dfn = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dfn().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .dfn()
            .element
        )


class DIALOG(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DIALOG HTML <dialog> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:dialog = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dialog().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .dialog()
            .element
        )


class DIV(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DIV HTML <div> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:div = Element(
        ).set_attrs(**self.attributes).set_content(self.content).div().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .div()
            .element
        )


class DL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DL HTML <dl> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:dl = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dl().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .dl()
            .element
        )


class DT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DT HTML <dt> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:dt = Element(
        ).set_attrs(**self.attributes).set_content(self.content).dt().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .dt()
            .element
        )


class EM(BaseHTMLElement,ElementNodeMixin,):
    """Represents an EM HTML <em> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:em = Element(
        ).set_attrs(**self.attributes).set_content(self.content).em().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .em()
            .element
        )


class FIELDSET(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FIELDSET HTML <fieldset> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:fieldset = Element(
        ).set_attrs(**self.attributes).set_content(self.content).fieldset().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .fieldset()
            .element
        )


class FIGCAPTION(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FIGCAPTION HTML <figcaption> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:figcaption = Element(
        ).set_attrs(**self.attributes).set_content(self.content).figcaption().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .figcaption()
            .element
        )


class FIGURE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FIGURE HTML <figure> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:figure = Element(
        ).set_attrs(**self.attributes).set_content(self.content).figure().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .figure()
            .element
        )


class FOOTER(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FOOTER HTML <footer> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:footer = Element(
        ).set_attrs(**self.attributes).set_content(self.content).footer().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .footer()
            .element
        )


class FORM(BaseHTMLElement,ElementNodeMixin,):
    """Represents an FORM HTML <form> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:form = Element(
        ).set_attrs(**self.attributes).set_content(self.content).form().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .form()
            .element
        )


class H1(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H1 HTML <h1> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:h1 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h1().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .h1()
            .element
        )


class H2(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H2 HTML <h2> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:h2 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h2().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .h2()
            .element
        )


class H3(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H3 HTML <h3> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:h3 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h3().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .h3()
            .element
        )


class H4(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H4 HTML <h4> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:h4 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h4().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .h4()
            .element
        )


class H5(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H5 HTML <h5> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:h5 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h5().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .h5()
            .element
        )


class H6(BaseHTMLElement,ElementNodeMixin,):
    """Represents an H6 HTML <h6> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:h6 = Element(
        ).set_attrs(**self.attributes).set_content(self.content).h6().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .h6()
            .element
        )


class HEAD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HEAD HTML <head> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:head = Element(
        ).set_attrs(**self.attributes).set_content(self.content).head().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .head()
            .element
        )


class HEADER(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HEADER HTML <header> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:header = Element(
        ).set_attrs(**self.attributes).set_content(self.content).header().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .header()
            .element
        )


class HGROUP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HGROUP HTML <hgroup> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:hgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).hgroup().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .hgroup()
            .element
        )


class HTML(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HTML HTML <html> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:html = Element(
        ).set_attrs(**self.attributes).set_content(self.content).html().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .html()
            .element
        )


class I(BaseHTMLElement,ElementNodeMixin,):
    """Represents an I HTML <i> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:i = Element(
        ).set_attrs(**self.attributes).set_content(self.content).i().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .i()
            .element
        )


class IFRAME(BaseHTMLElement,ElementNodeMixin,):
    """Represents an IFRAME HTML <iframe> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:iframe = Element(
        ).set_attrs(**self.attributes).set_content(self.content).iframe().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .iframe()
            .element
        )


class INS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an INS HTML <ins> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:ins = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ins().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .ins()
            .element
        )


class KBD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an KBD HTML <kbd> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:kbd = Element(
        ).set_attrs(**self.attributes).set_content(self.content).kbd().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .kbd()
            .element
        )


class LABEL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an LABEL HTML <label> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:label = Element(
        ).set_attrs(**self.attributes).set_content(self.content).label().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .label()
            .element
        )


class LEGEND(BaseHTMLElement,ElementNodeMixin,):
    """Represents an LEGEND HTML <legend> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:legend = Element(
        ).set_attrs(**self.attributes).set_content(self.content).legend().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .legend()
            .element
        )


class LI(BaseHTMLElement,ElementNodeMixin,):
    """Represents an LI HTML <li> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:li = Element(
        ).set_attrs(**self.attributes).set_content(self.content).li().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .li()
            .element
        )


class MAIN(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MAIN HTML <main> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:main = Element(
        ).set_attrs(**self.attributes).set_content(self.content).main().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .main()
            .element
        )


class MATH(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MATH HTML <math> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:math = Element(
        ).set_attrs(**self.attributes).set_content(self.content).math().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .math()
            .element
        )


class MAP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MAP HTML <map> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:map = Element(
        ).set_attrs(**self.attributes).set_content(self.content).map().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .Map()
            .element
        )


class MARK(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MARK HTML <mark> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:mark = Element(
        ).set_attrs(**self.attributes).set_content(self.content).mark().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .mark()
            .element
        )


class MENU(BaseHTMLElement,ElementNodeMixin,):
    """Represents an MENU HTML <menu> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:menu = Element(
        ).set_attrs(**self.attributes).set_content(self.content).menu().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .menu()
            .element
        )


class METER(BaseHTMLElement,ElementNodeMixin,):
    """Represents an METER HTML <meter> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:meter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).meter().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .meter()
            .element
        )


class NAV(BaseHTMLElement,ElementNodeMixin,):
    """Represents an NAV HTML <nav> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:nav = Element(
        ).set_attrs(**self.attributes).set_content(self.content).nav().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .nav()
            .element
        )


class NOSCRIPT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an NOSCRIPT HTML <noscript> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:noscript = Element(
        ).set_attrs(**self.attributes).set_content(self.content).noscript().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .noscript()
            .element
        )


class OBJECT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OBJECT HTML <object> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:object = Element(
        ).set_attrs(**self.attributes).set_content(self.content).object().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .object()
            .element
        )


class OL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OL HTML <ol> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:ol = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ol().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .ol()
            .element
        )


class OPTGROUP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OPTGROUP HTML <optgroup> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:optgroup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).optgroup().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .optgroup()
            .element
        )


class OPTION(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OPTION HTML <option> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:option = Element(
        ).set_attrs(**self.attributes).set_content(self.content).option().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .option()
            .element
        )


class OUTPUT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an OUTPUT HTML <output> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:output = Element(
        ).set_attrs(**self.attributes).set_content(self.content).output().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .output()
            .element
        )


class P(BaseHTMLElement,ElementNodeMixin,):
    """Represents an P HTML <p> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:p = Element(
        ).set_attrs(**self.attributes).set_content(self.content).p().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .p()
            .element
        )


class PORTAL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PORTAL HTML <portal> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:portal = Element(
        ).set_attrs(**self.attributes).set_content(self.content).portal().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .portal()
            .element
        )


class PICTURE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PICTURE HTML <picture> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:picture = Element(
        ).set_attrs(**self.attributes).set_content(self.content).picture().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .picture()
            .element
        )


class PRE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PRE HTML <pre> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:pre = Element(
        ).set_attrs(**self.attributes).set_content(self.content).pre().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .pre()
            .element
        )


class PROGRESS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PROGRESS HTML <progress> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:progress = Element(
        ).set_attrs(**self.attributes).set_content(self.content).progress().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .progress()
            .element
        )


class Q(BaseHTMLElement,ElementNodeMixin,):
    """Represents an Q HTML <q> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:q = Element(
        ).set_attrs(**self.attributes).set_content(self.content).q().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .q()
            .element
        )


class RP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an RP HTML <rp> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:rp = Element(
        ).set_attrs(**self.attributes).set_content(self.content).rp().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .rp()
            .element
        )


class RT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an RT HTML <rt> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:rt = Element(
        ).set_attrs(**self.attributes).set_content(self.content).rt().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .rt()
            .element
        )


class RUBY(BaseHTMLElement,ElementNodeMixin,):
    """Represents an RUBY HTML <ruby> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:ruby = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ruby().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .ruby()
            .element
        )


class S(BaseHTMLElement,ElementNodeMixin,):
    """Represents an S HTML <s> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:s = Element(
        ).set_attrs(**self.attributes).set_content(self.content).s().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .s()
            .element
        )


class SAMP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SAMP HTML <samp> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:samp = Element(
        ).set_attrs(**self.attributes).set_content(self.content).samp().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .samp()
            .element
        )


class SCRIPT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SCRIPT HTML <script> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:script = Element(
        ).set_attrs(**self.attributes).set_content(self.content).script().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .script()
            .element
        )


class SEARCH(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SEARCH HTML <search> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:search = Element(
        ).set_attrs(**self.attributes).set_content(self.content).search().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .search()
            .element
        )


class SECTION(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SECTION HTML <section> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:section = Element(
        ).set_attrs(**self.attributes).set_content(self.content).section().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .section()
            .element
        )


class SELECT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SELECT HTML <select> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:select = Element(
        ).set_attrs(**self.attributes).set_content(self.content).select().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .select()
            .element
        )


class SLOT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SLOT HTML <slot> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:slot = Element(
        ).set_attrs(**self.attributes).set_content(self.content).slot().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .slot()
            .element
        )


class SMALL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SMALL HTML <small> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:small = Element(
        ).set_attrs(**self.attributes).set_content(self.content).small().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .small()
            .element
        )


class SPAN(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SPAN HTML <span> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:span = Element(
        ).set_attrs(**self.attributes).set_content(self.content).span().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .span()
            .element
        )


class STRONG(BaseHTMLElement,ElementNodeMixin,):
    """Represents an STRONG HTML <strong> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:strong = Element(
        ).set_attrs(**self.attributes).set_content(self.content).strong().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .strong()
            .element
        )


class STYLE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an STYLE HTML <style> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:style = Element(
        ).set_attrs(**self.attributes).set_content(self.content).style().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .style()
            .element
        )


class SUB(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SUB HTML <sub> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:sub = Element(
        ).set_attrs(**self.attributes).set_content(self.content).sub().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .sub()
            .element
        )


class SUMMARY(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SUMMARY HTML <summary> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:summary = Element(
        ).set_attrs(**self.attributes).set_content(self.content).summary().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .summary()
            .element
        )


class SUP(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SUP HTML <sup> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:sup = Element(
        ).set_attrs(**self.attributes).set_content(self.content).sup().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .sup()
            .element
        )


class SVG(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SVG HTML <svg> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:svg = Element(
        ).set_attrs(**self.attributes).set_content(self.content).svg().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .svg()
            .element
        )


class TABLE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TABLE HTML <table> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:table = Element(
        ).set_attrs(**self.attributes).set_content(self.content).table().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .table()
            .element
        )


class TBODY(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TBODY HTML <tbody> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:tbody = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tbody().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .tbody()
            .element
        )


class TD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TD HTML <td> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:td = Element(
        ).set_attrs(**self.attributes).set_content(self.content).td().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .td()
            .element
        )


class TEMPLATE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TEMPLATE HTML <template> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:template = Element(
        ).set_attrs(**self.attributes).set_content(self.content).template().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .template()
            .element
        )


class TEXTAREA(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TEXTAREA HTML <textarea> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:textarea = Element(
        ).set_attrs(**self.attributes).set_content(self.content).textarea().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .textarea()
            .element
        )


class TFOOT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TFOOT HTML <tfoot> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:tfoot = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tfoot().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .tfoot()
            .element
        )


class TH(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TH HTML <th> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:th = Element(
        ).set_attrs(**self.attributes).set_content(self.content).th().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .th()
            .element
        )


class THEAD(BaseHTMLElement,ElementNodeMixin,):
    """Represents an THEAD HTML <thead> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:thead = Element(
        ).set_attrs(**self.attributes).set_content(self.content).thead().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .thead()
            .element
        )


class TIME(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TIME HTML <time> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:time = Element(
        ).set_attrs(**self.attributes).set_content(self.content).time().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .time()
            .element
        )


class TITLE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TITLE HTML <title> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:title = Element(
        ).set_attrs(**self.attributes).set_content(self.content).title().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .title()
            .element
        )


class TR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TR HTML <tr> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:tr = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tr().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .tr()
            .element
        )


class U(BaseHTMLElement,ElementNodeMixin,):
    """Represents an U HTML <u> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:u = Element(
        ).set_attrs(**self.attributes).set_content(self.content).u().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .u()
            .element
        )


class UL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an UL HTML <ul> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:ul = Element(
        ).set_attrs(**self.attributes).set_content(self.content).ul().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .ul()
            .element
        )


class VAR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an VAR HTML <var> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:var = Element(
        ).set_attrs(**self.attributes).set_content(self.content).var().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .var()
            .element
        )


class VIDEO(BaseHTMLElement,ElementNodeMixin,):
    """Represents an VIDEO HTML <video> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:video = Element(
        ).set_attrs(**self.attributes).set_content(self.content).video().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .video()
            .element
        )


class G(BaseHTMLElement,ElementNodeMixin,):
    """Represents an G HTML <g> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:g = Element(
        ).set_attrs(**self.attributes).set_content(self.content).g().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .g()
            .element
        )


class DEFS(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DEFS HTML <defs> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:defs = Element(
        ).set_attrs(**self.attributes).set_content(self.content).defs().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .defs()
            .element
        )


class TEXT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TEXT HTML <text> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:text = Element(
        ).set_attrs(**self.attributes).set_content(self.content).text().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .text()
            .element
        )


class TSPAN(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TSPAN HTML <tspan> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)

    def render(self):
        '''
        Blueprint:tspan = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tspan().element'''
        return (
            Element()
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .tspan()
            .element
        )
