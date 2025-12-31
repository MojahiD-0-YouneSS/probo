from src.probo.components.forms import ProboForm
from django import forms
from django.test import RequestFactory
from src.probo.request import RequestDataTransformer

# ==============================================================================
#  REAL DJANGO OBJECTS
# ==============================================================================


class ContactForm(forms.Form):
    """A real Django form with validation rules."""

    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)

    def clean_subject(self):
        # Custom cleaning logic to prove we are using real Django
        data = self.cleaned_data["subject"]
        if "spam" in data.lower():
            raise forms.ValidationError("No spam allowed!")
        return data.upper()


# ==============================================================================
#  1. THE MOCKS (Simulating the Django Environment)
# ==============================================================================


class MockWidget:
    """Simulates a Django Widget."""

    def __init__(self, input_type="text", attrs=None, choices=None):
        self.input_type = input_type
        self.attrs = attrs or {}
        self.choices = choices or []
        self.allow_multiple_selected = False


class MockField:
    """Simulates a Django BoundField."""

    def __init__(self, name, value="", errors=None, required=False, widget=None):
        self.name = name
        self.html_name = name
        self.label = name.capitalize()
        self.help_text = "Help"
        self.errors = errors or []
        self._value = value
        # Structure mimics django's field.field.widget
        self.field = type(
            "Inner", (), {"widget": widget or MockWidget(), "required": required}
        )

    def value(self):
        return self._value

    def id_for_label(self):
        return f"id_{self.name}"

    def label_tag(self):
        return f"<label>{self.label}</label>"


class MockSession(dict):
    def __init__(self):
        self["session_key"] = "test-session-key"
        self.modified = False


class MockRequest:
    """Simulates the HTTP Request."""

    def __init__(self, method="GET", POST=None):
        self.method = method
        self.POST = POST or {}
        self.GET = {}
        self.FILES = {}
        self.user = type("User", (), {"is_authenticated": True})()
        self.session = MockSession()
        self.META = {}


# ==============================================================================
#  INTEGRATION TESTS
# ==============================================================================


def test_rdt_with_real_valid_post():
    """
    Scenario: Real Django POST request with valid data.
    Goal: Verify cleaned_data is populated and accessible via RDT.
    """
    # 1. Create a Real Request
    factory = RequestFactory()
    data = {"subject": "Hello World", "email": "test@example.com", "age": 25}
    request = factory.post("/contact/", data)

    # Add session manually since RequestFactory doesn't run middleware automatically
    from django.contrib.sessions.middleware import SessionMiddleware

    middleware = SessionMiddleware(lambda r: None)
    middleware.process_request(request)
    request.session

    # 2. Initialize RDT
    rdt = RequestDataTransformer(request=request, form_class=ContactForm)

    # 3. Verify Validity
    # RDT should have triggered validation internally if designed correctly,
    # or we trigger it here.
    assert rdt.is_valid() is True

    # 4. Check Cleaned Data (The specific thing you missed in mocks)
    # Note: 'subject' should be UPPERCASE because of clean_subject() logic
    assert rdt.form.cleaned_data["subject"] == "HELLO WORLD"
    assert rdt.form.cleaned_data["age"] == 25


def test_rdt_with_real_invalid_post():
    """
    Scenario: Real POST with invalid data.
    Goal: Verify errors are caught.
    """
    factory = RequestFactory()
    # Invalid email, age too low, subject contains 'spam'
    data = {"subject": "Buy spam now", "email": "not-an-email", "age": 10}
    request = factory.post("/contact/", data)

    # Setup session
    from django.contrib.sessions.middleware import SessionMiddleware

    SessionMiddleware(lambda r: None).process_request(request)

    rdt = RequestDataTransformer(request=request, form_class=ContactForm)

    # 1. Should be invalid
    assert rdt.is_valid() is False

    # 2. Check Errors
    errors = rdt.form.errors
    assert "subject" in errors  # "No spam allowed"
    assert "email" in errors  # Invalid format
    assert "age" in errors  # Min value 18


def test_mf_render_real_django_form():
    """
    Scenario: Render the real ContactForm via ProboForm.
    Goal: Verify HTML output matches real field attributes.
    """
    # Unbound form (GET request equivalent)
    factory = RequestFactory()
    request = factory.get("/contact/")

    rdt = RequestDataTransformer(request=request, form_class=ContactForm)
    mf = ProboForm("/contact/", request_data=rdt)

    html = mf.render()
    # Verify specific attributes generated by Django's widgets
    assert 'name="email"' in html
    assert 'type="email"' in html
    assert 'min="18"' in html  # Django's IntegerWidget adds this automatically
    assert 'maxlength="100"' in html  # CharField adds this
    assert "required" in html  # Fields are required by default
