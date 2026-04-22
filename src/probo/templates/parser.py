from html.parser import HTMLParser
from typing import List, Dict, Any, Union, Callable,Generator
from probo.components.node import (
    ElementMutatorMixin,ElementNodeMixin
)
from probo.components.light_tags.node import LightNode
from probo.components.base import BaseHTMLElement
from probo.utility import StreamManager
import re

class HeavyNodeProxy(BaseHTMLElement,ElementNodeMixin,ElementMutatorMixin):
    __slots__ = ("parsed_tag","_el_instance", "use_list", "use_deque", "element_data")

    def __init__(
        self,tag, *content: tuple[str | ElementNodeMixin], **attrs: dict[str, Any]
    ):
        self.parsed_tag=tag
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        ElementMutatorMixin.__init__(self)

    def render(self) -> str:
        """
        Blueprint:a = Element(
        ).set_attrs(**self.attributes).set_content(self.content).a().element"""

        content = self._get_rendered_content()
        self.EL.set_attrs(**self.attributes).set_content(content)
        method = getattr(self.EL, self.parsed_tag, None)
        if callable(method):
            return method().element
        return str()

    def stream(self, chunk_size: int = 50) -> Generator[str, None, None]:
        """
        Yields HTML in chunks.
        Note: The builder's .a() method must support returning a generator.
        """
        self.delegate_render_conditions(
            use_list=True,
        )

        content_generator = self._get_stream_content(batch=chunk_size)

        (self.EL.set_attrs(**self.attributes)
        .set_generator_content(content_generator))
        method = getattr(self.EL, self.parsed_tag, None)

        if not callable(method):
            yield from content_generator

        elment_info = (
            method()
            .element
        )
        if len(elment_info) == 1:
            self.EL.reset_generator_content()
        stream_manager = StreamManager(
            elment_info[0],
            self.EL.stream(batch=chunk_size),
            elment_info[-1] if len(elment_info) != 1 else None,
            chunk_size=chunk_size,
        )
        yield from stream_manager

    def __repr__(self):
        children = f", children={len(self.content)}" if self.content else ""
        return f"HeavyNodeProxy(<{self.tag}>{children})"

class LightNodeProxy(LightNode,ElementNodeMixin):

    __slots__ = ("parsed_tag","_el_instance", "use_list", "use_deque", "element_data")

    def __init__(
        self,
        tag: str | None = None,
        *content: tuple[str | ElementNodeMixin],
        **attrs: dict[str, Any],
    ):
        self.parsed_tag=tag
        super().__init__(*content,tag=tag, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)

    def render(self,EL)->str:
        return super().render(EL)

    def stream(self, EL,chunk_size: int = 50) -> Generator[str, None, None]: 
        yield from super().stream(EL,chunk_size)       

    def __repr__(self):
        children = f", children={len(self.content)}" if self.content else ""
        return f"LightNodeProxy(<{self.tag}>{children})"


class ProboTemplateParser(HTMLParser):
    """
    Blazing-fast AST Builder.
    Converts raw HTML into nested native Python dictionaries,
    or directly bridges them into SSDOM objects (Heavy/Light).
    """

    __slots__ = ("root", "stack",'template_path')

    def __init__(self, file_path:str|None=None):
        super().__init__(convert_charrefs=False)
        self.root = []
        self.stack = []
        self.file_path =file_path

    def _preserve_attr_case(self, lower_attrs: list) -> dict:
        """Recovers the original case of attributes from the raw HTML string."""
        if not lower_attrs:
            return {}

        raw_tag = self.get_starttag_text()
        cased_attrs = {}

        for key, val in lower_attrs:
            # Search the raw HTML string for the attribute key, ignoring case
            match = re.search(rf'\b({key})\b(?=\s*=|\s*/>|\s*>)', raw_tag, re.IGNORECASE)
            real_key = match.group(1) if match else key
            cased_attrs[real_key] = val

        return cased_attrs

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]):
        cased_attrs = self._preserve_attr_case(attrs)
        node = {"tag": tag, "attrs": cased_attrs, "content": []}
        if self.stack:
            self.stack[-1]["content"].append(node)
        else:
            self.root.append(node)
        self.stack.append(node)

    def handle_endtag(self, tag: str):
        if self.stack:
            node = self.stack.pop()
            if not node["content"]:
                node["content"] = None
            elif len(node["content"]) == 1 and isinstance(node["content"][0], str):
                node["content"] = node["content"][0]

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str]]):
        cased_attrs = self._preserve_attr_case(attrs)
        node = {"tag": tag, "attrs": cased_attrs, "content": None}
        if self.stack:
            self.stack[-1]["content"].append(node)
        else:
            self.root.append(node)

    def handle_data(self, data: str):
        text = data.strip()
        if text:
            if self.stack:
                self.stack[-1]["content"].append(text)
            else:
                self.root.append(text)

    def _convert_to_ssdom(self, nodes: Union[List, Dict, str], mode: str) -> Any:
        """Recursively translates the JSON AST into Probo SSDOM instances."""
        if not isinstance(nodes, list):
            nodes = [nodes]

        result = []
        for node in nodes:
            if isinstance(node, str):
                result.append(node)
                continue

            content = node.get("content",None)
            if content is None:
                parsed_content = []
            elif isinstance(content, str):
                parsed_content = [content]
            else:
                parsed_content = self._convert_to_ssdom(content, mode)

            if not isinstance(parsed_content, list):
                parsed_content = [parsed_content]

            if mode == "heavy":
                result.append(
                    HeavyNodeProxy(
                       node["tag"], *parsed_content,  **node["attrs"]
                    )
                )
            elif mode == "light":
                result.append(
                    LightNodeProxy(
                         node["tag"], *parsed_content,**node["attrs"]
                    )
                )

        return result[0] if len(result) == 1 else result

    def parse(
        self, html_string: str|None=None, mode: str = "json"
    ) -> Union[List[Dict[str, Any]], Any, Callable]:
        """
        Feeds the string and returns the requested format.

        Modes:
          - 'json': Returns native Python dictionaries (AST).
          - 'heavy': Returns a HeavyNode tree.
          - 'light': Returns a LightNode tree.
          - 'callable': Returns a lambda that executes the conversion when called.
        """
        # Reset state before parsing
        self.root = []
        self.stack = []
        if not html_string and not self.file_path:
            return str()
        if not html_string and self.file_path:
            self.feed(open(self.file_path,"r").read())
        else:
            self.feed(html_string)

        if mode == "json":
            return self.root
        elif mode == "callable":
            # Stores the parsed AST securely in the closure and returns a factory function
            captured_ast = list(self.root)
            return lambda target_mode="heavy": self._convert_to_ssdom(
                captured_ast, target_mode
            )
        else:
            return self._convert_to_ssdom(self.root, mode)
