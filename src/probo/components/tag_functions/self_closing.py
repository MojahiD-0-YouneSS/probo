from probo.components.elements import Element
from typing import Any
EL = Element()
def doctype(content:str=None, **attrs:dict[str,Any]):
    """Represents an HTML <!DOCTYPE> line break element (self-closing)."""
    return EL.doctype(content, **attrs).element


def area(**attrs:dict[str,Any]):
    """Represents an HTML <area/> line break element (self-closing)."""
    return EL.area(**attrs).element


def base(**attrs:dict[str,Any]):
    """Represents an HTML <base/> line break element (self-closing)."""
    return EL.base(**attrs).element


def br(**attrs:dict[str,Any]):
    """Represents an HTML <br/> line break element (self-closing)."""
    return EL.br(**attrs).element


def col(**attrs:dict[str,Any]):
    """Represents an HTML <col/> line break element (self-closing)."""
    return EL.col(**attrs).element


def embed(**attrs:dict[str,Any]):
    """Represents an HTML <embed/> line break element (self-closing)."""
    return EL.embed(**attrs).element


def hr(**attrs:dict[str,Any]):
    """Represents an HTML <hr/> line break element (self-closing)."""
    return EL.hr(**attrs).element


def img(**attrs:dict[str,Any]):
    """Represents an HTML <img/> line break element (self-closing)."""
    return EL.img(**attrs).element


def Input(**attrs:dict[str,Any]):
    """Represents an HTML <input/> line break element (self-closing)."""
    return EL.input(**attrs).element


def link(**attrs:dict[str,Any]):
    """Represents an HTML <link/> line break element (self-closing)."""
    return EL.link(**attrs).element


def meta(**attrs:dict[str,Any]):
    """Represents an HTML <meta/> line break element (self-closing)."""
    return EL.meta(**attrs).element


def param(**attrs:dict[str,Any]):
    """Represents an HTML <param/> line break element (self-closing)."""
    return EL.param(**attrs).element


def source(**attrs:dict[str,Any]):
    """Represents an HTML <source/> line break element (self-closing)."""
    return EL.source(**attrs).element


def track(**attrs:dict[str,Any]):
    """Represents an HTML <track/> line break element (self-closing)."""
    return EL.track(**attrs).element


def wbr(**attrs:dict[str,Any]):
    """Represents an HTML <wbr/> line break element (self-closing)."""
    return EL.wbr(**attrs).element

