from probo.components.tag_classes import svg_tags



def g(*content, **attrs):
    """Represents an HTML <g> element."""
    return svg_tags.EL.g(*content, **attrs).render()

def defs(*content,**attrs):

    """Represents an HTML <dfs> element."""
    return svg_tags.EL.defs(*content, **attrs).render()

def text(*content, **attrs):
    """Represents an HTML <text> element."""
    return svg_tags.EL.text(*content, **attrs).render()

def tspan(*content, **attrs):
    """Represents an HTML <tspan> element."""
    return svg_tags.EL.tspan(*content, **attrs).render()

def svg(*content, **attrs):
    """Represents an HTML <svg> element."""
    return svg_tags.EL.svg(*content, **attrs).render()

def symbol(*content, **attrs):
    """Represents an HTML <symbol> element."""
    return svg_tags.EL.symbol(*content, **attrs).render()

def marker(*content, **attrs):
    """Represents an HTML <marker> element."""
    return svg_tags.EL.marker(*content, **attrs).render()

def pattern(*content, **attrs):
    """Represents an HTML <pattern> element."""
    return svg_tags.EL.pattern(*content, **attrs).render()

def mask(*content, **attrs):
    """Represents an HTML <mask> element."""
    return svg_tags.EL.mask(*content, **attrs).render()

def clippath(*content, **attrs):
    """Represents an HTML <clippath> element."""
    return svg_tags.EL.clippath(*content, **attrs).render()

def lineargradient(*content,**attrs):
    """Represents an HTML <lineargradient> element."""
    return svg_tags.EL.lineargradient(content, **attrs).render()

def radialgradient(*content,**attrs):
    """Represents an HTML <radialgradient> element."""
    return svg_tags.EL.radialgradient(content, **attrs).render()

def Filter(*content, **attrs):
    """Represents an HTML <filter> element."""
    return svg_tags.EL.Filter(*content, **attrs).render()

def fecomponenttransfer(*content,**attrs):
    """Represents an HTML <fecomponenttransfer> element."""
    return svg_tags.EL.fecomponenttransfer(*content, **attrs).render()

def fediffuselighting(*content,**attrs):
    """Represents an HTML <fediffuselighting> element."""
    return svg_tags.EL.fediffuselighting(*content, **attrs).render()

def femerge(*content, **attrs):
    """Represents an HTML <femerge> element."""
    return svg_tags.EL.femerge(*content, **attrs).render()

def fespecularlighting(*content,**attrs):
    """Represents an HTML <fespecularlighting> element."""
    return svg_tags.EL.fespecularlighting(*content, **attrs).render()

def animatemotion(*content,**attrs):
    """Represents an HTML <animatemotion> element."""
    return svg_tags.EL.animatemotion(*content, **attrs).render()

def forienobject(*content,**attrs):
    """Represents an HTML <forienobject> element."""
    return svg_tags.EL.forienobject(*content, **attrs).render()

# self closing
def path(**attrs):
    """Represents an HTML <path/> line break element (self-closing)."""
    return svg_tags.EL.path(**attrs).render()

def circle(**attrs):
    """Represents an HTML <circle/> line break element (self-closing)."""
    return svg_tags.EL.circle(**attrs).render()

def rect(**attrs):
    """Represents an HTML <rect/> line break element (self-closing)."""
    return svg_tags.EL.rect(**attrs).render()

def line(**attrs):
    """Represents an HTML <line/> line break element (self-closing)."""
    return svg_tags.EL.line(**attrs).render()

def polyline(**attrs):
    """Represents an HTML <polyline/> line break element (self-closing)."""
    return svg_tags.EL.polyline(**attrs).render()

def polygon(**attrs):
    """Represents an HTML <polygon/> line break element (self-closing)."""
    return svg_tags.EL.polygon(**attrs).render()

def ellipse(**attrs):
    """Represents an HTML <ellipse/> line break element (self-closing)."""
    return svg_tags.EL.ellipse(**attrs).render()

def image(**attrs):
    """Represents an HTML <image/> line break element (self-closing)."""
    return svg_tags.EL.image(**attrs).render()

def feBlend(**attrs):
    """Represents an HTML <feBlend/> line break element (self-closing)."""
    return svg_tags.EL.feBlend(**attrs).render()

