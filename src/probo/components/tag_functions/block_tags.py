from src.probo.components.tag_classes import block_tags

# --- Specific HTML Block Element Classes (accepting content and attributes) ---
# These classes now use the `Element` helper class as per your blueprint.


def a(*content, **attrs):
    """Represents an HTML <a> element."""
    return block_tags.A(*content, **attrs).render()


def abbr(*content, **attrs):
    """Represents an HTML <abbr> element."""
    return block_tags.ABBR(*content, **attrs).render()


def address(*content, **attrs):
    """Represents an HTML <address> element."""
    return block_tags.ADDRESS(*content, **attrs).render()


def article(*content, **attrs):
    """Represents an HTML <article> element."""
    return block_tags.ARTICLE(*content, **attrs).render()


def aside(*content, **attrs):
    """Represents an HTML <aside> element."""
    return block_tags.ASIDE(*content, **attrs).render()


def audio(*content, **attrs):
    """Represents an HTML <audio> element."""
    return block_tags.AUDIO(*content, **attrs).render()


def b(*content, **attrs):
    """Represents an HTML <b> element."""
    return block_tags.B(*content, **attrs).render()


def bdi(*content, **attrs):
    """Represents an HTML <bdi> element."""
    return block_tags.BDI(*content, **attrs).render()


def bdo(*content, **attrs):
    """Represents an HTML <bdo> element."""
    return block_tags.BDO(*content, **attrs).render()


def blockquote(*content, **attrs):
    """Represents an HTML <blockquote> element."""
    return block_tags.BLOCKQUOTE(*content, **attrs).render()


def body(*content, **attrs):
    """Represents an HTML <body> element."""
    return block_tags.BODY(*content, **attrs).render()


def button(*content, **attrs):
    """Represents an HTML <button> element."""
    return block_tags.BUTTON(*content, **attrs).render()


def canvas(*content, **attrs):
    """Represents an HTML <canvas> element."""
    return block_tags.CANVAS(*content, **attrs).render()


def caption(*content, **attrs):
    """Represents an HTML <caption> element."""
    return block_tags.CAPTION(*content, **attrs).render()


def cite(*content, **attrs):
    """Represents an HTML <cite> element."""
    return block_tags.CITE(*content, **attrs).render()


def code(*content, **attrs):
    """Represents an HTML <code> element."""
    return block_tags.CODE(*content, **attrs).render()


def colgroup(*content, **attrs):
    """Represents an HTML <colgroup> element."""
    return block_tags.COLGROUP(*content, **attrs).render()


def data(*content, **attrs):
    """Represents an HTML <data> element."""
    return block_tags.DATA(*content, **attrs).render()


def datalist(*content, **attrs):
    """Represents an HTML <datalist> element."""
    return block_tags.DATALIST(*content, **attrs).render()


def dd(*content, **attrs):
    """Represents an HTML <dd> element."""
    return block_tags.DD(*content, **attrs).render()


def Del(*content, **attrs):
    """Represents an HTML <del> element."""
    return block_tags.DEL(*content, **attrs).render()


def details(*content, **attrs):
    """Represents an HTML <details> element."""
    return block_tags.DETAILS(*content, **attrs).render()


def dfn(*content, **attrs):
    """Represents an HTML <dfn> element."""
    return block_tags.DFN(*content, **attrs).render()


def dialog(*content, **attrs):
    """Represents an HTML <dialog> element."""
    return block_tags.DIALOG(*content, **attrs).render()


def div(*content, **attrs):
    """Represents an HTML <div> element."""
    return block_tags.DIV(*content, **attrs).render()


def dl(*content, **attrs):
    """Represents an HTML <dl> element."""
    return block_tags.DL(*content, **attrs).render()


def dt(*content, **attrs):
    """Represents an HTML <dt> element."""
    return block_tags.DT(*content, **attrs).render()


def em(*content, **attrs):
    """Represents an HTML <em> element."""
    return block_tags.EM(*content, **attrs).render()


def fieldset(*content, **attrs):
    """Represents an HTML <fieldset> element."""
    return block_tags.FIELDSET(*content, **attrs).render()


def figcaption(*content, **attrs):
    """Represents an HTML <figcaption> element."""
    return block_tags.FIGCAPTION(*content, **attrs).render()


def figure(*content, **attrs):
    """Represents an HTML <figure> element."""
    return block_tags.FIGURE(*content, **attrs).render()


def footer(*content, **attrs):
    """Represents an HTML <footer> element."""
    return block_tags.FOOTER(*content, **attrs).render()


def form(*content, **attrs):
    """Represents an HTML <form> element."""
    return block_tags.FORM(*content, **attrs).render()


def h1(*content, **attrs):
    """Represents an HTML <h1> element."""
    return block_tags.H1(*content, **attrs).render()


