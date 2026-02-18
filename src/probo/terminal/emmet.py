from probo.components import tag_functions  # Your standard tags (div, span, etc.)
import shlex

def emmet(command_str: str):
    """
    Parses a shorthand string and returns a real Probo Element.
    Syntax: tag #id .class attr:val -s style:value -c "Content here"
    Example: emmet('div #main .container .p-4 type=text -s color:red -c "Hello World"')
    """

    try:
        args = shlex.split(command_str)
    except ValueError:
        return None

    if not args:
        return None

    # 1. Extract Tag
    tag_name = args[0]
    if not hasattr(tag_functions, tag_name):
        raise ValueError(f"Unknown tag: {tag_name}")

    tag_func = getattr(tag_functions, tag_name)

    # 2. Parse State
    attrs = {}
    classes = []
    content_parts = []
    styles = []

    i = 1
    while i < len(args):
        arg = args[i]

        if arg.startswith("#"):
            attrs["id"] = arg[1:]
        elif arg.startswith("."):
            classes.append(arg[1:])
        elif arg == "-s":
            i += 1
            if i < len(args) and ":" in args[i]:
                styles.append(args[i])
        elif arg == "-c":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                content_parts.append(args[i])
                i += 1
            continue
        elif "=" in arg:
            k, v = arg.split("=", 1)
            attrs[k] = v

        i += 1

    # 3. Assemble Attributes
    if classes:
        attrs["Class"] = " ".join(classes)
    if styles:
        attrs["style"] = "; ".join(styles)

    content = " ".join(content_parts)

    # 4. Create the Real Object
    return tag_func(content, **attrs)
