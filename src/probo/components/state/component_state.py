from probo.components.state.props import StateProps
from probo.components.elements import Element
from probo.components.attributes import ElementAttributeValidator
import re
from typing import Any, Self


class ComponentState:
    """
    The 'Brain' of the component system.
    Manages data storage (static/dynamic), logic gates (props), and data distribution to elements.

    It acts as a container for data and a controller for the rendering lifecycle.
    It resolves which data source (static vs dynamic) to use for each element and
    enforces security requirements via props validation.

    Args:
        s_data (dict[str, Any]): Static data dictionary (defaults/fallbacks).
        d_data (dict[str, Any], optional): Dynamic data dictionary (live data). Defaults to None.
        *elements_states (tuple[ElementState]): Variable list of child ElementState objects managed by this state.
        incoming_props (dict[str, Any], optional): Global context/props passed from the parent/view. Defaults to None.
        strict (bool, optional): If True, raises errors when required data keys are missing. Defaults to False.
        **props (dict[str, Any]): Local property requirements (e.g., requirement check against incoming_props).

    Attributes:
        resolved_state_elements (dict): Map of state_id to resolved ElementState after processing.
        state_errors (str): Error message if validation fails.

    Example:
        >>> # Define elements
        >>> es = ElementState('h1', s_state='title')
        >>>
        >>> # Define State
        >>> state = ComponentState(
        ...     {'title': 'Hello World'},
        ...     {'title': 'Live Update'}, # d_data takes precedence
        ...     es,
        ...     strict=True
        ... )
        ... print(state.resolve_template(es.placeholder))
            <h1>Live Update</h1>
    """

    def __init__(
        self,
        *elements_states: tuple["ElementState"],
        s_data: dict[str, Any] = None,
        d_data: dict[str, Any] = None,
        incoming_props: dict[str, Any] = None,
        strict: bool = False,
        **props: dict[str, Any],
    ) -> None:
        self.s_data = s_data or {}
        self.d_data = d_data or {}
        self.elements_states = elements_states
        self.resolved_state_elements = {}
        self.props = props
        self.strict = strict
        self.state_errors = None
        self.incoming_props = incoming_props or {}
        if elements_states:
            self.use_state()

    def _determine_state(self, s_el, d_el) -> tuple[dict[str, str]]:
        """
        generator from data available
        """
        s_value = self.s_data.get(s_el, None)
        d_value = self.d_data.get(d_el, None)
        if self.strict:
            if not d_value and not s_value:
                raise KeyError(
                    "[probo Strict] key  missing in d_data (and no static fallback)."
                )
        return {s_el: s_value}, {d_el: d_value}

    def resolve_props(self, prop: tuple[dict[str, str]]) -> dict[str, Any] | None:
        """Decides priority: Dynamic > Static."""
        static_dict, dynamic_dict = prop
        s_val = list(static_dict.values())[0]
        d_val = list(dynamic_dict.values())[0]
        if d_val is not None and d_val:
            return dynamic_dict
        elif s_val is not None and s_val:
            return static_dict
        else:
            return None

    def validate_global_props(self) -> bool:
        """
        Checks if local requirements (self.props) match the global context (incoming_props).
        Returns True if valid, False if mismatch found.
        """
        if not self.props:
            return True  # No requirements, always valid
        if not self.props and not self.incoming_props:
            return True  # No requirements, always valid

        if not self.incoming_props:
            # Requirements exist, but no global props provided -> Fail
            self.state_errors = "Missing Global Context"
            if self.strict:
                raise ValueError(f"[probo Strict] {self.state_errors}")
            return False

        for key, required_value in self.props.items():
            # 1. Check Existence
            if key not in self.incoming_props:
                self.state_errors = f"Missing required prop: '{key}'"
                if self.strict:
                    raise ValueError(f"[probo Strict] {self.state_errors}")
                return False

            # 2. Check Value Match
            # We assume strict equality here. You can relax this if needed.
            if self.incoming_props[key] != required_value:
                self.state_errors = (
                    f"Prop Mismatch for '{key}': "
                    f"Expected '{required_value}', got '{self.incoming_props[key]}'"
                )
                return False

        return True

    def use_state(
        self,
    ) -> Self:
        """
        Replace <$ s="..." d='None' i='None'>...</$> in children content with dynamic slot content
        """
        self.validate_global_props()
        if self.state_errors and self.strict:
            raise ValueError(f"[probo Strict]⚠️ Rendering Blocked: {self.state_errors}")

        for el in self.elements_states:
            data = self._determine_state(el.s_state, el.d_state)
            rsolved_data = self.resolve_props(data)
            if rsolved_data:
                resolved_el = el.change_state(rsolved_data, props=self.incoming_props)
                self.resolved_state_elements[el.state_id] = resolved_el
            else:
                self.resolved_state_elements[el.state_id] = el
        return self

    def remove_state_tag(self, markup: str) -> str:
        """
        Removes all <$ ... > ... </$> state tags and keeps everything else intact.
        """
        pattern = r"<\$\s[^>]*>(.*?)</\$>"
        return re.sub(pattern, r"\1", markup, flags=re.DOTALL)

    def resolved_template(self, template: str) -> str:
        self.use_state()

        for k, el in self.resolved_state_elements.items():
            if el.placeholder in template:
                if el.state_placeholder is None or self.state_errors:
                    # template = template.replace(el.placeholder, '')
                    template = re.sub(re.escape(el.placeholder), "", template)
                else:
                    # template = template.replace(el.placeholder, el.state_placeholder)
                    template = re.sub(
                        re.escape(el.placeholder), el.state_placeholder, template
                    )

        return self.remove_state_tag(template)


