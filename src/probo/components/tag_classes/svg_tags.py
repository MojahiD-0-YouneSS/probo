from probo.components.elements import Element
from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin
from probo.components.tag_classes.block_tags import EL

class G(BaseHTMLElement, ElementNodeMixin):
    """Represents an G HTML <g> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:g = Element(
        ).set_attrs(**self.attributes).set_content(self.content).g().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .g()
            .element
        )

class DEFS(BaseHTMLElement, ElementNodeMixin):
    """Represents an DEFS HTML <defs> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:defs = Element(
        ).set_attrs(**self.attributes).set_content(self.content).defs().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .defs()
            .element
        )

class TEXT(BaseHTMLElement, ElementNodeMixin):
    """Represents an TEXT HTML <text> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:text = Element(
        ).set_attrs(**self.attributes).set_content(self.content).text().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .text()
            .element
        )

class TSPAN(BaseHTMLElement, ElementNodeMixin):
    """Represents an TSPAN HTML <tspan> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:tspan = Element(
        ).set_attrs(**self.attributes).set_content(self.content).tspan().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .tspan()
            .element
        )

class SVG(BaseHTMLElement,ElementNodeMixin):
    """Represents an SVG HTML <svg> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:svg = Element(
        ).set_attrs(**self.attributes).set_content(self.content).svg().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .svg()
            .element
        )
    
class SYMBOL(BaseHTMLElement, ElementNodeMixin):
    """Represents an SYMBOL HTML <symbol> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:symbol = Element(
        ).set_attrs(**self.attributes).set_content(self.content).symbol().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .symbol()
            .element
        )

class MARKER(BaseHTMLElement, ElementNodeMixin):
    """Represents an MARKER HTML <marker> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:marker = Element(
        ).set_attrs(**self.attributes).set_content(self.content).marker().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .marker()
            .element
        )

class PATTERN(BaseHTMLElement, ElementNodeMixin):
    """Represents an PATTERN HTML <pattern> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:pattern = Element(
        ).set_attrs(**self.attributes).set_content(self.content).pattern().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .pattern()
            .element
        )

class MASK(BaseHTMLElement, ElementNodeMixin):
    """Represents an MASK HTML <mask> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:mask = Element(
        ).set_attrs(**self.attributes).set_content(self.content).mask().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .mask()
            .element
        )

class CLIPPATH(BaseHTMLElement, ElementNodeMixin):
    """Represents an CLIPPATH HTML <clipPath> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:clipPath = Element(
        ).set_attrs(**self.attributes).set_content(self.content).clipPath().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .clipPath()
            .element
        )

class LINEARGRADIENT(BaseHTMLElement, ElementNodeMixin):
    """Represents an LINEARGRADIENT HTML <linearGradient> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:linearGradient = Element(
        ).set_attrs(**self.attributes).set_content(self.content).linearGradient().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .linearGradient()
            .element
        )

class RADIALGRADIENT(BaseHTMLElement, ElementNodeMixin):
    """Represents an RADIALGRADIENT HTML <radialGradient> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:radialGradient = Element(
        ).set_attrs(**self.attributes).set_content(self.content).radialGradient().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .radialGradient()
            .element
        )

class FILTER(BaseHTMLElement, ElementNodeMixin):
    """Represents an FILTER HTML <filter> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:filter = Element(
        ).set_attrs(**self.attributes).set_content(self.content).filter().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .filter()
            .element
        )

class FECOMPONENTTRANSFER(BaseHTMLElement, ElementNodeMixin):
    """Represents an FECOMPONENTTRANSFER HTML <feComponentTransfer> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:feComponentTransfer = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feComponentTransfer().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .feComponentTransfer()
            .element
        )

class FEDIFFUSELIGHTING(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEDIFFUSELIGHTING HTML <feDiffuseLighting> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:feDiffuseLighting = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feDiffuseLighting().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .feDiffuseLighting()
            .element
        )

class FEMERGE(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEMERGE HTML <feMerge> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:feMerge = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feMerge().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .feMerge()
            .element
        )

class FESPECULARLIGHTING(BaseHTMLElement, ElementNodeMixin):
    """Represents an FESPECULARLIGHTING HTML <feSpecularLighting> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:feSpecularLighting = Element(
        ).set_attrs(**self.attributes).set_content(self.content).feSpecularLighting().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .feSpecularLighting()
            .element
        )

class ANIMATEMOTION(BaseHTMLElement, ElementNodeMixin):
    """Represents an ANIMATEMOTION HTML <animateMotion> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:animateMotion = Element(
        ).set_attrs(**self.attributes).set_content(self.content).animateMotion().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .animateMotion()
            .element
        )

