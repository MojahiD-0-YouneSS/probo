from probo.components.state.component_state import (
    ElementState,
)
from probo.components.tag_functions.block_tags import (
    form,
    div,
    button,
    textarea,
    select,
    fieldset,
    legend,
    datalist,
    output,
    optgroup,
    label,
    option,
)
from probo.components.tag_functions.self_closing import (
    Input,
)
from probo.request.transformer import (
    FormHandler,
    RequestDataTransformer,
)
from typing import (
    Any,
    Optional,
)


def get_widget_info(django_bound_field) -> dict[str, str]:
    """
    Analyzes a Django BoundField and returns a clean dictionary
    of tag type, attributes, and values.
    """
    widget = django_bound_field.field.widget
    attrs = dict(widget.attrs)

    # 1. Base Attributes
    attrs["name"] = django_bound_field.html_name
    attrs["id"] = django_bound_field.id_for_label

    # 2. Value Handling
    val = django_bound_field.value()
    if val is not None:
        attrs["value"] = val

    # 3. Required Handling
    if django_bound_field.field.required:
        attrs["required"] = True

    # 4. Tag Determination logic
    tag = "input"
    choices = []

    # Check for Select
    if getattr(widget, "allow_multiple_selected", None) is not None:
        tag = "select"
        choices = getattr(widget, "choices", [])
        if widget.allow_multiple_selected:
            attrs["multiple"] = True

    # Check for Textarea
    elif widget.__class__.__name__ == "Textarea":
        tag = "textarea"
        # Textarea content is value, not attribute
        if "value" in attrs:
            del attrs["value"]

    # Check for Input Type
    elif hasattr(widget, "input_type"):
        attrs["type"] = widget.input_type

    return {
        "tag": tag,
        "attrs": attrs,
        "value": val,
        "choices": choices,
        "label": django_bound_field.label,
        "errors": list(django_bound_field.errors),
    }


