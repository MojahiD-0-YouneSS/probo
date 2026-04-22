import pytest
from unittest.mock import MagicMock, patch
import sys

from probo.request.transformer import RequestDataTransformer, FormHandler

# ==========================================
# MOCKS (Simulating Django Internals)
# ==========================================


class MockQueryDict(dict):
    """Simulates Django's QueryDict (.POST / .GET) which supports .getlist()"""

    def get(self, key, default=None):
        # Django's standard .get() returns the LAST item in the list if it's a list
        val = super().get(key, default)
        if isinstance(val, list) and val:
            return val[-1]
        return val

    def getlist(self, key):
        val = super().get(key, [])
        return val if isinstance(val, list) else [val]


class MockUser:
    """Simulates a Django User object"""

    def __init__(self, is_auth=True):
        self.is_authenticated = is_auth
        self.username = "probo_admin"
        self.id = 1


class MockSession(dict):
    """Simulates a Django Session object"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.modified = False


class MockRequest:
    """Simulates a complete Django HttpRequest"""

    def __init__(self, method="POST", json_data=None):
        self.method = method
        self.user = MockUser()
        self.POST = MockQueryDict({"field1": ["val1"], "field2": ["val2a", "val2b"]})
        self.GET = MockQueryDict({"q": ["search"]})
        self.FILES = MockQueryDict({"avatar": ["avatar_file"]})
        self.session = MockSession({"session_key": "s-12345", "theme": "dark"})
        self._json_data = json_data
        self.path = "/api/submit"

    def json(self):
        """Simulates FastAPI/Django JSON parsing"""
        # Return empty dict if no JSON data is provided to prevent crashes in .has_field()
        if self._json_data is not None:
            return self._json_data
        return {}


class MockValidForm:
    """Simulates a Django ModelForm that passes validation"""

    __name__ = "MockValidForm"

    def __init__(self, data=None, files=None, prefix=None):
        self.cleaned_data = {"clean_field": "clean_val"}
        self.errors = {}
        self.saved = False

    def is_valid(self):
        return True

    def save(self, **kwargs):
        self.saved = True
        return self


class MockInvalidForm:
    """Simulates a Django ModelForm that fails validation"""

    __name__ = "MockInvalidForm"

    def __init__(self, data=None, files=None, prefix=None):
        self.cleaned_data = {}
        self.errors = {"error_field": ["Bad data provided"]}
        self.saved = False

    def is_valid(self):
        return False

    def save(self, **kwargs):
        self.saved = True


# ==========================================
# TESTS: Initialization & Data Processing
# ==========================================


def test_rdt_initialization_mono_form():
    """Tests standard initialization with a single form and files."""
    req = MockRequest()
    rdt = RequestDataTransformer(req, form_class=MockValidForm, request_files=True)

    assert rdt.request_method == "POST"
    assert rdt.mono_form is True
    assert isinstance(rdt.form, MockValidForm)

    # Check that lists of length 1 were safely collapsed to strings
    assert rdt.post_data["field1"] == "val1"
    # Check that actual lists were preserved
    assert rdt.post_data["field2"] == ["val2a", "val2b"]
    assert rdt.get_data["q"] == "search"
    assert rdt.request_files["avatar"] == "avatar_file"


def test_rdt_initialization_missing_attributes():
    """Tests fallback logic when the request is missing typical Django attributes."""

    # Ensure this is a bare object that DOES NOT inherit from MockRequest
    class BareRequest:
        POST=None

    rdt = RequestDataTransformer(BareRequest(), form_class=MockValidForm)
    assert rdt.request_method == ""
    assert rdt.user_data == {}
    assert rdt.post_data == {}
    assert rdt.session_data == {}
    assert rdt.id is None


def test_rdt_initialization_multi_form():
    """Tests initializing multiple forms (Formsets)."""
    req = MockRequest()
    # Passing a list of classes triggers the _initialize_multi_form_processing engine
    rdt = RequestDataTransformer(
        req, form_class=[MockValidForm, MockInvalidForm], mono_form=False
    )

    assert rdt.mono_form is False
    assert "mockvalidform" in rdt.form
    assert "mockinvalidform" in rdt.form

    # Valid form should populate cleaned data
    assert rdt.cleaned_data["mockvalidform"] == {"clean_field": "clean_val"}
    assert rdt.validations["mockvalidform"] is True

    # Invalid form should populate errors
    assert rdt.validations["mockinvalidform"] is False
    assert rdt.errors["mockinvalidform"] is not None


# ==========================================
# TESTS: Form Validation & Persistence
# ==========================================


def test_save_form_valid():
    rdt = RequestDataTransformer(MockRequest(), form_class=MockValidForm)
    res = rdt.save_form()

    assert rdt.is_valid() is True
    assert rdt.form.saved is True
    assert rdt.cleaned_data == {"clean_field": "clean_val"}
    assert isinstance(res, MockValidForm)  # Should return the saved form


def test_save_form_invalid():
    rdt = RequestDataTransformer(MockRequest(), form_class=MockInvalidForm)
    res = rdt.save_form()

    assert rdt.is_valid() is False
    assert rdt.form.saved is False
    assert "MockInvalidForm" in rdt.errors
    assert res is False  # Should return False on failure


def test_get_errors():
    rdt = RequestDataTransformer(MockRequest(), form_class=MockInvalidForm)
    rdt.is_valid()
    errors = rdt.get_errors()
    assert "MockInvalidForm" in errors


# ==========================================
# TESTS: Session Management
# ==========================================


def test_session_management():
    req = MockRequest()
    rdt = RequestDataTransformer(req)

    # 1. Get
    assert rdt.get_session_data("theme") == "dark"
    assert rdt.get_session_data("missing", default="light") == "light"

    # 2. Set
    rdt.set_session_data("new_key", "value")
    assert req.session["new_key"] == "value"
    assert req.session.modified is True
    assert rdt.session_data["new_key"] == "value"

    # 3. Update
    rdt.update_session_data("theme", lambda x: x + "-mode")
    assert req.session["theme"] == "dark-mode"

    # 4. Delete
    rdt.delete_session_data("new_key")
    assert "new_key" not in req.session

    # 5. Clear All
    rdt.clear_all_session_data()
    assert len(rdt.session_data) == 0


# ==========================================
# TESTS: Data Extraction & Verification
# ==========================================


def test_get_request_data():
    rdt = RequestDataTransformer(MockRequest(), form_class=MockValidForm)
    rdt.is_valid()  # Populate cleaned data

    # Unorganized (Flat merge)
    flat_data = rdt.get_request_data(organized=False)
    assert flat_data["clean_field"] == "clean_val"
    assert flat_data["field1"] == "val1"

    # Organized (Nested dictionaries)
    org_data = rdt.get_request_data(organized=True)
    assert "cleaned_data" in org_data
    assert "post_data" in org_data
    assert org_data["cleaned_data"]["clean_field"] == "clean_val"


def test_extract_target_data():
    req = MockRequest()
    rdt = RequestDataTransformer(req)

    # Standard extraction
    data = rdt.extract_target_data(
        fields=["field1", "field2"], multi_value_fields=["field2"]
    )
    assert data["field1"] == "val1"
    assert data["field2"] == ["val2a", "val2b"]  # Ensure multi-value fields pull lists


def test_extract_target_data_json():
    req = MockRequest(json_data={"api_key": "123"})
    rdt = RequestDataTransformer(req)

    data = rdt.extract_target_data(is_json=True)
    assert data["api_key"] == "123"


def test_get_field_value():
    rdt = RequestDataTransformer(MockRequest())
    assert rdt.get_field_value("field1") == "val1"
    assert rdt.get_field_value("missing_field", default="fallback") == "fallback"


def test_get_json_field_value():
    rdt = RequestDataTransformer(MockRequest(json_data={"api_key": "123"}))
    assert rdt.get_json_field_value("api_key") == "123"
    assert rdt.get_json_field_value("missing", default="none") == "none"


def test_get_json_field_value_missing_json():
    # A request that does not define a json method or attribute
    class NoJsonRequest:
        pass

    rdt = RequestDataTransformer(NoJsonRequest())

    with pytest.raises(ValueError, match="Request does not contain JSON data"):
        rdt.get_json_field_value("anything")


def test_has_field():
    # Check POST
    rdt_post = RequestDataTransformer(MockRequest())
    assert rdt_post.has_field("field1") is True
    assert rdt_post.has_field("invalid") is False

    # Check JSON fallback
    rdt_json = RequestDataTransformer(MockRequest(json_data={"json_key": "true"}))
    assert rdt_json.has_field("json_key") is True


# ==========================================
# TESTS: Multi-Form Handling
# ==========================================


def test_multi_form_are_valid():
    req = MockRequest()

    # All Valid
    rdt_valid = RequestDataTransformer(
        req, form_class=[MockValidForm, MockValidForm], mono_form=False
    )
    assert rdt_valid.are_valid() is True

    # One Invalid
    rdt_invalid = RequestDataTransformer(
        req, form_class=[MockValidForm, MockInvalidForm], mono_form=False
    )
    assert rdt_invalid.are_valid() is False


def test_multi_form_save_forms():
    req = MockRequest()
    rdt = RequestDataTransformer(
        req, form_class=[MockValidForm, MockValidForm], mono_form=False
    )

    res = rdt.save_forms()
    assert res is True

    for prefix, form_instance in rdt.form.items():
        assert form_instance.saved is True


# ==========================================
# TESTS: Integration Features
# ==========================================


def test_get_csrf_token(monkeypatch):
    """Tests that CSRF is safely bypassed if Django is not installed, but fetched if it is."""
    req = MockRequest()
    rdt = RequestDataTransformer(req)

    # 1. Test Failure (Returns empty string when django isn't found)
    assert rdt.get_csrf_token() == ""

    # 2. Test Success (Mocking django.middleware.csrf)
    mock_django_csrf = MagicMock()
    mock_django_csrf.get_token.return_value = "secret_csrf_token"
    monkeypatch.setitem(sys.modules, "django.middleware.csrf", mock_django_csrf)

    assert rdt.get_csrf_token() == "secret_csrf_token"


@patch("probo.request.transformer.RequestProps")
def test_extract_props(mock_props):
    """Tests that properties are correctly segregated into Global and Local contexts."""
    req = MockRequest()
    rdt = RequestDataTransformer(req, form_class=MockValidForm)

    rdt.extract_props()

    # Ensure RequestProps was instantiated with the correct dictionaries
    mock_props.assert_called_once()
    kwargs = mock_props.call_args.kwargs

    assert "global_context" in kwargs
    assert "local_context" in kwargs
    assert kwargs["global_context"]["request_method"] == "POST"
    assert kwargs["local_context"]["is_valid"] is True


# ==========================================
# TESTS: FormHandler Execution
# ==========================================


def test_form_handler_mono_valid():
    rdt = RequestDataTransformer(MockRequest(), form_class=MockValidForm)
    handler = FormHandler(rdt)
    assert handler.form_handling() is True


def test_form_handler_mono_invalid():
    rdt = RequestDataTransformer(MockRequest(), form_class=MockInvalidForm)
    handler = FormHandler(rdt)
    assert handler.form_handling() is False


def test_form_handler_multi_valid():
    rdt = RequestDataTransformer(
        MockRequest(), form_class=[MockValidForm], mono_form=False
    )
    handler = FormHandler(rdt)
    assert handler.form_handling() is True


def test_form_handler_multi_invalid():
    rdt = RequestDataTransformer(
        MockRequest(), form_class=[MockInvalidForm], mono_form=False
    )
    handler = FormHandler(rdt)
    assert handler.form_handling() is False
