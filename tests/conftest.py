# ... existing fixtures ...
import pytest
# from django.conf import settings


class MockUser:
    def __init__(self, is_staff=False, permissions=None):
        self.is_staff = is_staff
        self.permissions = permissions or []
        self.is_authenticated = True

    def has_perm(self, perm):
        return perm in self.permissions

@pytest.fixture
def mock_props_context():
    """Simulates the 'props' dictionary passed to a Component."""
    return {
        'user': MockUser(is_staff=True, permissions=['can_edit', 'can_delete']),
        'request': {'method': 'POST', 'path': '/dashboard'},
        'flags': {'maintenance_mode': False, 'beta_feature': True},
        'theme': 'dark',
        'csrf_token': 'abc-123'
    }

'''def pytest_configure():
    """
    Configure a minimal Django settings environment for testing.
    This allows us to use RequestFactory and Forms without a full project.
    """
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            SECRET_KEY='test-secret-key',
            ROOT_URLCONF=__name__,
            INSTALLED_APPS=[
                'django.contrib.contenttypes',
                'django.contrib.auth',
                'django.contrib.sessions',
                # 'mui', # Add your lib if it has models/tags
            ],
            MIDDLEWARE=[
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
            ],
            TEMPLATES=[{
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
            }],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            }
        )'''
