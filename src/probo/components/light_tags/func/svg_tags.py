from probo.components.elements import Element
from typing import Any,Generator
from probo.utility import ProboSourceString, StreamManager, _resolve_stream
from collections import deque

def l_g(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <g> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).g(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.g(*content, **attrs).element


def l_defs(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <dfs> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).defs(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.defs(*content, **attrs).element


def l_text(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <text> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).text(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.text(*content, **attrs).element


def l_tspan(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <tspan> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).tspan(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.tspan(*content, **attrs).element


def l_svg(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <svg> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).svg(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.svg(*content, **attrs).element


def l_symbol(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <symbol> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).symbol(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.symbol(*content, **attrs).element


def l_marker(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <marker> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).marker(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.marker(*content, **attrs).element


def l_pattern(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <pattern> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).pattern(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.pattern(*content, **attrs).element


def l_mask(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <mask> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).mask(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.mask(*content, **attrs).element


def l_clippath(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <clippath> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).clippath(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.clippath(*content, **attrs).element


def l_lineargradient(EL:Element,*content: tuple[str], **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <lineargradient> element."""
    return EL.lineargradient(content, **attrs).element


def l_radialgradient(EL:Element,*content: tuple[str], **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <radialgradient> element."""
    return EL.radialgradient(content, **attrs).element


def l_filter(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <filter> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).Filter(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.Filter(*content, **attrs).element


def l_fecomponenttransfer(EL:Element,
    *content: tuple[str], stream:bool=False,batch:int=50,**attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <fecomponenttransfer> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).fecomponenttransfer(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.fecomponenttransfer(*content, **attrs).element


def l_fediffuselighting(EL:Element,
    *content: tuple[str], stream:bool=False,batch:int=50,**attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <fediffuselighting> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).fediffuselighting(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.fediffuselighting(*content, **attrs).element


def l_femerge(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <femerge> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).femerge(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.femerge(*content, **attrs).element


def l_fespecularlighting(EL:Element,
    *content: tuple[str], stream:bool=False,batch:int=50,**attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <fespecularlighting> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).fespecularlighting(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.fespecularlighting(*content, **attrs).element


def l_animatemotion(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <animatemotion> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).animatemotion(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.animatemotion(*content, **attrs).element


def l_foreignobject(EL:Element,*content: tuple[str],stream:bool=False,batch:int=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <forienobject> element."""

    if stream:
        content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
        EL.set_generator_content(content_gen).foreignobject(**attrs)
        stream_manager = StreamManager(
            opening=EL.element[0],
            content_gen=EL.stream(batch),
            closing=EL.element[1],
            chunk_size=batch
        )
        return stream_manager

    else:
        return EL.foreignobject(*content, **attrs).element


# self closing
def l_path(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <path/> line break element (self-closing)."""
    if stream:
        def __stream_path():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .path(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_path()
    else:
        return EL.path(**attrs).element


def l_circle(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <circle/> line break element (self-closing)."""
    if stream:
        def __stream_circle():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .circle(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_circle()
    else:
        return EL.circle(**attrs).element


def l_rect(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <rect/> line break element (self-closing)."""
    if stream:
        def __stream_rect():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .rect(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_rect()
    else:
        return EL.rect(**attrs).element


def l_line(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <line/> line break element (self-closing)."""
    if stream:
        def __stream_line():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .line(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_line()
    else:
        return EL.line(**attrs).element


def l_polyline(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <polyline/> line break element (self-closing)."""
    if stream:
        def __stream_polyline():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .polyline(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_polyline()
    else:
        return EL.polyline(**attrs).element


def l_polygon(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <polygon/> line break element (self-closing)."""
    if stream:
        def __stream_polygon():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .polygon(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_polygon()
    else:
        return EL.polygon(**attrs).element


def l_ellipse(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <ellipse/> line break element (self-closing)."""
    if stream:
        def __stream_ellipse():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .ellipse(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_ellipse()
    else:
        return EL.ellipse(**attrs).element


def l_image(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <image/> line break element (self-closing)."""
    if stream:
        def __stream_image():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .image(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_image()
    else:
        return EL.image(**attrs).element


def l_feBlend(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feBlend/> line break element (self-closing)."""
    if stream:
        def __stream_feBlend():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feBlend(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feBlend()
    else:
        return EL.feBlend(**attrs).element


def l_feColorMatrix(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feColorMatrix/> line break element (self-closing)."""
    if stream:
        def __stream_feColorMatrix():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feColorMatrix(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feColorMatrix()
    else:
        return EL.feColorMatrix(**attrs).element


def l_feComposite(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feComposite/> line break element (self-closing)."""
    if stream:
        def __stream_feComposite():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feComposite(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feComposite()
    else:
        return EL.feComposite(**attrs).element


def l_feConvolveMatrix(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feConvolveMatrix/> line break element (self-closing)."""
    if stream:
        def __stream_feConvolveMatrix():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feConvolveMatrix(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feConvolveMatrix()
    else:
        return EL.feConvolveMatrix(**attrs).element


def l_feDisplacementMap(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feDisplacementMap/> line break element (self-closing)."""
    if stream:
        def __stream_feDisplacementMap():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feDisplacementMap(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feDisplacementMap()
    else:
        return EL.feDisplacementMap(**attrs).element


def l_feDropShadow(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feDropShadow/> line break element (self-closing)."""
    if stream:
        def __stream_feDropShadow():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feDropShadow(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feDropShadow()
    else:
        return EL.feDropShadow(**attrs).element


def l_feFlood(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feFlood/> line break element (self-closing)."""
    if stream:
        def __stream_feFlood():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feFlood(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feFlood()
    else:
        return EL.feFlood(**attrs).element


def l_feFuncA(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feFuncA/> line break element (self-closing)."""
    if stream:
        def __stream_feFuncA():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feFuncA(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feFuncA()
    else:
        return EL.feFuncA(**attrs).element


def l_feFuncB(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feFuncB/> line break element (self-closing)."""
    if stream:
        def __stream_feFuncB():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feFuncB(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feFuncB()
    else:
        return EL.feFuncB(**attrs).element


def l_feFuncG(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feFuncG/> line break element (self-closing)."""
    if stream:
        def __stream_feFuncG():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feFuncG(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feFuncG()
    else:
        return EL.feFuncG(**attrs).element


def l_feFuncR(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feFuncR/> line break element (self-closing)."""
    if stream:
        def __stream_feFuncR():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feFuncR(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feFuncR()
    else:
        return EL.feFuncR(**attrs).element


def l_feGaussianBlur(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feGaussianBlur/> line break element (self-closing)."""
    if stream:
        def __stream_feGaussianBlur():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feGaussianBlur(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feGaussianBlur()
    else:
        return EL.feGaussianBlur(**attrs).element


def l_feImage(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feImage/> line break element (self-closing)."""
    if stream:
        def __stream_feImage():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feImage(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feImage()
    else:
        return EL.feImage(**attrs).element


def l_feMergeNode(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feMergeNode/> line break element (self-closing)."""
    if stream:
        def __stream_feMergeNode():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feMergeNode(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feMergeNode()
    else:
        return EL.feMergeNode(**attrs).element


def l_feMorphology(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feMorphology/> line break element (self-closing)."""
    if stream:
        def __stream_feMorphology():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feMorphology(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feMorphology()
    else:
        return EL.feMorphology(**attrs).element


def l_feOffset(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feOffset/> line break element (self-closing)."""
    if stream:
        def __stream_feOffset():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feOffset(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feOffset()
    else:
        return EL.feOffset(**attrs).element


def l_fePointLight(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <fePointLight/> line break element (self-closing)."""
    if stream:
        def __stream_fePointLight():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .fePointLight(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_fePointLight()
    else:
        return EL.fePointLight(**attrs).element


def l_feSpotLight(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feSpotLight/> line break element (self-closing)."""
    if stream:
        def __stream_feSpotLight():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feSpotLight(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feSpotLight()
    else:
        return EL.feSpotLight(**attrs).element


def l_feTile(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feTile/> line break element (self-closing)."""
    if stream:
        def __stream_feTile():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feTile(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feTile()
    else:
        return EL.feTile(**attrs).element


def l_feTurbulence(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <feTurbulence/> line break element (self-closing)."""
    if stream:
        def __stream_feTurbulence():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .feTurbulence(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_feTurbulence()
    else:
        return EL.feTurbulence(**attrs).element


def l_animate(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <animate/> line break element (self-closing)."""
    if stream:
        def __stream_animate():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .animate(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_animate()
    else:
        return EL.animate(**attrs).element


def l_animateTransform(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <animateTransform/> line break element (self-closing)."""
    if stream:
        def __stream_animateTransform():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .animateTransform(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_animateTransform()
    else:
        return EL.animateTransform(**attrs).element


def l_set(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <set/> line break element (self-closing)."""
    if stream:
        def __stream_Set():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .Set(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_Set()
    else:
        return EL.Set(**attrs).element


def l_view(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <view/> line break element (self-closing)."""
    if stream:
        def __stream_view():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .view(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_view()
    else:
        return EL.view(**attrs).element


def l_use(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <use/> line break element (self-closing)."""
    if stream:
        def __stream_use():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .use(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_use()
    else:
        return EL.use(**attrs).element


def l_stop(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager|Generator:
    """Represents an HTML <stop/> line break element (self-closin)."""
    if stream:
        def __stream_stop():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .stop(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_stop()
    else:
        return EL.stop(**attrs).element
