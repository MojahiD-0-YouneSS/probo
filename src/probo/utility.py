from typing import Any, Dict, Set, Generator, Self
import html
from collections import deque
import inspect

# --- HIGH-SPEED CACHE ---
_html_escape = html.escape
MARKER = "\u200b"


class ProboSourceString(str):
    __slots__ = ()

    @property
    def is_html(self):
        # Ultra-fast lazy evaluation using C-optimized string search
        return '<' in self and '>' in self

    def __html__(self):
        return self

    def __add__(self, other):
        # Triggers for: ProboSourceString + string (This also handles +=)
        return ProboSourceString(super().__add__(other))

    def __radd__(self, other):
        # Triggers for: string + ProboSourceString
        # (Important if a standard string is on the left side of the + sign)
        return ProboSourceString(other + str(self))


def markup_escape(value: Any, quote: bool = False) -> str:
    """
    The 'Zero-Tax' Escaper.
    If the value is already marked as Safe, it is returned untouched.
    Otherwise, it is escaped to prevent XSS or broken layouts.
    By default, quote=False for prettier HTML text content.
    Attributes must explicitly use quote=True.
    """
    if hasattr(value, 'render'):
        value = value.render()
    # str() call handles numbers/bools; html.escape handles the security.
    return _html_escape(str(value), quote=quote)

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
            # Check nested key
            if any(s in value for s in x):
                return True
            # Check nested values (handle space-separated strings like classes)
            for val in value.values():
                if isinstance(val, str):
                    val_parts = val.split()
                    if any(s in val_parts for s in x):
                        return True
                elif any(s == val for s in x):
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
        for k in [key.replace('__','_') if '__' in key else key.replace("_", "-") if "_" in key else  key]
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

from typing import Callable, Iterable, Optional, Union

class HTMLCollection:
    """
    A collection wrapper for HTML nodes returned by SSDOM APIs.
    Provides JavaScript DOM-like methods for traversing and processing multiple nodes.
    """
    __slots__ = ('nodes',)

    def __init__(self, nodes: Optional[Iterable[Any]] = None):
        self.nodes = list(nodes) if nodes is not None else []

    def __iter__(self):
        return iter(self.nodes)

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, index: Union[int, slice]):
        result = self.nodes[index]
        if isinstance(index, slice):
            return HTMLCollection(result)
        return result
        
    def __bool__(self):
        return bool(self.nodes)

    def __eq__(self, other):
        # Allow testing HTMLCollection against lists
        if isinstance(other, list):
            return self.nodes == other
        if isinstance(other, HTMLCollection):
            return self.nodes == other.nodes
        return False

    def for_each(self, callback: Callable) -> Self:
        """
        Executes a provided function once for each node.
        Similar to JavaScript's NodeList.forEach().
        The callback can accept (node), or (node, index).
        """
        import inspect
        sig = inspect.signature(callback)
        params = len(sig.parameters)
        
        for i, node in enumerate(self.nodes):
            if params == 1:
                callback(node)
            else:
                callback(node, i)
        return self

    def maping(self, callback: Callable) -> list:
        """
        Creates a new list populated with the results of calling a provided function 
        on every node in the collection.
        """
        import inspect
        sig = inspect.signature(callback)
        params = len(sig.parameters)
        
        results = []
        for i, node in enumerate(self.nodes):
            if params == 1:
                results.append(callback(node))
            else:
                results.append(callback(node, i))
        return results

    def filter(self, predicate: Callable) -> Self:
        """
        Creates a new HTMLCollection with all nodes that pass the test implemented 
        by the provided function.
        """
        import inspect
        sig = inspect.signature(predicate)
        params = len(sig.parameters)
        
        filtered = []
        for i, node in enumerate(self.nodes):
            keep = predicate(node) if params == 1 else predicate(node, i)
            if keep:
                filtered.append(node)
        return HTMLCollection(filtered)

    @property
    def first(self) -> Optional[Any]:
        """Returns the first node in the collection."""
        return self.nodes[0] if self.nodes else None

    @property
    def last(self) -> Optional[Any]:
        """Returns the last node in the collection."""
        return self.nodes[-1] if self.nodes else None
        
    def add_class(self, *classes: str) -> Self:
        """Convenience method to add classes to all nodes in the collection."""
        for node in self.nodes:
            if hasattr(node, 'attr_manager'):
                node.attr_manager.add_class(*classes)
            elif hasattr(node, 'add_class'):
                node.add_class(*classes)
        return self


