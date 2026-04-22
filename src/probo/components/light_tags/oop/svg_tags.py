from probo.components.light_tags.node import LightNode
from probo.components.node import ElementNodeMixin,ElementMutatorMixin
from typing import Any

class Lg(LightNode, ElementNodeMixin):
    """Represents an G HTML <g> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="g".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

        
    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch) 

class Ldefs(LightNode, ElementNodeMixin):
    """Represents an DEFS HTML <defs> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="defs".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)

class Ltext(LightNode, ElementNodeMixin):
    """Represents an TEXT HTML <text> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="text".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch) 

class Ltspan(LightNode, ElementNodeMixin):
    """Represents an TSPAN HTML <tspan> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="tspan".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch) 


class Lsvg(LightNode, ElementNodeMixin,):
    """Represents an SVG HTML <svg> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)


class Lsymbol(LightNode, ElementNodeMixin):
    """Represents an SYMBOL HTML <symbol> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="symbol".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)  

class Lmarker(LightNode, ElementNodeMixin):
    """Represents an MARKER HTML <marker> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="marker".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)

class Lpattern(LightNode, ElementNodeMixin):
    """Represents an PATTERN HTML <pattern> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="pattern".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch) 

class Lmask(LightNode, ElementNodeMixin):
    """Represents an MASK HTML <mask> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="mask".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)

class LclipPath(LightNode, ElementNodeMixin):
    """Represents an CLIPPATH HTML <clipPath> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="clipPath".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class LlinearGradient(LightNode, ElementNodeMixin):
    """Represents an LINEARGRADIENT HTML <linearGradient> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="linearGradient".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class LradialGradient(LightNode, ElementNodeMixin):
    """Represents an RADIALGRADIENT HTML <radialGradient> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="radialGradient".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class Lfilter(LightNode, ElementNodeMixin):
    """Represents an FILTER HTML <filter> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="filter".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class LfeComponentTransfer(LightNode, ElementNodeMixin):
    """Represents an FECOMPONENTTRANSFER HTML <feComponentTransfer> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="feComponentTransfer".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class LfeDiffuseLighting(LightNode, ElementNodeMixin):
    """Represents an FEDIFFUSELIGHTING HTML <feDiffuseLighting> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="feDiffuseLighting".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class LfeMerge(LightNode, ElementNodeMixin):
    """Represents an FEMERGE HTML <feMerge> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="feMerge".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class LfeSpecularLighting(LightNode, ElementNodeMixin):
    """Represents an FESPECULARLIGHTING HTML <feSpecularLighting> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="feSpecularLighting".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class LanimateMotion(LightNode, ElementNodeMixin):
    """Represents an ANIMATEMOTION HTML <animateMotion> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="animateMotion".lower(),**attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

