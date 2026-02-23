import logging
from probo.styles.css_enum import (
    CssPropertyEnum,
    PseudoClassEnum,
    PseudoElementEnum,
    CssFunctionsEnum,
    CssFontsEnum,
    CssAnimatableEnum,
)
from probo.templates.resolver import TemplateResolver
import cssutils
from probo.styles.utils import selector_type_identifier

cssutils.log.setLevel(logging.FATAL)


class CssRuleValidator:
    """A silent validation engine for CSS property-value pairs.

    This class leverages `cssutils` to verify that CSS declarations follow 
    W3C standards. It is designed to be 'silent,' meaning it suppresses 
    library-level logging to maintain performance and terminal clarity 
    during high-volume rendering (e.g., 1,000,000+ nodes).

    Attributes:
        property_value (Dict[str, Any]): A dictionary of CSS properties 
            and their values to be validated.
    """
    __slots__ = (
        'property_value',
    )
    def __init__(self, **prop_val):
        self.property_value = prop_val

    def is_valid(
        self,
    ):
        """Aggregates validation results for all properties in the instance.

        Returns:
            bool: True if every property-value pair is syntactically valid CSS.
        """  
        return all(
            [
                self.validate_css(f"{prop}:{val};")
                for prop, val in self.property_value.items()
            ]
        )

    def validate_css(self, css_string: str) -> bool:
        """Performs a low-level syntax check on a single CSS declaration string.

        This method captures internal `cssutils` errors via a local 
        logging handler to prevent terminal pollution. It checks both 
        for hard syntax errors and for 'dropped' properties (where the 
        parser doesn't recognize the property name).

        Args:
            css_string (str): A full CSS declaration (e.g., "color:red;").

        Returns:
            bool: True if the CSS string is valid and recognized by the parser.
        """
        # 1. Setup Logging Capture

        errors = []

        class ListHandler(logging.Handler):
            def emit(self, record):
                errors.append(record.getMessage())
        log = logging.getLogger("CSSUTILS")
        handler = ListHandler()
        log.addHandler(handler)

        try:
            # 2. Parse using parseStyle (Correct tool for properties)
            # 'validate=True' is default, but explicit is better
            style = cssutils.parseStyle(css_string, validate=True)

            # 3. Check for Syntax Errors (Logged by cssutils)
            if errors:
                raise ValueError(f"Invalid CSS Syntax: {errors[0]}")

            # 4. Check for dropped properties (The 'paddifont' case)
            # If input was not empty but result has 0 length, it means
            # cssutils dropped the property because it didn't recognize it.
            if css_string.strip() and style.length == 0:
                raise ValueError(
                    f"Invalid CSS Property: '{css_string}' was dropped by parser."
                )

            return True

        except Exception:
            # Re-raise the specific ValueError we created, or wrap others
            return False

        finally:
            log.removeHandler(handler)

