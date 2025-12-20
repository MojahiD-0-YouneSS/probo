from typing import Dict, Any, Union, List, Optional

class XMLElement:
    """
    Represents a generic XML element.
    Unlike HTML, XML tags are case-sensitive and must strictly handle attributes.
    """
    def __init__(self, tag: str, content: Union[str, 'XMLElement', List['XMLElement']] = "", **attrs):
        self.tag = tag
        self.content = content
        self.attrs = attrs
        self.children = []
        
        # Handle initial content if it's a list
        if isinstance(content, list):
            self.children.extend(content)
        elif content:
             # If it's a single item (str or Element), add to children list for uniform handling
             self.children.append(content)

    def add(self, child: Union['XMLElement', str]):
        """Fluent API to add children."""
        self.children.append(child)
        return self

    def set_attr(self, key: str, value: Any):
        self.attrs[key] = value
        return self

    def _render_attrs(self) -> str:
        """
        Renders attributes. 
        XML Rule: No boolean attributes (e.g. 'disabled'). Must be key="value".
        """
        parts = []
        for k, v in self.attrs.items():
            # XML allows any key characters, but usually we keep them as is.
            # We convert values to string strictly.
            if v is None:
                continue
            if isinstance(v,bool):
                parts.append(f'{k}="{k}"')
            else: parts.append(f'{k}="{v}"')
        return " ".join(parts)

    def render(self) -> str:
        attr_str = self._render_attrs()
        if attr_str:
            attr_str = " " + attr_str

        # Render children
        inner_html = ""
        for child in self.children:
            if hasattr(child, 'render'):
                inner_html += child.render()
            else:
                inner_html += str(child)

        # XML Rule: Self-closing tag is mandatory if empty
        if not inner_html:
            return f"<{self.tag}{attr_str} />"
        
        return f"<{self.tag}{attr_str}>{inner_html}</{self.tag}>"


class XMLSection:
    """
    Represents a CDATA section.
    Used to escape blocks of text that would otherwise be interpreted as markup.
    Output: <![CDATA[ ...content... ]]>
    """
    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return f"<![CDATA[{self.content}]]>"


class XMLComment:
    """
    Represents an XML comment.
    Output: <!-- ...content... -->
    """
    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return f"<!-- {self.content} -->"


class XMLInstruction:
    """
    Represents a Processing Instruction (PI).
    Output: <?target content?>
    Example: <?xml-stylesheet type="text/xsl" href="style.xsl"?>
    """
    def __init__(self, target: str, data: str = ""):
        self.target = target
        self.data = data

    def render(self) -> str:
        data_str = f" {self.data}" if self.data else ""
        return f"<?{self.target}{data_str}?>"


class XMLDocument:
    """
    Represents a full XML document.
    Manages the Declaration (<?xml ... ?>) and the Root Element.
    """
    def __init__(self, root: Optional[XMLElement] = None, version="1.0", encoding="UTF-8", standalone=None):
        self.root = root
        self.version = version
        self.encoding = encoding
        self.standalone = standalone
        self.instructions = [] # List for things like xml-stylesheet

    def set_root(self, root: XMLElement):
        self.root = root
        return self

    def add_instruction(self, target: str, data: str):
        """Add processing instructions before the root."""
        self.instructions.append(XMLInstruction(target, data))
        return self

    def render(self) -> str:
        # 1. Declaration
        decl = f'<?xml version="{self.version}" encoding="{self.encoding}"'
        if self.standalone:
            decl += f' standalone="{self.standalone}"'
        decl += "?>"

        # 2. Instructions
        instr_str = ""
        if self.instructions:
            instr_str = "\n" + "\n".join(i.render() for i in self.instructions)

        # 3. Root
        root_str = ""
        if self.root:
             root_str = "\n" + (self.root.render() if hasattr(self.root,'render') else str(self.root))
        
        return f"{decl}{instr_str}{root_str}"