from typing import Generator, Any, Union, Optional
from collections import deque
from probo.utility import StreamManager,ProboSourceString
import inspect

class LightNode:
    """
    Light SSDOM Node v1.3.4.

    Architecture:
    - No parent pointers.
    - No recursive search (find/find_all).
    - No specialized subclasses (usually).
    - __slots__ for O(1) memory per node.
    - Drives a shared 'Element' engine (The Typewriter).
    """

    __slots__ = (
        "tag_name",
        "content",
        "attributes",
        "node_children",
        "_ElementNodeMixin__void_node",
        "parent",
        "light_tag"
    )

    def __init__(self, *content: Any, tag: str|None = None, **attributes: Any):
        self.content = (
            deque(
                content,
            )
            if isinstance(content, tuple)
            else deque((content,))
        )
        self.attributes = attributes
        # Logic to use class name as tag if not provided
        self.tag_name = (
            tag
            if tag
            else (
                self.__class__.__name__.lower()[1:]
                if self.__class__.__name__ == self.__class__.__name__.capitalize()
                and self.__class__.__name__[0] == "L"
                else self.__class__.__name__.lower()
            )
        )
        if not hasattr(self, "light_tag"):
            self.light_tag = f"L-{self.tag_name}"

    def render(self, EL) -> str:
        """
        Synchronous string rendering using the shared EL typewriter.
        """
        content = self._get_rendered_content(EL)
        method = getattr(EL, self.tag_name, None)
        if method:
            method(content,**self.attributes)

        res = EL.element
        return res

    def _get_rendered_content(self, EL) -> str|list[str]|deque[str]:
        """Recursively renders children to strings."""
        collector = []
        for item in self.content:

            if isinstance(item, LightNode):
                if EL.is_list or EL.is_list and EL.use_deque:
                    collector.extend(item.render(EL))
                else:
                    collector.append(item.render(EL))
            elif inspect.isgenerator(item):
                if EL.is_list and EL.use_deque:
                    collector.extend( deque(ProboSourceString(x)if not hasattr(x,"render") else x.render() for x in item))
                elif EL.is_list and not EL.use_deque:
                    collector.extend( list(ProboSourceString(x)if not hasattr(x,"render") else x.render() for x in item))
                else:
                    collector.extend( ProboSourceString("".join(ProboSourceString(x)if not hasattr(x,"render") else x.render() for x in item)))
            elif hasattr(item, "render"):
                collector.append(ProboSourceString(item.render()))
            else:
                collector.append(ProboSourceString(str(item)))
        if EL.is_list or EL.is_list and EL.use_deque:
            return collector  # Return list of strings for the caller to join
        return ProboSourceString("".join(collector))

    def stream(self, EL, batch_size: int = 50) -> Generator[str, None, None]:
        """
        Drives the shared EL engine for streaming without building metadata.
        """
        # 1. Setup the content generator
        content_gen = self._get_stream_content(EL, batch_size)

        # 2. Configure the shared EL
        method = getattr(EL, self.tag_name, None)
        EL.set_attrs(**self.attributes)

        if not method:
            elment_info = [f"<{self.tag_name}>", "", f"</{self.tag_name}>"]
        else:
            method()
            elment_info = EL.element
            if len(elment_info) == 1:
                elment_info.append(None)
        EL.set_generator_content(content_gen)
        stream_manager = StreamManager(
            elment_info[0],
            EL.stream(batch=batch_size),
            elment_info[-1],
            chunk_size=batch_size,
        )
        yield from stream_manager

    def _get_stream_content(self, EL, batch_size):
        """Pulls streams from children into the pipeline."""

        def _process_item(item):
            # BUGFIX: Catch generators and consume them lazily!
            if inspect.isgenerator(item):
                for sub_item in item:
                    yield from _process_item(sub_item)
            elif hasattr(item, "stream"):
                if hasattr(item, "light_tag"):
                    yield from item.stream(EL, batch_size=batch_size)
                else:
                    yield from item.stream(batch=batch_size)
            elif hasattr(item, "render"):
                res = item.render()
                if isinstance(res, (list, deque)):
                    yield from res
                else:
                    yield res
            else:
                yield str(item)

        for item in self.content:
            yield from _process_item(item)