class ElementState:
    """
    The 'Neuron' of the system.
    Defines how a specific HTML element binds to data and behaves under different conditions.

    It handles data resolution (choosing between static/dynamic sources),
    attribute binding (injecting data into attributes like 'href'),
    and logic gates (hiding if requirements aren't met).

    Args:
        element (str): The HTML tag name (e.g., 'div', 'span').
        s_state (str, optional): Key to look up in s_data. Defaults to "".
        d_state (str, optional): Key to look up in d_data. Defaults to None.
        c_state (str, optional): Constant content or fallback key. Defaults to "" (used when binding).
        is_custom (bool, optional): If True, bypasses standard HTML attribute validation. Defaults to False.
        props (StateProps, optional): Logic gate rules for visibility. Defaults to None.
        bind_to (str, optional): HTML attribute to inject resolved data into (e.g., 'src', 'href'). Defaults to None.
        inner_html (Callable, optional): A function defined by user to define inner html thus passing the data before rendering. Defaults to None.
        i_state (bool, optional): If True, treats resolved data as iterable and renders a list. Defaults to False.
        hide_dynamic (bool, optional): If True and d_state is missing, hides the element completely. Defaults to False.
        is_void_element (bool, optional): If True, renders as a self-closing tag. Defaults to False.
        **attrs: Static HTML attributes for the element (e.g., Class='btn').

    Attributes:
        placeholder (str): The unique <$ ... $> string used in templates.
        state_id (str): Unique UUID for this element state.

    Example:print
        >>> # Simple text binding
        >>> es = ElementState('span', d_state='username')
        >>>
        >>> # Attribute binding
        >>> es_link = ElementState('a', d_state='url', bind_to='href', c_state='Click Me')
        >>>
        >>> # List rendering
        >>> es_list = ElementState('li', d_state='items', i_state=True)
    """

    def __init__(
        self,
        element,
        s_state: str = str(),
        d_state: str = None,
        c_state=str(),
        is_custom=False,
        props: StateProps = None,
        bind_to=None,
        inner_html=None,
        i_state=False,
        hide_dynamic=False,
        is_void_element: bool = False,
        key_as_content=False,
        **attrs,
    ):
        import uuid

        self.state_id = f"{element}=={uuid.uuid4().hex}"
        self.placeholder = (
            Element()
            .custom_element(
                "$",
                content=Element()
                .custom_element(element, str(s_state), is_void_element, **attrs)
                .element,
                s=s_state,
                d=d_state,
                c=c_state,
                i=bool(i_state),
            )
            .element
        )  # <$ s="..." d='None' i='None'>...</$>
        self.state_placeholder = None
        self.element = element
        self.s_state = s_state
        self.d_state = d_state
        self.c_state = c_state if c_state else None
        self.i_state = bool(i_state)
        self.attrs = (
            {k.lower().replace("_", "-"): v for k, v in attrs.items()} if attrs else {}
        )
        self.props = props or StateProps()
        self.props.element_state_id = self.state_id
        self.is_void_element = is_void_element
        self.hide_dynamic = hide_dynamic
        self.bind_to = bind_to
        self.is_custom = is_custom
        self.key_as_content = key_as_content
        self.inner_html = (
            inner_html
            if callable(inner_html)
            else lambda x: str(x) if not isinstance(x, tuple) else str(x[1])
        )
        if not self.is_custom:
            # Check if static attrs passed in __init__ are valid
            self.valid_element = ElementAttributeValidator(
                f"<{self.element}>", **self.attrs
            ).is_valid
        else:
            self.valid_element = True

    def change_state(self, data: dict[str, str], props=dict()):
        if not self.props.validator(props).is_valid() or not self.valid_element:
            self.state_placeholder = None
        else:
            if not self.is_void_element:
                if self.bind_to and (
                    not self.c_state or self.bind_to not in self.attrs
                ):
                    self.state_placeholder = None
                else:
                    if self.key_as_content and not data:
                        key = self.d_state if self.d_state else self.s_state
                        print(key)
                        if not key:
                            self.state_placeholder = None
                        if self.i_state:
                                self.state_placeholder = "".join(
                                    [
                                        Element()
                                        .custom_element(
                                            self.element, self.inner_html(d), **self.attrs
                                        )
                                        .element
                                        for d in enumerate(key)
                                    ]
                                )
                        else:
                            self.state_placeholder = Element().custom_element(
                                            self.element, self.inner_html(key), **self.attrs
                                        ).element
                    else:
                        if self.hide_dynamic and self.d_state and self.d_state not in data:
                            self.state_placeholder = None
                        elif self.d_state and self.d_state in data:
                            if self.i_state:
                                self.state_placeholder = "".join(
                                    [
                                        Element()
                                        .custom_element(
                                            self.element, self.inner_html(d), **self.attrs
                                        )
                                        .element
                                        for d in enumerate(data.get(self.d_state))
                                    ]
                                )
                            else:
                                self.state_placeholder = (
                                    Element()
                                    .custom_element(
                                        self.element,
                                        self.inner_html(self.c_state),
                                        **self.bind_data_to(str(data.get(self.d_state))),
                                    )
                                    .element
                                    if self.bind_to
                                    else Element()
                                    .custom_element(
                                        self.element,
                                        self.inner_html(data.get(self.d_state)),
                                        **self.attrs,
                                    )
                                    .element
                                )
                        elif self.s_state in data:
                            if self.i_state:
                                self.state_placeholder = "".join(
                                    [
                                        Element()
                                        .custom_element(
                                            self.element, self.inner_html(s), **self.attrs
                                        )
                                        .element
                                        for s in enumerate(data.get(self.s_state))
                                    ]
                                )
                            else:
                                self.state_placeholder = (
                                    Element()
                                    .custom_element(
                                        self.element,
                                        self.inner_html(self.c_state),
                                        **self.bind_data_to(str(data.get(self.s_state))),
                                    )
                                    .element
                                    if self.bind_to
                                    else Element()
                                    .custom_element(
                                        self.element,
                                        self.inner_html(data.get(self.s_state)),
                                        **self.attrs,
                                    )
                                    .element
                                )
                        else:
                            self.state_placeholder = None
            else:
                target_value = data.get(self.s_state) or data.get(self.d_state)
                self.state_placeholder = (
                    Element()
                    .custom_element(
                        self.element, **self.bind_data_to(str(target_value))
                    )
                    .element
                    if self.bind_to
                    else Element()
                    .custom_element(
                        self.element, is_void_element=self.is_void_element, **self.attrs
                    )
                    .element
                )
        return self

    def bind_data_to(self, target_value):
        if self.bind_to is None:
            return self.attrs
        else:
            if self.bind_to in self.attrs:
                render_attrs = self.attrs.copy()
                render_attrs[self.bind_to] = target_value

                return render_attrs
            return self.attrs

    def render(self, **data) -> str | None:
        return self.change_state(data).state_placeholder