class FOREIGNOBJECT(BaseHTMLElement, ElementNodeMixin):
    """Represents an FOREIGNOBJECT HTML <foreignObject> element."""

    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self):
        '''
        Blueprint:foreignObject = Element(
        ).set_attrs(**self.attributes).set_content(self.content).foreignObject().element'''
        return (
            EL
            .set_attrs(**self.attributes)
            .set_content(self._get_rendered_content())
            .foreignObject()
            .element
        )

# self closing tags

class PATH(BaseHTMLElement, ElementNodeMixin):
    """Represents an PATH HTML <path> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).path().element

class CIRCLE(BaseHTMLElement, ElementNodeMixin):
    """Represents an CIRCLE HTML <circle> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).circle().element

class RECT(BaseHTMLElement, ElementNodeMixin):
    """Represents an RECT HTML <rect> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).rect().element

class LINE(BaseHTMLElement, ElementNodeMixin):
    """Represents an LINE HTML <line> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).line().element

class POLYLINE(BaseHTMLElement, ElementNodeMixin):
    """Represents an POLYLINE HTML <polyline> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).polyline().element

class POLYGON(BaseHTMLElement, ElementNodeMixin):
    """Represents an POLYGON HTML <polygon> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).polygon().element

class ELLIPSE(BaseHTMLElement, ElementNodeMixin):
    """Represents an ELLIPSE HTML <ellipse> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).ellipse().element

class IMAGE(BaseHTMLElement, ElementNodeMixin):
    """Represents an IMAGE HTML <image> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).image().element

class FEBLEND(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEBLEND HTML <feBlend> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feBlend().element

class FECOLORMATRIX(BaseHTMLElement, ElementNodeMixin):
    """Represents an FECOLORMATRIX HTML <feColorMatrix> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feColorMatrix().element

class FECOMPOSITE(BaseHTMLElement, ElementNodeMixin):
    """Represents an FECOMPOSITE HTML <feComposite> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feComposite().element

class FECONVOLVEMATRIX(BaseHTMLElement, ElementNodeMixin):
    """Represents an FECONVOLVEMATRIX HTML <feConvolveMatrix> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feConvolveMatrix().element

class FEDISPLACEMENTMAP(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEDISPLACEMENTMAP HTML <feDisplacementMap> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feDisplacementMap().element

class FEDROPSHADOW(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEDROPSHADOW HTML <feDropShadow> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feDropShadow().element

class FEFLOOD(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEFLOOD HTML <feFlood> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feFlood().element

class FEFUNCA(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEFUNCA HTML <feFuncA> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feFuncA().element

class FEFUNCB(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEFUNCB HTML <feFuncB> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feFuncB().element

class FEFUNCG(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEFUNCG HTML <feFuncG> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feFuncG().element

class FEFUNCR(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEFUNCR HTML <feFuncR> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feFuncR().element

class FEGAUSSIANBLUR(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEGAUSSIANBLUR HTML <feGaussianBlur> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feGaussianBlur().element

class FEIMAGE(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEIMAGE HTML <feImage> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feImage().element

class FEMERGENODE(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEMERGENODE HTML <feMergeNode> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feMergeNode().element

class FEMORPHOLOGY(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEMORPHOLOGY HTML <feMorphology> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feMorphology().element

class FEOFFSET(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEOFFSET HTML <feOffset> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feOffset().element

class FEPOINTLIGHT(BaseHTMLElement, ElementNodeMixin):
    """Represents an FEPOINTLIGHT HTML <fePointLight> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).fePointLight().element

class FESPOTLIGHT(BaseHTMLElement, ElementNodeMixin):
    """Represents an FESPOTLIGHT HTML <feSpotLight> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feSpotLight().element

class FETILE(BaseHTMLElement, ElementNodeMixin):
    """Represents an FETILE HTML <feTile> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feTile().element

class FETURBULENCE(BaseHTMLElement, ElementNodeMixin):
    """Represents an FETURBULENCE HTML <feTurbulence> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).feTurbulence().element

class ANIMATE(BaseHTMLElement, ElementNodeMixin):
    """Represents an ANIMATE HTML <animate> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).animate().element

class ANIMATETRANSFORM(BaseHTMLElement, ElementNodeMixin):
    """Represents an ANIMATETRANSFORM HTML <animateTransform> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).animateTransform().element

class SET(BaseHTMLElement, ElementNodeMixin):
    """Represents an SET HTML <set> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).set().element

class VIEW(BaseHTMLElement, ElementNodeMixin):
    """Represents an VIEW HTML <view> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).view().element

class USE(BaseHTMLElement, ElementNodeMixin):
    """Represents an USE HTML <use> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).use().element

class STOP(BaseHTMLElement, ElementNodeMixin):
    """Represents an STOP HTML <stop> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self):
        return EL.set_attrs(**self.attributes).stop().element
