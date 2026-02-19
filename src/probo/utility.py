from typing import Any, Union, List, Self, Dict, Set

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

    # parts = [
        
    #     # 1. Skip if value is strictly False or None
    #     key.replace("_", "-")
    #     if value is True
    #     else
    #     f'{key.replace("_", "-")}="{" ".join(str(v) for v in value)}"'
    #     if isinstance(value, list)
    #     else ''
    #     if value is False or value is None or key in defaults and str(value).lower() == defaults[key]
    #     else''
    #     for key, value in attrs.items()

    # ]
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
        cls.keys_set = {m.name.lower() for m in cls}
        cls.values_map = {m.name.lower(): m for m in cls}
        # Check if the Enum value has a metadata dict with 'void'
        cls.void_set = {
            m.value[0] for m in cls 
            if isinstance(m.value[1], dict) and m.value[1].get("void")
        }
    def __iter__(self):
        return self.keys_set
