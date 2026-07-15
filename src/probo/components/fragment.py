from typing import Generator, Any, Union, Callable
import inspect
from probo.components.elements import Element
from probo.utility import ProboSourceString
from collections import deque
from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin, ElementMutatorMixin, DataPipeLineMixin, MutationPipelineMixin

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
    *content, stream: bool = False, batch: int = 50, EL: Element = None, fragments: list[Callable] = None
) -> Union[ProboSourceString, Generator[str, None, None]]:
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
    if fragments:
        extracted = []
        for item in content:
            # Check if it's an SSDOM tree (it has a 'find' method)
            if hasattr(item, "find"):
                for func in fragments:
                    found = item.find(func)
                    if found:
                        extracted.append(found)
        content = tuple(extracted)

    if stream:
        return _resolve_content(content, stream=True, batch=batch, EL=EL)

    # Eagerly join content into a single joint string
    return ProboSourceString("".join(_resolve_content(content, stream=False, EL=EL)))

class Frag(DataPipeLineMixin, ElementNodeMixin, ElementMutatorMixin, MutationPipelineMixin, BaseHTMLElement):
    """
    A Fragment class that acts like a ghost node but has the data pipeline.
    Useful when you need to return children and also provide a data source.
    """
    __slots__ = ()

    def __init__(self, *content: Any, fragments: list[Callable] = None, **attrs: Any):
        super().__init__(*content, **attrs)
        
        if fragments:
            extracted = []
            for item in self.content:
                if hasattr(item, "find"):
                    for func in fragments:
                        found = item.find(func)
                        if found:
                            extracted.append(found)
            from collections import deque
            self.content = deque(extracted)
            
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False), kwargs=self.attributes)

    def render(self) -> Union[ProboSourceString, list, deque, str]:
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content = self._get_rendered_content()
        else:
            content = self._get_rendered_content()
        if isinstance(content, (str,int,float)):
            return ProboSourceString(str(content))
        return content

    def stream(self, batch: int = 50) -> Generator[str, None, None]:
        # self.delegate_render_conditions(use_list=self.use_list, use_deque=self.use_deque)

        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
            content_generator = self._get_stream_content(batch=batch)

        yield from content_generator
