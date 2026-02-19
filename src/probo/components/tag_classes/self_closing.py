from probo.components.elements import Element
from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin
from probo.components.tag_classes.block_tags import EL
# --- Specific HTML Self-Closing Element Classes ---
# These classes use the `Element` helper class and are designed for self-closing tags.


class DOCTYPE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an DOCTYPE HTML <!> line break element (self-closing)."""

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)  # Self-closing tags don't have content

    def render(self):
        return EL.set_attrs(**self.attributes).doctype().element


class AREA(BaseHTMLElement,ElementNodeMixin,):
    """Represents an AREA HTML <area> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).area().element


class BASE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BASE HTML <base> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).base().element


class BR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an BR HTML <br> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).br().element


class COL(BaseHTMLElement,ElementNodeMixin,):
    """Represents an COL HTML <col> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).col().element


class EMBED(BaseHTMLElement,ElementNodeMixin,):
    """Represents an EMBED HTML <embed> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).embed().element


class HR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an HR HTML <hr> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).hr().element


class IMG(BaseHTMLElement,ElementNodeMixin,):
    """Represents an IMG HTML <img> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).img().element


class INPUT(BaseHTMLElement,ElementNodeMixin,):
    """Represents an INPUT HTML <input> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).input().element


class LINK(BaseHTMLElement,ElementNodeMixin,):
    """Represents an LINK HTML <link> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).link().element


class META(BaseHTMLElement,ElementNodeMixin,):
    """Represents an META HTML <meta> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).meta().element


class PARAM(BaseHTMLElement,ElementNodeMixin,):
    """Represents an PARAM HTML <param> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).param().element


class SOURCE(BaseHTMLElement,ElementNodeMixin,):
    """Represents an SOURCE HTML <source> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).source().element


class TRACK(BaseHTMLElement,ElementNodeMixin,):
    """Represents an TRACK HTML <track> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).track().element


class WBR(BaseHTMLElement,ElementNodeMixin,):
    """Represents an WBR HTML <wbr> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)


    def render(self):
        return EL.set_attrs(**self.attributes).wbr().element
