from probo.components.tag_functions.self_closing import EL
from probo.utility import ProboSourceString
from typing import Any

def a(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <a> element."""
    return EL.a(*content, **attrs).element


def abbr(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <abbr> element."""
    return EL.abbr(*content, **attrs).element


def address(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <address> element."""
    return EL.address(*content, **attrs).element


def article(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <article> element."""
    return EL.article(*content, **attrs).element


def aside(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <aside> element."""
    return EL.aside(*content, **attrs).element


def audio(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <audio> element."""
    return EL.audio(*content, **attrs).element


def b(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <b> element."""
    return EL.b(*content, **attrs).element


def bdi(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <bdi> element."""
    return EL.bdi(*content, **attrs).element


def bdo(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <bdo> element."""
    return EL.bdo(*content, **attrs).element


def blockquote(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <blockquote> element."""
    return EL.blockquote(*content, **attrs).element


def body(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <body> element."""
    return EL.body(*content, **attrs).element


def button(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <button> element."""
    return EL.button(*content, **attrs).element


def canvas(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <canvas> element."""
    return EL.canvas(*content, **attrs).element


def caption(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <caption> element."""
    return EL.caption(*content, **attrs).element


def cite(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <cite> element."""
    return EL.cite(*content, **attrs).element


def code(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <code> element."""
    return EL.code(*content, **attrs).element


def colgroup(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <colgroup> element."""
    return EL.colgroup(*content, **attrs).element


def data(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <data> element."""
    return EL.data(*content, **attrs).element


def datalist(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <datalist> element."""
    return EL.datalist(*content, **attrs).element


def dd(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <dd> element."""
    return EL.dd(*content, **attrs).element


def Del(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <del> element."""
    return EL.Del(*content, **attrs).element


def details(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <details> element."""
    return EL.details(*content, **attrs).element


def dfn(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <dfn> element."""
    return EL.dfn(*content, **attrs).element


def dialog(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <dialog> element."""
    return EL.dialog(*content, **attrs).element


def div(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <div> element."""
    return EL.div(*content, **attrs).element


def dl(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <dl> element."""
    return EL.dl(*content, **attrs).element


def dt(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <dt> element."""
    return EL.dt(*content, **attrs).element


def em(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <em> element."""
    return EL.em(*content, **attrs).element


def fieldset(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <fieldset> element."""
    return EL.fieldset(*content, **attrs).element


def figcaption(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <figcaption> element."""
    return EL.figcaption(*content, **attrs).element


def figure(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <figure> element."""
    return EL.figure(*content, **attrs).element


def footer(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <footer> element."""
    return EL.footer(*content, **attrs).element


def form(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <form> element."""
    return EL.form(*content, **attrs).element


def h1(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <h1> element."""
    return EL.h1(*content, **attrs).element


def h2(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <h2> element."""
    return EL.h2(*content, **attrs).element


def h3(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <h3> element."""
    return EL.h3(*content, **attrs).element


def h4(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <h4> element."""
    return EL.h4(*content, **attrs).element


def h5(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <h5> element."""
    return EL.h5(*content, **attrs).element


def h6(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <h6> element."""
    return EL.h6(*content, **attrs).element


def head(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <head> element."""
    return EL.head(*content, **attrs).element


def header(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <header> element."""
    return EL.header(*content, **attrs).element


def hgroup(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <hgroup> element."""
    return EL.hgroup(*content, **attrs).element


def html(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <html> element."""
    return EL.html(*content, **attrs).element


def i(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <i> element."""
    return EL.i(*content, **attrs).element


def iframe(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <iframe> element."""
    return EL.iframe(*content, **attrs).element


def ins(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <ins> element."""
    return EL.ins(*content, **attrs).element


def kbd(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <kbd> element."""
    return EL.kbd(*content, **attrs).element


def label(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <label> element."""
    return EL.label(*content, **attrs).element


def legend(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <legend> element."""
    return EL.legend(*content, **attrs).element


def li(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <li> element."""
    return EL.li(*content, **attrs).element


def main(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <main> element."""
    return EL.main(*content, **attrs).element


def math(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <math> element."""
    return EL.math(*content, **attrs).element


def Map(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <map> element."""
    return EL.map(*content, **attrs).element


def mark(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <mark> element."""
    return EL.mark(*content, **attrs).element


def menu(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <menu> element."""
    return EL.menu(*content, **attrs).element


def meter(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <meter> element."""
    return EL.meter(*content, **attrs).element


def nav(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <nav> element."""
    return EL.nav(*content, **attrs).element


def noscript(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <noscript> element."""
    return EL.noscript(*content, **attrs).element


def Object(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <object> element."""
    return EL.Object(*content, **attrs).element


def ol(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <ol> element."""
    return EL.ol(*content, **attrs).element


def optgroup(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <optgroup> element."""
    return EL.optgroup(*content, **attrs).element


def option(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <option> element."""
    return EL.option(*content, **attrs).element


def output(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <output> element."""
    return EL.output(*content, **attrs).element


def p(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <p> element."""
    return EL.p(*content, **attrs).element


def portal(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <portal> element."""
    return EL.portal(*content, **attrs).element


def picture(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <picture> element."""
    return EL.picture(*content, **attrs).element


def pre(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <pre> element."""
    return EL.pre(*content, **attrs).element


def progress(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <progress> element."""
    return EL.progress(*content, **attrs).element


def q(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <q> element."""
    return EL.q(*content, **attrs).element


def rp(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <rp> element."""
    return EL.rp(*content, **attrs).element


def rt(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <rt> element."""
    return EL.rt(*content, **attrs).element


def ruby(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <ruby> element."""
    return EL.ruby(*content, **attrs).element


def s(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <s> element."""
    return EL.s(*content, **attrs).element


def samp(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <samp> element."""
    return EL.samp(*content, **attrs).element


def script(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <script> element."""
    return EL.script(*content, **attrs).element


def search(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <search> element."""
    return EL.search(*content, **attrs).element


def section(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <section> element."""
    return EL.section(*content, **attrs).element


def select(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <select> element."""
    return EL.select(*content, **attrs).element


def slot(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <slot> element."""
    return EL.slot(*content, **attrs).element


def small(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <small> element."""
    return EL.small(*content, **attrs).element


def span(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <span> element."""
    return EL.span(*content, **attrs).element


def strong(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <strong> element."""
    return EL.strong(*content, **attrs).element


def style(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <style> element."""
    return EL.style(*content, **attrs).element


def sub(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <sub> element."""
    return EL.sub(*content, **attrs).element


def summary(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <summary> element."""
    return EL.summary(*content, **attrs).element


def sup(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <sup> element."""
    return EL.sup(*content, **attrs).element

def table(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <table> element."""
    return EL.table(*content, **attrs).element


def tbody(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <tbody> element."""
    return EL.tbody(*content, **attrs).element


def td(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <td> element."""
    return EL.td(*content, **attrs).element


def template(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <template> element."""
    return EL.template(*content, **attrs).element


def textarea(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <textarea> element."""
    return EL.textarea(*content, **attrs).element


def tfoot(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <tfoot> element."""
    return EL.tfoot(*content, **attrs).element


def th(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <th> element."""
    return EL.th(*content, **attrs).element


def thead(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <thead> element."""
    return EL.thead(*content, **attrs).element


def time(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <time> element."""
    return EL.time(*content, **attrs).element


def title(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <title> element."""
    return EL.title(*content, **attrs).element


def tr(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <tr> element."""
    return EL.tr(*content, **attrs).element


def u(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <u> element."""
    return EL.u(*content, **attrs).element


def ul(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <ul> element."""
    return EL.ul(*content, **attrs).element


def var(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <var> element."""
    return EL.var(*content, **attrs).element


def video(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <video> element."""
    return EL.video(*content, **attrs).element
