from probo.components.tag_classes import block_tags

# --- Specific HTML Block Element Classes (accepting content and attributes) ---
# These classes now use the `Element` helper class as per your blueprint.


def a(*content, **attrs):
    """Represents an HTML <a> element."""
    return block_tags.EL.a(*content, **attrs).render()


def abbr(*content, **attrs):
    """Represents an HTML <abbr> element."""
    return block_tags.EL.abbr(*content, **attrs).render()


def address(*content, **attrs):
    """Represents an HTML <address> element."""
    return block_tags.EL.address(*content, **attrs).render()


def article(*content, **attrs):
    """Represents an HTML <article> element."""
    return block_tags.EL.article(*content, **attrs).render()


def aside(*content, **attrs):
    """Represents an HTML <aside> element."""
    return block_tags.EL.aside(*content, **attrs).render()


def audio(*content, **attrs):
    """Represents an HTML <audio> element."""
    return block_tags.EL.audio(*content, **attrs).render()


def b(*content, **attrs):
    """Represents an HTML <b> element."""
    return block_tags.EL.b(*content, **attrs).render()


def bdi(*content, **attrs):
    """Represents an HTML <bdi> element."""
    return block_tags.EL.bdi(*content, **attrs).render()


def bdo(*content, **attrs):
    """Represents an HTML <bdo> element."""
    return block_tags.EL.bdo(*content, **attrs).render()


def blockquote(*content, **attrs):
    """Represents an HTML <blockquote> element."""
    return block_tags.EL.blockquote(*content, **attrs).render()


def body(*content, **attrs):
    """Represents an HTML <body> element."""
    return block_tags.EL.body(*content, **attrs).render()


def button(*content, **attrs):
    """Represents an HTML <button> element."""
    return block_tags.EL.button(*content, **attrs).render()


def canvas(*content, **attrs):
    """Represents an HTML <canvas> element."""
    return block_tags.EL.canvas(*content, **attrs).render()


def caption(*content, **attrs):
    """Represents an HTML <caption> element."""
    return block_tags.EL.caption(*content, **attrs).render()


def cite(*content, **attrs):
    """Represents an HTML <cite> element."""
    return block_tags.EL.cite(*content, **attrs).render()


def code(*content, **attrs):
    """Represents an HTML <code> element."""
    return block_tags.EL.code(*content, **attrs).render()


def colgroup(*content, **attrs):
    """Represents an HTML <colgroup> element."""
    return block_tags.EL.colgroup(*content, **attrs).render()


def data(*content, **attrs):
    """Represents an HTML <data> element."""
    return block_tags.EL.data(*content, **attrs).render()


def datalist(*content, **attrs):
    """Represents an HTML <datalist> element."""
    return block_tags.EL.datalist(*content, **attrs).render()


def dd(*content, **attrs):
    """Represents an HTML <dd> element."""
    return block_tags.EL.dd(*content, **attrs).render()


def Del(*content, **attrs):
    """Represents an HTML <del> element."""
    return block_tags.EL.Del(*content, **attrs).render()


def details(*content, **attrs):
    """Represents an HTML <details> element."""
    return block_tags.EL.details(*content, **attrs).render()


def dfn(*content, **attrs):
    """Represents an HTML <dfn> element."""
    return block_tags.EL.dfn(*content, **attrs).render()


def dialog(*content, **attrs):
    """Represents an HTML <dialog> element."""
    return block_tags.EL.dialog(*content, **attrs).render()


def div(*content, **attrs):
    """Represents an HTML <div> element."""
    return block_tags.EL.div(*content, **attrs).render()


def dl(*content, **attrs):
    """Represents an HTML <dl> element."""
    return block_tags.EL.dl(*content, **attrs).render()


def dt(*content, **attrs):
    """Represents an HTML <dt> element."""
    return block_tags.EL.dt(*content, **attrs).render()


def em(*content, **attrs):
    """Represents an HTML <em> element."""
    return block_tags.EL.em(*content, **attrs).render()


def fieldset(*content, **attrs):
    """Represents an HTML <fieldset> element."""
    return block_tags.EL.fieldset(*content, **attrs).render()


def figcaption(*content, **attrs):
    """Represents an HTML <figcaption> element."""
    return block_tags.EL.figcaption(*content, **attrs).render()


def figure(*content, **attrs):
    """Represents an HTML <figure> element."""
    return block_tags.EL.figure(*content, **attrs).render()


def footer(*content, **attrs):
    """Represents an HTML <footer> element."""
    return block_tags.EL.footer(*content, **attrs).render()


