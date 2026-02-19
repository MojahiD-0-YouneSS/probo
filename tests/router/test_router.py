import pytest
from webtest import TestApp
from probo.context import TemplateComponentMap
from probo.router import ProboRouter
from probo.components.tag_functions import div

# To run these tests:
# 1. pip install pytest webtest
# 2. run command: pytest test_router.py

@pytest.fixture
def client():
    """
    Fixture to set up the ProboRouter and wrap it in a WebTest TestApp.
    """
    router = ProboRouter(app_name="TestApp", secret_key="test_secret")

    @router.page("/")
    def home():
        return "Home Page"

    @router.page("/context")
    def context_page(request, response):
        # Test session-like behavior with cookies
        val = request.get_cookie("test_cookie", secret="test_secret")
        response.set_cookie("response_cookie", "set_by_server", secret="test_secret")
        return f"Value: {val}"

    # We return the TestApp which allows us to simulate requests
    return TestApp(router.app)

def test_home_route(client):
    """Test a simple manual route."""
    res = client.get('')
    assert res.status_code == 200
    assert "Home Page" in res.text

def test_404_handling(client):
    """Test that non-existent routes return 404."""
    res = client.get('/non-existent', status=404)
    assert res.status_code == 404
    assert "404 Not Found" in res.text

def test_tcm_fallback(client):
    """
    Test that the router correctly falls back to TCM if a route isn't found.
    """
    class MockTCM(TemplateComponentMap):
        def __init__(self,):
            super().__init__()
            self.set_component("/tcm-page","TCM Content")
            
    router_with_tcm = ProboRouter(app_name="TCMApp", secret_key="secret")
    router_with_tcm.register_tcm(MockTCM())
    tcm_client = TestApp(router_with_tcm.app)
    
    res = tcm_client.get('/tcm-page')
    assert res.status_code == 200
    assert "TCM Content" in res.text