from collections import deque
from probo.components.elements import Element
from probo.utility import ProboSourceString, _resolve_stream, StreamManager
from typing import Any, Generator

def l_doctype(EL:Element,content: str |None= None,stream=False,batch=50, **attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <!DOCTYPE> line break element (self-closing)."""
    if stream:
        def __stream_doctype():
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
        return EL.doctype(content or str(), **attrs).element


def l_area(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <area/> line break element (self-closing)."""
    if stream:
        def __stream_area():
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
        return EL.area(**attrs).element


def l_base(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <base/> line break element (self-closing)."""
    if stream:
        def __stream_base():
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
        return EL.base(**attrs).element


def l_br(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <br/> line break element (self-closing)."""
    if stream:
        def __stream_br():
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
        return EL.br(**attrs).element


def l_col(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <col/> line break element (self-closing)."""
    if stream:
        def __stream_col():
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
        return EL.col(**attrs).element


def l_embed(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <embed/> line break element (self-closing)."""
    if stream:
        def __stream_embed():
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
        return EL.embed(**attrs).element


def l_hr(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <hr/> line break element (self-closing)."""
    if stream:
        def __stream_hr():
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
        return EL.hr(**attrs).element


def l_img(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <img/> line break element (self-closing)."""
    if stream:
        def __stream_img():
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
        return EL.img(**attrs).element


def l_input(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <input/> line break element (self-closing)."""
    if stream:
        def __stream_input():
            stream_manager = StreamManager(
                None,
                (
                    EL
                    .input(**attrs)
                    .reset_generator_content()
                    .stream(batch=batch)
                ),
                chunk_size=batch,
            )
            return stream_manager
        return __stream_input()
    else:
        return EL.input(**attrs).element


def l_link(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <link/> line break element (self-closing)."""
    if stream:
        def __stream_link():
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
        return EL.link(**attrs).element


def l_meta(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <meta/> line break element (self-closing)."""
    if stream:
        def __stream_meta():
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
        return EL.meta(**attrs).element


def l_param(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <param/> line break element (self-closing)."""
    if stream:
        def __stream_param():
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
        return EL.param(**attrs).element


def l_source(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <source/> line break element (self-closing)."""
    if stream:
        def __stream_source():
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
        return EL.source(**attrs).element


def l_track(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <track/> line break element (self-closing)."""
    if stream:
        def __stream_track():
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
        return EL.track(**attrs).element


def l_wbr(EL:Element,stream:bool=False,batch:int=50,**attrs: dict[str, Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|Generator|StreamManager:
    """Represents an HTML <wbr/> line break element (self-closing)."""
    if stream:
        def __stream_wbr():
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
        return EL.wbr(**attrs).element