class PipelineDict(dict):
    def __init__(self, node, *args,attrs:dict[str,Any]=None, **kwargs):
        self._node = node
        kwargs.update(attrs or {})
        super().__init__(*args, **kwargs)
        self._check_for_sets(self.values())

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if isinstance(value, set):
            self._node._has_pipeline_vars = True
            self._node._has_unresolved_pipeline_vars = True
            self._node.resolved = False

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._check_for_sets(self.values())
        
    def _check_for_sets(self, values):
        for v in values:
            if isinstance(v, set):
                self._node._has_pipeline_vars = True
                self._node._has_unresolved_pipeline_vars = True
                self._node.resolved = False
                break

class PipelineDeque(deque):
    def __init__(self, node, iterable=(), *args, **kwargs):
        self._node = node
        super().__init__(iterable, *args, **kwargs)
        self._check_for_sets(self)

    def append(self, x):
        super().append(x)
        if isinstance(x, set):
            self._node._has_pipeline_vars = True
            self._node._has_unresolved_pipeline_vars = True
            self._node.resolved = False

    def appendleft(self, x):
        super().appendleft(x)
        if isinstance(x, set):
            self._node._has_pipeline_vars = True
            self._node._has_unresolved_pipeline_vars = True
            self._node.resolved = False

    def extend(self, iterable):
        super().extend(iterable)
        self._check_for_sets(iterable)

    def extendleft(self, iterable):
        super().extendleft(iterable)
        self._check_for_sets(iterable)

    def insert(self, i, x):
        super().insert(i, x)
        if isinstance(x, set):
            self._node._has_pipeline_vars = True
            self._node._has_unresolved_pipeline_vars = True
            self._node.resolved = False

    def __setitem__(self, i, x):
        super().__setitem__(i, x)
        if isinstance(x, set):
            self._node._has_pipeline_vars = True
            self._node._has_unresolved_pipeline_vars = True
            self._node.resolved = False

    def _check_for_sets(self, iterable):
        for v in iterable:
            if isinstance(v, set):
                self._node._has_pipeline_vars = True
                self._node._has_unresolved_pipeline_vars = True
                self._node.resolved = False
                break

def deep_get(obj: Any, key: str, default: Any = None) -> Any:
    _no_val = object()
    if isinstance(key, str) and '.' in key:
        parts = key.split('.')
        if hasattr(obj, 'get') and isinstance(obj, dict):
            current = obj.get(parts[0], _no_val)
        else:
            current = getattr(obj, parts[0], _no_val)
            
        if current is not _no_val:
            for part in parts[1:]:
                if hasattr(current, 'get') and isinstance(current, dict):
                    current = current.get(part, _no_val)
                else:
                    current = getattr(current, part, _no_val)
                if current is _no_val:
                    break
            if current is not _no_val:
                return current

    if hasattr(obj, 'get'):
        return obj.get(key, default)
    return getattr(obj, key, default)

class DataPipeLineSource:
    """
    Hosts multiple data pipeline sources.
    Allows for name-spaced data access via 'variable|source_name' syntax.
    If no source_name is provided, it searches through all attached sources.
    """
    def __init__(self, *sources, **named_sources):
        self.sources = list(sources)
        self.named_sources = named_sources
        self._key_cache = {}
        
    def add(self, source, name: str = None):
        """Adds a new data source."""
        if name:
            self.named_sources[name] = source
        else:
            self.sources.append(source)
            
    def get(self, key: str, default: Any = None) -> Any:
        source_name = None
        if isinstance(key, str):
            if '|' in key:
                key, source_name = key.split('|', 1)
            elif '.' in key:
                source_name, key = key.split('.', 1)
            
        if source_name:
            if source_name in self.named_sources:
                return self._get_from_src(self.named_sources[source_name], key, default)
                
            for src in self.sources + list(self.named_sources.values()):
                if self._get_source_name(src) == source_name:
                    return self._get_from_src(src, key, default)
                    
            return default
            
        _no_val = object()
        
        # 1. Fast path: check cache first
        if key in self._key_cache:
            val = self._get_from_src(self._key_cache[key], key, _no_val)
            if val is not _no_val:
                return val
            # If not found in cached source (e.g., data was removed), fall through to full search
                
        # 2. Full search across all sources
        for src in list(self.named_sources.values()) + self.sources:
            val = self._get_from_src(src, key, _no_val)
            if val is not _no_val:
                self._key_cache[key] = src  # Cache the successful source for next time
                return val
                
        return default
        
    def _get_source_name(self, src: Any) -> str:
        if isinstance(src, dict) and '_data_pipeline_name' in src:
            return src['_data_pipeline_name']
        if hasattr(src, '__class__'):
            return src.__class__.__name__
        return None

    def _get_from_src(self, src: Any, key: str, default: Any) -> Any:
        return deep_get(src, key, default)


