from probo.components.elements import Element
from probo.components.state.component_state import (
    ComponentState,
)
from probo.components.base import ComponentAttrManager
from probo.styles.elements import (
    ComponentStyle,
    element_style_state,
    CssRule,
    CssSelector,
    SelectorRuleBridge,
)
from typing import Any, Self
from probo.templates.resolver import TemplateResolver


class Component:
    """
    The base class for all UI components in PROBO.
    Orchestrates state management, template rendering, and JIT CSS compilation.

    This class acts as the conductor, coordinating the Body (Template/Elements),
    the Brain (ComponentState), and the Skin (JIT CSS). It supports lifecycle
    hooks, skin swapping, and root element proxying.

    Args:
        name (str): Unique identifier for the component registry. Used for debugging and hydration.
        state (ComponentState, optional): The state manager containing static/dynamic data and logic gates.
        template (str, optional): The raw HTML string containing element state placeholders.
        props (dict, optional):  context or configuration properties passed to the component.
        **elements (dict): Child components or template fragments keyed by name.

    Attributes:
        name (str): The component's registry name.
        comp_state (ComponentState): The internal state manager.
        active_css_rules (List[CssRule]): The list of CSS rules currently applied.
        default_css_rules (List[CssRule]): The baseline CSS rules (used for resetting skins).

    Example:

        static:

            >>> # Define template
            >>> template_string = div(span('hello',strong('world!')),)
            >>>
            >>> # Define Component
            >>> comp = Component("UserBadge",template_string)
            >>>
            >>>  #set root element
            >>>  comp.set_root_element('section',Id='root',Class='root-class')
            >>>
            >>> # Apply Style
            >>> comp.load_css_rules(span=CssRule(font_weight="bold"))
            >>>
            >>> # Render
            >>> html, css = comp.render()
            >>> html -> <section id="root" class="root-class"><span>hello<strong>world!</strong></span></section>
            >>> css -> span {font-weight:bold;}

        state defined:
            >>> # Define State
            >>> es = ElementState('span', d_state='username')
            >>> template_string = div(span('User:',strong(es.placeholder)),)
            >>> state = ComponentState(d_data={'username': 'Admin'}, es)
            >>>
            >>> # Define Component
            >>> comp = Component("UserBadge", state=state, template=template_string)
            >>>
            >>> # Apply Style
            >>> comp.load_css_rules(span=CssRule(font_weight="bold"))
            >>>
            >>> # Render
            >>> html, css = comp.render()
            >>> html -> <section id="root" class="root-class"><span>User:<strong><span>Admin</span></strong></span></section>
            >>> css -> span {font-weight:bold;}
    """


    _registry = {}  # Global component registry

    def __init__(
        self,
        name: str,
        state: ComponentState = None,
        template: str = str(),
        props: dict = None,
        **elements,
    ):
        self.name: str = name
        self.index: int = 0

        self.children: dict[str, Any] = elements or {}
        self.children_info = {
            k: TemplateResolver(v).template_resolver() for k, v in elements.items()
        }
        self.attr_manager = ComponentAttrManager()
        if isinstance(template,str):
            self.template_obj = TemplateResolver(tmplt_str=template, load_it=True)
        else:
            self.template_obj = template

        self.is_root_element: bool = False
        self.root_element_tag = None
        self.root_element_attrs = {}

        self.props = props or {}
        self.comp_state = state or ComponentState()

        self.default_css_rules = list()
        self.active_css_rules = list()
        self.cmp_style = None

        self._registry[name] = self  # Auto-register

        self.on_init()

    def on_init(self):
        """Lifecycle Hook: Called after initialization. Override to add setup logic."""
        pass

    def before_render(self, **props):
        """Lifecycle Hook: Called before render. Override to modify state/props dynamically."""
        return self

    @classmethod
    def get(cls, name: str):
        """Retrieves a registered component by name."""
        return cls._registry.get(name)

    @classmethod
    def register(
        cls, name: str, state: ComponentState = None, props: dict = None, *elements
    ):
        """Registers a new component instance."""
        comp = cls(name=name, template="".join(elements), state=state, props=props)
        cls._registry[name] = comp
        return comp

    def set_root_element(self, root: str = "div", **attrs):
        """Defines a wrapper element for the component."""
        self.root_element_tag = root
        self.is_root_element = True
        self.root_element_attrs = attrs
        return self

    def add_root_class(self, class_name: str):
        """Adds a CSS class to the root element."""
        current = self.root_element_attrs.get("class", "")
        # simple check to avoid duplicates or extra spaces
        if class_name not in current.split():
            self.root_element_attrs["class"] = f"{current} {class_name}".strip()
        return self

    def set_root_id(self, element_id: str):
        """Sets the ID of the root element."""
        self.root_element_attrs["id"] = element_id
        return self

    def add_child(self, child: "str|Component", name: str = None):
        """Adds a child component or string content."""
        if child:
            if isinstance(child, type(self)):
                self.children.update({child.name: child.render()})
            elif isinstance(child, str) and name is not None:
                child_obj = TemplateResolver(
                    tmplt_str=child, load_it=True
                ).template_resolver()
                self.children[name] = child
                self.children_info[name] = child_obj
            else:
                raise ValueError("invalid child type or no name")

        return self

    def sub_component(self, component: Self):
        """Embeds another component inside this one."""

        render_result = component.render()
        if isinstance(render_result, tuple):
            html, _ = render_result
            # Note: You might want to bubble up the CSS here too,
            # but for now we just store HTML
            self.children.update({component.name: html})
            self.active_css_rules.update(component.active_css_rules)
        else:
            self.children.update({component.name: render_result})

        self.props.update(component.props)
        return self

    def render(
        self,
        override_props: dict = None,
        force_state: bool = False,
        add_to_global: bool = False,
    ) -> str | tuple:
        """
        Compiles the component into final HTML and CSS.

        Returns:
            tuple: (html_string, css_string) or str: html_string (if no CSS)
        """
        self.before_render(**(override_props or {}))

        if isinstance(override_props, dict):
            if add_to_global:
                self.props.update(override_props)
            if force_state:
                self.comp_state.props = override_props  # not quite
            else:
                self.comp_state.props.update(override_props)  # not quite
            self.comp_state.state_errors = None

        template = self.template_obj.render() if hasattr(self.template_obj,'render') else str(self.template_obj.tmplt_str)
        if self.children:
            template += "".join(list(self.children.values()))

        self.comp_state.incoming_props = self.props  # not quite

        final_template = str(self.comp_state.resolved_template(template))
        if self.is_root_element:
            final_template = Element(
                content=final_template, **self.root_element_attrs
            ).build_tag(
                self.root_element_tag,
            )
        if self.active_css_rules:
            valid_css = element_style_state(
                final_template,
                self.comp_state.resolved_state_elements,
                *self.active_css_rules,
            )
            self.cmp_style = ComponentStyle(final_template, *valid_css)
            return final_template, self.cmp_style.render()
        else:
            return final_template

    def change_skin(
        self,
        source: dict["str", Any] | Self = None,
        root_attr: str = None,
        root_attr_value: str = None,
        **root_css: dict["CssSelector", "CssRule"],
    ):
        """
        Applies a new skin (CSS rules) to the component.
        Supports Dictionaries, other Components, Theme lists, and Root kwargs.
        """
        new_rules = {}

        # --- CASE 1: Dictionary {selector: {prop: val}} ---
        if isinstance(source, dict):
            new_rules.update(source)

        # --- CASE 2: Component Inheritance ---
        elif hasattr(source, "active_css_rules") and isinstance(
            source.active_css_rules, list
        ):
            self.active_css_rules.extend(source.active_css_rules)
        # --- CASE 3: Root Inheritance (kwargs) ---
        if root_css:
            if root_attr:
                if self.root_element_attrs and root_attr not in self.root_element_attrs:
                    self.root_element_attrs[root_attr] = (
                        "true" if not root_attr_value else root_attr_value
                    )
                    new_rules[f"{self.root_element_tag}[{root_attr}]"] = root_css
            # Auto-detect if no explicit root_attr provided
            if not root_attr:
                if self.root_element_attrs:
                    if "id" in self.root_element_attrs:
                        root_attr = f"#{self.root_element_attrs['id']}"
                    elif "class" in self.root_element_attrs:
                        # root_attr the first class
                        root_attr = f".{self.root_element_attrs['class'].split()[0]}"

                # Fallback to tag
                if not root_attr and self.root_element_tag:
                    root_attr = self.root_element_tag

            new_rules[root_attr] = root_css

        # Set the new skin dictionary.
        # Note: We assign the DICT, not .values(), because render() calls .keys() on it.
        self.active_css_rules = SelectorRuleBridge.make_bridge_list(new_rules)
        return self

    def load_css_rules(self, **css):
        """Loads initial CSS rules into the component."""

        if css:
            self.default_css_rules.extend(SelectorRuleBridge.make_bridge_list(css))

        self.active_css_rules = self.default_css_rules.copy()
        return self
