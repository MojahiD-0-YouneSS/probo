from probo.components.tag_functions.self_closing import EL
from typing import Any
from probo.utility import ProboSourceString

def g(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <g> element."""
    return EL.g(*content, **attrs).element

def defs(*content:tuple[str],**attrs:dict[str,Any]) -> ProboSourceString:

    """Represents an HTML <dfs> element."""
    return EL.defs(*content, **attrs).element

def text(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <text> element."""
    return EL.text(*content, **attrs).element

def tspan(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <tspan> element."""
    return EL.tspan(*content, **attrs).element

def svg(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <svg> element."""
    return EL.svg(*content, **attrs).element

def symbol(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <symbol> element."""
    return EL.symbol(*content, **attrs).element

def marker(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <marker> element."""
    return EL.marker(*content, **attrs).element

def pattern(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <pattern> element."""
    return EL.pattern(*content, **attrs).element

def mask(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <mask> element."""
    return EL.mask(*content, **attrs).element

def clippath(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <clippath> element."""
    return EL.clippath(*content, **attrs).element

def lineargradient(*content:tuple[str],**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <lineargradient> element."""
    return EL.lineargradient(content, **attrs).element

def radialgradient(*content:tuple[str],**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <radialgradient> element."""
    return EL.radialgradient(content, **attrs).element

def Filter(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <filter> element."""
    return EL.Filter(*content, **attrs).element

def fecomponenttransfer(*content:tuple[str],**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <fecomponenttransfer> element."""
    return EL.fecomponenttransfer(*content, **attrs).element

def fediffuselighting(*content:tuple[str],**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <fediffuselighting> element."""
    return EL.fediffuselighting(*content, **attrs).element

def femerge(*content:tuple[str], **attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <femerge> element."""
    return EL.femerge(*content, **attrs).element

def fespecularlighting(*content:tuple[str],**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <fespecularlighting> element."""
    return EL.fespecularlighting(*content, **attrs).element

def animatemotion(*content:tuple[str],**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <animatemotion> element."""
    return EL.animatemotion(*content, **attrs).element

def forienobject(*content:tuple[str],**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <forienobject> element."""
    return EL.forienobject(*content, **attrs).element

# self closing
def path(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <path/> line break element (self-closing)."""
    return EL.path(**attrs).element

def circle(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <circle/> line break element (self-closing)."""
    return EL.circle(**attrs).element

def rect(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <rect/> line break element (self-closing)."""
    return EL.rect(**attrs).element

def line(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <line/> line break element (self-closing)."""
    return EL.line(**attrs).element

def polyline(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <polyline/> line break element (self-closing)."""
    return EL.polyline(**attrs).element

def polygon(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <polygon/> line break element (self-closing)."""
    return EL.polygon(**attrs).element

def ellipse(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <ellipse/> line break element (self-closing)."""
    return EL.ellipse(**attrs).element

def image(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <image/> line break element (self-closing)."""
    return EL.image(**attrs).element

def feBlend(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feBlend/> line break element (self-closing)."""
    return EL.feBlend(**attrs).element

def feColorMatrix(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feColorMatrix/> line break element (self-closing)."""
    return EL.feColorMatrix(**attrs).element

def feComposite(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feComposite/> line break element (self-closing)."""
    return EL.feComposite(**attrs).element

def feConvolveMatrix(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feConvolveMatrix/> line break element (self-closing)."""
    return EL.feConvolveMatrix(**attrs).element

def feDisplacementMap(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feDisplacementMap/> line break element (self-closing)."""
    return EL.feDisplacementMap(**attrs).element

def feDropShadow(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feDropShadow/> line break element (self-closing)."""
    return EL.feDropShadow(**attrs).element

def feFlood(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feFlood/> line break element (self-closing)."""
    return EL.feFlood(**attrs).element

def feFuncA(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feFuncA/> line break element (self-closing)."""
    return EL.feFuncA(**attrs).element

def feFuncB(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feFuncB/> line break element (self-closing)."""
    return EL.feFuncB(**attrs).element

def feFuncG(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feFuncG/> line break element (self-closing)."""
    return EL.feFuncG(**attrs).element

def feFuncR(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feFuncR/> line break element (self-closing)."""
    return EL.feFuncR(**attrs).element

def feGaussianBlur(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feGaussianBlur/> line break element (self-closing)."""
    return EL.feGaussianBlur(**attrs).element

def feImage(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feImage/> line break element (self-closing)."""
    return EL.feImage(**attrs).element

def feMergeNode(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feMergeNode/> line break element (self-closing)."""
    return EL.feMergeNode(**attrs).element

def feMorphology(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feMorphology/> line break element (self-closing)."""
    return EL.feMorphology(**attrs).element

def feOffset(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feOffset/> line break element (self-closing)."""
    return EL.feOffset(**attrs).element

def fePointLight(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <fePointLight/> line break element (self-closing)."""
    return EL.fePointLight(**attrs).element

def feSpotLight(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feSpotLight/> line break element (self-closing)."""
    return EL.feSpotLight(**attrs).element

def feTile(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feTile/> line break element (self-closing)."""
    return EL.feTile(**attrs).element

def feTurbulence(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <feTurbulence/> line break element (self-closing)."""
    return EL.feTurbulence(**attrs).element

def animate(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <animate/> line break element (self-closing)."""
    return EL.animate(**attrs).element

def animateTransform(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <animateTransform/> line break element (self-closing)."""
    return EL.animateTransform(**attrs).element

def Set(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <set/> line break element (self-closing)."""
    return EL.Set(**attrs).element

def view(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <view/> line break element (self-closing)."""
    return EL.view(**attrs).element

def use(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <use/> line break element (self-closing)."""
    return EL.use(**attrs).element

def stop(**attrs:dict[str,Any]) -> ProboSourceString:
    """Represents an HTML <stop/> line break element (self-closin).""" 
    return EL.stop(**attrs).element