def form(*content, **attrs):
    """Represents an HTML <form> element."""
    return block_tags.EL.form(*content, **attrs).render()


def h1(*content, **attrs):
    """Represents an HTML <h1> element."""
    return block_tags.EL.h1(*content, **attrs).render()


def h2(*content, **attrs):
    """Represents an HTML <h2> element."""
    return block_tags.EL.h2(*content, **attrs).render()


def h3(*content, **attrs):
    """Represents an HTML <h3> element."""
    return block_tags.EL.h3(*content, **attrs).render()


def h4(*content, **attrs):
    """Represents an HTML <h4> element."""
    return block_tags.EL.h4(*content, **attrs).render()


def h5(*content, **attrs):
    """Represents an HTML <h5> element."""
    return block_tags.EL.h5(*content, **attrs).render()


def h6(*content, **attrs):
    """Represents an HTML <h6> element."""
    return block_tags.EL.h6(*content, **attrs).render()


def head(*content, **attrs):
    """Represents an HTML <head> element."""
    return block_tags.EL.head(*content, **attrs).render()


def header(*content, **attrs):
    """Represents an HTML <header> element."""
    return block_tags.EL.header(*content, **attrs).render()


def hgroup(*content, **attrs):
    """Represents an HTML <hgroup> element."""
    return block_tags.EL.hgroup(*content, **attrs).render()


def html(*content, **attrs):
    """Represents an HTML <html> element."""
    return block_tags.EL.html(*content, **attrs).render()


def i(*content, **attrs):
    """Represents an HTML <i> element."""
    return block_tags.EL.i(*content, **attrs).render()


def iframe(*content, **attrs):
    """Represents an HTML <iframe> element."""
    return block_tags.EL.iframe(*content, **attrs).render()


def ins(*content, **attrs):
    """Represents an HTML <ins> element."""
    return block_tags.EL.ins(*content, **attrs).render()


def kbd(*content, **attrs):
    """Represents an HTML <kbd> element."""
    return block_tags.EL.kbd(*content, **attrs).render()


def label(*content, **attrs):
    """Represents an HTML <label> element."""
    return block_tags.EL.label(*content, **attrs).render()


def legend(*content, **attrs):
    """Represents an HTML <legend> element."""
    return block_tags.EL.legend(*content, **attrs).render()


def li(*content, **attrs):
    """Represents an HTML <li> element."""
    return block_tags.EL.li(*content, **attrs).render()


def main(*content, **attrs):
    """Represents an HTML <main> element."""
    return block_tags.EL.main(*content, **attrs).render()


def math(*content, **attrs):
    """Represents an HTML <math> element."""
    return block_tags.EL.math(*content, **attrs).render()


def Map(*content, **attrs):
    """Represents an HTML <map> element."""
    return block_tags.EL.map(*content, **attrs).render()


def mark(*content, **attrs):
    """Represents an HTML <mark> element."""
    return block_tags.EL.mark(*content, **attrs).render()


def menu(*content, **attrs):
    """Represents an HTML <menu> element."""
    return block_tags.EL.menu(*content, **attrs).render()


def meter(*content, **attrs):
    """Represents an HTML <meter> element."""
    return block_tags.EL.meter(*content, **attrs).render()


def nav(*content, **attrs):
    """Represents an HTML <nav> element."""
    return block_tags.EL.nav(*content, **attrs).render()


def noscript(*content, **attrs):
    """Represents an HTML <noscript> element."""
    return block_tags.EL.noscript(*content, **attrs).render()


def Object(*content, **attrs):
    """Represents an HTML <object> element."""
    return block_tags.EL.Object(*content, **attrs).render()


def ol(*content, **attrs):
    """Represents an HTML <ol> element."""
    return block_tags.EL.ol(*content, **attrs).render()


def optgroup(*content, **attrs):
    """Represents an HTML <optgroup> element."""
    return block_tags.EL.optgroup(*content, **attrs).render()


def option(*content, **attrs):
    """Represents an HTML <option> element."""
    return block_tags.EL.option(*content, **attrs).render()


def output(*content, **attrs):
    """Represents an HTML <output> element."""
    return block_tags.EL.output(*content, **attrs).render()


def p(*content, **attrs):
    """Represents an HTML <p> element."""
    return block_tags.EL.p(*content, **attrs).render()


def portal(*content, **attrs):
    """Represents an HTML <portal> element."""
    return block_tags.EL.portal(*content, **attrs).render()


def picture(*content, **attrs):
    """Represents an HTML <picture> element."""
    return block_tags.EL.picture(*content, **attrs).render()