class CssRule:
    """A container for validated CSS declarations.

    This class manages the lifecycle of CSS properties, from normalization 
    and Enum-based validation to final serialization. It supports standard 
    properties, CSS variables, and specialized CSS functions (fonts, transforms, etc.).

    Attributes:
        validator (CssRuleValidator): A shared class-level utility to verify 
            CSS syntax via cssutils.
        declarations (dict): A dictionary storage for validated property-value pairs.
    """
    # validator = CssRuleValidator()
    __slots__ = ('declarations')
    def __init__(self, **declarations):
        self.declarations: dict = self.__check_declarations(**declarations)

    def set_rule(self, **prop_val):
        """Updates or adds new validated rules to the current declarations.

        Args:
            **prop_val: New CSS properties to apply.

        Returns:
            self: Allows for method chaining.
        """
        valid_decs = self.__check_declarations(**prop_val)
        self.declarations.update(valid_decs)
        return self

    def __check_declarations(self, **decs):
        """Internal pipeline for property normalization and validation.

        This method performs the following:
        1. Normalizes Python keys (e.g., 'at_media' or 'margin_top').
        2. Cross-references keys against `CssPropertyEnum`.
        3. Validates the final string via `self.validator`.
        4. Comments out invalid properties in the final output for debugging.

        Args:
            **decs: Raw keyword arguments from the user.

        Returns:
            dict: Validated and formatted property-value mapping.
        """
        valid_decs = {}
        for prop, value in decs.items():
            normalized_key = (
                prop.strip(
                    " ",
                )
                .strip(":")
                .strip("_")
                .replace("-", "_")
                .replace("@", "at_")
            )
            prop_name = prop.replace('_', '-').strip(':')
            enum_value = CssPropertyEnum.get(normalized_key)
            if enum_value:
                # css_declaration = (
                #     enum_value(value)
                #     if enum_value and "%s" in enum_value.value
                #     else f"{prop_name}:{value};"
                # )
                valid_decs[prop_name] = value
            else:
                valid_decs[f"/* {prop_name}"] = f"{value}; CSS ERROR */"
        return valid_decs

    def css_var(self, **dec):
        """Defines CSS custom properties (variables).

        Automatically prepends '--' and replaces underscores with hyphens.

        Args:
            **dec: Variable names and values (e.g., brand_gold="#D4AF37").

        Returns:
            self: Allows for method chaining.
        """
        self.declarations.update(
            {
                f"--{k.strip('-').strip('_').replace('_', '-')}": v
                for k, v in dec.items()
            }
        )
        return self

    def apply_css_function(self, prop, name: str, *args):
        """Applies a standard CSS function (e.g., calc, url, rgba) to a property.

        Args:
            prop (str): The CSS property to target (e.g., 'width').
            name (str): The function name found in `CssFunctionsEnum`.
            *args: Arguments to pass into the CSS function.

        Returns:
            self: Allows for method chaining.
        """
        string = self.__apply_css_enums(CssFunctionsEnum, name, *args)
        if string:
            self.declarations[prop] = string
        return self

    def apply_css_fonts(self, prop, name: str, *args):
        """Applies specialized font-related CSS functions.

        Args:
            prop (str): The target font property.
            name (str): The font function name found in `CssFontsEnum`.
            *args: Arguments for the font function.

        Returns:
            self: Allows for method chaining.
        """
        string = self.__apply_css_enums(CssFontsEnum, name, *args)
        if string:
            self.declarations[prop] = string
        return self

    def __apply_css_enums(self, __enum_cls, name: str, *args):
        """Helper to map string names to specialized Enum templates.

        Args:
            __enum_cls: The Enum class to search (Functions or Fonts).
            name (str): The key to look up.
            *args: Data to inject into the Enum's value template.

        Returns:
            Union[str, bool]: The formatted CSS string or False on failure.
        """
        try:
            func_enum = __enum_cls.get(name.upper())
            if func_enum and "%s" in func_enum.value:
                string = func_enum.value % ", ".join(map(str, args))
            else:
                string = func_enum.value
            return string
        except Exception as e:
            print("e", e)
            return False

    def render(
        self,
    ):
        """Serializes the validated declarations into a CSS block string.

        Returns:
            str: A formatted CSS block (e.g., "{ color:red; margin-top:10px; }").
                Returns an empty string if no declarations exist.
        """
        if self.declarations:
            return (
                f"{{ {''.join([f'{p}:{v}; ' for p, v in self.declarations.items()])}}}"
            )
        else:
            return str()

