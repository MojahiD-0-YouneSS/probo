from probo.components.tag_classes import self_closing

# --- Specific HTML Self-Closing Element Classes ---
# These classes use the `Element` helper class and are designed for self-closing tags.


def doctype(content=None, **attrs):
    """Represents an HTML <!DOCTYPE> line break element (self-closing)."""
    return self_closing.DOCTYPE(content, **attrs).render()
    # return el.replace('/>', '>')


def area(**attrs):
    """Represents an HTML <area/> line break element (self-closing)."""
    return self_closing.AREA(**attrs).render()


def base(**attrs):
    """Represents an HTML <base/> line break element (self-closing)."""
    return self_closing.BASE(**attrs).render()


def br(**attrs):
    """Represents an HTML <br/> line break element (self-closing)."""
    return self_closing.BR(**attrs).render()


def col(**attrs):
    """Represents an HTML <col/> line break element (self-closing)."""
    return self_closing.COL(**attrs).render()


def embed(**attrs):
    """Represents an HTML <embed/> line break element (self-closing)."""
    return self_closing.EMBED(**attrs).render()


def hr(**attrs):
    """Represents an HTML <hr/> line break element (self-closing)."""
    return self_closing.HR(**attrs).render()


def img(**attrs):
    """Represents an HTML <img/> line break element (self-closing)."""
    return self_closing.IMG(**attrs).render()


def Input(**attrs):
    """Represents an HTML <input/> line break element (self-closing)."""
    return self_closing.INPUT(**attrs).render()


def link(**attrs):
    """Represents an HTML <link/> line break element (self-closing)."""
    return self_closing.LINK(**attrs).render()


def meta(**attrs):
    """Represents an HTML <meta/> line break element (self-closing)."""
    return self_closing.META(**attrs).render()


def param(**attrs):
    """Represents an HTML <param/> line break element (self-closing)."""
    return self_closing.PARAM(**attrs).render()


def source(**attrs):
    """Represents an HTML <source/> line break element (self-closing)."""
    return self_closing.SOURCE(**attrs).render()


def track(**attrs):
    """Represents an HTML <track/> line break element (self-closing)."""
    return self_closing.TRACK(**attrs).render()


def wbr(**attrs):
    """Represents an HTML <wbr/> line break element (self-closing)."""
    return self_closing.WBR(**attrs).render()

