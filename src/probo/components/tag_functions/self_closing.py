from probo.components.elements import Element
from probo.utility import ProboSourceString,StreamManager,_resolve_stream
from typing import Any,Generator
from collections import deque

def doctype(
    content: str |None= None,
    return_list: bool = False,
    return_deque: bool = False,
    stream:bool=False,
    batch:int=50,
    **attrs: dict[str, Any],
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <!DOCTYPE> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_doctype():
            EL = Element(is_list=return_list, use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            yield from (EL.doctype(**attrs).reset_generator_content().stream(batch))

            stream_manager = StreamManager(
                opening=None,
                content_gen=content_gen,
                chunk_size=batch,
            )
            return stream_manager
        return __stream_doctype()
    else:
        return( Element(is_list=return_list, use_deque=return_deque)
        .doctype(content or str(), **attrs)
        .element
    )


def area(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <area/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_area():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .area(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_area()

    else:
        return Element(is_list=return_list, use_deque=return_deque).area(**attrs).element


def base(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <base/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_base():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .base(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_base()

    else:
        return Element(is_list=return_list, use_deque=return_deque).base(**attrs).element


def br(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <br/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_br():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .br(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_br()

    else:
        return Element(is_list=return_list, use_deque=return_deque).br(**attrs).element


def col(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <col/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_col():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .col(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_col()

    else:
        return Element(is_list=return_list, use_deque=return_deque).col(**attrs).element


def embed(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <embed/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_embed():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .embed(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_embed()

    else:
        return Element(is_list=return_list, use_deque=return_deque).embed(**attrs).element


def hr(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <hr/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_hr():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .hr(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_hr()

    else:
        return Element(is_list=return_list, use_deque=return_deque).hr(**attrs).element


def img(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <img/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_img():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .img(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_img()

    else:
        return Element(is_list=return_list, use_deque=return_deque).img(**attrs).element


def Input(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <input/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_Input():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .Input(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_Input()

    else:
        return Element(is_list=return_list, use_deque=return_deque).input(**attrs).element


def link(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <link/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_link():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .link(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_link()

    else:
        return Element(is_list=return_list, use_deque=return_deque).link(**attrs).element


def meta(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <meta/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_meta():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .meta(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_meta()

    else:
        return Element(is_list=return_list, use_deque=return_deque).meta(**attrs).element


def param(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <param/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_param():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .param(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_param()

    else:
        return Element(is_list=return_list, use_deque=return_deque).param(**attrs).element


def source(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <source/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_source():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .source(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_source()

    else:
        return Element(is_list=return_list, use_deque=return_deque).source(**attrs).element


def track(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <track/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_track():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .track(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_track()

    else:
        return Element(is_list=return_list, use_deque=return_deque).track(**attrs).element


def wbr(
    return_list: bool = False, return_deque: bool = False,stream:bool=False,batch:int=50, **attrs: dict[str, Any]
) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <wbr/> line break element (self-closing)."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_wbr():
            EL = Element(is_list=return_list, use_deque=return_deque)
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .wbr(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_wbr()

    else:
        return Element(is_list=return_list, use_deque=return_deque).wbr(**attrs).element
