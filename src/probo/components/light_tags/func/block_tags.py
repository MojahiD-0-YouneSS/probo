from probo.components.elements import Element
from probo.utility import ProboSourceString, _resolve_stream,StreamManager
from typing import Any,Generator
from collections import deque

def l_a(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <a> element."""
    if stream:
        def __stream_a():
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
        return EL.a(*content, **attrs).element


def l_abbr(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <abbr> element."""
    if stream:
        def __stream_abbr():
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
        return EL.abbr(*content, **attrs).element


def l_address(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <address> element."""
    if stream:
        def __stream_address():
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
        return EL.address(*content, **attrs).element


def l_article(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <article> element."""
    if stream:
        def __stream_article():
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
        return EL.article(*content, **attrs).element


def l_aside(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <aside> element."""
    if stream:
        def __stream_aside():
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
        return EL.aside(*content, **attrs).element


def l_audio(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <audio> element."""
    if stream:
        def __stream_audio():
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
        return EL.audio(*content, **attrs).element


def l_b(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <b> element."""
    if stream:
        def __stream_b():
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
        return EL.b(*content, **attrs).element


def l_bdi(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <bdi> element."""
    if stream:
        def __stream_bdi():
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
        return EL.bdi(*content, **attrs).element


def l_bdo(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <bdo> element."""
    if stream:
        def __stream_bdo():
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
        return EL.bdo(*content, **attrs).element


def l_blockquote(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <blockquote> element."""
    if stream:
        def __stream_blockquote():
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
        return EL.blockquote(*content, **attrs).element


def l_body(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <body> element."""
    if stream:
        def __stream_body():
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
        return EL.body(*content, **attrs).element


def l_button(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <button> element."""
    if stream:
        def __stream_button():
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
        return EL.button(*content, **attrs).element


def l_canvas(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <canvas> element."""
    if stream:
        def __stream_canvas():
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
        return EL.canvas(*content, **attrs).element


def l_caption(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <caption> element."""
    if stream:
        def __stream_caption():
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
        return EL.caption(*content, **attrs).element


def l_cite(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <cite> element."""
    if stream:
        def __stream_cite():
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
        return EL.cite(*content, **attrs).element


def l_code(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <code> element."""
    if stream:
        def __stream_code():
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
        return EL.code(*content, **attrs).element


def l_colgroup(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <colgroup> element."""
    if stream:
        def __stream_colgroup():
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
        return EL.colgroup(*content, **attrs).element


def l_data(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <data> element."""
    if stream:
        def __stream_data():
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
        return EL.data(*content, **attrs).element


def l_datalist(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <datalist> element."""
    if stream:
        def __stream_datalist():
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
        return EL.datalist(*content, **attrs).element


def l_dd(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dd> element."""
    if stream:
        def __stream_dd():
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
        return EL.dd(*content, **attrs).element


def l_Del(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <del> element."""
    if stream:
        def __stream_Del():
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
        return EL.Del(*content, **attrs).element


def l_details(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <details> element."""
    if stream:
        def __stream_details():
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
        return EL.details(*content, **attrs).element


def l_dfn(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dfn> element."""
    if stream:
        def __stream_dfn():
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
        return EL.dfn(*content, **attrs).element


def l_dialog(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dialog> element."""
    if stream:
        def __stream_dialog():
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
        return EL.dialog(*content, **attrs).element


def l_div(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <div> element."""
    if stream:
        def __stream_div():
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
        return EL.div(*content, **attrs).element


def l_dl(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dl> element."""
    if stream:
        def __stream_dl():
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
        return EL.dl(*content, **attrs).element


def l_dt(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <dt> element."""
    if stream:
        def __stream_dt():
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
        return EL.dt(*content, **attrs).element


def l_em(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <em> element."""
    if stream:
        def __stream_em():
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
        return EL.em(*content, **attrs).element


def l_fieldset(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <fieldset> element."""
    if stream:
        def __stream_fieldset():
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
        return EL.fieldset(*content, **attrs).element


def l_figcaption(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <figcaption> element."""
    if stream:
        def __stream_figcaption():
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
        return EL.figcaption(*content, **attrs).element


def l_figure(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <figure> element."""
    if stream:
        def __stream_figure():
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
        return EL.figure(*content, **attrs).element


def l_footer(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <footer> element."""
    if stream:
        def __stream_footer():
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
        return EL.footer(*content, **attrs).element


def l_form(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <form> element."""
    if stream:
        def __stream_form():
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
        return EL.form(*content, **attrs).element


def l_h1(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h1> element."""
    if stream:
        def __stream_h1():
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
        return EL.h1(*content, **attrs).element


def l_h2(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h2> element."""
    if stream:
        def __stream_h2():
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
        return EL.h2(*content, **attrs).element


def l_h3(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h3> element."""
    if stream:
        def __stream_h3():
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
        return EL.h3(*content, **attrs).element


def l_h4(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h4> element."""
    if stream:
        def __stream_h4():
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
        return EL.h4(*content, **attrs).element


def l_h5(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h5> element."""
    if stream:
        def __stream_h5():
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
        return EL.h5(*content, **attrs).element


def l_h6(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <h6> element."""
    if stream:
        def __stream_h6():
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
        return EL.h6(*content, **attrs).element


def l_head(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <head> element."""
    if stream:
        def __stream_head():
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
        return EL.head(*content, **attrs).element


def l_header(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <header> element."""
    if stream:
        def __stream_header():
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
        return EL.header(*content, **attrs).element


def l_hgroup(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <hgroup> element."""
    if stream:
        def __stream_hgroup():
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
        return EL.hgroup(*content, **attrs).element


def l_html(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <html> element."""
    if stream:
        def __stream_html():
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
        return EL.html(*content, **attrs).element


def l_i(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <i> element."""
    if stream:
        def __stream_i():
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
        return EL.i(*content, **attrs).element


def l_iframe(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <iframe> element."""
    if stream:
        def __stream_iframe():
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
        return EL.iframe(*content, **attrs).element


def l_ins(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ins> element."""
    if stream:
        def __stream_ins():
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
        return EL.ins(*content, **attrs).element


def l_kbd(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <kbd> element."""
    if stream:
        def __stream_kbd():
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
        return EL.kbd(*content, **attrs).element


def l_label(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <label> element."""
    if stream:
        def __stream_label():
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
        return EL.label(*content, **attrs).element


def l_legend(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <legend> element."""
    if stream:
        def __stream_legend():
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
        return EL.legend(*content, **attrs).element


def l_li(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <li> element."""
    if stream:
        def __stream_li():
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
        return EL.li(*content, **attrs).element


def l_main(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <main> element."""
    if stream:
        def __stream_main():
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
        return EL.main(*content, **attrs).element


def l_math(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <math> element."""
    if stream:
        def __stream_math():
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
        return EL.math(*content, **attrs).element


def l_map(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <map> element."""
    if stream:
        def __stream_map():
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).map(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_map()
    else:
        return EL.map(*content, **attrs).element


def l_mark(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <mark> element."""
    if stream:
        def __stream_mark():
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
        return EL.mark(*content, **attrs).element


def l_menu(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <menu> element."""
    if stream:
        def __stream_menu():
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
        return EL.menu(*content, **attrs).element


def l_meter(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <meter> element."""
    if stream:
        def __stream_meter():
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
        return EL.meter(*content, **attrs).element


def l_nav(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <nav> element."""
    if stream:
        def __stream_nav():
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
        return EL.nav(*content, **attrs).element


def l_noscript(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <noscript> element."""
    if stream:
        def __stream_noscript():
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
        return EL.noscript(*content, **attrs).element


def l_object(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <object> element."""
    if stream:
        def __stream_object():
            content_gen = _resolve_stream(content, chunk_size=batch, EL=EL)
            EL.set_generator_content(content_gen).object(**attrs)
            stream_manager = StreamManager(
                opening=EL.element[0],
                content_gen=EL.stream(batch),
                closing=EL.element[1],
                chunk_size=batch
            )
            return stream_manager
        return __stream_object()
    else:
        return EL.object(*content, **attrs).element


def l_ol(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ol> element."""
    if stream:
        def __stream_ol():
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
        return EL.ol(*content, **attrs).element


def l_optgroup(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <optgroup> element."""
    if stream:
        def __stream_optgroup():
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
        return EL.optgroup(*content, **attrs).element


def l_option(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <option> element."""
    if stream:
        def __stream_option():
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
        return EL.option(*content, **attrs).element


def l_output(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <output> element."""
    if stream:
        def __stream_output():
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
        return EL.output(*content, **attrs).element


def l_p(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <p> element."""
    if stream:
        def __stream_p():
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
        return EL.p(*content, **attrs).element


def l_portal(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <portal> element."""
    if stream:
        def __stream_portal():
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
        return EL.portal(*content, **attrs).element


def l_picture(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <picture> element."""
    if stream:
        def __stream_picture():
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
        return EL.picture(*content, **attrs).element


def l_pre(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <pre> element."""
    if stream:
        def __stream_pre():
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
        return EL.pre(*content, **attrs).element


def l_progress(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <progress> element."""
    if stream:
        def __stream_progress():
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
        return EL.progress(*content, **attrs).element


def l_q(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <q> element."""
    if stream:
        def __stream_q():
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
        return EL.q(*content, **attrs).element


def l_rp(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <rp> element."""
    if stream:
        def __stream_rp():
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
        return EL.rp(*content, **attrs).element


def l_rt(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <rt> element."""
    if stream:
        def __stream_rt():
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
        return EL.rt(*content, **attrs).element


def l_ruby(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ruby> element."""
    if stream:
        def __stream_ruby():
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
        return EL.ruby(*content, **attrs).element


def l_s(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <s> element."""
    if stream:
        def __stream_s():
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
        return EL.s(*content, **attrs).element


def l_samp(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <samp> element."""
    if stream:
        def __stream_samp():
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
        return EL.samp(*content, **attrs).element


def l_script(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <script> element."""
    if stream:
        def __stream_script():
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
        return EL.script(*content, **attrs).element


def l_search(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <search> element."""
    if stream:
        def __stream_search():
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
        return EL.search(*content, **attrs).element


def l_section(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <section> element."""
    if stream:
        def __stream_section():
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
        return EL.section(*content, **attrs).element


def l_select(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <select> element."""
    if stream:
        def __stream_select():
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
        return EL.select(*content, **attrs).element


def l_slot(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <slot> element."""
    if stream:
        def __stream_slot():
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
        return EL.slot(*content, **attrs).element


def l_small(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <small> element."""
    if stream:
        def __stream_small():
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
        return EL.small(*content, **attrs).element


def l_span(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <span> element."""
    if stream:
        def __stream_span():
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
        return EL.span(*content, **attrs).element


def l_strong(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <strong> element."""
    if stream:
        def __stream_strong():
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
        return EL.strong(*content, **attrs).element


def l_style(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <style> element."""
    if stream:
        def __stream_style():
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
        return EL.style(*content, **attrs).element


def l_sub(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <sub> element."""
    if stream:
        def __stream_sub():
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
        return EL.sub(*content, **attrs).element


def l_summary(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <summary> element."""
    if stream:
        def __stream_summary():
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
        return EL.summary(*content, **attrs).element


def l_sup(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <sup> element."""
    if stream:
        def __stream_sup():
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
        return EL.sup(*content, **attrs).element

def l_table(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <table> element."""
    if stream:
        def __stream_table():
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
        return EL.table(*content, **attrs).element


def l_tbody(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <tbody> element."""
    if stream:
        def __stream_tbody():
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
        return EL.tbody(*content, **attrs).element


def l_td(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <td> element."""
    if stream:
        def __stream_td():
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
        return EL.td(*content, **attrs).element


def l_template(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <template> element."""
    if stream:
        def __stream_template():
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
        return EL.template(*content, **attrs).element


def l_textarea(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <textarea> element."""
    if stream:
        def __stream_textarea():
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
        return EL.textarea(*content, **attrs).element


def l_tfoot(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <tfoot> element."""
    if stream:
        def __stream_tfoot():
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
        return EL.tfoot(*content, **attrs).element


def l_th(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <th> element."""
    if stream:
        def __stream_th():
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
        return EL.th(*content, **attrs).element


def l_thead(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <thead> element."""
    if stream:
        def __stream_thead():
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
        return EL.thead(*content, **attrs).element


def l_time(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <time> element."""
    if stream:
        def __stream_time():
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
        return EL.time(*content, **attrs).element


def l_title(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <title> element."""
    if stream:
        def __stream_title():
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
        return EL.title(*content, **attrs).element


def l_tr(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <tr> element."""
    if stream:
        def __stream_tr():
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
        return EL.tr(*content, **attrs).element


def l_u(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <u> element."""
    if stream:
        def __stream_u():
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
        return EL.u(*content, **attrs).element


def l_ul(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <ul> element."""
    if stream:
        def __stream_ul():
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
        return EL.ul(*content, **attrs).element


def l_var(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <var> element."""
    if stream:
        def __stream_var():
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
        return EL.var(*content, **attrs).element


def l_video(EL:Element,*content:tuple[str], stream:bool=False,batch:int=50,**attrs:dict[str,Any]) -> ProboSourceString|list[ProboSourceString]|deque[ProboSourceString]|StreamManager:
    """Represents an HTML <video> element."""
    if stream:
        def __stream_video():
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
        return EL.video(*content, **attrs).element
