from src.probo.components.elements import Element
from src.probo.components.base import BaseHTMLElement

# --- Specific HTML Self-Closing Element Classes ---
# These classes use the `Element` helper class and are designed for self-closing tags.


class DOCTYPE(BaseHTMLElement):
    """Represents an DOCTYPE HTML <!> line break element (self-closing)."""

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).doctype().element


class AREA(BaseHTMLElement):
    """Represents an AREA HTML <area> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).area().element


class BASE(BaseHTMLElement):
    """Represents an BASE HTML <base> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).base().element


class BR(BaseHTMLElement):
    """Represents an BR HTML <br> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).br().element


class COL(BaseHTMLElement):
    """Represents an COL HTML <col> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).col().element


class EMBED(BaseHTMLElement):
    """Represents an EMBED HTML <embed> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).embed().element


class HR(BaseHTMLElement):
    """Represents an HR HTML <hr> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).hr().element


class IMG(BaseHTMLElement):
    """Represents an IMG HTML <img> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).img().element


class INPUT(BaseHTMLElement):
    """Represents an INPUT HTML <input> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).input().element


class LINK(BaseHTMLElement):
    """Represents an LINK HTML <link> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).link().element


class META(BaseHTMLElement):
    """Represents an META HTML <meta> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).meta().element


class PARAM(BaseHTMLElement):
    """Represents an PARAM HTML <param> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).param().element


class SOURCE(BaseHTMLElement):
    """Represents an SOURCE HTML <source> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).source().element


class TRACK(BaseHTMLElement):
    """Represents an TRACK HTML <track> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).track().element


class WBR(BaseHTMLElement):
    """Represents an WBR HTML <wbr> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).wbr().element


class PATH(BaseHTMLElement):
    """Represents an PATH HTML <path> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).path().element


class CIRCLE(BaseHTMLElement):
    """Represents an CIRCLE HTML <circle> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).circle().element


class RECT(BaseHTMLElement):
    """Represents an RECT HTML <rect> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).rect().element


class LINE(BaseHTMLElement):
    """Represents an LINE HTML <line> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).line().element


class POLYLINE(BaseHTMLElement):
    """Represents an POLYLINE HTML <polyline> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).polyline().element


class POLYGON(BaseHTMLElement):
    """Represents an POLYGON HTML <polygon> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).polygon().element


class USE(BaseHTMLElement):
    """Represents an USE HTML <use> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).use().element


class STOP(BaseHTMLElement):
    """Represents an STOP HTML <stop> line break element (self-closing)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Self-closing tags don't have content

    def render(self):
        return Element().set_attrs(**self.attributes).stop().element