class ProboFormField:
    """
    A declarative renderer for individual form fields.
    Bridging Django BoundFields with probo Elements.

    This class handles the extraction of widget attributes (type, class, choices)
    from Django fields and renders them into semantic HTML using probo's functional tags.
    It supports both automatic extraction (from Django) and manual declaration (for static forms).

    Args:
        tag_name (str, optional): The HTML tag name (e.g., 'input', 'select', 'textarea').
        field_label (str, optional): The text label for the field. Defaults to "".
        content (str, optional): Inner content for the element (used for textareas or custom containers). Defaults to "".
        dj_field (BoundField, optional): A Django BoundField object. If provided, attributes are extracted automatically.
        **attrs: Additional HTML attributes (e.g., id, class, placeholder, required).

    Attributes:
        info (dict): The normalized dictionary containing tag type, attributes, value, and choices.

    Example:
        >>> # Automatic (Django)
        >>> mff = ProboFormField(dj_field=form['username'])
        >>>
        >>> # Manual
        >>> mff = ProboFormField(
        ...     tag_name='input',
        ...     type='email',
        ...     name='email',
        ...     field_label='Email Address'
        ... )
        >>> print(mff.render())
       <label>Email Address</label><input type="email" name="email"/>
    """

    def __init__(
        self,
        tag_name: str = None,
        field_label: str = "",
        content: str = "",
        label_attr:dict[str,str]=None,
        dj_field=None,
        wraper_func=None,
        **attrs: dict[str, str],
    ):
        self.content = content
        self.wraper_func = wraper_func
        self.field_label = field_label
        self.attrs = attrs
        self.label_attr = label_attr or {}
        self.tag_name = tag_name
        self.widget_info: dict[str, str] = dict()
        self.form_field = str()
        self.dj_field = None
        self.dj_field_info = dict()
        self.dj_field = (dj_field,)
        if dj_field:
            self.include_dj_field(dj_field)

        if tag_name:
            info = self._make_info(
                self.attrs, self.field_label, {"for": attrs.get("id", None),**self.label_attr}, content
            )
            self._field_build(tag_name, **info)

    def _make_info(
        self,
        attrs: dict[str, str],
        label_string: str,
        label_attr: dict[str, str],
        content: str = None,
    ) -> dict[str, str]:
        return {
            "attrs": {k.lower().replace("_", "-"): v for k, v in attrs.items()},
            "label_string": label_string,
            "label_attr ": label_attr,
            "content": content,
        }

    def _field_build(self, tag: str, **info):
        tag_info_dict = {
            "input": {"method": Input, "void": True},
            "textarea": {"method": textarea, "void": False},
            "select": {"method": select, "void": False},
            "fieldset": {"method": fieldset, "void": False},
            "datalist": {"method": datalist, "void": False},
            "output": {"method": output, "void": False},
        }
        valid_tag = tag in tag_info_dict
        if valid_tag:
            tag_method = tag_info_dict[tag]["method"]
            tag_void = tag_info_dict[tag]["void"]
            tag_content = info.get("content", None)
            tag_attrs = {x: y for x, y in info["attrs"].items()}
            input_id = info["attrs"].get("id", None)
            label_string = info.get("label_string", None)
            tag_string = (
                tag_method(**tag_attrs)
                if tag_void
                else tag_method(tag_content, **tag_attrs)
            )
            if not label_string:
                self.widget_info[f"{input_id}-{tag}"] = self.wraper_func(tag_string) if callable(self.wraper_func) else tag_string
            else:
                label_attrs = info.get("label_attrs", {}) or {}
                if not label_attrs and input_id:
                    label_attrs["for"] = input_id
                self.widget_info[f"{input_id}-{tag}"] = (
                    self.wraper_func(label(label_string, **label_attrs) + tag_string) if callable(self.wraper_func) else label(label_string, **label_attrs) + tag_string
                )
        return self

    def include_dj_field(self, dj_field):
        if hasattr(dj_field, "field") and hasattr(dj_field.field, "widget"):
            field_info = get_widget_info(dj_field)
            tag = field_info["tag"]
            self.dj_field_info[tag] = field_info

            dj_attrs = self.dj_field_info[tag]["attrs"]
            dj_label = self.dj_field_info[tag]["label"]
            info = self._make_info(
                dj_attrs,
                dj_label,
                {"for": dj_attrs.get("id", None)},
            )
            self._field_build(tag, **info)
        else:
            raise ValueError("MFF expects a Django Field or a Dict.")
        self.dj_field = (dj_field,)
        return self

    def add_input(
        self,
        label_string: str = None,
        label_attrs: dict[str, str] = None,
        **input_attrs,
    ):
        """
        <label for="xyz">...</label>
        <input type="..." id="xyz" name="xyz">
        if
        """
        info = self._make_info(
            input_attrs,
            label_string,
            label_attrs,
        )

        return self._field_build("input", **info)

    def add_textarea(
        self,
        textarea_content: str = None,
        label_string: str = None,
        label_attrs: dict[str, str] = None,
        **textarea_attrs,
    ):
        _defaults = {
            "textarea_rows": 8,
            "textarea_cols": 50,
        }
        _defaults.update(textarea_attrs)
        info = self._make_info(_defaults, label_string, label_attrs, textarea_content)

        return self._field_build("textarea", **info)

    def add_select_option(
        self,
        option_values: list[str],
        selected_options_indexes: list[int] = None,
        label_string: str = None,
        label_attrs: dict[str, str] = None,
        **select_attrs,
    ):
        """option"""
        content = " ".join(
            [
                option(y, value=y, selected=True)
                if x in selected_options_indexes
                else option(y, value=y)
                for x, y in enumerate(option_values)
            ]
        )

        info = self._make_info(select_attrs, label_string, label_attrs, content)

        return self._field_build("select", **info)

    def add_select_optgroup(
        self,
        optgroups: dict[str, list[str]],
        selected_options_indexes: list[int] = None,
        label_string: str = None,
        label_attrs: dict[str, str] = None,
        **select_attrs,
    ):
        """option"""

        optgroup_content = []
        for x, y in enumerate(optgroups.values()):
            optgroup_content.append(
                "".join(
                    [
                        option(v, value=v, selected=True)
                        if x in selected_options_indexes
                        else option(v, value=v)
                        for v in y
                    ]
                )
            )
        content = "".join(
            [
                optgroup(k, **{"label": v})
                for k, v in zip(optgroup_content, optgroups.keys())
            ]
        )
        info = self._make_info(select_attrs, label_string, label_attrs, content)

        return self._field_build("select", **info)

    def add_field_set(
        self,
        legend_content: str,
        form_elements: list[str],
        label_string: str = None,
        label_attrs: str = None,
        **fieldset_attrs,
    ):
        content = "".join([legend(legend_content), *form_elements])
        info = self._make_info(fieldset_attrs, label_string, label_attrs, content)

        return self._field_build("fieldset", **info)

    def add_data_list(
        self,
        option_value_list: list[str],
        label_string: str = None,
        label_attrs: dict[str, str] = None,
        **data_list_attrs,
    ):
        content = "".join([option(value=k) for k in option_value_list])

        info = self._make_info(data_list_attrs, label_string, label_attrs, content)

        return self._field_build("datalist", **info)

    def add_output(
        self,
        label_string: str = None,
        label_attrs: dict[str, str] = None,
        **output_attrs,
    ):
        info = self._make_info(output_attrs, label_string, label_attrs)

        return self._field_build("output", **info)

    def add_custom_field(self,*field_string,skip_wraper=False):
        field_string = ''.join(field_string)
        if skip_wraper:
            self.widget_info['custm-field'] = field_string
        else:
            self.widget_info['custm-field'] = self.wraper_func(field_string) if callable(self.wraper_func) else field_string
        return self

    def render(
        self,
    ) -> str:
        fields = ""
        if self.widget_info:
            fields = "".join(self.widget_info.values())
        state_error = {
            "field_errors": "",
        }
        if self.dj_field_info:
            tag = list(self.dj_field_info.keys())[0]
            if tag:
                err_list = [
                    div(str(e), Class="invalid-feedback")
                    for e in self.dj_field_info[tag]["errors"]
                ]
                errors_html = div(*err_list, Class="errors")
                state_error = {
                    "field_errors": errors_html,
                }
        errors = ElementState("div", s_state="field_errors")
        error_string = (
            errors.change_state(
                state_error,
            ).state_placeholder
            or str()
        )
        self.form_field = fields + error_string
        return fields


