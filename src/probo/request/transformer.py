from probo.request.props import RequestProps
from typing import Any, Dict, List, Optional
class RequestDataTransformer:
    """RequestDataTransformer or RDT is a class that parses and extracts contents from django  request object ,also supports form hundling
    args:
        request : the django request object
        form_class: the form class definition
        request_files: indicates support for files and media, can be list or single class
        mono_form: indicates if only one form or multiple
    example:
        >>> # single form
        >>> from .forms import ExampleModelForm
        >>> def example_view(request,)
        >>>     rdt = RequestDataTransformer(request,ExampleModelForm)
        >>>     if rdt.request_method == 'POST':
        >>>         if rdt.is_valid():
        >>>             rdt.save_form()
        >>>
        >>>
        >>>
        >>> # multiform
        >>> from .forms import (ExampleModelForm1,ExampleModelForm2,ExampleModelForm3,ExampleModelForm4,ExampleModelForm5,)
        >>> def example_view(request,)
        >>>     rdt = RequestDataTransformer(request,[ExampleModelForm1,ExampleModelForm2,ExampleModelForm3,ExampleModelForm4,ExampleModelForm5,],mono_form=False)
        >>>     if rdt.request_method == 'POST':
        >>>         if rdt.are_valid():
        >>>             rdt.save_forms()
    """

    def __init__(
        self, request=None, form_class=None, request_files=False, mono_form=True
    ):
        self.target_data = {}
        self.request = request
        self.form_class = form_class
        self.errors = {}
        self.cleaned_data = {}

        # BUGFIX: Move validations up so _initialize_multi_form_processing can use it
        self.validations = {}

        # Safe getattr fetching
        self.request_method = getattr(request, "method", "") or ""
        self.request_user = getattr(request, "user", dict()) or dict()
        self.mono_form = mono_form

        if mono_form:
            self.form = (
                form_class(
                    getattr(request, "POST", None), getattr(request, "FILES", None)
                )
                if form_class and request_files
                else (
                    form_class(getattr(request, "POST", None)) if form_class else None
                )
            )
        else:
            self.form = self._initialize_multi_form_processing()

        self.user_data = self._prepare_user_data()

        # BUGFIX: Ensure we explicitly check 'is not None' because hasattr returns True for POST=None
        self.request_files = (
            self._process_post_files()
            if getattr(request, "FILES", None) is not None
            else dict()
        )
        self.post_data = (
            self._process_post_data()
            if getattr(request, "POST", None) is not None
            else dict()
        )
        self.get_data = (
            self._process_get_data()
            if getattr(request, "GET", None) is not None
            else dict()
        )
        self.session_data = (
            self._get_all_session_data()
            if getattr(request, "session", None) is not None
            else dict()
        )

        self.id = self.session_data.get("session_key", None)

    def _process_get_data(self) -> dict[str, Any]:
        get_data_dict = {}
        for field, field_data in self.request.GET.items():
            if isinstance(field_data, list):
                if len(field_data) == 1:
                    get_data_dict[field] = field_data[0]
                else:
                    get_data_dict[field] = field_data
            else:
                get_data_dict[field] = field_data
        return get_data_dict

    def _process_post_data(self) -> dict[str, Any]:
        post_data_dict = {}
        for field, field_data in self.request.POST.items():
            if isinstance(field_data, list):
                if len(field_data) == 1:
                    post_data_dict[field] = field_data[0]
                else:
                    post_data_dict[field] = field_data
            else:
                post_data_dict[field] = field_data
        return post_data_dict

    def _process_post_files(self) -> dict[str, Any]:
        post_data_dict = {}
        for field, field_data in self.request.FILES.items():
            if isinstance(field_data, list):
                if len(field_data) == 1:
                    post_data_dict[field] = field_data[0]
                else:
                    post_data_dict[field] = field_data
            else:
                post_data_dict[field] = field_data
        return post_data_dict

    def save_form(self, **kwargs) -> bool:
        if self.is_valid():
            self.form.save(**kwargs)
            return self.form
        return not self.errors

    def is_valid(self) -> bool:
        if self.form and not self.form.is_valid():
            self.errors.update(**{self.form_class.__name__: self.form.errors.values()})

        if self.form and self.form.is_valid():
            self.cleaned_data.update(self.form.cleaned_data)

        return not self.errors

    def get_errors(self) -> dict[str, Any]:
        return self.errors

    def get_request_data(self, organized: bool = False) -> dict[str, Any]:
        return (
            {
                "cleaned_data": self.cleaned_data,
                "post_data": self.post_data,
                "self.get_data": self.get_data,
            }
            if organized
            else {
                **self.cleaned_data,
                **self.post_data,
                **self.get_data,
                **self.request_files,
            }
        )

    def _prepare_user_data(self) -> dict[str, Any]:
        # Safely handle user objects vs dictionaries
        if hasattr(self.request_user, "__dict__"):
            return self.request_user.__dict__
        elif isinstance(self.request_user, dict):
            return self.request_user
        return dict()

    def _get_all_session_data(self) -> dict[str, Any]:
        return dict(self.request.session)

    def set_session_data(self, key: str, value: Any) -> dict[str, Any]:
        self.request.session[key] = value
        self.request.session.modified = True
        self.session_data = self._get_all_session_data()
        return {key: value}

    def get_session_data(self, key: str, default: str | None = None) -> Any:
        return self.request.session.get(key, default)

    def update_session_data(self, key: str, update_func: callable) -> dict[str, Any]:
        if key in self.request.session:
            self.request.session[key] = update_func(self.request.session[key])
            self.request.session.modified = True
            self.session_data = self._get_all_session_data()
        return {key: self.request.session.get(key)}

    def delete_session_data(self, key: str) -> None:
        if key in self.request.session:
            del self.request.session[key]
            self.request.session.modified = True
            self.session_data = self._get_all_session_data()

    def extract_target_data(
        self,
        fields: list[str] | None = None,
        multi_value_fields: list[str] | None = None,
        is_json: bool = False,
    ) -> dict[str, Any]:
        if is_json:
            self.target_data = (
                self.request.json() if hasattr(self.request, "json") else {}
            )
        else:
            fields = fields or self.request.POST.keys()
            multi_value_fields = multi_value_fields or []

            for field in fields:
                if field in multi_value_fields:
                    values = self.request.POST.getlist(field)
                    self.target_data[field] = values if len(values) > 1 else values[0]
                else:
                    self.target_data[field] = self.request.POST.get(field)

        return self.target_data

    def clear_all_session_data(self) -> bool:
        self.session_data.clear()
        return True

    def get_field_value(self, field: str, default: str | None = None) -> Any:
        return self.post_data.get(field) if field in self.post_data else default

    def get_json_field_value(self, field: str, default: str | None = None) -> Any:
        if not hasattr(self.request, "json"):
            raise ValueError("Request does not contain JSON data.")
        json_data = self.request.json()
        return json_data.get(field, default)

    def has_field(self, field: str) -> bool:
        return field in self.post_data or (
            hasattr(self.request, "json") and field in self.request.json()
        )

    def _initialize_multi_form_processing(self) -> dict[str, Any]:
        form_instances = {}
        for form_class in self.form_class:
            prefix = form_class.__name__.lower()
            form_instance = form_class(
                getattr(self.request, "POST", None), prefix=prefix
            )
            form_instances[prefix] = form_instance
            if form_instance.is_valid():
                self.cleaned_data[prefix] = form_instance.cleaned_data
                self.errors[prefix] = None
                self.validations[prefix] = True
            else:
                self.errors[prefix] = form_instance.errors.values()
                self.validations[prefix] = False
                self.cleaned_data[prefix] = None
        return form_instances

    def are_valid(self) -> bool:
        all_valid = True
        for prefix, instance in self.validations.items():
            if not instance:
                all_valid = False
        return all_valid

    def save_forms(self) -> bool:
        if self.are_valid():
            # BUGFIX: self.form is a dictionary. Must iterate over .values()!
            for form in self.form.values():
                form.save(commit=False)
        return self.are_valid()

    def get_csrf_token(self) -> str:
        try:
            from django.middleware.csrf import get_token

            return get_token(self.request)
        except:
            return ""

    def extract_props(self) -> RequestProps:
        global_ctx = {
            "user": self.request_user,
            "is_authenticated": (
                self.request.user.is_authenticated
                if self.request and hasattr(self.request, "user")
                else False
            ),
            "session": self.session_data,
            "csrf_token": self.get_csrf_token(),
            "path": getattr(self.request, "path", ""),
            "request_method": self.request_method,
        }

        local_ctx = {
            "form": self.form,
            "errors": self.errors,
            "cleaned_data": self.cleaned_data,
            "raw_post_data": self.post_data,
            "raw_get_data": self.get_data,
            "is_valid": self.is_valid() if self.mono_form else self.are_valid(),
        }

        return RequestProps(global_context=global_ctx, local_context=local_ctx)


class FormHandler:
    """Orchestrates form validation and persistence logic within a view.

    This utility uses a `RequestDataTransformer` to decide whether to process 
    a single form ('mono') or a collection of forms. It provides a high-level 
    interface for views to execute 'save' operations without manually 
    handling validation checks.

    Attributes:
        request_data (RequestDataTransformer): The data source containing 
            the forms and their current state.
        logger_instance (Optional[Any]): Hook for attaching a logging utility 
            to track form success or failure.
    """
    __slots__ = (
        "request_data",
        "logger_instance",
        "logger_instance_message",
    )

    def __init__(self, request_data: RequestDataTransformer):
        self.request_data = request_data
        self.logger_instance = None
        self.logger_instance_message = None

    def form_handling(self) -> bool:
        if self.request_data.mono_form:
            return self.mono_form_true_option()
        else:
            return self.mono_form_false_option()

    def mono_form_true_option(self) -> bool:
        if self.request_data.is_valid():
            self.request_data.save_form()
            return True
        return False

    def mono_form_false_option(self) -> bool:
        if self.request_data.are_valid():
            self.request_data.save_forms()
            return True
        return False
