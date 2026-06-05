from collections import deque
from typing import Any, Generator
from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin, ElementMutatorMixin
from probo.utility import StreamManager

class CustomElement(BaseHTMLElement, ElementNodeMixin, ElementMutatorMixin):
    """Represents a Custom HTML element dynamically integrated into SSDOM."""
    
    __slots__ = ('tag', 'is_self_closing')

    def __init__(self, tag_name: str, *content: Any, is_self_closing: bool=False, **attrs: Any):
        #Initialize base class
        super().__init__(*content,**attrs)
        #Force uppercase as the default for the tag name
        self.tag = tag_name.upper() 
        self.is_self_closing = is_self_closing

        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)

    def render(self) -> str:
        '''
        Blueprint:custom_element = Element(
        ).set_attrs(**self.attributes).set_content(self.content).custom_element(self.tag).element'''
        content = self._get_rendered_content()
        return (
            self.EL
            .set_attrs(**self.attributes)
            .set_content(content)
            .custom_element(self.tag)
            .element
        )
    
    def stream(self, batch: int=50) -> Generator[str,None,None]:
        '''
        Blueprint:custom_element = Element(
        ).set_attrs(**self.attributes).set_content(self.content).custom_element(self.tag).element'''
        self.delegate_render_conditions(
            use_list=True,
        )

        content_generator = self._get_stream_content(batch=batch)

        element_info = (
            self.EL
            .set_attrs(**self.attributes)
            .set_generator_content(content_generator)
            .custom_element(self.tag)
            .element
        )

        stream_manager = StreamManager(
            element_info[0],
            self.EL.stream(batch=batch),
            element_info[-1],
            chunk_size=batch,
        )
        yield from stream_manager