def h2(*content, **attrs):
    """Represents an HTML <h2> element."""
    return block_tags.H2(*content, **attrs).render()


def h3(*content, **attrs):
    """Represents an HTML <h3> element."""
    return block_tags.H3(*content, **attrs).render()


def h4(*content, **attrs):
    """Represents an HTML <h4> element."""
    return block_tags.H4(*content, **attrs).render()


def h5(*content, **attrs):
    """Represents an HTML <h5> element."""
    return block_tags.H5(*content, **attrs).render()


def h6(*content, **attrs):
    """Represents an HTML <h6> element."""
    return block_tags.H6(*content, **attrs).render()


def head(*content, **attrs):
    """Represents an HTML <head> element."""
    return block_tags.HEAD(*content, **attrs).render()


def header(*content, **attrs):
    """Represents an HTML <header> element."""
    return block_tags.HEADER(*content, **attrs).render()


def hgroup(*content, **attrs):
    """Represents an HTML <hgroup> element."""
    return block_tags.HGROUP(*content, **attrs).render()


def html(*content, **attrs):
    """Represents an HTML <html> element."""
    return block_tags.HTML(*content, **attrs).render()


def i(*content, **attrs):
    """Represents an HTML <i> element."""
    return block_tags.I(*content, **attrs).render()


def iframe(*content, **attrs):
    """Represents an HTML <iframe> element."""
    return block_tags.IFRAME(*content, **attrs).render()


def ins(*content, **attrs):
    """Represents an HTML <ins> element."""
    return block_tags.INS(*content, **attrs).render()


def kbd(*content, **attrs):
    """Represents an HTML <kbd> element."""
    return block_tags.KBD(*content, **attrs).render()


def label(*content, **attrs):
    """Represents an HTML <label> element."""
    return block_tags.LABEL(*content, **attrs).render()


def legend(*content, **attrs):
    """Represents an HTML <legend> element."""
    return block_tags.LEGEND(*content, **attrs).render()


def li(*content, **attrs):
    """Represents an HTML <li> element."""
    return block_tags.LI(*content, **attrs).render()


def main(*content, **attrs):
    """Represents an HTML <main> element."""
    return block_tags.MAIN(*content, **attrs).render()


def math(*content, **attrs):
    """Represents an HTML <math> element."""
    return block_tags.MATH(*content, **attrs).render()


def Map(*content, **attrs):
    """Represents an HTML <map> element."""
    return block_tags.MAP(*content, **attrs).render()


def mark(*content, **attrs):
    """Represents an HTML <mark> element."""
    return block_tags.MARK(*content, **attrs).render()


def menu(*content, **attrs):
    """Represents an HTML <menu> element."""
    return block_tags.MENU(*content, **attrs).render()


def meter(*content, **attrs):
    """Represents an HTML <meter> element."""
    return block_tags.METER(*content, **attrs).render()


def nav(*content, **attrs):
    """Represents an HTML <nav> element."""
    return block_tags.NAV(*content, **attrs).render()


def noscript(*content, **attrs):
    """Represents an HTML <noscript> element."""
    return block_tags.NOSCRIPT(*content, **attrs).render()


def Object(*content, **attrs):
    """Represents an HTML <object> element."""
    return block_tags.OBJECT(*content, **attrs).render()


def ol(*content, **attrs):
    """Represents an HTML <ol> element."""
    return block_tags.OL(*content, **attrs).render()


def optgroup(*content, **attrs):
    """Represents an HTML <optgroup> element."""
    return block_tags.OPTGROUP(*content, **attrs).render()


def option(*content, **attrs):
    """Represents an HTML <option> element."""
    return block_tags.OPTION(*content, **attrs).render()


def output(*content, **attrs):
    """Represents an HTML <output> element."""
    return block_tags.OUTPUT(*content, **attrs).render()


def p(*content, **attrs):
    """Represents an HTML <p> element."""
    return block_tags.P(*content, **attrs).render()


def portal(*content, **attrs):
    """Represents an HTML <portal> element."""
    return block_tags.PORTAL(*content, **attrs).render()


def picture(*content, **attrs):
    """Represents an HTML <picture> element."""
    return block_tags.PICTURE(*content, **attrs).render()


def pre(*content, **attrs):
    """Represents an HTML <pre> element."""
    return block_tags.PRE(*content, **attrs).render()


def progress(*content, **attrs):
    """Represents an HTML <progress> element."""
    return block_tags.PROGRESS(*content, **attrs).render()


def q(*content, **attrs):
    """Represents an HTML <q> element."""
    return block_tags.Q(*content, **attrs).render()


def rp(*content, **attrs):
    """Represents an HTML <rp> element."""
    return block_tags.RP(*content, **attrs).render()


