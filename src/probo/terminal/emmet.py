from src.probo.components import tag_functions  # Your standard tags (div, span, etc.)


def emmet(command_str: str):
    """
    Parses a shorthand string and returns a real MUI Element.
    Syntax: tag #id .class -s style:value -c "Content here"
    Example: emmet('div #main .container -c "Hello World"')
    """
    # 1. Tokenize (Simple split, respecting quotes would require shlex)
    import shlex

    try:
        args = shlex.split(command_str)
    except ValueError:
        return None

    if not args:
        return None

    # 2. Extract Tag
    tag_name = args[0]
    if not hasattr(tag_functions, tag_name):
        raise ValueError(f"Unknown tag: {tag_name}")

    tag_func = getattr(tag_functions, tag_name)

    # 3. Parse Attributes
    attrs = {}
    classes = []
    content_parts = []
    styles = {}

    i = 1
    while i < len(args):
        arg = args[i]

        if arg.startswith("#"):
            attrs["id"] = arg[1:]
        elif arg.startswith("."):
            classes.append(arg[1:])  # Collect classes list
        elif arg == "-s":
            # Style parsing (simple key:value)
            i += 1
            if i < len(args) and ":" in args[i]:
                k, v = args[i].split(":", 1)
                styles[k] = v
        elif arg == "-c":
            # Content parsing (everything until end or next flag)
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                content_parts.append(args[i])
                i += 1
            continue  # Skip the increment at end of loop
        elif ":" in arg:
            # Arbitrary attributes (type:text)
            k, v = arg.split(":", 1)
            attrs[k] = v

        i += 1

    # 4. Assemble
    if classes:
        attrs["class_"] = " ".join(classes)

    # Handle Style object if you support it in v1, or just string
    # if styles: attrs['style'] = ES(**styles)

    content = " ".join(content_parts)

    # 5. Create the Real Object
    return tag_func(content, **attrs)
