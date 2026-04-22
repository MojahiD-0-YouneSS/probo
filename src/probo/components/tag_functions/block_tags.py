from probo.components.elements import Element
from probo.utility import ProboSourceString, StreamManager, _resolve_stream
from collections import deque
from typing import Any,Generator

def a(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <a> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_a():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).a(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_a()
    else:
        return Element(is_list=return_list,use_deque=return_deque).a(*content, **attrs).element


def abbr(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <abbr> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_abbr():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).abbr(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_abbr()
    else:
        return Element(is_list=return_list,use_deque=return_deque).abbr(*content, **attrs).element


def address(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <address> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_address():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).address(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_address()
    else:
        return Element(is_list=return_list,use_deque=return_deque).address(*content, **attrs).element


def article(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <article> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_article():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).article(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_article()
    else:
        return Element(is_list=return_list,use_deque=return_deque).article(*content, **attrs).element


def aside(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <aside> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_aside():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).aside(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_aside()
    else:
        return Element(is_list=return_list,use_deque=return_deque).aside(*content, **attrs).element


def audio(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <audio> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_audio():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).audio(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_audio()
    else:
        return Element(is_list=return_list,use_deque=return_deque).audio(*content, **attrs).element


def b(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <b> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_b():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).b(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_b()
    else:
        return Element(is_list=return_list,use_deque=return_deque).b(*content, **attrs).element


def bdi(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <bdi> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_bdi():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).bdi(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_bdi()
    else:
        return Element(is_list=return_list,use_deque=return_deque).bdi(*content, **attrs).element


def bdo(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <bdo> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_bdo():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).bdo(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_bdo()
    else:
        return Element(is_list=return_list,use_deque=return_deque).bdo(*content, **attrs).element


def blockquote(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <blockquote> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_blockquote():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).blockquote(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_blockquote()
    else:
        return Element(is_list=return_list,use_deque=return_deque).blockquote(*content, **attrs).element


def body(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <body> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_body():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).body(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_body()
    else:
        return Element(is_list=return_list,use_deque=return_deque).body(*content, **attrs).element


def button(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <button> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_button():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).button(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_button()
    else:
        return Element(is_list=return_list,use_deque=return_deque).button(*content, **attrs).element


def canvas(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <canvas> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_canvas():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).canvas(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_canvas()
    else:
        return Element(is_list=return_list,use_deque=return_deque).canvas(*content, **attrs).element


def caption(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <caption> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_caption():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).caption(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_caption()
    else:
        return Element(is_list=return_list,use_deque=return_deque).caption(*content, **attrs).element


def cite(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <cite> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_cite():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).cite(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_cite()
    else:
        return Element(is_list=return_list,use_deque=return_deque).cite(*content, **attrs).element


def code(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <code> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_code():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).code(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_code()
    else:
        return Element(is_list=return_list,use_deque=return_deque).code(*content, **attrs).element


def colgroup(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <colgroup> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_colgroup():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).colgroup(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_colgroup()
    else:
        return Element(is_list=return_list,use_deque=return_deque).colgroup(*content, **attrs).element


def data(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <data> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_data():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).data(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_data()
    else:
        return Element(is_list=return_list,use_deque=return_deque).data(*content, **attrs).element


def datalist(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <datalist> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_datalist():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).datalist(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_datalist()
    else:
        return Element(is_list=return_list,use_deque=return_deque).datalist(*content, **attrs).element


def dd(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dd> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_dd():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).dd(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_dd()
    else:
        return Element(is_list=return_list,use_deque=return_deque).dd(*content, **attrs).element


def Del(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <del> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_Del():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).Del(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_Del()
    else:
        return Element(is_list=return_list,use_deque=return_deque).Del(*content, **attrs).element


def details(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <details> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_details():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).details(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_details()
    else:
        return Element(is_list=return_list,use_deque=return_deque).details(*content, **attrs).element


def dfn(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dfn> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_dfn():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).dfn(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_dfn()
    else:
        return Element(is_list=return_list,use_deque=return_deque).dfn(*content, **attrs).element


def dialog(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dialog> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_dialog():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).dialog(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_dialog()
    else:
        return Element(is_list=return_list,use_deque=return_deque).dialog(*content, **attrs).element


def div(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <div> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_div():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).div(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_div()
    else:
        return Element(is_list=return_list,use_deque=return_deque).div(*content, **attrs).element


def dl(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dl> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_dl():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).dl(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_dl()
    else:
        return Element(is_list=return_list,use_deque=return_deque).dl(*content, **attrs).element


def dt(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dt> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_dt():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).dt(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_dt()
    else:
        return Element(is_list=return_list,use_deque=return_deque).dt(*content, **attrs).element


def em(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <em> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_em():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).em(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_em()
    else:
        return Element(is_list=return_list,use_deque=return_deque).em(*content, **attrs).element


def fieldset(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <fieldset> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_fieldset():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).fieldset(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_fieldset()
    else:
        return Element(is_list=return_list,use_deque=return_deque).fieldset(*content, **attrs).element


def figcaption(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <figcaption> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_figcaption():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).figcaption(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_figcaption()
    else:
        return Element(is_list=return_list,use_deque=return_deque).figcaption(*content, **attrs).element


def figure(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <figure> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_figure():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).figure(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_figure()
    else:
        return Element(is_list=return_list,use_deque=return_deque).figure(*content, **attrs).element


def footer(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <footer> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_footer():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).footer(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_footer()
    else:
        return Element(is_list=return_list,use_deque=return_deque).footer(*content, **attrs).element


def form(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <form> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_form():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).form(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_form()
    else:
        return Element(is_list=return_list,use_deque=return_deque).form(*content, **attrs).element


def h1(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h1> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_h1():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).h1(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_h1()
    else:
        return Element(is_list=return_list,use_deque=return_deque).h1(*content, **attrs).element


def h2(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h2> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_h2():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).h2(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_h2()
    else:
        return Element(is_list=return_list,use_deque=return_deque).h2(*content, **attrs).element


def h3(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h3> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_h3():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).h3(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_h3()
    else:
        return Element(is_list=return_list,use_deque=return_deque).h3(*content, **attrs).element


def h4(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h4> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_h4():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).h4(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_h4()
    else:
        return Element(is_list=return_list,use_deque=return_deque).h4(*content, **attrs).element


def h5(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h5> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_h5():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).h5(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_h5()
    else:
        return Element(is_list=return_list,use_deque=return_deque).h5(*content, **attrs).element


def h6(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h6> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_h6():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).h6(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_h6()
    else:
        return Element(is_list=return_list,use_deque=return_deque).h6(*content, **attrs).element


def head(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <head> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_head():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).head(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_head()
    else:
        return Element(is_list=return_list,use_deque=return_deque).head(*content, **attrs).element


def header(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <header> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_header():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).header(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_header()
    else:
        return Element(is_list=return_list,use_deque=return_deque).header(*content, **attrs).element


def hgroup(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <hgroup> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_hgroup():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).hgroup(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_hgroup()
    else:
        return Element(is_list=return_list,use_deque=return_deque).hgroup(*content, **attrs).element


def html(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <html> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_html():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).html(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_html()
    else:
        return Element(is_list=return_list,use_deque=return_deque).html(*content, **attrs).element


def i(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <i> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_i():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).i(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_i()
    else:
        return Element(is_list=return_list,use_deque=return_deque).i(*content, **attrs).element


def iframe(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <iframe> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_iframe():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).iframe(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_iframe()
    else:
        return Element(is_list=return_list,use_deque=return_deque).iframe(*content, **attrs).element


def ins(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ins> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_ins():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).ins(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_ins()
    else:
        return Element(is_list=return_list,use_deque=return_deque).ins(*content, **attrs).element


def kbd(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <kbd> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_kbd():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).kbd(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_kbd()
    else:
        return Element(is_list=return_list,use_deque=return_deque).kbd(*content, **attrs).element


def label(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <label> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_label():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).label(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_label()
    else:
        return Element(is_list=return_list,use_deque=return_deque).label(*content, **attrs).element


def legend(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <legend> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_legend():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).legend(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_legend()
    else:
        return Element(is_list=return_list,use_deque=return_deque).legend(*content, **attrs).element


def li(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <li> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_li():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).li(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_li()
    else:
        return Element(is_list=return_list,use_deque=return_deque).li(*content, **attrs).element


def main(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <main> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_main():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).main(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_main()
    else:
        return Element(is_list=return_list,use_deque=return_deque).main(*content, **attrs).element


def math(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <math> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_math():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).math(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_math()
    else:
        return Element(is_list=return_list,use_deque=return_deque).math(*content, **attrs).element


def Map(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <map> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_Map():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).map(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_Map()
    else:
        return Element(is_list=return_list,use_deque=return_deque).map(*content, **attrs).element


def mark(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <mark> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_mark():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).mark(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_mark()
    else:
        return Element(is_list=return_list,use_deque=return_deque).mark(*content, **attrs).element


def menu(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <menu> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_menu():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).menu(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_menu()
    else:
        return Element(is_list=return_list,use_deque=return_deque).menu(*content, **attrs).element


def meter(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <meter> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_meter():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).meter(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_meter()
    else:
        return Element(is_list=return_list,use_deque=return_deque).meter(*content, **attrs).element


def nav(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <nav> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_nav():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).nav(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_nav()
    else:
        return Element(is_list=return_list,use_deque=return_deque).nav(*content, **attrs).element


def noscript(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <noscript> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_noscript():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).noscript(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_noscript()
    else:
        return Element(is_list=return_list,use_deque=return_deque).noscript(*content, **attrs).element


def Object(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <object> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_Object():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).Object(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_Object()
    else:
        return Element(is_list=return_list,use_deque=return_deque).Object(*content, **attrs).element


def ol(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ol> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_ol():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).ol(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_ol()
    else:
        return Element(is_list=return_list,use_deque=return_deque).ol(*content, **attrs).element


def optgroup(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <optgroup> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_optgroup():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).optgroup(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_optgroup()
    else:
        return Element(is_list=return_list,use_deque=return_deque).optgroup(*content, **attrs).element


def option(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <option> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_option():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).option(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_option()
    else:
        return Element(is_list=return_list,use_deque=return_deque).option(*content, **attrs).element


def output(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <output> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_output():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).output(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_output()
    else:
        return Element(is_list=return_list,use_deque=return_deque).output(*content, **attrs).element


def p(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <p> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_p():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).p(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_p()
    else:
        return Element(is_list=return_list,use_deque=return_deque).p(*content, **attrs).element


def portal(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <portal> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_portal():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).portal(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_portal()
    else:
        return Element(is_list=return_list,use_deque=return_deque).portal(*content, **attrs).element


def picture(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <picture> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_picture():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).picture(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_picture()
    else:
        return Element(is_list=return_list,use_deque=return_deque).picture(*content, **attrs).element


def pre(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <pre> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_pre():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).pre(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_pre()
    else:
        return Element(is_list=return_list,use_deque=return_deque).pre(*content, **attrs).element


def progress(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <progress> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_progress():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).progress(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_progress()
    else:
        return Element(is_list=return_list,use_deque=return_deque).progress(*content, **attrs).element


def q(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <q> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_q():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).q(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_q()
    else:
        return Element(is_list=return_list,use_deque=return_deque).q(*content, **attrs).element


def rp(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <rp> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_rp():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).rp(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_rp()
    else:
        return Element(is_list=return_list,use_deque=return_deque).rp(*content, **attrs).element


def rt(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <rt> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_rt():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).rt(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_rt()
    else:
        return Element(is_list=return_list,use_deque=return_deque).rt(*content, **attrs).element


def ruby(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ruby> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_ruby():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).ruby(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_ruby()
    else:
        return Element(is_list=return_list,use_deque=return_deque).ruby(*content, **attrs).element


def s(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <s> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_s():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).s(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_s()
    else:
        return Element(is_list=return_list,use_deque=return_deque).s(*content, **attrs).element


def samp(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <samp> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_samp():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).samp(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_samp()
    else:
        return Element(is_list=return_list,use_deque=return_deque).samp(*content, **attrs).element


def script(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <script> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_script():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).script(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_script()
    else:
        return Element(is_list=return_list,use_deque=return_deque).script(*content, **attrs).element


def search(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <search> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_search():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).search(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_search()
    else:
        return Element(is_list=return_list,use_deque=return_deque).search(*content, **attrs).element


def section(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <section> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_section():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).section(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_section()
    else:
        return Element(is_list=return_list,use_deque=return_deque).section(*content, **attrs).element


def select(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <select> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_select():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).select(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_select()
    else:
        return Element(is_list=return_list,use_deque=return_deque).select(*content, **attrs).element


def slot(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <slot> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_slot():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).slot(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_slot()
    else:
        return Element(is_list=return_list,use_deque=return_deque).slot(*content, **attrs).element


def small(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <small> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_small():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).small(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_small()
    else:
        return Element(is_list=return_list,use_deque=return_deque).small(*content, **attrs).element


def span(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <span> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_span():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).span(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_span()
    else:
        return Element(is_list=return_list,use_deque=return_deque).span(*content, **attrs).element


def strong(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <strong> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_strong():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).strong(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_strong()
    else:
        return Element(is_list=return_list,use_deque=return_deque).strong(*content, **attrs).element


def style(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <style> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_style():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).style(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_style()
    else:
        return Element(is_list=return_list,use_deque=return_deque).style(*content, **attrs).element


def sub(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <sub> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_sub():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).sub(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_sub()
    else:
        return Element(is_list=return_list,use_deque=return_deque).sub(*content, **attrs).element


def summary(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <summary> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_summary():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).summary(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_summary()
    else:
        return Element(is_list=return_list,use_deque=return_deque).summary(*content, **attrs).element


def sup(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <sup> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_sup():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).sup(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_sup()
    else:
        return Element(is_list=return_list,use_deque=return_deque).sup(*content, **attrs).element

def table(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <table> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_table():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).table(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_table()
    else:
        return Element(is_list=return_list,use_deque=return_deque).table(*content, **attrs).element


def tbody(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <tbody> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_tbody():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).tbody(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_tbody()
    else:
        return Element(is_list=return_list,use_deque=return_deque).tbody(*content, **attrs).element


def td(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <td> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_td():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).td(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_td()
    else:
        return Element(is_list=return_list,use_deque=return_deque).td(*content, **attrs).element


def template(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <template> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_template():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).template(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_template()
    else:
        return Element(is_list=return_list,use_deque=return_deque).template(*content, **attrs).element


def textarea(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <textarea> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_textarea():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).textarea(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_textarea()
    else:
        return Element(is_list=return_list,use_deque=return_deque).textarea(*content, **attrs).element


def tfoot(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <tfoot> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_tfoot():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).tfoot(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_tfoot()
    else:
        return Element(is_list=return_list,use_deque=return_deque).tfoot(*content, **attrs).element


def th(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <th> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_th():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).th(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_th()
    else:
        return Element(is_list=return_list,use_deque=return_deque).th(*content, **attrs).element


def thead(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <thead> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_thead():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).thead(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_thead()
    else:
        return Element(is_list=return_list,use_deque=return_deque).thead(*content, **attrs).element


def time(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <time> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_time():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).time(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_time()
    else:
        return Element(is_list=return_list,use_deque=return_deque).time(*content, **attrs).element


def title(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <title> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_title():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).title(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_title()
    else:
        return Element(is_list=return_list,use_deque=return_deque).title(*content, **attrs).element


def tr(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <tr> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_tr():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).tr(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_tr()
    else:
        return Element(is_list=return_list,use_deque=return_deque).tr(*content, **attrs).element


def u(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <u> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_u():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).u(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_u()
    else:
        return Element(is_list=return_list,use_deque=return_deque).u(*content, **attrs).element


def ul(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ul> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_ul():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).ul(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_ul()
    else:
        return Element(is_list=return_list,use_deque=return_deque).ul(*content, **attrs).element


def var(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <var> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_var():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).var(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_var()
    else:
        return Element(is_list=return_list,use_deque=return_deque).var(*content, **attrs).element


def video(*content:tuple[str],return_list:bool=False,return_deque=False,stream:bool=False,batch:int=50, **attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <video> element."""
    if stream:
        if not return_list:
            return_list=True
        def __stream_video():
            EL=Element(is_list=return_list,use_deque=return_deque)
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).video(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_video()
    else:
        return Element(is_list=return_list,use_deque=return_deque).video(*content, **attrs).element
