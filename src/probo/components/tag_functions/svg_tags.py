from probo.components.tag_classes import svg_tags



def g(*content, **attrs):
    """Represents an HTML <g> element."""
    return svg_tags.G(*content, **attrs).render()

def dfs(*content,**attrs):

    """Represents an HTML <dfs> element."""
    return svg_tags.DEFS(*content, **attrs).render()

def text(*content, **attrs):
    """Represents an HTML <text> element."""
    return svg_tags.TEXT(*content, **attrs).render()

def tspan(*content, **attrs):
    """Represents an HTML <tspan> element."""
    return svg_tags.TSPAN(*content, **attrs).render()

def svg(*content, **attrs):
    """Represents an HTML <svg> element."""
    return svg_tags.SVG(*content, **attrs).render()

def symbol(*content, **attrs):
    """Represents an HTML <symbol> element."""
    return svg_tags.SYMBOL(*content, **attrs).render()

def marker(*content, **attrs):
    """Represents an HTML <marker> element."""
    return svg_tags.MARKER(*content, **attrs).render()

def pattern(*content, **attrs):
    """Represents an HTML <pattern> element."""
    return svg_tags.PATTERN(*content, **attrs).render()

def mask(*content, **attrs):
    """Represents an HTML <mask> element."""
    return svg_tags.MASK(*content, **attrs).render()

def clippath(*content, **attrs):
    """Represents an HTML <clippath> element."""
    return svg_tags.CLIPPATH(*content, **attrs).render()

def lineargradient(*content,**attrs):
    """Represents an HTML <lineargradient> element."""
    return svg_tags.LINEARGRADIENT(content, **attrs).render()

def radialgradient(*content,**attrs):
    """Represents an HTML <radialgradient> element."""
    return svg_tags.RADIALGRADIENT(content, **attrs).render()

def Filter(*content, **attrs):
    """Represents an HTML <filter> element."""
    return svg_tags.FILTER(*content, **attrs).render()

def fecomponenttransfer(*content,**attrs):
    """Represents an HTML <fecomponenttransfer> element."""
    return svg_tags.FECOMPONENTTRANSFER(*content, **attrs).render()

def fediffuselighting(*content,**attrs):
    """Represents an HTML <fediffuselighting> element."""
    return svg_tags.FEDIFFUSELIGHTING(*content, **attrs).render()

def femerge(*content, **attrs):
    """Represents an HTML <femerge> element."""
    return svg_tags.FEMERGE(*content, **attrs).render()

def fespecularlighting(*content,**attrs):
    """Represents an HTML <fespecularlighting> element."""
    return svg_tags.FESPECULARLIGHTING(*content, **attrs).render()

def animatemotion(*content,**attrs):
    """Represents an HTML <animatemotion> element."""
    return svg_tags.ANIMATEMOTION(*content, **attrs).render()

def forienobject(*content,**attrs):
    """Represents an HTML <forienobject> element."""
    return svg_tags.FOREIGNOBJECT(*content, **attrs).render()

# self closing
def path(**attrs):
    """Represents an HTML <path/> line break element (self-closing)."""
    return svg_tags.PATH(**attrs).render()

def circle(**attrs):
    """Represents an HTML <circle/> line break element (self-closing)."""
    return svg_tags.CIRCLE(**attrs).render()

def rect(**attrs):
    """Represents an HTML <rect/> line break element (self-closing)."""
    return svg_tags.RECT(**attrs).render()

def line(**attrs):
    """Represents an HTML <line/> line break element (self-closing)."""
    return svg_tags.LINE(**attrs).render()

def polyline(**attrs):
    """Represents an HTML <polyline/> line break element (self-closing)."""
    return svg_tags.POLYLINE(**attrs).render()

def polygon(**attrs):
    """Represents an HTML <polygon/> line break element (self-closing)."""
    return svg_tags.POLYGON(**attrs).render()

def ellipse(**attrs):
    """Represents an HTML <ellipse/> line break element (self-closing)."""
    return svg_tags.ELLIPSE(**attrs).render()

def image(**attrs):
    """Represents an HTML <image/> line break element (self-closing)."""
    return svg_tags.IMAGE(**attrs).render()

