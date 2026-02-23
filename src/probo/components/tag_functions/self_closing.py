from probo.components.tag_classes import self_closing

# --- Specific HTML Self-Closing Element Classes ---
# These classes use the `Element` helper class and are designed for self-closing tags.


def doctype(content=None, **attrs):
    """Represents an HTML <!DOCTYPE> line break element (self-closing)."""
    return self_closing.EL.doctype(content, **attrs).render()
    # return el.replace('/>', '>')


def area(**attrs):
    """Represents an HTML <area/> line break element (self-closing)."""
    return self_closing.EL.area(**attrs).render()


def base(**attrs):
    """Represents an HTML <base/> line break element (self-closing)."""
    return self_closing.EL.base(**attrs).render()


def br(**attrs):
    """Represents an HTML <br/> line break element (self-closing)."""
    return self_closing.EL.br(**attrs).render()


def col(**attrs):
    """Represents an HTML <col/> line break element (self-closing)."""
    return self_closing.EL.col(**attrs).render()


def embed(**attrs):
    """Represents an HTML <embed/> line break element (self-closing)."""
    return self_closing.EL.embed(**attrs).render()


def hr(**attrs):
    """Represents an HTML <hr/> line break element (self-closing)."""
    return self_closing.EL.hr(**attrs).render()


def img(**attrs):
    """Represents an HTML <img/> line break element (self-closing)."""
    return self_closing.EL.img(**attrs).render()


def Input(**attrs):
    """Represents an HTML <input/> line break element (self-closing)."""
    return self_closing.EL.input(**attrs).render()


def link(**attrs):
    """Represents an HTML <link/> line break element (self-closing)."""
    return self_closing.EL.link(**attrs).render()


def meta(**attrs):
    """Represents an HTML <meta/> line break element (self-closing)."""
    return self_closing.EL.meta(**attrs).render()


def param(**attrs):
    """Represents an HTML <param/> line break element (self-closing)."""
    return self_closing.EL.param(**attrs).render()


def source(**attrs):
    """Represents an HTML <source/> line break element (self-closing)."""
    return self_closing.EL.source(**attrs).render()


def track(**attrs):
    """Represents an HTML <track/> line break element (self-closing)."""
    return self_closing.EL.track(**attrs).render()


def wbr(**attrs):
    """Represents an HTML <wbr/> line break element (self-closing)."""
    return self_closing.EL.wbr(**attrs).render()

