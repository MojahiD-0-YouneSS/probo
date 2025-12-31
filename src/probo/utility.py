from src.probo.styles.utils import resolve_complex_selector


def exists_in_dict(data: dict, x):
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


def render_attributes(tag_name, attrs):
    parts = []

    # Get defaults for this specific tag
    defaults = HTML_DEFAULTS.get(tag_name, {})

    for key, value in attrs.items():
        # 1. Skip if value is strictly False or None
        if value is False or value is None:
            continue

        # 2. Boolean Attribute (True) -> Render key only
        if value is True:
            parts.append(key.replace("_", "-"))
            continue

        # 3. Skip Default Values (Optimization)
        if key in defaults and str(value).lower() == defaults[key]:
            continue

        # 4. Handle Lists (e.g., classes)
        if isinstance(value, list):
            value = " ".join(str(v) for v in value)

        # 5. Standard Render
        parts.append(f'{key.replace("_", "-")}="{value}"')

    return " ".join(parts)
