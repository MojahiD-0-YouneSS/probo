import pytest
import os
from probo.components.conf import ProboUISettings
from probo.components.conf.configs import ProboSettingConfigs
from probo import DIV, H1, UL, LI, STRONG, SPAN, P

@pytest.fixture
def settings():
    """Provides a fresh, unlocked settings instance for each test."""
    return ProboUISettings()

@pytest.fixture
def setting_configs():
    """Provides a fresh ProboSettingConfigs instance for testing."""
    return ProboSettingConfigs()

def test_settings_initialization(settings):
    assert settings.config == {}
    # Accessing internal attribute directly for testing purposes
    assert settings._LOCKED is False

def test_magic_methods_get_set(settings):
    # Test dictionary-style assignment
    settings["THEME_MODE"] = "dark"
    assert settings["THEME_MODE"] == "dark"
    
    # Test that dict-assignment mirrors attribute access
    assert settings.THEME_MODE == "dark"
    
    # Test attribute assignment mirrors dict access
    settings.APP_NAME = "Probo Dashboard"
    assert settings["APP_NAME"] == "Probo Dashboard"

def test_missing_key_raises_error(settings):
    with pytest.raises(KeyError):
        _ = settings["NON_EXISTENT_KEY"]

def test_freeze_prevents_modification(settings):
    settings.MAX_USERS = 100
    settings.freeze()
    
    # Test attribute modification
    with pytest.raises(AttributeError, match="is frozen"):
        settings.MAX_USERS = 200
        
    # Test dict-style modification
    with pytest.raises(AttributeError, match="is frozen"):
        settings["NEW_KEY"] = "value"

def test_from_file_parsing_and_type_casting(settings, tmp_path):
    # Use pytest's built-in tmp_path fixture to generate a safe temp file
    config_file = tmp_path / "ui_config.txt"
    config_file.write_text(
        "DEBUG_MODE = True\n"
        "PORT = 8080\n"
        "# This is a comment\n"
        "APP_NAME = 'Probo UI'\n"
        "FLOAT_VAL = 3.14\n"
    )
    
    settings.from_file(str(config_file))
    
    # Assert Type Casting works correctly
    assert settings.DEBUG_MODE is True        # Boolean cast
    assert settings.PORT == 8080              # Integer cast
    assert settings.APP_NAME == "Probo UI"    # String (quotes stripped) cast
    assert settings.FLOAT_VAL == 3.14         # Float cast

def test_basic_element_rendering(settings,tmp_path):
    """Ensures standard tags render without nested children."""
    config_file = tmp_path / "ui_config.txt"
    config_file.write_text(
        "DEBUG_MODE = True\n"
        "PORT = 8080\n"
        "# This is a comment\n"
        "APP_NAME = 'Probo UI'\n"
        "FLOAT_VAL = 3.14\n"
    )
    
    settings.from_file(str(config_file))
    
    element = H1("Hello World in",{'APP_NAME'}, Class="title-text",data_pipeline=settings)
    html = str(element.render())
    
    # Check tag and content
    assert "<h1>" in html or "<h1 " in html
    assert "Hello World" in html
    assert "Probo UI" in html
    # Check attributes
    assert 'class="title-text"' in html or "class='title-text'" in html

# --- 10 Tests for ProboSettingConfigs ---

class DummyConfigA:
    primary_color = "#ff0000"
    shared_key = "from A"

class DummyConfigB:
    secondary_color = "#00ff00"
    shared_key = "from B"

def test_configs_initialization(setting_configs):
    """1. Test initialization of ProboSettingConfigs."""
    assert setting_configs._configs == {}
    assert setting_configs._is_configured is False

def test_configs_configure_success(setting_configs):
    """2. Test configure method populates _configs and locks configuration."""
    conf_a = DummyConfigA()
    conf_b = DummyConfigB()
    setting_configs.configure(a=conf_a, b=conf_b)
    
    assert setting_configs._is_configured is True
    assert "a" in setting_configs._configs
    assert "b" in setting_configs._configs
    assert setting_configs._configs["a"] is conf_a

def test_configs_configure_twice_raises_error(setting_configs):
    """3. Test calling configure twice raises RuntimeError."""
    setting_configs.configure(a=DummyConfigA())
    with pytest.raises(RuntimeError, match="are already configured"):
        setting_configs.configure(b=DummyConfigB())

def test_configs_register_dynamic(setting_configs):
    """4. Test register dynamically adds config object."""
    conf = DummyConfigA()
    setting_configs.register("dynamic_conf", conf)
    assert "dynamic_conf" in setting_configs._configs
    assert setting_configs._configs["dynamic_conf"] is conf
    # Shouldn't lock configure method
    assert setting_configs._is_configured is False

def test_configs_get_successful(setting_configs):
    """5. Test get retrieves attribute from registered configs."""
    setting_configs.register("dummy", DummyConfigA())
    assert setting_configs.get("primary_color") == "#ff0000"

def test_configs_get_not_found(setting_configs):
    """6. Test get returns None for missing key."""
    setting_configs.register("dummy", DummyConfigA())
    assert setting_configs.get("missing_key") is None

def test_configs_get_precedence(setting_configs):
    """7. Test get precedence when multiple configs have the same attribute."""
    # Since python 3.7 dicts preserve insertion order, 'a' will be checked before 'b'
    setting_configs.register("a", DummyConfigA())
    setting_configs.register("b", DummyConfigB())
    assert setting_configs.get("shared_key") == "from A"

def test_configs_register_overwrite(setting_configs):
    """8. Test register overwrites previous object for same key."""
    setting_configs.register("target", DummyConfigA())
    assert setting_configs.get("primary_color") == "#ff0000"
    
    setting_configs.register("target", DummyConfigB())
    assert setting_configs.get("primary_color") is None
    assert setting_configs.get("secondary_color") == "#00ff00"

def test_configs_get_with_custom_default(setting_configs):
    """9. Test get returns custom default when key is not found."""
    setting_configs.register("dummy", DummyConfigA())
    assert setting_configs.get("missing_key", "custom_fallback") == "custom_fallback"

def test_configs_empty_get(setting_configs):
    """10. Test get on completely empty registry."""
    assert setting_configs.get("anything") is None
    assert setting_configs.get("anything", "fallback") == "fallback"


# --- 2 SSDOM Tests explicitly using DataPipeline ---

def test_ssdom_pipeline_with_multiple_variables():
    """1. Test that SSDOM can pull multiple variables natively from settings passed via data_pipeline."""
    settings = ProboUISettings()
    settings.TITLE = "Dashboard"
    settings.USER = "Youness"
    
    tree = DIV(
        H1({'TITLE'}),
        P("Welcome back, ", STRONG({'USER'})),
        data_pipeline=settings
    )
    html = str(tree.render())
    
    assert "<h1>Dashboard</h1>" in html
    assert "<p>Welcome back, <strong>Youness</strong></p>" in html

def test_ssdom_pipeline_missing_variable():
    """2. Test that SSDOM gracefully handles missing variables in the data_pipeline."""
    settings = ProboUISettings()
    settings.TITLE = "Dashboard"
    # settings.USER is explicitly missing!
    
    tree = DIV(
        H1({'TITLE'}),
        SPAN("User: ", {'USER'}),
        data_pipeline=settings
    )
    
    html = str(tree.render())
    
    assert "<h1>Dashboard</h1>" in html
    # In Probo, missing pipeline variables default to empty string during render when swap_vars=True
    assert "User: </span>" in html or "User:  </span>" in html