class ProboForm:
    """
    The orchestrator for rendering HTML forms.
    Manages CSRF tokens, field iteration, and validation integration.

    This class acts as the bridge between Django's backend form handling (via RDT)
    and probo's frontend rendering. It supports both automatic rendering of Django forms
    and manual construction of forms for static sites or other frameworks.

    Args:
        action (str): The URL to submit the form to (e.g., "/login/").
        *form_field_declarations (tuple[ProboFormField]): Variable length list of manual field declarations.
        request_data (RequestDataTransformer, optional): The RDT instance wrapping the Django request. Required for auto-magic mode.
        method (str, optional): HTTP method (e.g., "post", "get"). If None, defaults based on context.
        manual (bool, optional): If True, bypasses RDT and uses manually provided fields/tokens. Defaults to False.
        use_htmx (bool, optional): If True, prepares the form for HTMX injection. Defaults to True.
        form_class (Any, optional): The Django Form class (used for validation logic if RDT is present).
        form_declaration (Optional[str], optional): Optional identifier or string representation for the form declaration.
        csrf_token (str, optional): Manual CSRF token string. Used if RDT is missing or in manual mode.

    Attributes:
        handler (FormHandler): The business logic handler for saving/validating data.

    Example:
        >>> # Django Mode (Auto)
        >>> rdt = RequestDataTransformer(request, MyForm)
        >>> form = ProboForm(action=".", request_data=rdt)
        >>> html = form.render()
        >>> # Manual Mode
        >>> email_field = ProboFormField("input", 'email to contact with',Type="email",value="",name="email",)
        >>> form = ProboForm("/search",email_field, method="get", manual=True, csrf_token="xyz")
        >>> html = form.render()
        >>> html -> <form action="/search"  method="get"><input type="hidden" value="xyz"/><label for="email">email to contact with</label><input type="email" name="email" value=""/>
    """

    def __init__(
        self,
        action: str,
        *form_field_declarations: tuple[ProboFormField],
        request_data: Optional[RequestDataTransformer] = None,
        method: str = None,
        manual: bool = False,
        use_htmx: bool = True,
        form_class: Any = None,
        form_declaration: Optional[str] = None,
        override_button=False,
        override_button_attrs=None,
        csrf_token: str = None,
            **attrs
    ):
        self.form_class = form_class
        self.request_data = request_data
        self.request_form_bool: bool = bool(request_data)
        self.is_handled = False
        self.use_htmx = use_htmx
        self.method = method if method else request_data.request_method if request_data else 'GET'
        self.action = action
        self.attrs={'action': self.action,
             'method': self.method.lower(),
             'enctype': "multipart/form-data",
             }
        self.attrs.update(attrs)
        self.override_button =override_button
        self.override_button_attrs =override_button_attrs
        self.handler = None
        self.is_valid = False
        self.form_declaration = form_declaration
        self.manual = manual
        self.submit_btn = None
        self._manual_csrf = csrf_token
        self.fields = form_field_declarations
        if not manual and self.request_data:
            self.form_class = (
                self.request_data.form_class if not self.form_class else self.form_class
            )

    def get_csrf_token(self):
        if self._manual_csrf:
            return self._manual_csrf
        if self.request_data:
            return self.request_data.get_csrf_token()
        return ""

    def render(
        self,
    ):
        token = self.get_csrf_token()
        csrf_field = Input(type="hidden", name="csrfmiddlewaretoken", value=token)
        fields_html = list(self.fields)
        if self.request_data and self.request_data.form:
            # Iterate over the Django Form Fields
            for field in self.request_data.form:
                # Wrap each Django field in MFF and render
                mff = ProboFormField(dj_field=field)
                fields_html.append(mff.render())
        if self.form_declaration:
            fields_html.append(self.form_declaration)
        submit_btn=''
        if not self.override_button :
            if self.override_button_attrs:
                submit_btn = button("Submit", **self.override_button_attrs)
            else:
                submit_btn = button("Submit", type="submit", Class="btn btn-lg")

        return form(
            csrf_field,
            *fields_html,
            submit_btn,
             **self.attrs,# Safe default

        )

    def save_to_db(
        self,
    ):
        if self.request_form_bool:
            self.handler = FormHandler(self.request_data)
            self.is_handled = self.handler.form_handling()
        return self.is_handled