class LforeignObject(LightNode, ElementNodeMixin):
    """Represents an FOREIGNOBJECT HTML <foreignObject> element."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, *content:tuple[str|ElementNodeMixin], **attrs:dict[str,Any]):
        super().__init__(*content,tag="foreignObject".lower(), **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)        

# self closing tags

class Lpath(LightNode, ElementNodeMixin):
    """Represents an PATH HTML <path> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="path".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lcircle(LightNode, ElementNodeMixin):
    """Represents an CIRCLE HTML <circle> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="circle".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lrect(LightNode, ElementNodeMixin):
    """Represents an RECT HTML <rect> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="rect".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lline(LightNode, ElementNodeMixin):
    """Represents an LINE HTML <line> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="line".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lpolyline(LightNode, ElementNodeMixin):
    """Represents an POLYLINE HTML <polyline> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="polyline".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lpolygon(LightNode, ElementNodeMixin):
    """Represents an POLYGON HTML <polygon> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="polygon".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lellipse(LightNode, ElementNodeMixin):
    """Represents an ELLIPSE HTML <ellipse> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="ellipse".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Limage(LightNode, ElementNodeMixin):
    """Represents an IMAGE HTML <image> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="image".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeBlend(LightNode, ElementNodeMixin):
    """Represents an FEBLEND HTML <feBlend> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feBlend".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeColorMatrix(LightNode, ElementNodeMixin):
    """Represents an FECOLORMATRIX HTML <feColorMatrix> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feColorMatrix".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeComposite(LightNode, ElementNodeMixin):
    """Represents an FECOMPOSITE HTML <feComposite> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feComposite".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeConvolveMatrix(LightNode, ElementNodeMixin):
    """Represents an FECONVOLVEMATRIX HTML <feConvolveMatrix> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feConvolveMatrix".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeDisplacementMap(LightNode, ElementNodeMixin):
    """Represents an FEDISPLACEMENTMAP HTML <feDisplacementMap> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feDisplacementMap".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeDropShadow(LightNode, ElementNodeMixin):
    """Represents an FEDROPSHADOW HTML <feDropShadow> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feDropShadow".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeFlood(LightNode, ElementNodeMixin):
    """Represents an FEFLOOD HTML <feFlood> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feFlood".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeFuncA(LightNode, ElementNodeMixin):
    """Represents an FEFUNCA HTML <feFuncA> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feFuncA".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeFuncB(LightNode, ElementNodeMixin):
    """Represents an FEFUNCB HTML <feFuncB> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feFuncB".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeFuncG(LightNode, ElementNodeMixin):
    """Represents an FEFUNCG HTML <feFuncG> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feFuncG".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeFuncR(LightNode, ElementNodeMixin):
    """Represents an FEFUNCR HTML <feFuncR> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feFuncR".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeGaussianBlur(LightNode, ElementNodeMixin):
    """Represents an FEGAUSSIANBLUR HTML <feGaussianBlur> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feGaussianBlur".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeImage(LightNode, ElementNodeMixin):
    """Represents an FEIMAGE HTML <feImage> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feImage".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeMergeNode(LightNode, ElementNodeMixin):
    """Represents an FEMERGENODE HTML <feMergeNode> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feMergeNode".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeMorphology(LightNode, ElementNodeMixin):
    """Represents an FEMORPHOLOGY HTML <feMorphology> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feMorphology".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeOffset(LightNode, ElementNodeMixin):
    """Represents an FEOFFSET HTML <feOffset> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feOffset".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfePointLight(LightNode, ElementNodeMixin):
    """Represents an FEPOINTLIGHT HTML <fePointLight> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="fePointLight".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeSpotLight(LightNode, ElementNodeMixin):
    """Represents an FESPOTLIGHT HTML <feSpotLight> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feSpotLight".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeTile(LightNode, ElementNodeMixin):
    """Represents an FETILE HTML <feTile> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feTile".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LfeTurbulence(LightNode, ElementNodeMixin):
    """Represents an FETURBULENCE HTML <feTurbulence> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="feTurbulence".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lanimate(LightNode, ElementNodeMixin):
    """Represents an ANIMATE HTML <animate> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="animate".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class LanimateTransform(LightNode, ElementNodeMixin):
    """Represents an ANIMATETRANSFORM HTML <animateTransform> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="animateTransform".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lset(LightNode, ElementNodeMixin):
    """Represents an SET HTML <set> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="set".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lview(LightNode, ElementNodeMixin):
    """Represents an VIEW HTML <view> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="view".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Luse(LightNode, ElementNodeMixin):
    """Represents an USE HTML <use> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="use".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
class Lstop(LightNode, ElementNodeMixin):
    """Represents an STOP HTML <stop> line break element (self-closing)."""

    __slots__ = ("_el_instance", "use_list", "use_deque", "element_data")
    def __init__(self, **kwargs):
        super().__init__(tag="stop".lower(),**kwargs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)

    def render(self,EL):
        return super().render(EL)

    def stream(self, EL,batch=50):
        yield from super().stream(EL,batch)