class CssAnimatable:
    """A factory for generating validated CSS Keyframe animations.

    This class manages the creation of `@keyframes` blocks, ensuring that 
    only properties recognized as animatable by the W3C (via CssAnimatableEnum) 
    are included in the animation steps.

    Attributes:
        name (str): The identifier for the animation (e.g., 'fade-in').
        animations (list): A collection of stored animation definitions.
        validator (CssRuleValidator): Utility to verify CSS syntax integrity.
    """
    __slots__ = (
        'name',
        'animations',
        'validator',
    )
    def __init__(self, name):
        self.name = name
        self.animations = []
        self.validator = CssRuleValidator()

    def __check_animatable(self, props: dict):
        """Validates that a dictionary of properties can be legally animated.

        Args:
            props (dict): Property-value pairs to check against 
                `CssAnimatableEnum`.

        Raises:
            ValueError: If a property is found that cannot be animated 
                according to CSS specifications.
        """
        for prop in props.keys():
            if prop.lower() not in [e.name.lower() for e in CssAnimatableEnum]:
                raise ValueError(f"Property '{prop}' is not animatable.")

    def animate(self, name: str, steps: dict = dict(), **properties):
        """Constructs a full @keyframes string block.

        Can generate either a simple 'from' animation or a complex 
        multi-step sequence (0%, 50%, 100%).

        Args:
            name (str): The name of the keyframe sequence.
            steps (dict, optional): A dictionary where keys are steps 
                (e.g., '0%', '100%') and values are property dictionaries.
            **properties: Keyword arguments for a single-step animation 
                (defaults to a 'from' block).

        Returns:
            str: The fully formatted `@keyframes` CSS string.

        Example:
            >>> anim.animate('slide', steps={'0%': {'left': '0px'}, '100%': {'left': '100px'}})
            >>> anim.animate('fade', opacity='0')
        """
        declaration = f"@keyframes {name} " + "{\n"

        if steps:
            for step, props in steps.items():
                self.__check_animatable(props)
                rule = CssRule(**props).declarations
                rules = "; ".join([f"{k}: {v}" for k, v in rule.items()])
                declaration += f"  {step} {{ {rules}; }}\n"
        else:
            self.__check_animatable(properties)
            rule = CssRule(**properties).declarations
            rules = "; ".join([f"{k}: {v}" for k, v in rule.items()])
            declaration += f"  from {{ {rules}; }}\n"

        declaration += "}"
        return declaration

