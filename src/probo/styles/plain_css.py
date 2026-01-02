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


class CssRuleValidator:
    def __init__(self, **prop_val):
        self.property_value = prop_val

    def is_valid(
        self,
    ):
        return all(
            [
                self.validate_css(f"{prop}:{val};")
                for prop, val in self.property_value.items()
            ]
        )

    def validate_css(self, css_string: str) -> bool:
        # 1. Setup Logging Capture
        import logging

        errors = []

        class ListHandler(logging.Handler):
            def emit(self, record):
                errors.append(record.getMessage())

        log = logging.getLogger("CSSUTILS")
        handler = ListHandler()
        log.addHandler(handler)
        log.setLevel(logging.ERROR)

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
    validator = CssRuleValidator()

    def __init__(self, **declarations):
        self.declarations: dict = self.__check_declarations(**declarations)

    def set_rule(self, **prop_val):
        valid_decs = self.__check_declarations(**prop_val)
        self.declarations.update(valid_decs)
        return self

    def __check_declarations(self, **decs):
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
            enum_value = CssPropertyEnum.get(normalized_key)
            css_declaration = (
                enum_value(value)
                if enum_value and "%s" in enum_value.value
                else f"{prop.replace('_', '-').strip(':')}:{value};"
            )
            prop_name = css_declaration.split(":")[0]
            if self.validator.validate_css(css_declaration) and enum_value:
                valid_decs[prop_name] = value
            else:
                valid_decs[f"/* {prop_name}"] = f"{value}; CSS ERROR */"
        return valid_decs

    def css_var(self, **dec):
        self.declarations.update(
            {
                f"--{k.strip('-').strip('_').replace('_', '-')}": v
                for k, v in dec.items()
            }
        )
        return self

    def apply_css_function(self, prop, name: str, *args):
        """Apply a CSS function to the given arguments."""
        string = self.__apply_css_enums(CssFunctionsEnum, name, *args)
        if string:
            self.declarations[prop] = string
        return self

    def apply_css_fonts(self, prop, name: str, *args):
        """Apply a CSS font function to the given arguments."""
        string = self.__apply_css_enums(CssFontsEnum, name, *args)
        if string:
            self.declarations[prop] = string
        return self

    def __apply_css_enums(self, __enum_cls, name: str, *args):
        """Apply a CSS function to the given arguments."""
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
        if self.declarations:
            return (
                f"{{ {''.join([f'{p}:{v}; ' for p, v in self.declarations.items()])}}}"
            )
        else:
            return str()


class CssAnimatable:
    def __init__(self, name):
        self.name = name
        self.animations = []
        self.validator = CssRuleValidator()

    def __check_animatable(self, props: dict):
        for prop in props.keys():
            if prop.lower() not in [e.name.lower() for e in CssAnimatableEnum]:
                raise ValueError(f"Property '{prop}' is not animatable.")

    def animate(self, name: str, steps: dict = dict(), **properties):
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
        if self.template_attributes and value not in self.template_attributes["id"]:
            raise ValueError("in valid value class not found")
        self.selectors.append(f"#{value.strip('#')}")
        self._selector_type_maping[self.selectors[-1]] = "ID"
        return self

    def cls(self, value):
        if self.template_attributes and value not in self.template_attributes["class"]:
            raise ValueError("in valid value class not found")
        self.selectors.append(f".{value.strip('.')}")
        self._selector_type_maping[self.selectors[-1]] = "CLS"
        return self

    def el(self, value):
        if self.template_tags and value not in self.template_tags:
            raise ValueError("in valid value element not found in ")
        self.selectors.append(value)
        self._selector_type_maping[self.selectors[-1]] = "EL"
        return self

    def attr(self, attr, value=None, op="="):
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
        _, selector_type = selector_type_identifier(selector)
        self.selectors.append(selector)
        self._selector_type_maping[self.selectors[-1]] = selector_type
        return self

    def child(self, child):
        if self.template_tags and child not in self.template_tags:
            raise ValueError("in valid value element not found in ")
        if len(self.selectors) > 0:
            self.selectors.append(f" > {child}")
        else:
            self.selectors.append(child)
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR >"
        return self

    def group(self, *selectors):
        if len(selectors) == 1:
            self.selectors.append(f", {', '.join(selectors)}")
        else:
            self.selectors.append(", ".join(selectors))
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR ,"
        return self

    def descendant(self, *selectors):
        if len(selectors) == 1:
            self.selectors.append(f" {' '.join(selectors)}")
        else:
            self.selectors.append(" ".join(selectors))
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR  "
        return self

    def adjacent(self, *selectors):
        if len(selectors) == 1:
            self.selectors.append(f" + {' + '.join(selectors)}")
        else:
            self.selectors.append(" + ".join(selectors))
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR +"
        return self

    def sibling(self, *selectors):
        if len(selectors) == 1:
            self.selectors.append(f" ~ {' ~ '.join(selectors)}")
        else:
            self.selectors.append(" ~ ".join(selectors))
        self._selector_type_maping[self.selectors[-1]] = "COMBINATOR ~"
        return self

    def _polish_selectors(
        self,
    ):
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
        self._polish_selectors()
        if not self.__template:
            return "".join(self.selectors)
        else:
            return "".join(self.selectors)


def css_style(selectors_rules: dict[CssSelector, CssRule] = None, **declarations):
    """Create a CSS style string from selectors and declarations."""
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


def css_comment(css, return_type=str()):
    if isinstance(return_type, str):
        return f"/* {css} */"
    else:
        return ["/* ", css, " */"]


def box_model(
    margins="10px",
    padding="10px",
    border="10px",
    content_width="10px",
):
    string = f"""
     {{
            width:{content_width};
            border:{border};
            padding:{padding};
            margin:{margins};
    }}"""
    return string


def make_important(css_string):
    return f"{css_string} !important;"


class Animation:
    def __init__(
        self,
        name,
    ):
        self.name = name
        self.animation_body = str()
        self.frames = {}  # Store frames as dict to allow incremental updates

    def add_frame(self, step: str, **properties):
        """
        Adds a keyframe step.
        step: '0%', '100%', 'from', 'to'
        properties: CSS properties (e.g., opacity=0, top='10px')
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
        """
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
        """
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
        declaration_name = f"@keyframes {self.name} "
        if self.animation_body:
            return f"{declaration_name}{{ {self.animation_body} }}"
        frames = ""
        for step, props in self.frames.items():
            frames += f" {step} {props}"

        return f"{declaration_name} {{{frames}}}"


class MediaQueries:
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
