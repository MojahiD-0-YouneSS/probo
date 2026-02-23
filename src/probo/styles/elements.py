from probo.styles.plain_css import (
    CssAnimatable,
    CssRule,
    CssSelector,
)
from dataclasses import dataclass
from typing import List, Dict, Any, Union
from probo.styles.utils import resolve_complex_selector


class ComponentStyle:
    """Manages scoped CSS styling with structural validation for Components.

    ComponentStyle acts as a bridge between the component's HTML structure 
    and its visual rules. It validates that CSS selectors target existing 
    elements within the provided template, preventing broken styles.

    Attributes:
        template (str): The HTML string representation of the component.
        css_rules (tuple): A collection of SelectorRuleBridge objects 
            defining the styling logic.
        template_info (dict): A pre-computed dictionary of selectors 
            extracted from the template for fast validation.

    Example:
        >>> style = ComponentStyle(my_html, SelectorRuleBridge(".card", my_rule))
        >>> style.render(with_style_tag=True)
    """

    Css_rule = CssRule
    Css_animatable = CssAnimatable
    __slots__ =(
        'template',
        'css_rules',
        'template_representation',
        'template_info',
    )
    def __init__(self, template: str = "", *css):
        self.template = template
        self.css_rules: tuple["SelectorRuleBridge"] = css
        self.template_representation = str()
        if template:
            self.template_info = CssSelector(self.template).template_info

    def link_component(self, cmp_str: str):
        """Binds a specific HTML representation to this style for validation.

        Allows for late-binding of structural templates. This is useful for 
        applying the same logic to different instances of a component or 
        updating the template before final CSS validation.

        Args:
            cmp_str (str): The HTML string representation of the component.

        Returns:
            Self: Returns the instance to allow for method chaining.
        """
        self.template = cmp_str
        return self

    def render(self, as_string=True, with_style_tag=False):
        """Serializes the CSS rules into a validated string or list.

        This method triggers the validation pipeline for every rule bridge. 
        If 'with_style_tag' is set, it automatically wraps the output in 
        Probo's standard <style> tags.

        Args:
            as_string (bool): If True, joins the rules into a single string.
                If False, returns the raw list of validated rule strings.
            with_style_tag (bool): If True, wraps the CSS in a <style> block.
                Forces as_string to be True.

        Returns:
            Union[str, List[str]]: The final CSS output or a list of rules.
        """
        container = [self._validate_css(bridge) for bridge in self.css_rules]
        if with_style_tag:
            as_string = True
        self.template_representation = container
        if not as_string:
            return self.template_representation
        else:
            from probo.components.tag_functions.block_tags import style

            return (
                "".join(self.template_representation)
                if not with_style_tag
                else style("".join(self.template_representation))
            )

    def _validate_css(self, bridge):
        """Internally validates a SelectorRuleBridge against the template.

        Checks the existence of CSS selectors within the template_info 
        dictionary. Supports compound selectors using the '_$_' delimiter, 
        which represents a CSS descendant selector (space).

        Logic:
            1. Splice selectors based on the '_$_' delimiter.
            2. Strip '.' and '#' to check class/ID existence in template_info.
            3. Raise ValueError if any part of the selector is missing.

        Args:
            bridge (SelectorRuleBridge): The bridge object connecting a 
                selector string to a CssRule.

        Returns:
            str: A formatted CSS rule string (e.g., ".card .title { color: red; }").

        Raises:
            ValueError: If a selector targets an element not found in 
                the provided template.
        """
        s, r = bridge.selector_str, bridge.rule.render()
        from probo.utility import exists_in_dict

        if "_$_" in s:
            if all(
                [
                    exists_in_dict(self.template_info, ss.strip(".").strip("#"))
                    for ss in s.split("_$_")
                ]
            ):
                selectors = " ".join(s.split("_$_"))
            else:
                raise ValueError("invalid selectors")
        else:
            if exists_in_dict(self.template_info, s):
                selectors = s
            else:
                raise ValueError("invalid selectors")
        # css_rules = f"{' '.join([ c for cr in self.css_rules])}"
        return f"{selectors} {r} \n"

def element_style(
    with_style_attr=False,
    **prop_val,
):
    """Generates inline CSS strings from Python keyword arguments.

    This utility converts Pythonic snake_case or standard CSS properties 
    into a semicolon-delimited string. It leverages the CssRule engine 
     to ensure declarations are formatted correctly.

    Args:
        with_style_attr (bool): If True, wraps the result in the HTML 
            'style=""' attribute syntax. Defaults to False.
        **prop_val: Arbitrary keyword arguments representing CSS 
            properties and their values (e.g., color="red", margin_top="10px").

    Returns:
        str: A formatted CSS string or a full HTML style attribute.

    Example:
        >>> element_style(color="blue", font_size="12px")
        'color:blue; font-size:12px;'
        
        >>> element_style(with_style_attr=True, display="flex")
        'style="display:flex;"'
    """
    style_string = (
        " ".join([f"{k}:{v};" for k, v in CssRule(**prop_val).declarations.items()])
        or ""
    )
    if with_style_attr:
        return f'style="{style_string}"'
    else:
        return style_string