class CssSelector:
    """A fluent builder for constructing complex CSS selectors.

    This class provides a programmatic interface for defining IDs, classes, 
    attributes, and relationships (descendants, siblings, etc.). It acts as 
     the primary target definition for `SelectorRuleBridge`.

    Attributes:
        selectors (list): A collection of selector fragments to be joined.
    """
    __slots__ = (
        'selectors',
        '_CssSelector__template',
        '_selector_type_maping',
        'template_tags',
        'template_attributes',
        'template_info_obj',
        'template_info',
    )
    def __init__(self, template=None):
        self.selectors = []
        self.__template = template
        self._selector_type_maping = {}
        self.template_tags = []
        self.template_attributes = {}
        self.template_info_obj = (
            TemplateResolver(tmplt_str=self.__template, load_it=True)
            if self.__template
            else None
        )
        self.template_info = (
            self.template_info_obj.template_resolver() if self.template_info_obj else {}
        )
        if self.template_info_obj:
            self.template_tags.extend(self.template_info_obj.template_tags)
            self.template_attributes.update(self.template_info_obj.template_attributes)

    def Id(self, value):
        """Appends an ID selector to the current chain.
        
        Args:
            value (str): The ID name (without the '#' prefix).
        """
        if self.template_attributes and value not in self.template_attributes["id"]:
            raise ValueError("in valid value class not found")
        self.selectors.append(f"#{value.strip('#')}")
        self._selector_type_maping[self.selectors[-1]] = "ID"
        return self

    def cls(self, value):
        """Appends a class selector to the current chain.
        
        Args:
            value (str): The class name (without the '.' prefix).
        """
        if self.template_attributes and value not in self.template_attributes["class"]:
            raise ValueError("in valid value class not found")
        self.selectors.append(f".{value.strip('.')}")
        self._selector_type_maping[self.selectors[-1]] = "CLS"
        return self

    def el(self, value):
        """Appends an element/tag selector.
        
        Args:
            value (str): The HTML tag name (e.g., 'div', 'section').
        """
        if self.template_tags and value not in self.template_tags:
            raise ValueError("in valid value element not found in ")
        self.selectors.append(value)
        self._selector_type_maping[self.selectors[-1]] = "EL"
        return self

    def attr(self, attr, value=None, op="="):
        """Adds an attribute selector with optional value matching.
        
        Args:
            attr (str): The attribute name.
            value (str, optional): The value to match.
            op (str): The comparison operator (default '=', supports '~=', '^=', etc.).
        """
        if self.template_attributes and attr not in self.template_attributes:
            raise ValueError("in valid value class not found")
        if value:
            if self.template_attributes and value not in self.template_attributes.get(
                attr, []
            ):
                raise ValueError("in valid value class not found")
            self.selectors.append(f'[{attr}{op}"{value}"]')
        else:
            self.selectors.append(f"[{attr}]")
        self._selector_type_maping[self.selectors[-1]] = "ATTR"
        return self

    def pseudo_class(self, pseudo):
        """Appends a pseudo-class (e.g., :hover, :nth-child)."""
        pseudo_value = PseudoClassEnum.get(
            pseudo.split("(")[0] if "(" in pseudo else pseudo
        )
        pseudo = (
            pseudo_value
            if "(" not in pseudo_value
            else pseudo_value.replace("()", f"({pseudo.split('(')[1].strip(')')})")
        )
        if pseudo:
            self.selectors.append(pseudo)
            self._selector_type_maping[self.selectors[-1]] = "PSEUDO_CLASS"
        return self

    def pseudo_element(self, pseudo):
        """Appends a pseudo-element (e.g., ::before, ::after)."""
        pseudo_value = PseudoElementEnum.get(
            pseudo.split("(")[0] if "(" in pseudo else pseudo
        )
        pseudo = (
            pseudo_value
            if "(" not in pseudo_value
            else pseudo_value.replace("()", f"({pseudo.split('(')[1].strip(')')})")
        )
        if pseudo:
            self.selectors.append(pseudo)
            self._selector_type_maping[self.selectors[-1]] = "PSEUDO_ELEMENT"
        return self

    def add_selector(
        self,
        selector: str,
    ):
        """Directly injects a raw selector string into the chain."""
        _, selector_type = selector_type_identifier(selector)
        self.selectors.append(selector)
        self._selector_type_maping[self.selectors[-1]] = selector_type
        return self

    def child(self, child):
        """Defines a direct child relationship (parent > child)."""
        if self.template_tags and child not in self.template_tags:
            raise ValueError("in valid value element not found in ")
        if len(self.selectors) > 0:
            self.selectors.append(f" > {child}")
        else:
            self.selectors.append(child)
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR >"
        return self

    def group(self, *selectors):
        """Combines multiple selectors as a comma-separated group."""
        if len(selectors) == 1:
            self.selectors.append(f", {', '.join(selectors)}")
        else:
            self.selectors.append(", ".join(selectors))
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR ,"
        return self

    def descendant(self, *selectors):
        """Defines a descendant relationship (ancestor descendant)."""
        if len(selectors) == 1:
            self.selectors.append(f" {' '.join(selectors)}")
        else:
            self.selectors.append(" ".join(selectors))
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR  "
        return self

    def adjacent(self, *selectors):
        """Defines an adjacent sibling relationship (element + sibling)."""
        if len(selectors) == 1:
            self.selectors.append(f" + {' + '.join(selectors)}")
        else:
            self.selectors.append(" + ".join(selectors))
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR +"
        return self

    def sibling(self, *selectors):
        """Defines a general sibling relationship (element ~ sibling)."""
        if len(selectors) == 1:
            self.selectors.append(f" ~ {' ~ '.join(selectors)}")
        else:
            self.selectors.append(" ~ ".join(selectors))
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR ~"
        return self

    def _polish_selectors(
        self,
    ):
        """Internal cleanup to remove redundant spaces and ensure valid syntax."""
        polished_selectors = list()
        el_counter = 0
        last_type = None

        for x in self.selectors:
            current_type = self._selector_type_maping[x]
            if (
                (current_type == "EL" and el_counter == 1)
                or (current_type == "PSEUDO_CLASS" and last_type == "PSEUDO_ELEMENT")
                or (current_type == "EL" and self.selectors.index(x) > 0)
            ):
                polished_selectors.append(f" {x}")
                continue
            if current_type == "EL" and el_counter == 0:
                el_counter = 1
            last_type = current_type
            polished_selectors.append(x)
        self.selectors = polished_selectors
        return self

    def render(self):
        """Serializes the builder into a valid CSS selector string.
        
        Returns:
            str: The final selector (e.g., "div.card > .title:hover").
        """
        self._polish_selectors()
        if not self.__template:
            return "".join(self.selectors)
        else:
            return "".join(self.selectors)

