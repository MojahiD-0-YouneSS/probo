from probo.components.tag_classes import block_tags

# --- Specific HTML Block Element Classes (accepting content and attributes) ---
# These classes now use the `Element` helper class as per your blueprint.


def a(*content, **attrs):
    """Represents an HTML <a> element."""
    return block_tags.EL.a(*content, **attrs).element


def abbr(*content, **attrs):
    """Represents an HTML <abbr> element."""
    return block_tags.EL.abbr(*content, **attrs).element


def address(*content, **attrs):
    """Represents an HTML <address> element."""
    return block_tags.EL.address(*content, **attrs).element


def article(*content, **attrs):
    """Represents an HTML <article> element."""
    return block_tags.EL.article(*content, **attrs).element


def aside(*content, **attrs):
    """Represents an HTML <aside> element."""
    return block_tags.EL.aside(*content, **attrs).element


def audio(*content, **attrs):
    """Represents an HTML <audio> element."""
    return block_tags.EL.audio(*content, **attrs).element


def b(*content, **attrs):
    """Represents an HTML <b> element."""
    return block_tags.EL.b(*content, **attrs).element


def bdi(*content, **attrs):
    """Represents an HTML <bdi> element."""
    return block_tags.EL.bdi(*content, **attrs).element


def bdo(*content, **attrs):
    """Represents an HTML <bdo> element."""
    return block_tags.EL.bdo(*content, **attrs).element


def blockquote(*content, **attrs):
    """Represents an HTML <blockquote> element."""
    return block_tags.EL.blockquote(*content, **attrs).element


def body(*content, **attrs):
    """Represents an HTML <body> element."""
    return block_tags.EL.body(*content, **attrs).element


def button(*content, **attrs):
    """Represents an HTML <button> element."""
    return block_tags.EL.button(*content, **attrs).element


def canvas(*content, **attrs):
    """Represents an HTML <canvas> element."""
    return block_tags.EL.canvas(*content, **attrs).element


def caption(*content, **attrs):
    """Represents an HTML <caption> element."""
    return block_tags.EL.caption(*content, **attrs).element


def cite(*content, **attrs):
    """Represents an HTML <cite> element."""
    return block_tags.EL.cite(*content, **attrs).element


def code(*content, **attrs):
    """Represents an HTML <code> element."""
    return block_tags.EL.code(*content, **attrs).element


def colgroup(*content, **attrs):
    """Represents an HTML <colgroup> element."""
    return block_tags.EL.colgroup(*content, **attrs).element


def data(*content, **attrs):
    """Represents an HTML <data> element."""
    return block_tags.EL.data(*content, **attrs).element


def datalist(*content, **attrs):
    """Represents an HTML <datalist> element."""
    return block_tags.EL.datalist(*content, **attrs).element


def dd(*content, **attrs):
    """Represents an HTML <dd> element."""
    return block_tags.EL.dd(*content, **attrs).element


def Del(*content, **attrs):
    """Represents an HTML <del> element."""
    return block_tags.EL.Del(*content, **attrs).element


def details(*content, **attrs):
    """Represents an HTML <details> element."""
    return block_tags.EL.details(*content, **attrs).element


def dfn(*content, **attrs):
    """Represents an HTML <dfn> element."""
    return block_tags.EL.dfn(*content, **attrs).element


def dialog(*content, **attrs):
    """Represents an HTML <dialog> element."""
    return block_tags.EL.dialog(*content, **attrs).element


def div(*content, **attrs):
    """Represents an HTML <div> element."""
    return block_tags.EL.div(*content, **attrs).element


def dl(*content, **attrs):
    """Represents an HTML <dl> element."""
    return block_tags.EL.dl(*content, **attrs).element


def dt(*content, **attrs):
    """Represents an HTML <dt> element."""
    return block_tags.EL.dt(*content, **attrs).element


def em(*content, **attrs):
    """Represents an HTML <em> element."""
    return block_tags.EL.em(*content, **attrs).element


def fieldset(*content, **attrs):
    """Represents an HTML <fieldset> element."""
    return block_tags.EL.fieldset(*content, **attrs).element


def figcaption(*content, **attrs):
    """Represents an HTML <figcaption> element."""
    return block_tags.EL.figcaption(*content, **attrs).element


def figure(*content, **attrs):
    """Represents an HTML <figure> element."""
    return block_tags.EL.figure(*content, **attrs).element


def footer(*content, **attrs):
    """Represents an HTML <footer> element."""
    return block_tags.EL.footer(*content, **attrs).element