def pre(*content, **attrs):
    """Represents an HTML <pre> element."""
    return block_tags.EL.pre(*content, **attrs).render()


def progress(*content, **attrs):
    """Represents an HTML <progress> element."""
    return block_tags.EL.progress(*content, **attrs).render()


def q(*content, **attrs):
    """Represents an HTML <q> element."""
    return block_tags.EL.q(*content, **attrs).render()


def rp(*content, **attrs):
    """Represents an HTML <rp> element."""
    return block_tags.EL.rp(*content, **attrs).render()


def rt(*content, **attrs):
    """Represents an HTML <rt> element."""
    return block_tags.EL.rt(*content, **attrs).render()


def ruby(*content, **attrs):
    """Represents an HTML <ruby> element."""
    return block_tags.EL.ruby(*content, **attrs).render()


def s(*content, **attrs):
    """Represents an HTML <s> element."""
    return block_tags.EL.s(*content, **attrs).render()


def samp(*content, **attrs):
    """Represents an HTML <samp> element."""
    return block_tags.EL.samp(*content, **attrs).render()


def script(*content, **attrs):
    """Represents an HTML <script> element."""
    return block_tags.EL.script(*content, **attrs).render()


def search(*content, **attrs):
    """Represents an HTML <search> element."""
    return block_tags.EL.search(*content, **attrs).render()


def section(*content, **attrs):
    """Represents an HTML <section> element."""
    return block_tags.EL.section(*content, **attrs).render()


def select(*content, **attrs):
    """Represents an HTML <select> element."""
    return block_tags.EL.select(*content, **attrs).render()


def slot(*content, **attrs):
    """Represents an HTML <slot> element."""
    return block_tags.EL.slot(*content, **attrs).render()


def small(*content, **attrs):
    """Represents an HTML <small> element."""
    return block_tags.EL.small(*content, **attrs).render()


def span(*content, **attrs):
    """Represents an HTML <span> element."""
    return block_tags.EL.span(*content, **attrs).render()


def strong(*content, **attrs):
    """Represents an HTML <strong> element."""
    return block_tags.EL.strong(*content, **attrs).render()


def style(*content, **attrs):
    """Represents an HTML <style> element."""
    return block_tags.EL.style(*content, **attrs).render()


def sub(*content, **attrs):
    """Represents an HTML <sub> element."""
    return block_tags.EL.sub(*content, **attrs).render()


def summary(*content, **attrs):
    """Represents an HTML <summary> element."""
    return block_tags.EL.summary(*content, **attrs).render()


def sup(*content, **attrs):
    """Represents an HTML <sup> element."""
    return block_tags.EL.sup(*content, **attrs).render()

def table(*content, **attrs):
    """Represents an HTML <table> element."""
    return block_tags.EL.table(*content, **attrs).render()


def tbody(*content, **attrs):
    """Represents an HTML <tbody> element."""
    return block_tags.EL.tbody(*content, **attrs).render()


def td(*content, **attrs):
    """Represents an HTML <td> element."""
    return block_tags.EL.td(*content, **attrs).render()


def template(*content, **attrs):
    """Represents an HTML <template> element."""
    return block_tags.EL.template(*content, **attrs).render()


def textarea(*content, **attrs):
    """Represents an HTML <textarea> element."""
    return block_tags.EL.textarea(*content, **attrs).render()


def tfoot(*content, **attrs):
    """Represents an HTML <tfoot> element."""
    return block_tags.EL.tfoot(*content, **attrs).render()


def th(*content, **attrs):
    """Represents an HTML <th> element."""
    return block_tags.EL.th(*content, **attrs).render()


def thead(*content, **attrs):
    """Represents an HTML <thead> element."""
    return block_tags.EL.thead(*content, **attrs).render()


def time(*content, **attrs):
    """Represents an HTML <time> element."""
    return block_tags.EL.time(*content, **attrs).render()


def title(*content, **attrs):
    """Represents an HTML <title> element."""
    return block_tags.EL.title(*content, **attrs).render()


def tr(*content, **attrs):
    """Represents an HTML <tr> element."""
    return block_tags.EL.tr(*content, **attrs).render()


def u(*content, **attrs):
    """Represents an HTML <u> element."""
    return block_tags.EL.u(*content, **attrs).render()


def ul(*content, **attrs):
    """Represents an HTML <ul> element."""
    return block_tags.EL.ul(*content, **attrs).render()


def var(*content, **attrs):
    """Represents an HTML <var> element."""
    return block_tags.EL.var(*content, **attrs).render()


def video(*content, **attrs):
    """Represents an HTML <video> element."""
    return block_tags.EL.video(*content, **attrs).render()