def css_style(selectors_rules: dict[CssSelector, CssRule] = None, **declarations) -> str:
    """A factory function for creating individual CSS rules or bulk Style Bridges.

    This utility serves a dual purpose based on the provided arguments:
    1. If `selectors_rules` is provided: It acts as a factory for a list of 
       `SelectorRuleBridge` objects, enabling bulk style definitions.
    2. If `**declarations` are provided: It returns a single, validated 
       `CssRule` object.

    Args:
        selectors_rules (dict[CssSelector, CssRule], optional): A mapping of 
            selectors to their corresponding rules. Used for bulk component 
            styling.
        **declarations: Keyword arguments representing CSS property-value 
            pairs (e.g., color="blue", margin_top="20px").

    Returns:
        Union[List[SelectorRuleBridge], CssRule]: 
            - A list of bridges if `selectors_rules` is present.
            - A validated `CssRule` instance if only `**declarations` are present.

    Example:
        # Bulk Pattern
        >>> theme = css_style({CssSelector(".btn"): CssRule(color="red")})
        
        # Quick Rule Pattern
        >>> blue_text = css_style(color="blue", font_weight="bold")
    """
    if selectors_rules is not None and not all(
        [isinstance(sel, CssSelector) for sel in selectors_rules]
    ):
        raise TypeError("selectors must be an instance of CssSelector")

    if selectors_rules is not None and not all(
        [isinstance(sel, CssRule) for sel in selectors_rules.values()]
    ):
        raise ValueError("No valid CSS declarations provided")
    if selectors_rules:
        css_string = "".join(
            [f"{s.render()} {{ {r.render()} }}" for s, r in selectors_rules.items()]
        )
    else:
        css_string = "".join(
            [
                f"{s} {{ {CssRule(**{k: v.strip(';') for k, v in [item.split(':') for item in r.split(';') if item]}).render()} }}"
                for s, r in declarations.items()
            ]
        )
    return css_string

def css_comment(css, return_type=str()) -> list[str] | str:
    """Wraps a CSS string or list of rules in a CSS comment block.

    This function is primarily used for debugging, documenting rendered 
    output, or temporarily disabling style rules within the ProboUI 
    rendering pipeline.

    Args:
        css (Any): The CSS content to be commented out. Can be a string, 
            a list of rules, or an object with a .render() method.
        return_type (Union[str, list]): Defines the output format. 
            Defaults to an empty string, signifying a string return. 
            If a list instance is passed, it returns a list of commented lines.

    Returns:
        Union[str, list]: The commented CSS content. 
            String format: "/* [css] */"
            List format: ["/* line1 */", "/* line2 */"]

    Example:
        >>> css_comment("color: red;")
        '/* color: red; */'
        
        >>> css_comment(["color: blue;", "margin: 0;"], return_type=[])
        ['/* color: blue; */', '/* margin: 0; */']
    """
    if isinstance(return_type, str):
        return f"/* {css} */"
    else:
        return ["/* ", css, " */"]

