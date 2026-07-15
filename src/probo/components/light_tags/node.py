from typing import Generator, Any, Union, Optional, Self
from collections import deque
from probo.utility import StreamManager,ProboSourceString,markup_escape, PipelineDeque,PipelineDict
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
        "_void_node",
        "parent",
        "light_tag"
    )

    def __init__(self, *content: Any, tag: str|None = None, **attributes: Any):
        super().__init__()

        self.content = PipelineDeque(self,iterable=
            content
            if isinstance(content, (tuple, list,deque))
            else (content,)
        )
        self.attributes = PipelineDict(self,attrs=attributes)
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
    def inner_html(self, *content: Any, overwrite: bool = False) -> Self:
        if overwrite:
            self.content = PipelineDeque(self, iterable=
                content
                if isinstance(content, (tuple, list,deque))
                else (content,)
            )
        else:
            self.content.extend(content)
        if hasattr(self,'reset_node_children'):
            self.reset_node_children()
            self._set_node_children(self.content)
            if hasattr(self,'resolve_pipeline_variables'):
                self.resolve_pipeline_variables()
        return self

    def render(self, EL) -> str:
        """
        Synchronous string rendering using the shared EL typewriter.
        """
        if hasattr(self, 'before_render_exe'):
            self.before_render_exe()
        # if hasattr(self, "resolve_pipeline_variables"):
        #     if not self.resolve_pipeline_variables(swap_vars=True):
        #         return [] if getattr(EL, 'is_list', False) else ""
        if getattr(self,'has_unresolved_pipeline_vars',False):
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = [] if EL.is_list else deque() if EL.is_deque else ""
            else:
                content = self._get_rendered_content(EL)
        else:
            content = self._get_rendered_content(EL)
        method = getattr(EL, self.tag_name, None)
        if method:
            method(content,**self.attributes)

        res = EL.element
        return res

    def _get_rendered_content(self, EL) -> str|list[str]|deque[str]:
        """Recursively renders children to strings."""
        collector = []
        last_was_text = False

        def flatten(items):
            for it in items:
                if inspect.isgenerator(it) or isinstance(it, (list, tuple, deque,PipelineDeque)):
                    yield from flatten(it)
                else:
                    yield it
        
        for item in flatten(self.content):
            rendered = None

            if isinstance(item, LightNode):
                rendered = item.render(EL)
            elif hasattr(item, "render"):
                rendered_item = item.render()
                rendered = rendered_item if isinstance(rendered_item, ProboSourceString) else markup_escape(rendered_item)
            else:
                rendered = item if isinstance(item, ProboSourceString) else markup_escape(item)

            # Determine if we should add a space
            current_is_text = False
            if isinstance(rendered, ProboSourceString):
                if getattr(rendered, 'is_html', False):
                    current_is_text = False
                else:
                    current_is_text = True
            elif isinstance(rendered, (list, deque, tuple)):
                current_is_text = False
            elif isinstance(rendered, (str, int, float, bool)):
                current_is_text = True
            else:
                current_is_text = False

            if current_is_text:
                if last_was_text:
                    collector.append(" ")
                last_was_text = True
            else:
                last_was_text = False

            # Merge the rendered result into our main collector
            if isinstance(rendered, (list, deque)):
                if not EL.is_list:
                    collector.append(" ".join(str(x) for x in rendered))
                else:
                    collector.extend(rendered)
            else:
                if not EL.is_list:
                    collector.append(str(rendered))
                else:
                    collector.append(rendered)
                    
        if EL.is_list:
            return collector  # Return list of strings for the caller to join
        return ProboSourceString("".join(str(x) for x in collector))

    def stream(self, EL, batch_size: int = 50) -> Generator[str, None, None]:
        """
        Drives the shared EL engine for streaming without building metadata.
        """
        if hasattr(self, 'before_render_exe'):
            self.before_render_exe()
        # if hasattr(self, "resolve_pipeline_variables"):
        #     if not self.resolve_pipeline_variables(swap_vars=True):
        #         return

        # 1. Setup the content generator
        if getattr(self,'has_unresolved_pipeline_vars',False):
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_gen = []
            else:
                content_gen = self._get_stream_content(EL, batch_size)
        else:
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
        last_was_text = [False]

        def _process_item(item):
            # Catch generators and iterables and consume them lazily!
            if inspect.isgenerator(item) or isinstance(item, (list, tuple, deque, PipelineDeque)):
                for sub_item in item:
                    yield from _process_item(sub_item)
            elif hasattr(item, "stream"):
                last_was_text[0] = False
                if hasattr(item, "light_tag"):
                    yield from item.stream(EL, batch_size=batch_size)
                else:
                    yield from item.stream(batch=batch_size)
                last_was_text[0] = False
            elif hasattr(item, "render"):
                last_was_text[0] = False
                res = item.render()
                if isinstance(res, (list, deque)):
                    yield from res
                else:
                    yield res
                last_was_text[0] = False
            else:
                # Leaf node: raw string, int, etc.
                res_str = item if isinstance(item, ProboSourceString) else markup_escape(item)
                
                current_is_text = False
                if isinstance(res_str, ProboSourceString):
                    current_is_text = not getattr(res_str, 'is_html', False)
                elif isinstance(item, (str, int, float, bool)):
                    current_is_text = True
                
                if current_is_text:
                    if last_was_text[0]:
                        yield " "
                    last_was_text[0] = True
                else:
                    last_was_text[0] = False
                    
                yield str(res_str)

        for item in self.content:
            yield from _process_item(item)