def form(*content, **attrs):
    """Represents an HTML <form> element."""
    return block_tags.EL.form(*content, **attrs).element


def h1(*content, **attrs):
    """Represents an HTML <h1> element."""
    return block_tags.EL.h1(*content, **attrs).element


def h2(*content, **attrs):
    """Represents an HTML <h2> element."""
    return block_tags.EL.h2(*content, **attrs).element


def h3(*content, **attrs):
    """Represents an HTML <h3> element."""
    return block_tags.EL.h3(*content, **attrs).element


def h4(*content, **attrs):
    """Represents an HTML <h4> element."""
    return block_tags.EL.h4(*content, **attrs).element


def h5(*content, **attrs):
    """Represents an HTML <h5> element."""
    return block_tags.EL.h5(*content, **attrs).element


def h6(*content, **attrs):
    """Represents an HTML <h6> element."""
    return block_tags.EL.h6(*content, **attrs).element


def head(*content, **attrs):
    """Represents an HTML <head> element."""
    return block_tags.EL.head(*content, **attrs).element


def header(*content, **attrs):
    """Represents an HTML <header> element."""
    return block_tags.EL.header(*content, **attrs).element


def hgroup(*content, **attrs):
    """Represents an HTML <hgroup> element."""
    return block_tags.EL.hgroup(*content, **attrs).element


def html(*content, **attrs):
    """Represents an HTML <html> element."""
    return block_tags.EL.html(*content, **attrs).element


def i(*content, **attrs):
    """Represents an HTML <i> element."""
    return block_tags.EL.i(*content, **attrs).element


def iframe(*content, **attrs):
    """Represents an HTML <iframe> element."""
    return block_tags.EL.iframe(*content, **attrs).element


def ins(*content, **attrs):
    """Represents an HTML <ins> element."""
    return block_tags.EL.ins(*content, **attrs).element


def kbd(*content, **attrs):
    """Represents an HTML <kbd> element."""
    return block_tags.EL.kbd(*content, **attrs).element


def label(*content, **attrs):
    """Represents an HTML <label> element."""
    return block_tags.EL.label(*content, **attrs).element


def legend(*content, **attrs):
    """Represents an HTML <legend> element."""
    return block_tags.EL.legend(*content, **attrs).element


def li(*content, **attrs):
    """Represents an HTML <li> element."""
    return block_tags.EL.li(*content, **attrs).element


def main(*content, **attrs):
    """Represents an HTML <main> element."""
    return block_tags.EL.main(*content, **attrs).element


def math(*content, **attrs):
    """Represents an HTML <math> element."""
    return block_tags.EL.math(*content, **attrs).element


def Map(*content, **attrs):
    """Represents an HTML <map> element."""
    return block_tags.EL.map(*content, **attrs).element


def mark(*content, **attrs):
    """Represents an HTML <mark> element."""
    return block_tags.EL.mark(*content, **attrs).element


def menu(*content, **attrs):
    """Represents an HTML <menu> element."""
    return block_tags.EL.menu(*content, **attrs).element


def meter(*content, **attrs):
    """Represents an HTML <meter> element."""
    return block_tags.EL.meter(*content, **attrs).element


def nav(*content, **attrs):
    """Represents an HTML <nav> element."""
    return block_tags.EL.nav(*content, **attrs).element


def noscript(*content, **attrs):
    """Represents an HTML <noscript> element."""
    return block_tags.EL.noscript(*content, **attrs).element


def Object(*content, **attrs):
    """Represents an HTML <object> element."""
    return block_tags.EL.Object(*content, **attrs).element


def ol(*content, **attrs):
    """Represents an HTML <ol> element."""
    return block_tags.EL.ol(*content, **attrs).element


def optgroup(*content, **attrs):
    """Represents an HTML <optgroup> element."""
    return block_tags.EL.optgroup(*content, **attrs).element


def option(*content, **attrs):
    """Represents an HTML <option> element."""
    return block_tags.EL.option(*content, **attrs).element


def output(*content, **attrs):
    """Represents an HTML <output> element."""
    return block_tags.EL.output(*content, **attrs).element


def p(*content, **attrs):
    """Represents an HTML <p> element."""
    return block_tags.EL.p(*content, **attrs).element


def portal(*content, **attrs):
    """Represents an HTML <portal> element."""
    return block_tags.EL.portal(*content, **attrs).element


def picture(*content, **attrs):
    """Represents an HTML <picture> element."""
    return block_tags.EL.picture(*content, **attrs).element


