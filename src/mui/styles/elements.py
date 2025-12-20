from mui.styles.plain_css import (
    CssAnimatable, 
    CssRule, 
    CssSelector, 
)
from dataclasses import dataclass
from typing import List, Dict, Any,Union
from mui.styles.utils import resolve_complex_selector

class ComponentStyle:
    """
    A class to represent the css style of a Component object.
    args:
        template: a html representation to validate selectors against
        *css: the css is tuple of SelectorRuleBridge objects 
    
    """
    
    Css_rule= CssRule
    Css_animatable= CssAnimatable
    def __init__(self, template:str='',*css):
        self.template = template
        self.css_rules:tuple['SelectorRuleBridge'] = css
        self.template_representation = str()
        if template:
            self.template_info= CssSelector(self.template).template_info

    def link_component(self, cmp_str:str):
        self.template = cmp_str
        return self
    
    def render(self,as_string=True,with_style_tag=False):
        container= [self._validate_css(bridge)  for bridge in self.css_rules]
        if with_style_tag:  as_string=True
        self.template_representation = container
        if not as_string:
            return self.template_representation
        else:
            from mui.components.tag_functions.block_tags import style

            return ''.join(self.template_representation) if not with_style_tag else style(''.join(self.template_representation))

    def _validate_css(self, bridge):
        s,r = bridge.selector_str, bridge.rule.render()
        from mui.utility import exists_in_dict

        if '_$_' in s:
            
            if all([exists_in_dict(self.template_info, ss.strip('.').strip('#') )  for ss in s.split('_$_')]):
                selectors = ' '.join(s.split('_$_'))
            else:
                raise ValueError('invalid selectors')
        else:
            if exists_in_dict(self.template_info, s ):
                selectors = s
            else:
                raise ValueError('invalid selectors')
        #css_rules = f"{' '.join([ c for cr in self.css_rules])}"
        return f"{selectors} {r} \n"

def element_style(with_style_attr=False,**prop_val,):
    """A function to represent inline styles for an HTML element."""
    style_string= ' '.join([f'{k}:{v};' for k, v in CssRule(**prop_val).declarations.items()]) or ''
    if with_style_attr:
        return f'style="{style_string}"'
    else: return style_string

@dataclass
class SelectorRuleBridge:
    """
    
    The atomic unit of the Style Engine.
    Binds a specific Selector to a specific Rule definition and unifizes  CssSelectort and CssRule objects
    """
    selector:  Union[CssSelector, str]
    rule: CssRule
    def __post_init__(self):
        """
        Automatically runs after the object is created.
        Ensures self.selector is normalized to a CssSelector object.
        """
        self.make_selector_obj()
    @property
    def selector_str(self) -> str:
        """Helper to get the raw string for lxml/cssselect."""
        if hasattr(self.selector, 'render'):
            return self.selector.render()
        return str(self.selector)

    def make_selector_obj(self,)-> None:
        if isinstance(self.selector, str):
            sel_obj=CssSelector()
            for x in resolve_complex_selector(self.selector):
                sel_obj.add_selector(x)
            self.selector = sel_obj
        elif isinstance(self.selector, CssSelector):
            pass
        else:
            raise TypeError('selector must be str or CssSelector')
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
            return ''  # No styles to render
#f'{k.strip(':')}:{v.strip(';')};\n'.replace('_','-')
    @classmethod
    def make_bridge_list(cls, source: Dict) -> List['SelectorRuleBridge']:
        """
        Factory: Converts a User Dictionary into a Strict List of Bridges.
        Preserves insertion order (Python 3.7+ dicts are ordered).
        
        Input: { CssSelector('.btn'): CssRule(color='red') }
        Output: [SRB(selector=..., rule=...)]
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
                continue # Skip invalid
            if not isinstance(sel, CssSelector):
                sel_obj=CssSelector()
                for x in resolve_complex_selector(sel):
                    sel_obj.add_selector(x)
            else:continue
            # 2. Create Bridge
            bridges.append(cls(selector=sel_obj, rule=final_rule))
            
        return bridges

def _check_selector_in_template_re(selector: list[str], template: str) -> bool:
    """
    Uses RegEx to find if a simple selector (tag, id, or class)
    exists in the rendered HTML template string.
    """
    template_info= CssSelector(template).template_info
    # 1. ID selector (e.g., '#my-id')
    for key, value in template_info.items():
        if key in selector:
            return True
        # Check nested dict
        if isinstance(value, dict):
            # Check nested key or nested value
            #any([k in selector for k in value.keys()])  or 
            if any([all([s in v for s in  selector]) for v in value.values()]):
                return True
        else:
            return False
    return False

def element_style_state(
    template: str,
    rslvd_el: Dict[str, Any],   # Dict[str, ElementState]
    *css: SelectorRuleBridge,
):
    """
    Validate CSS selectors against the rendered template and element state.

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
        selector:List[str]  = [s.strip('.').strip('#').strip('[').strip(']') for s in resolve_complex_selector(sel.selector_str) if not s.startswith(':')]
        exists_in_template = _check_selector_in_template_re(selector, template)
        # Check if selector is managed in rslvd_el
        is_managed = any(
            [( all([s in x.attrs for s in selector]) or all([s in x.attrs.values() for s in selector])) if not x.props.display_it else True
            for x in rslvd_el.values()]
        ) if rslvd_el else True
# --- Case 2: ERROR THROWER ---
        if is_managed and not exists_in_template:
            continue  # skip it entirely
        if sel in css:
            valid_css.append(sel)
    return valid_css