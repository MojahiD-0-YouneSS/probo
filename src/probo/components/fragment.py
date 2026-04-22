from typing import Generator, Any, Union
import inspect
from probo.components.elements import Element
from probo.utility import ProboSourceString

def _resolve_content(content, stream=False, batch=50,EL:Element=None):
    """
    Internal helper to recursively resolve content for the fragment.
    """
    for item in content:
        if stream:
            if inspect.isgenerator(item):
                yield from item
            elif hasattr(item, "stream"):
                if "EL" in inspect.signature(item.render).parameters:
                    yield from item.stream(EL,batch=batch)
                else:
                    yield from item.stream(batch=batch)
            elif hasattr(item, "render"):
                if "EL" in inspect.signature(item.render).parameters:
                    yield ProboSourceString(item.render(EL))
                else:
                    yield ProboSourceString(item.render())
            else:
                yield ProboSourceString(item)
        else:
            # Eager resolution for standard rendering
            if hasattr(item, "render"):
                if "EL" in inspect.signature(item.render).parameters:
                    yield ProboSourceString(item.render(EL))
                else:
                    yield ProboSourceString(item.render())
            else:
                yield ProboSourceString(item)

def frag(
    *content, stream: bool = False, batch: int = 50, EL: Element = None
) -> Union[str, Generator[str, None, None]]:
    """
    The Functional Ghost Node (v1.3.4).

    Acts as a transparent bridge for grouping elements.
    Returns a joined string if stream=False, or a generator if stream=True.

    Usage:
        return frag(
            div("Updated", id="status"),
            div("New Data", id="content", hx_swap_oob="true"),
            stream=True
        )
    """
    if stream:
        return _resolve_content(content, stream=True, batch=batch,EL=EL)

    # Eagerly join content into a single joint string
    return ProboSourceString("".join(_resolve_content(content, stream=False, EL=EL)))