def rt(*content, **attrs):
    """Represents an HTML <rt> element."""
    return block_tags.RT(*content, **attrs).render()


def ruby(*content, **attrs):
    """Represents an HTML <ruby> element."""
    return block_tags.RUBY(*content, **attrs).render()


def s(*content, **attrs):
    """Represents an HTML <s> element."""
    return block_tags.S(*content, **attrs).render()


def samp(*content, **attrs):
    """Represents an HTML <samp> element."""
    return block_tags.SAMP(*content, **attrs).render()


def script(*content, **attrs):
    """Represents an HTML <script> element."""
    return block_tags.SCRIPT(*content, **attrs).render()


def search(*content, **attrs):
    """Represents an HTML <search> element."""
    return block_tags.SEARCH(*content, **attrs).render()


def section(*content, **attrs):
    """Represents an HTML <section> element."""
    return block_tags.SECTION(*content, **attrs).render()


def select(*content, **attrs):
    """Represents an HTML <select> element."""
    return block_tags.SELECT(*content, **attrs).render()


def slot(*content, **attrs):
    """Represents an HTML <slot> element."""
    return block_tags.SLOT(*content, **attrs).render()


def small(*content, **attrs):
    """Represents an HTML <small> element."""
    return block_tags.SMALL(*content, **attrs).render()


def span(*content, **attrs):
    """Represents an HTML <span> element."""
    return block_tags.SPAN(*content, **attrs).render()


def strong(*content, **attrs):
    """Represents an HTML <strong> element."""
    return block_tags.STRONG(*content, **attrs).render()


def style(*content, **attrs):
    """Represents an HTML <style> element."""
    return block_tags.STYLE(*content, **attrs).render()


def sub(*content, **attrs):
    """Represents an HTML <sub> element."""
    return block_tags.SUB(*content, **attrs).render()


def summary(*content, **attrs):
    """Represents an HTML <summary> element."""
    return block_tags.SUMMARY(*content, **attrs).render()


def sup(*content, **attrs):
    """Represents an HTML <sup> element."""
    return block_tags.SUP(*content, **attrs).render()


def svg(*content, **attrs):
    """Represents an HTML <svg> element."""
    return block_tags.SVG(*content, **attrs).render()


def table(*content, **attrs):
    """Represents an HTML <table> element."""
    return block_tags.TABLE(*content, **attrs).render()


def tbody(*content, **attrs):
    """Represents an HTML <tbody> element."""
    return block_tags.TBODY(*content, **attrs).render()


def td(*content, **attrs):
    """Represents an HTML <td> element."""
    return block_tags.TD(*content, **attrs).render()


def template(*content, **attrs):
    """Represents an HTML <template> element."""
    return block_tags.TEMPLATE(*content, **attrs).render()


def textarea(*content, **attrs):
    """Represents an HTML <textarea> element."""
    return block_tags.TEXTAREA(*content, **attrs).render()


def tfoot(*content, **attrs):
    """Represents an HTML <tfoot> element."""
    return block_tags.TFOOT(*content, **attrs).render()


def th(*content, **attrs):
    """Represents an HTML <th> element."""
    return block_tags.TH(*content, **attrs).render()


def thead(*content, **attrs):
    """Represents an HTML <thead> element."""
    return block_tags.THEAD(*content, **attrs).render()


def time(*content, **attrs):
    """Represents an HTML <time> element."""
    return block_tags.TIME(*content, **attrs).render()


def title(*content, **attrs):
    """Represents an HTML <title> element."""
    return block_tags.TITLE(*content, **attrs).render()


def tr(*content, **attrs):
    """Represents an HTML <tr> element."""
    return block_tags.TR(*content, **attrs).render()


def u(*content, **attrs):
    """Represents an HTML <u> element."""
    return block_tags.U(*content, **attrs).render()


def ul(*content, **attrs):
    """Represents an HTML <ul> element."""
    return block_tags.UL(*content, **attrs).render()


def var(*content, **attrs):
    """Represents an HTML <var> element."""
    return block_tags.VAR(*content, **attrs).render()


def video(*content, **attrs):
    """Represents an HTML <video> element."""
    return block_tags.VIDEO(*content, **attrs).render()


def g(*content, **attrs):
    """Represents an HTML <g> element."""
    return block_tags.G(*content, **attrs).render()


def defs(*content, **attrs):
    """Represents an HTML <defs> element."""
    return block_tags.DEFS(*content, **attrs).render()


def text(*content, **attrs):
    """Represents an HTML <text> element."""
    return block_tags.TEXT(*content, **attrs).render()


def tspan(*content, **attrs):
    """Represents an HTML <tspan> element."""
    return block_tags.TSPAN(*content, **attrs).render()
