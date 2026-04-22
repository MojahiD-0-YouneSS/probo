import pytest
from probo.router.settings import RouterSettings


def test_default_initialization():
    """Ensure defaults are properly set up for a fresh instance."""
    settings = RouterSettings()

    assert settings.HOST == "127.0.0.1"
    assert settings.PORT == 8080
    assert settings.DEBUG is True
    assert settings.STATIC_FOLDER == "static"
    assert settings.ALLOWED_HOSTS == ["*"]
    assert settings.CORS_ORIGINS == []
    assert settings.WORKERS == 1
    assert getattr(settings, "_LOCKED") is False


def test_custom_initialization():
    """Ensure keyword arguments properly override defaults during instantiation."""
    settings = RouterSettings(
        PORT=9000,
        DEBUG=False,
        STATIC_FOLDER="assets",
        CORS_ORIGINS=["https://probo-ui.com"],
    )

    assert settings.PORT == 9000
    assert settings.DEBUG is False
    assert settings.STATIC_FOLDER == "assets"
    assert settings.CORS_ORIGINS == ["https://probo-ui.com"]


def test_mutation_before_freeze():
    """Tests that a user can freely change settings in their app.py before starting the server."""
    settings = RouterSettings()

    # Simple attribute change
    settings.HOST = "0.0.0.0"
    assert settings.HOST == "0.0.0.0"

    # List appending
    settings.ALLOWED_HOSTS.append("probo.dev")
    assert "probo.dev" in settings.ALLOWED_HOSTS


def test_freeze_prevents_mutation():
    """Tests that calling freeze() strictly locks down the object."""
    settings = RouterSettings()
    settings.freeze()

    # Modifying an existing attribute should fail
    with pytest.raises(AttributeError, match="ProboSettings is frozen"):
        settings.PORT = 80

    # Adding a brand new attribute should also fail
    with pytest.raises(AttributeError, match="ProboSettings is frozen"):
        settings.NEW_CUSTOM_SETTING = "This should crash"


def test_list_factory_isolation():
    """
    CRITICAL: Ensures that using `default_factory` prevents lists from
    sharing memory across different RouterSettings instances.
    """
    s1 = RouterSettings()
    s2 = RouterSettings()

    # Modify list on instance 1
    s1.CORS_ORIGINS.append("http://localhost:3000")

    # Instance 1 should have it, Instance 2 should still be empty
    assert "http://localhost:3000" in s1.CORS_ORIGINS
    assert len(s2.CORS_ORIGINS) == 0
