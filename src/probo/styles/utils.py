import re
from typing import List


def resolve_complex_selector(selector_str: str) -> List[str]:
    """
    Deconstructs a complex CSS selector into its atomic checkable parts.

    Examples:
        "div.container" -> ['div', '.container']
        "#main > span[data-id]" -> ['#main', 'span', '[data-id]']
        "input.btn:hover" -> ['input', '.btn', ':hover']

    Useful for JIT validation: checking if these atomic parts exist in the template
    before committing to compiling the full rule.
    """
    # 1. Clean Combinators
    # Replace >, +, ~ with spaces to treat them as separate compound selectors
    # We keep the space as a delimiter
    clean_sel = re.sub(r"\s*[>+~]\s*", " ", selector_str)

    # 2. Identify Atomic Parts using Regex
    # Group 1: Attributes [type="text"] (Greedy match inside brackets)
    # Group 2: IDs #header
    # Group 3: Classes .btn
    # Group 4: Pseudo-classes/elements :hover, ::before, :not(.x)
    # Group 5: Tags div, h1 (Must start with letter)

    token_pattern = re.compile(
        r"(\[[^\]]+\])|"  # [Attribute]
        r"(#[a-zA-Z0-9_-]+)|"  # #ID
        r"(\.[a-zA-Z0-9_-]+)|"  # .Class
        r"(::?[a-zA-Z0-9_-]+(?:\(.*?\))?)|"  # :Pseudo / ::Pseudo
        r"([a-zA-Z][a-zA-Z0-9_-]*)"  # Tag
    )

    parts = []

    # Scan the string
    matches = token_pattern.findall(clean_sel)

    for groups in matches:
        # 'groups' is a tuple like ('', '#main', '', '', '')
        # We want the one non-empty string from the group
        token = next((g for g in groups if g), None)
        if token:
            parts.append(token)

    return parts

def selector_type_identifier(token: str) -> tuple[str, str]:
    """
    Identifies the type of a single CSS selector token.
    Returns tuple: (clean_value, type_code)

    Type Codes:
    - EL    : Element/Tag (div)
    - CLS   : Class (.btn)
    - ID    : ID (#header)
    - ATR   : Attribute ([type="text"])
    - PSD-C : Pseudo-Class (:hover)
    - PSD-E : Pseudo-Element (::before)
    - CHLD  : Child Combinator (>)
    - SIB   : Sibling Combinator (~ or +)
    """
    token = token.strip()

    if not token:
        return "", "UNKNOWN"

    # 1. Pseudo-Element (::)
    # Must check before Pseudo-Class because it starts with : too
    if token.startswith("::"):
        return token[2:], "PSEUDO_ELEMENT"

    # 2. Pseudo-Class (:)
    elif token.startswith(":"):
        return token[1:], "PSEUDO_CLASS"

    # 3. ID (#)
    elif token.startswith("#"):
        return token[1:], "ID"

    # 4. Class (.)
    elif token.startswith("."):
        return token[1:], "CLS"

    # 5. Attribute ([...])
    elif token.startswith("[") and token.endswith("]"):
        # Return content inside brackets
        return token[1:-1], "ATR"

    # 6. Combinators
    elif token.startswith(">"):
        return token, "COMBINATOR >"
    elif token.startswith("~"):
        return token, "COMBINATOR ~"
    elif token.startswith("+"):
        return token, "COMBINATOR +"
    elif token.startswith(","):
        return token, "COMBINATOR ,"
    elif token.startswith(" "):
        return token, "COMBINATOR  "

    # 7. Element / Tag (Default)
    # Basic validation to ensure it looks like a tag
    else:
        return token, "EL"