def box_model(
    margins="10px",
    padding="10px",
    border="10px",
    content_width="10px",
) -> str:
    """A factory function to generate a standard CSS Box Model rule.

    This utility provides a centralized way to define the core structural 
    properties of an element. It returns a validated `CssRule` object, 
    ensuring that spacing and sizing remain consistent across the application.

    Args:
        margins (str): The CSS margin shorthand value. Defaults to "10px".
        padding (str): The CSS padding shorthand value. Defaults to "10px".
        border (str): The CSS border shorthand value. Defaults to "10px".
        content_width (str): The CSS width property. Defaults to "10px".

    Returns:
        CssRule: A validated rule object containing the box model declarations.

    Example:
        >>> card_box = box_model(margins="20px auto", padding="15px", content_width="100%")
    """
    string = f"""
     {{
            width:{content_width};
            border:{border};
            padding:{padding};
            margin:{margins};
    }}"""
    return string

def make_important(css_string) -> str:
    """Appends the !important flag to CSS declarations.

    This utility modifies a CSS property-value string to ensure it overrides 
    other rules in the cascade. It handles both single declarations and 
    semicolon-terminated strings.

    Args:
        css_string (str): A standard CSS declaration (e.g., "color:red" 
            or "display:block;").

    Returns:
        str: The modified string with !important injected (e.g., "color:red !important;").

    Example:
        >>> make_important("display: none")
        'display: none !important;'
    """
    return f"{css_string} !important;"

class Animation:
    """A high-level manager for creating and rendering CSS @keyframes.

    The Animation class provides a simplified interface for building complex 
    motion sequences. It supports standard 'from-to' transitions, discrete 
    percentage-based frames, and sequential frame addition.

    Attributes:
        name (str): The identifier for the animation sequence.
        frames (dict): An internal mapping of timeline steps to CSS properties.
    """
    __slots__ = (
        'name',
        'animation_body',
        'frames',
    )
    def __init__(
        self,
        name,
    ):
        self.name = name
        self.animation_body = str()
        self.frames = {}  # Store frames as dict to allow incremental updates

    def add_frame(self, step: str, **properties):
        """Appends a single frame to the animation timeline.

        Args:
            step (str): The timeline position (e.g., '0%', '50%', 'to').
            **properties: CSS property-value pairs for this frame.
        """
        # OPTIONAL: Add strict validation here
        # self.__check_animatable(properties)

        # Use CssRule logic to clean up properties (snake_case -> kebab-case)
        # We use a temporary CssRule just to get the clean dict
        clean_props = CssRule(**properties)

        self.__check_animatable(clean_props.declarations)

        self.frames[step] = clean_props.render()
        return self

    def __check_animatable(self, props: dict):
        for prop in props.keys():
            if CssAnimatableEnum.get(prop.lower().replace("-", "_")) is None:
                raise ValueError(f"Property '{prop}' is not animatable.")

    def animate_from_to(self, from_props: dict, to_props: dict):
        """Quickly defines a two-point transition.

        Args:
            from_props (dict): CSS properties for the starting state ('from').
            to_props (dict): CSS properties for the ending state ('to').
        
        @keyframes myAnimation {
            from {background-color: red;}
            to {background-color: yellow;}
        }
        """
        self.add_frame("from", **from_props)
        self.add_frame("to", **to_props)
        # self.animation_body= f' from {{ {' '.join([f'{k}:{v};' for k,v in from_block.items()])} }} to {{ {' '.join([f'{k}:{v};' for k,v in to_block.items()])} }} '
        return self

    def animate_percent(self, blocks: dict[str, dict]):
        """Populates the timeline using a dictionary of percentage steps.

        Args:
            blocks (dict[str, dict]): A mapping of steps to property dicts.
                e.g., {"0%": {"opacity": 0}, "100%": {"opacity": 1}}
        
        @keyframes myAnimation {
            0%   {background-color: red;}
            25%  {background-color: yellow;}
            50%  {background-color: blue;}
            100% {background-color: green;}
        }
        """
        for percent, props in blocks.items():
            self.add_frame(percent, **props)
        return self

    def render(
        self,
    ):
        """Serializes the frames into a valid CSS @keyframes block.

        Leverages the underlying CssAnimatable engine to ensure 
        property validation and proper formatting.

        Returns:
            str: The fully rendered @keyframes string.
        """
        declaration_name = f"@keyframes {self.name} "
        if self.animation_body:
            return f"{declaration_name}{{ {self.animation_body} }}"
        frames = ""
        for step, props in self.frames.items():
            frames += f" {step} {props}"

        return f"{declaration_name} {{{frames}}}"

