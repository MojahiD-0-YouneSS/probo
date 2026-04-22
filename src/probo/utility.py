from typing import Any, Dict, Set, Generator
import html
from collections import deque
import inspect

# --- HIGH-SPEED CACHE ---
_html_escape = html.escape
MARKER = "\u200b"


class ProboSourceString(str):
    __slots__ = ()

    def __html__(self):
        return self

    def __add__(self, other):
        # Triggers for: ProboSourceString + string (This also handles +=)
        return ProboSourceString(super().__add__(other))

    def __radd__(self, other):
        # Triggers for: string + ProboSourceString
        # (Important if a standard string is on the left side of the + sign)
        return ProboSourceString(other + str(self))


def markup_escape(value: Any) -> str:
    """
    The 'Zero-Tax' Escaper.
    If the value is already marked as Safe, it is returned untouched.
    Otherwise, it is escaped to prevent XSS or broken layouts.
    """
    if hasattr(value, 'render'):
        value = value.render()
    # str() call handles numbers/bools; html.escape handles the security.
    return _html_escape(str(value))

def exists_in_dict(data: dict, x:Any) -> bool:
    """Checks if processed selectors exist within a dictionary's keys or values.

    This utility resolves complex selectors (like CSS-style classes or IDs), 
    strips common delimiters (., #, :, ::), and performs a search across 
    the top-level keys and the immediate nested values of the dictionary.

    Args:
        data: The dictionary to search through.
        x: A string or list of strings representing the selectors to look for.

    Returns:
        True: if any of the processed selectors are found as a key in the dictionary or within the keys/values of a nested dictionary.
        False: if otherwise.

    Examples:
        >>> my_data = {"container": {"class": "main-btn", "id": "submit"}}
        >>> # Search for a class selector
        >>> exists_in_dict(my_data, ".main-btn")
        True
        >>> # Search for a non-existent ID
        >>> exists_in_dict(my_data, "#missing")
        False
        >>> # Search for a top-level key
        >>> exists_in_dict(my_data, "container")
        True
    """
    from probo.styles.utils import resolve_complex_selector
    x = [
        s.strip(".").strip("#").strip(":").strip("::")
        for s in resolve_complex_selector(x)
    ]
    for key, value in data.items():
        # Check key
        if key in x:
            return True

        # Check nested dict
        if isinstance(value, dict):
            # Check nested key or nested value
            if any(s in value for s in x) or any(s in value.values() for s in x):
                return True

    return False

HTML_DEFAULTS = {
    "input": {"type": "text"},
    "form": {"method": "get"},
}

def render_attributes(tag_name:str, attrs:dict[str,Any]) -> str:
    """Converts a dictionary of attributes into a valid HTML attribute string.

    This function processes attributes by converting Python underscores to hyphens,
    handling boolean flags, merging lists into space-separated strings (useful 
    for CSS classes), and skipping attributes that match the global HTML defaults 
    to keep the output clean.

    Args:
        tag_name: The name of the HTML tag (e.g., 'input', 'div'). Used to 
            look up default attribute values in `HTML_DEFAULTS`.
        attrs: A dictionary where keys are attribute names and values are 
            their corresponding values.

    Returns:
        string: A space-separated string of HTML attributes. If an attribute value is True, only the key is rendered. If False or None, it is omitted.

    Examples:
        >>> # Standard usage with list and boolean
        >>> render_attributes("div", {"class": ["btn", "primary"], "hidden": True})
        'class="btn primary" hidden'

        >>> # Underscore to hyphen conversion
        >>> render_attributes("input", {"data_id": "123", "aria_label": "Submit"})
        'data-id="123" aria-label="Submit"'

        >>> # Skipping defaults (assuming {'type': 'text'} is default for input)
        >>> render_attributes("input", {"type": "text", "placeholder": "Name"})
        'placeholder="Name"'
    """

    # Get defaults for this specific tag
    defaults = HTML_DEFAULTS.get(tag_name, {})

    parts = [
        (
            k
            if v is True
            else f'{k}="{" ".join(map(str, v))}"' if type(v) is list else f'{k}="{v}"'
        )
        for key, v in attrs.items()
        if v is not False and v is not None
        if not (key in defaults and str(v).lower() == defaults[key])
        for k in [key.replace("_", "-") if "_" in key else key]
    ]
        
    return " ".join(parts)

class EnumLookUPMixin:
    """
    Mixin that automatically generates high-speed O(1) caches for Enums.
    Inherit from this to bypass the slow Python Enum machinery.
    """
    keys_set: Set[str] = set()
    values_map: Dict[str, Any] = {}
    void_set: Set[str] = set()

    @classmethod
    def thaw(cls):
        """
        'Thaws' the Enum members into raw sets and dicts for high-speed access.
        Call this once after defining your Enum.
        """
        cls.keys_set = set(cls._member_names_)
        cls.values_map = {m.name.lower(): m for m in cls}
        # Check if the Enum value has a metadata dict with 'void'
        cls.void_set = {
            m.value[0] for m in cls 
            if isinstance(m.value[1], dict) and m.value[1].get("void")
        }
    def __iter__(self):
        return self.keys_set


class StreamManager:
    """
    A lightweight wrapper that carries a generator and its wrapping tags.
    This prevents the Element class from collapsing generators into strings.
    """

    def __init__(
        self, opening: str|None, content_gen: Generator, closing: str|None=None, chunk_size: int = 50
    ):
        self.opening = opening
        self.content_gen = content_gen
        self.closing = closing
        self.chunk_size = chunk_size

    def __iter__(self) -> Generator[str, None, None]:
        """
        The actual linking logic: Yield opening tag first, then stream
        the internal content in chunks, then yield the closing tag.
        """
        # Yield opening tag before starting the content loop
        if self.opening:
            yield self.opening

        buffer = []
        for fragment in self.content_gen:
            # Handle fragments (strings or nested list/deques)
            if isinstance(fragment, (list, deque)):
                buffer.append("".join(map(str, fragment)))
            else:
                buffer.append(str(fragment))

            if len(buffer) >= self.chunk_size:
                yield "".join(buffer)
                buffer.clear()

        if buffer:
            yield "".join(buffer)

        # Yield closing tag after the content loop is exhausted
        if self.closing:
            yield self.closing
    
    def tolist(self,) -> list:
        return  list(self)
    def tostring(self,) -> str:
        return  "".join(list(self))

def _resolve_stream(content_tuple, chunk_size=50,EL=None):
    """
    Helper to flatten nested generators and classes.
    Ensures that if a user passes a generator, it is consumed lazily.
    """
    for item in content_tuple:
        if inspect.isgenerator(item):
            yield from item
        elif hasattr(item, "stream"):
            if hasattr(item, "light_tag") and item.light_tag and EL is not None:
                yield from item.stream(batch=chunk_size, EL=EL)  # Bridge to classes
            else:
                 yield from item.stream(batch=chunk_size)  # Bridge to classes
        else:
            yield ProboSourceString(item)


def data_escaper(data: Any) -> Any:
    """
    Recursively iterates through data structures (dicts, lists, tuples) 
    and HTML-escapes any strings to prevent XSS.
    Leaves other data types (int, bool, lists, dicts) intact so filters
    like |length continue to work on the actual collections.
    """
    if isinstance(data, str):
        return ProboSourceString(html.escape(data))
    elif isinstance(data, dict):
        return {k: data_escaper(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [data_escaper(v) for v in data]
    elif isinstance(data, tuple):
        return tuple(data_escaper(v) for v in data)
    elif isinstance(data, set):
        return {data_escaper(v) for v in data}
    return data
