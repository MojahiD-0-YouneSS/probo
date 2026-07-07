from collections import deque
from typing import Any, Generator
from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin, ElementMutatorMixin, DataPipeLineMixin, MutationPipelineMixin
from probo.utility import StreamManager

class CustomElement(DataPipeLineMixin, ElementNodeMixin, ElementMutatorMixin, MutationPipelineMixin, BaseHTMLElement, ):
    """Represents a Custom HTML element dynamically integrated into SSDOM."""
    
    __slots__ = ('tag', 'is_self_closing')

    def __init__(self, tag_name: str, *content: Any, is_self_closing: bool=False, **attrs: Any):
        #Initialize base class
        super().__init__(*content,**attrs)
        #Force uppercase as the default for the tag name
        self.tag = tag_name.upper() 
        self.is_self_closing = is_self_closing
        self.extract_pipeline_args(self.attributes)
        self._set_node_children(self.content)
        self.resolve_pipeline_variables()
        self.extract_mutation_args(self.attributes)
        self.detect_effect_nodes(self.content)
        if self.custom_attrs:
            self.enforce_custom_attrs(global_tree=(True if self.custom_attrs == 'global' else False),kwargs=self.attributes)


    def render(self) -> str:
        '''
        Blueprint:custom_element = Element(
        ).set_attrs(**self.attributes).set_content(self.content).custom_element(self.tag).element'''
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content = ""
            else:
                content=self._get_rendered_content()
        else:
            content=self._get_rendered_content()
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

        
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                content_generator = (_ for _ in range(0))
            else:
                content_generator = self._get_stream_content(batch=batch)
        else:
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