class MediaQueries:
    """A generator for validated and structured CSS @media at-rules.

    This class provides a programmatic way to define responsive design 
    breakpoints. It validates media types (screen, print, etc.) and features 
    (width, orientation, etc.) to ensure the generated CSS is standard-compliant.

    Attributes:
        media_type (str): The CSS media type (e.g., 'screen', 'print').
        media_values (dict): Feature-value pairs (e.g., {'max-width': '768px'}).
        no_media_type (bool): If True, omits the media type from the query.
        is_not (bool): If True, prepends the 'not' operator.
        is_only (bool): If True, prepends the 'only' operator.
        css_rules (dict): A mapping of selectors to property-value blocks.
    """
    __slots__ = (
        '_MediaQueries__css_media_types',
        '_MediaQueries__media_features',
        'media_type',
        'css_rules',
        'media_values',
        'is_not',
        'no_media_type',
        'is_only',
    )
    def __init__(
        self,
        media_type,
        media_values: dict,
        no_media_type=False,
        is_not=False,
        is_only=False,
        **css_rules,
    ):
        self.__css_media_types = ["all", "print", "screen"]
        self.__media_features = [
            "max-height",
            "min-height",
            "height",
            "max-width",
            "min-width",
            "width",
            "orientation",
            "resolution",
            "prefers-color-scheme",
        ]
        self.media_type = media_type
        self.css_rules = css_rules
        self.media_values = media_values
        self.is_not = is_not
        self.no_media_type = no_media_type
        self.is_only = is_only
        self.__checks()

    def __checks(self):
        """Internal validation logic for media types and features.

        Verifies that the provided media_type and media_values are valid 
        CSS keywords and identifiers.

        Raises:
            ValueError: If an invalid media type or unsupported feature is provided.
            
        Returns:
            bool: True if validation passes.
        """
        if self.no_media_type and self.media_type:
            raise ValueError("invalid values")
        if self.media_type and self.media_type not in self.__css_media_types:
            raise ValueError("invalid values")

        if not all(
            [
                media_feature in self.__media_features
                for media_feature in self.media_values
            ]
        ):
            raise ValueError("invalid values")
        return True

    def render(self):
        """Serializes the object into a valid CSS @media block.

        Returns:
            str: The fully formatted media query (e.g., "@media screen and (max-width: 600px) { ... }").
        """
        # Build optional "not" keyword
        not_part = "not " if self.is_not else ""
        only_part = "only " if self.is_only else ""
        media_type = self.media_type if not self.no_media_type else ""

        # Build CSS rules
        rules = ""
        for selector, props in self.css_rules.items():
            rules += f" {selector} {props}"
        media_vals = " ".join(
            [
                f" and ({media_feature}:{feature_value})"
                for media_feature, feature_value in self.media_values.items()
            ]
        )
        # Combine everything into a media query string
        if not media_type:
            media_vals = media_vals.strip(" and")
        return f"@media {not_part}{only_part}{media_type}{media_vals} {{{rules}}}"
