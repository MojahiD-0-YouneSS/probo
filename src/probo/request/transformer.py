from probo.request.props import RequestProps


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
        self.request_method = request.method if hasattr(request, "method") else str()
        self.request_user = request.user if hasattr(request, "user") else dict()
        self.mono_form = mono_form

        if mono_form:
            self.form = (
                form_class(request.POST, request.FILES)
                if form_class and request_files
                else (form_class(request.POST) if form_class else None)
            )
        else:
            self.form = self._initialize_multi_form_processing()

        self.user_data = (
            self._prepare_user_data() if hasattr(request, "user") else dict()
        )
        self.request_files = (
            self._process_post_files() if hasattr(request, "FILES") else dict()
        )
        self.post_data = (
            self._process_post_data() if hasattr(request, "POST") else dict()
        )
        self.get_data = self._process_get_data() if hasattr(request, "GET") else dict()
        self.session_data = (
            self._get_all_session_data() if hasattr(request, "session") else dict()
        )
        self.id = self.session_data.get("session_key", None)
        self.validations = {}
        # Initialize the form if a form_class is provided
        # Process target data fields as a dictionary of lists

    def _process_get_data(self):
        get_data_dict = {}
        for field, field_data in self.request.GET.items():
            if isinstance(field_data, list):
                if len(field_data) == 1:
                    get_data_dict[field] = field_data[
                        0
                    ]  # Single value, store as string
                else:
                    get_data_dict[field] = field_data  # Multiple values, store as list
            else:
                get_data_dict[field] = field_data  # Single value, store as string
        return get_data_dict

    def _process_post_data(self):
        post_data_dict = {}
        for field, field_data in self.request.POST.items():
            if isinstance(field_data, list):
                if len(field_data) == 1:
                    post_data_dict[field] = field_data[
                        0
                    ]  # Single value, store as string
                else:
                    post_data_dict[field] = field_data  # Multiple values, store as list
            else:
                post_data_dict[field] = field_data  # Single value, store as string
        return post_data_dict

    def _process_post_files(self):
        post_data_dict = {}
        for field, field_data in self.request.FILES.items():
            if isinstance(field_data, list):
                if len(field_data) == 1:
                    post_data_dict[field] = field_data[
                        0
                    ]  # Single value, store as string
                else:
                    post_data_dict[field] = field_data  # Multiple values, store as list
            else:
                post_data_dict[field] = field_data  # Single value, store as string
        return post_data_dict

    def save_form(self, **kwargs):
        if self.is_valid():
            self.form.save(**kwargs)
            return self.form
        return not self.errors

    def is_valid(self):
        """Validates the request form and ensures all target data fields are provided."""

        # Validate the form if it was provided
        if self.form and not self.form.is_valid():
            self.errors.update(**{self.form_class.__name__: self.form.errors.values()})

        # Check if each target data field has at least one value
        """for field, values in self.post_data.items():
            if not values:
                self.errors.update(f'{field}':f"Please select at least one option for '{field}'.")
        """
        # Populate cleaned_data with form data if the form is valid
        if self.form and self.form.is_valid():
            self.cleaned_data.update(self.form.cleaned_data)

        return not self.errors  # Returns True if there are no errors

    def get_errors(self):
        """Returns a list of validation errors."""
        return self.errors

    def get_request_data(self, organized=False):
        """
        Returns cleaned form data and target fields.

        Parameters:
        - organized: If True, returns a dictionary with cleaned and target data organized in separate keys.

        Returns: Dictionary of cleaned data and target fields.
        """
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

    def _prepare_user_data(self):
        return self.request_user.__dict__ if self.request else None

    def _get_all_session_data(self):
        """Retrieve all session data as a dictionary."""
        return dict(self.request.session)  # Convert session to a dictionary

    def set_session_data(self, key, value):
        """Sets a session variable."""
        self.request.session[key] = value
        self.request.session.modified = True  # Mark session as modified
        self.session_data = self._get_all_session_data()  # Update session_data

    def get_session_data(self, key, default=None):
        """Retrieves a session variable, returning a default if not found."""
        return self.request.session.get(key, default)

    def update_session_data(self, key, update_func):
        """Updates a session variable using a provided function."""
        if key in self.request.session:
            self.request.session[key] = update_func(self.request.session[key])
            self.request.session.modified = True
            self.session_data = self._get_all_session_data()  # Update session_data

    def delete_session_data(self, key):
        """Deletes a session variable if it exists."""
        if key in self.request.session:
            del self.request.session[key]
            self.request.session.modified = True
            self.session_data = self._get_all_session_data()

    def extract_target_data(self, fields=None, multi_value_fields=None, is_json=False):
        """
        Extracts data from the request. Supports both form data (default) and JSON payloads.
        :param fields: List of fields to retrieve. If None, retrieves all fields in the request.
        :param multi_value_fields: List of fields that may contain multiple values (e.g., checkboxes).
        :param is_json: If True, treats the request as containing JSON data.
        :return: Dictionary with extracted data.
        """
        if is_json:
            self.target_data = (
                self.request.json() if hasattr(self.request, "json") else {}
            )
        else:
            fields = fields or self.request.POST.keys()
            multi_value_fields = multi_value_fields or []

            for field in fields:
                if field in multi_value_fields:
                    # Get a list for fields that may contain multiple values
                    values = self.request.POST.getlist(field)
                    self.target_data[field] = values if len(values) > 1 else values[0]
                else:
                    self.target_data[field] = self.request.POST.get(field)

        return self.target_data

    def clear_all_session_data(
        self,
    ):
        """
        Clears specific session data by key, or clears all session data if no key is provided.
        """
        self.session_data.clear()
        return True

    def get_field_value(
        self,
        field,
        default=None,
    ):
        """
        Retrieves the value of a specific field from the request data.
        :param field: Field name to retrieve
        :param default: Default value if the field does not exist
        """
        return self.post_data.get(field) if field in self.post_data else default

    def get_json_field_value(self, field, default=None):
        """
        Retrieves a field's value from JSON data in the request.
        """
        if not hasattr(self.request, "json"):
            raise ValueError("Request does not contain JSON data.")
        json_data = self.request.json()
        return json_data.get(field, default)

    def has_field(self, field):
        """
        Checks if a field exists in the request data.
        """
        return field in self.post_data or (
            hasattr(self.request, "json") and field in self.request.json()
        )

    def _initialize_multi_form_processing(self):
        """
        Initializes data structures and validation status for each form class specified.
        """
        form_instances = {}
        for form_class in self.form_class:
            prefix = form_class.__name__.lower()
            form_instance = form_class(self.request.POST, prefix=prefix)
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

    def are_valid(self):
        """
        Checks if all forms are valid and updates error tracking.
        """
        all_valid = True
        for prefix, instance in self.validations.items():
            if not instance:
                all_valid = False
        return all_valid

    def save_forms(
        self,
    ):
        if self.are_valid():
            for form in self.form:
                form.save(commit=False)
        return self.are_valid()

    def get_csrf_token(self):
        try:
            from django.middleware.csrf import get_token

            return get_token(self.request)
        except:
            return ""

    def extract_props(self):
        """
        Separates data into Global Context (User/Session) and
        Local Context (Form/Data) for the TCM.
        """

        # 1. GLOBAL DATA (Context for all components)
        # This data is needed by Layouts, Navbars, User Menus, etc.
        global_ctx = {
            "user": self.request_user,
            "is_authenticated": self.request.user.is_authenticated
            if self.request
            else False,
            "session": self.session_data,
            "csrf_token": self.get_csrf_token(),  # Crucial for FormElement
            "path": self.request.path,
            "request_method": self.request_method,
        }

        # 2. LOCAL DATA (Specific to the component/form being rendered)
        # This data is needed by the specific FormElement or Content Component
        local_ctx = {
            "form": self.form,  # The specific form instance
            "errors": self.errors,  # Validation errors
            "cleaned_data": self.cleaned_data,
            "raw_post_data": self.post_data,
            "raw_get_data": self.get_data,
            "is_valid": self.is_valid() if self.mono_form else self.are_valid(),
        }

        # Return the structured object
        return RequestProps(global_context=global_ctx, local_context=local_ctx)


class FormHandler:
    """
    this class utility the RequestDataTransformer to save the forms in a view setting
    """

    def __init__(self, request_data: RequestDataTransformer):
        """
        Initializes FormHandler with request data and operation type.
        """
        self.request_data = request_data
        self.logger_instance = None
        self.logger_instance_message = None
        super().__init__()

    def form_handling(
        self,
    ):
        if self.request_data.mono_form:
            operation_status = self.mono_form_true_option()
        else:
            operation_status = self.mono_form_false_option()
        return operation_status

    def mono_form_true_option(
        self,
    ):
        if self.request_data.is_valid():
            self.request_data.save_form()
            return True
        else:
            return False

    def mono_form_false_option(
        self,
    ):
        if self.request_data.are_valid():
            self.request_data.save_forms()
            return True
        else:
            return False
