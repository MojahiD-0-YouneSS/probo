from src.probo.request import RequestDataTransformer
from dataclasses import dataclass


# --- MOCKS ---
@dataclass
class MockUser:
    username: str = "testuser"
    is_authenticated: bool = True


@dataclass
class MockHttpRequest:
    method: str = "GET"
    POST: dict = None
    GET: dict = None
    FILES: dict = None
    user: MockUser = None
    path: str = "/"

    def __post_init__(self):
        self.POST = self.POST or {}
        self.GET = self.GET or {}
        self.FILES = self.FILES or {}
        self.user = self.user or MockUser()


# --- TESTS ---


def test_rdt_initialization_get():
    """Test extracting data from a GET request."""
    req = MockHttpRequest(method="GET", GET={"q": "search"})
    rdt = RequestDataTransformer(request=req)

    # Check if props extracted correctly
    props = rdt.extract_props()
    assert props.global_context["request_method"] == "GET"
    assert "q" in rdt.request.GET


def test_rdt_initialization_post():
    """Test extracting data from a POST request."""
    req = MockHttpRequest(method="POST", POST={"username": "youness"})
    rdt = RequestDataTransformer(request=req)

    assert rdt.request_method == "POST"
    assert rdt.post_data["username"] == "youness"

def test_rdt_form_instantiation():
    """Test that RDT instantiates the Django Form class passed to it."""

    class MockForm:
        def __init__(self, data=None, **kwargs):
            self.data = data
            self.is_bound = data is not None

        def is_valid(self):
            return True

    # Case 1: GET (Unbound)
    req_get = MockHttpRequest(method="GET")
    rdt_get = RequestDataTransformer(request=req_get, form_class=MockForm)
    assert rdt_get.form is not None
    assert rdt_get.form.is_bound is True

    # Case 2: POST (Bound)
    req_post = MockHttpRequest(method="POST", POST={"foo": "bar"})
    rdt_post = RequestDataTransformer(request=req_post, form_class=MockForm)
    assert rdt_post.form is not None
    assert rdt_post.form.is_bound is True
    assert rdt_post.form.data["foo"] == "bar"