def feColorMatrix(**attrs):
    """Represents an HTML <feColorMatrix/> line break element (self-closing)."""
    return svg_tags.EL.feColorMatrix(**attrs).render()

def feComposite(**attrs):
    """Represents an HTML <feComposite/> line break element (self-closing)."""
    return svg_tags.EL.feComposite(**attrs).render()

def feConvolveMatrix(**attrs):
    """Represents an HTML <feConvolveMatrix/> line break element (self-closing)."""
    return svg_tags.EL.feConvolveMatrix(**attrs).render()

def feDisplacementMap(**attrs):
    """Represents an HTML <feDisplacementMap/> line break element (self-closing)."""
    return svg_tags.EL.feDisplacementMap(**attrs).render()

def feDropShadow(**attrs):
    """Represents an HTML <feDropShadow/> line break element (self-closing)."""
    return svg_tags.EL.feDropShadow(**attrs).render()

def feFlood(**attrs):
    """Represents an HTML <feFlood/> line break element (self-closing)."""
    return svg_tags.EL.feFlood(**attrs).render()

def feFuncA(**attrs):
    """Represents an HTML <feFuncA/> line break element (self-closing)."""
    return svg_tags.EL.feFuncA(**attrs).render()

def feFuncB(**attrs):
    """Represents an HTML <feFuncB/> line break element (self-closing)."""
    return svg_tags.EL.feFuncB(**attrs).render()

def feFuncG(**attrs):
    """Represents an HTML <feFuncG/> line break element (self-closing)."""
    return svg_tags.EL.feFuncG(**attrs).render()

def feFuncR(**attrs):
    """Represents an HTML <feFuncR/> line break element (self-closing)."""
    return svg_tags.EL.feFuncR(**attrs).render()

def feGaussianBlur(**attrs):
    """Represents an HTML <feGaussianBlur/> line break element (self-closing)."""
    return svg_tags.EL.feGaussianBlur(**attrs).render()

def feImage(**attrs):
    """Represents an HTML <feImage/> line break element (self-closing)."""
    return svg_tags.EL.feImage(**attrs).render()

def feMergeNode(**attrs):
    """Represents an HTML <feMergeNode/> line break element (self-closing)."""
    return svg_tags.EL.feMergeNode(**attrs).render()

def feMorphology(**attrs):
    """Represents an HTML <feMorphology/> line break element (self-closing)."""
    return svg_tags.EL.feMorphology(**attrs).render()

def feOffset(**attrs):
    """Represents an HTML <feOffset/> line break element (self-closing)."""
    return svg_tags.EL.feOffset(**attrs).render()

def fePointLight(**attrs):
    """Represents an HTML <fePointLight/> line break element (self-closing)."""
    return svg_tags.EL.fePointLight(**attrs).render()

def feSpotLight(**attrs):
    """Represents an HTML <feSpotLight/> line break element (self-closing)."""
    return svg_tags.EL.feSpotLight(**attrs).render()

def feTile(**attrs):
    """Represents an HTML <feTile/> line break element (self-closing)."""
    return svg_tags.EL.feTile(**attrs).render()

def feTurbulence(**attrs):
    """Represents an HTML <feTurbulence/> line break element (self-closing)."""
    return svg_tags.EL.feTurbulence(**attrs).render()

def animate(**attrs):
    """Represents an HTML <animate/> line break element (self-closing)."""
    return svg_tags.EL.animate(**attrs).render()

def animateTransform(**attrs):
    """Represents an HTML <animateTransform/> line break element (self-closing)."""
    return svg_tags.EL.animateTransform(**attrs).render()

def Set(**attrs):
    """Represents an HTML <set/> line break element (self-closing)."""
    return svg_tags.EL.Set(**attrs).render()

def view(**attrs):
    """Represents an HTML <view/> line break element (self-closing)."""
    return svg_tags.EL.view(**attrs).render()

def use(**attrs):
    """Represents an HTML <use/> line break element (self-closing)."""
    return svg_tags.EL.use(**attrs).render()

def stop(**attrs):
    """Represents an HTML <stop/> line break element (self-closin).""" 
    return svg_tags.EL.stop(**attrs).render()