def pre(*content, **attrs):
    """Represents an HTML <pre> element."""
    return block_tags.EL.pre(*content, **attrs).element


def progress(*content, **attrs):
    """Represents an HTML <progress> element."""
    return block_tags.EL.progress(*content, **attrs).element


def q(*content, **attrs):
    """Represents an HTML <q> element."""
    return block_tags.EL.q(*content, **attrs).element


def rp(*content, **attrs):
    """Represents an HTML <rp> element."""
    return block_tags.EL.rp(*content, **attrs).element


def rt(*content, **attrs):
    """Represents an HTML <rt> element."""
    return block_tags.EL.rt(*content, **attrs).element


def ruby(*content, **attrs):
    """Represents an HTML <ruby> element."""
    return block_tags.EL.ruby(*content, **attrs).element


def s(*content, **attrs):
    """Represents an HTML <s> element."""
    return block_tags.EL.s(*content, **attrs).element


def samp(*content, **attrs):
    """Represents an HTML <samp> element."""
    return block_tags.EL.samp(*content, **attrs).element


def script(*content, **attrs):
    """Represents an HTML <script> element."""
    return block_tags.EL.script(*content, **attrs).element


def search(*content, **attrs):
    """Represents an HTML <search> element."""
    return block_tags.EL.search(*content, **attrs).element


def section(*content, **attrs):
    """Represents an HTML <section> element."""
    return block_tags.EL.section(*content, **attrs).element


def select(*content, **attrs):
    """Represents an HTML <select> element."""
    return block_tags.EL.select(*content, **attrs).element


def slot(*content, **attrs):
    """Represents an HTML <slot> element."""
    return block_tags.EL.slot(*content, **attrs).element


def small(*content, **attrs):
    """Represents an HTML <small> element."""
    return block_tags.EL.small(*content, **attrs).element


def span(*content, **attrs):
    """Represents an HTML <span> element."""
    return block_tags.EL.span(*content, **attrs).element


def strong(*content, **attrs):
    """Represents an HTML <strong> element."""
    return block_tags.EL.strong(*content, **attrs).element


def style(*content, **attrs):
    """Represents an HTML <style> element."""
    return block_tags.EL.style(*content, **attrs).element


def sub(*content, **attrs):
    """Represents an HTML <sub> element."""
    return block_tags.EL.sub(*content, **attrs).element


def summary(*content, **attrs):
    """Represents an HTML <summary> element."""
    return block_tags.EL.summary(*content, **attrs).element


def sup(*content, **attrs):
    """Represents an HTML <sup> element."""
    return block_tags.EL.sup(*content, **attrs).element

def table(*content, **attrs):
    """Represents an HTML <table> element."""
    return block_tags.EL.table(*content, **attrs).element


def tbody(*content, **attrs):
    """Represents an HTML <tbody> element."""
    return block_tags.EL.tbody(*content, **attrs).element


def td(*content, **attrs):
    """Represents an HTML <td> element."""
    return block_tags.EL.td(*content, **attrs).element


def template(*content, **attrs):
    """Represents an HTML <template> element."""
    return block_tags.EL.template(*content, **attrs).element


def textarea(*content, **attrs):
    """Represents an HTML <textarea> element."""
    return block_tags.EL.textarea(*content, **attrs).element


def tfoot(*content, **attrs):
    """Represents an HTML <tfoot> element."""
    return block_tags.EL.tfoot(*content, **attrs).element


def th(*content, **attrs):
    """Represents an HTML <th> element."""
    return block_tags.EL.th(*content, **attrs).element


def thead(*content, **attrs):
    """Represents an HTML <thead> element."""
    return block_tags.EL.thead(*content, **attrs).element


def time(*content, **attrs):
    """Represents an HTML <time> element."""
    return block_tags.EL.time(*content, **attrs).element


def title(*content, **attrs):
    """Represents an HTML <title> element."""
    return block_tags.EL.title(*content, **attrs).element


def tr(*content, **attrs):
    """Represents an HTML <tr> element."""
    return block_tags.EL.tr(*content, **attrs).element


def u(*content, **attrs):
    """Represents an HTML <u> element."""
    return block_tags.EL.u(*content, **attrs).element


def ul(*content, **attrs):
    """Represents an HTML <ul> element."""
    return block_tags.EL.ul(*content, **attrs).element


def var(*content, **attrs):
    """Represents an HTML <var> element."""
    return block_tags.EL.var(*content, **attrs).element


def video(*content, **attrs):
    """Represents an HTML <video> element."""
    return block_tags.EL.video(*content, **attrs).element
