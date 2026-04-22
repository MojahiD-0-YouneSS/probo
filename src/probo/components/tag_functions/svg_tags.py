from collections import deque
from probo.components.elements import Element
from typing import Any
from probo.utility import ProboSourceString, StreamManager,_resolve_stream


def g(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <g> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_g():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).g(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_g()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .g(*content, **attrs)
        .element
    )


def defs(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dfs> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_defs():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).defs(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_defs()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .defs(*content, **attrs)
        .element
    )


def text(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <text> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_text():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).text(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_text()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .text(*content, **attrs)
        .element
    )


def tspan(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <tspan> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_tspan():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).tspan(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_tspan()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .tspan(*content, **attrs)
        .element
    )


def svg(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <svg> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_svg():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).svg(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_svg()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .svg(*content, **attrs)
        .element
    )


def symbol(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <symbol> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_symbol():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).symbol(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_symbol()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .symbol(*content, **attrs)
        .element
    )


def marker(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <marker> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_marker():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).marker(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_marker()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .marker(*content, **attrs)
        .element
    )


def pattern(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <pattern> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_pattern():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).pattern(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_pattern()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .pattern(*content, **attrs)
        .element
    )


def mask(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <mask> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_mask():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).mask(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_mask()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .mask(*content, **attrs)
        .element
    )


def clippath(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <clippath> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_clippath():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).clippath(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_clippath()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .clippath(*content, **attrs)
        .element
    )


def lineargradient(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <lineargradient> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_lineargradient():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).lineargradient(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_lineargradient()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .lineargradient(*content, **attrs)
        .element
    )


def radialgradient(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <radialgradient> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_radialgradient():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).radialgradient(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_radialgradient()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .radialgradient(*content, **attrs)
        .element
    )


def Filter(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <filter> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_Filter():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).Filter(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_Filter()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .Filter(*content, **attrs)
        .element
    )


def fecomponenttransfer(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <fecomponenttransfer> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_fecomponenttransfer():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).fecomponenttransfer(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_fecomponenttransfer()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .fecomponenttransfer(*content, **attrs)
        .element
    )


def fediffuselighting(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <fediffuselighting> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_fediffuselighting():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).fediffuselighting(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_fediffuselighting()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .fediffuselighting(*content, **attrs)
        .element
    )


def femerge(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <femerge> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_femerge():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).femerge(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_femerge()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .femerge(*content, **attrs)
        .element
    )


def fespecularlighting(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <fespecularlighting> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_fespecularlighting():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).fespecularlighting(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_fespecularlighting()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .fespecularlighting(*content, **attrs)
        .element
    )


def animatemotion(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <animatemotion> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_animatemotion():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).animatemotion(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_animatemotion()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .animatemotion(*content, **attrs)
        .element
    )


def foreignobject(
    *content: tuple[str],
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <forienobject> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_foreignobject():
            EL = Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).foreignobject(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_foreignobject()
    else:
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .foreignobject(*content, **attrs)
        .element
    )


# self closing
def path(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <path/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_path():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).path(**attrs).element


def circle(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <circle/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_circle():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).circle(**attrs).element


def rect(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <rect/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_rect():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).rect(**attrs).element


def line(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <line/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_line():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).line(**attrs).element


def polyline(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <polyline/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_polyline():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque).polyline(**attrs).element
    )


def polygon(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <polygon/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_polygon():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).polygon(**attrs).element


def ellipse(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ellipse/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_ellipse():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).ellipse(**attrs).element


def image(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <image/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_image():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).image(**attrs).element


def feBlend(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feBlend/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feBlend():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).feBlend(**attrs).element


def feColorMatrix(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feColorMatrix/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feColorMatrix():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feColorMatrix(**attrs)
        .element
    )


def feComposite(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feComposite/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feComposite():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feComposite(**attrs)
        .element
    )


def feConvolveMatrix(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feConvolveMatrix/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feConvolveMatrix():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feConvolveMatrix(**attrs)
        .element
    )


def feDisplacementMap(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feDisplacementMap/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feDisplacementMap():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feDisplacementMap(**attrs)
        .element
    )


def feDropShadow(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feDropShadow/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feDropShadow():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feDropShadow(**attrs)
        .element
    )


def feFlood(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feFlood/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feFlood():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).feFlood(**attrs).element


def feFuncA(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feFuncA/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feFuncA():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).feFuncA(**attrs).element


def feFuncB(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feFuncB/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feFuncB():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).feFuncB(**attrs).element


def feFuncG(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feFuncG/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feFuncG():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).feFuncG(**attrs).element


def feFuncR(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feFuncR/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feFuncR():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).feFuncR(**attrs).element


def feGaussianBlur(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feGaussianBlur/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feGaussianBlur():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feGaussianBlur(**attrs)
        .element
    )


def feImage(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feImage/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feImage():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).feImage(**attrs).element


def feMergeNode(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feMergeNode/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feMergeNode():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feMergeNode(**attrs)
        .element
    )


def feMorphology(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feMorphology/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feMorphology():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feMorphology(**attrs)
        .element
    )


def feOffset(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feOffset/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feOffset():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque).feOffset(**attrs).element
    )


def fePointLight(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <fePointLight/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_fePointLight():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .fePointLight(**attrs)
        .element
    )


def feSpotLight(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feSpotLight/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feSpotLight():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feSpotLight(**attrs)
        .element
    )


def feTile(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feTile/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feTile():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).feTile(**attrs).element


def feTurbulence(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <feTurbulence/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_feTurbulence():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .feTurbulence(**attrs)
        .element
    )


def animate(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <animate/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_animate():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).animate(**attrs).element


def animateTransform(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <animateTransform/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_animateTransform():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return (
        Element(is_list=return_list, use_deque=return_deque)
        .animateTransform(**attrs)
        .element
    )


def Set(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <set/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_Set():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).Set(**attrs).element


def view(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <view/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_view():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).view(**attrs).element


def use(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <use/> line break element (self-closing)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_use():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).use(**attrs).element


def stop(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <stop/> line break element (self-closin)."""
    
    if stream:
        if not return_list:
            return_list=True
        def __stream_stop():
            EL = Element(is_list=return_list,use_deque=return_deque)
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
        return Element(is_list=return_list, use_deque=return_deque).stop(**attrs).element