@dataclass
class SelectorRuleBridge:
    """The atomic binding unit of the ProboUI Style Engine.

    SelectorRuleBridge unifies a target (CssSelector) with a declaration (CssRule). 
    It ensures structural integrity by normalizing string-based selectors into 
    objects and providing a consistent interface for the final CSS render.

    Attributes:
        selector (Union[CssSelector, str]): The CSS selector target. 
            Normalized to CssSelector during post-initialization.
        rule (CssRule): The declaration block containing CSS properties.
    """

    selector: Union[CssSelector, str]
    rule: CssRule

    def __post_init__(self):
        """Standardizes the selector input immediately after instantiation.
        
        This ensures that internal logic can always rely on the selector 
        having a '.render()' method and participating in validation.
        """
        self.make_selector_obj()

    @property
    def selector_str(self) -> str:
        """Returns the raw string representation of the selector.

        Used primarily for integration with lxml, cssselect, or standard 
        CSS output.
        """
        if hasattr(self.selector, "render"):
            return self.selector.render()
        return str(self.selector)

    def make_selector_obj(
        self,
    ) -> None:
        """Normalizes the selector attribute into a CssSelector instance.

        If the selector is a string, it uses 'resolve_complex_selector' to 
        break down compound strings into a structured object.

        Raises:
            TypeError: If the selector is neither a string nor a CssSelector.
        """
        if isinstance(self.selector, CssSelector):
            return None
        
        if isinstance(self.selector, str):
            sel_obj = CssSelector()
            for x in resolve_complex_selector(self.selector):
                sel_obj.add_selector(x)
            self.selector = sel_obj
        else:
            raise TypeError("selector must be str or CssSelector", self.selector)

    def render(self) -> str:
        """
        Renders the full CSS block for this bridge.
        Example: .btn { color: red; }
        """
        # CssRule.render_declarations() is assumed to return just the body "prop: val;"
        # If CssRule.render() includes selectors, we might need to adjust CssRule
        # or just use the rule's properties here.

        body = self.rule.render()
        if body:
            return f"{self.selector_str} {body}"
        else:
            return ""  # No styles to render

    # f'{k.strip(':')}:{v.strip(';')};\n'.replace('_','-')
    @classmethod
    def make_bridge_list(cls, source: Dict) -> List["SelectorRuleBridge"]:
        """Factory method to convert a dictionary into a list of Bridge objects.

        This is the primary entry point for bulk style definitions. It 
        automatically wraps dictionaries into CssRule objects and 
        string selectors into CssSelector objects.

        Args:
            source (Dict): A mapping of selectors to rule definitions.
                e.g., { ".btn": {"color": "red"}, "#id": my_rule_obj }

        Returns:
            List[SelectorRuleBridge]: A list of validated, ready-to-render bridges.
        """
        bridges = []

        for sel, rule_def in source.items():
            # 1. Normalize Rule
            # If user passed a dict {'color': 'red'}, wrap it in CssRule
            if isinstance(rule_def, dict):
                final_rule = CssRule(**rule_def)
            elif isinstance(rule_def, CssRule):
                final_rule = rule_def
            else:
                continue  # Skip invalid
            if not isinstance(sel, CssSelector):
                sel_obj = CssSelector()
                for x in resolve_complex_selector(sel):
                    sel_obj.add_selector(x)
            else:
                continue
            # 2. Create Bridge
            bridges.append(cls(selector=sel_obj, rule=final_rule))

        return bridges

def _check_selector_in_template_re(selector: list[str], template: str) -> bool:
    """
    Uses RegEx to find if a simple selector (tag, id, or class)
    exists in the rendered HTML template string.
    """
    template_info = CssSelector(template).template_info
    # 1. ID selector (e.g., '#my-id')
    for key, value in template_info.items():
        if key in selector:
            return True
        # Check nested dict
        if isinstance(value, dict):
            # Check nested key or nested value
            # any([k in selector for k in value.keys()])  or
            if any([all([s in v for s in selector]) for v in value.values()]):
                return True
        else:
            return False
    return False

def element_style_state(
    template: str,
    rslvd_el: Dict[str, Any],  # Dict[str, ElementState]
    *css: SelectorRuleBridge,
):
    """Applies and validates styles based on the resolved state of a template.

    This function acts as a state-aware style applicator. It cross-references 
    provided SelectorRuleBridge objects against the resolved element states 
    to ensure that dynamic styling logic remains consistent with the 
    underlying HTML structure.

    Args:
        template (str): The HTML string template to be styled.
        rslvd_el (Dict[str, Any]): A dictionary mapping element selectors 
            to their current State objects (ElementState).
        *css (SelectorRuleBridge): A variable number of bridge objects 
            defining the target selectors and their corresponding rules.

    Returns:
        str: The rendered CSS string block for the state-specific styles.

    Cases:
        Case 2 (Error Thrower):
            - Selector state is managed (in rslvd_el)
            - BUT selector does NOT exist in final template
            → Skip it.

        Case 1:
            - Managed AND present in template
            → Keep it

        Case 3:
            - Not managed
            → Keep it
    """
    # Pair selectors with css blocks
    # selectors: ("h1.big", "a.btn")
    # css: {"h1_big": {"color":"red"}, "a_btn": {"font":"12px"}}

    valid_css = []
    for sel in css:
        selector: List[str] = [
            s.strip(".").strip("#").strip("[").strip("]")
            for s in resolve_complex_selector(sel.selector_str)
            if not s.startswith(":")
        ]
        exists_in_template = _check_selector_in_template_re(selector, template)
        # Check if selector is managed in rslvd_el
        is_managed = (
            any(
                [
                    (
                        all([s in x.attrs for s in selector])
                        or all([s in x.attrs.values() for s in selector])
                    )
                    if not x.props.display_it
                    else True
                    for x in rslvd_el.values()
                ]
            )
            if rslvd_el
            else True
        )
        # --- Case 2: ERROR THROWER ---
        if is_managed and not exists_in_template:
            continue  # skip it entirely
        if sel in css:
            valid_css.append(sel)
    return valid_css