def feBlend(**attrs):
    """Represents an HTML <feBlend/> line break element (self-closing)."""
    return svg_tags.FEBLEND(**attrs).render()

def feColorMatrix(**attrs):
    """Represents an HTML <feColorMatrix/> line break element (self-closing)."""
    return svg_tags.FECOLORMATRIX(**attrs).render()

def feComposite(**attrs):
    """Represents an HTML <feComposite/> line break element (self-closing)."""
    return svg_tags.FECOMPOSITE(**attrs).render()

def feConvolveMatrix(**attrs):
    """Represents an HTML <feConvolveMatrix/> line break element (self-closing)."""
    return svg_tags.FECONVOLVEMATRIX(**attrs).render()

def feDisplacementMap(**attrs):
    """Represents an HTML <feDisplacementMap/> line break element (self-closing)."""
    return svg_tags.FEDISPLACEMENTMAP(**attrs).render()

def feDropShadow(**attrs):
    """Represents an HTML <feDropShadow/> line break element (self-closing)."""
    return svg_tags.FEDROPSHADOW(**attrs).render()

def feFlood(**attrs):
    """Represents an HTML <feFlood/> line break element (self-closing)."""
    return svg_tags.FEFLOOD(**attrs).render()

def feFuncA(**attrs):
    """Represents an HTML <feFuncA/> line break element (self-closing)."""
    return svg_tags.FEFUNCA(**attrs).render()

def feFuncB(**attrs):
    """Represents an HTML <feFuncB/> line break element (self-closing)."""
    return svg_tags.FEFUNCB(**attrs).render()

def feFuncG(**attrs):
    """Represents an HTML <feFuncG/> line break element (self-closing)."""
    return svg_tags.FEFUNCG(**attrs).render()

def feFuncR(**attrs):
    """Represents an HTML <feFuncR/> line break element (self-closing)."""
    return svg_tags.FEFUNCR(**attrs).render()

def feGaussianBlur(**attrs):
    """Represents an HTML <feGaussianBlur/> line break element (self-closing)."""
    return svg_tags.FEGAUSSIANBLUR(**attrs).render()

def feImage(**attrs):
    """Represents an HTML <feImage/> line break element (self-closing)."""
    return svg_tags.FEIMAGE(**attrs).render()

def feMergeNode(**attrs):
    """Represents an HTML <feMergeNode/> line break element (self-closing)."""
    return svg_tags.FEMERGENODE(**attrs).render()

def feMorphology(**attrs):
    """Represents an HTML <feMorphology/> line break element (self-closing)."""
    return svg_tags.FEMORPHOLOGY(**attrs).render()

def feOffset(**attrs):
    """Represents an HTML <feOffset/> line break element (self-closing)."""
    return svg_tags.FEOFFSET(**attrs).render()

def fePointLight(**attrs):
    """Represents an HTML <fePointLight/> line break element (self-closing)."""
    return svg_tags.FEPOINTLIGHT(**attrs).render()

def feSpotLight(**attrs):
    """Represents an HTML <feSpotLight/> line break element (self-closing)."""
    return svg_tags.FESPOTLIGHT(**attrs).render()

def feTile(**attrs):
    """Represents an HTML <feTile/> line break element (self-closing)."""
    return svg_tags.FETILE(**attrs).render()

def feTurbulence(**attrs):
    """Represents an HTML <feTurbulence/> line break element (self-closing)."""
    return svg_tags.FETURBULENCE(**attrs).render()

def animate(**attrs):
    """Represents an HTML <animate/> line break element (self-closing)."""
    return svg_tags.ANIMATE(**attrs).render()

def animateTransform(**attrs):
    """Represents an HTML <animateTransform/> line break element (self-closing)."""
    return svg_tags.ANIMATETRANSFORM(**attrs).render()

def Set(**attrs):
    """Represents an HTML <set/> line break element (self-closing)."""
    return svg_tags.SET(**attrs).render()

def view(**attrs):
    """Represents an HTML <view/> line break element (self-closing)."""
    return svg_tags.VIEW(**attrs).render()

def use(**attrs):
    """Represents an HTML <use/> line break element (self-closing)."""
    return svg_tags.USE(**attrs).render()

def stop(**attrs):
    """Represents an HTML <stop/> line break element (self-closin).""" 
    return svg_tags.STOP(**attrs).render()