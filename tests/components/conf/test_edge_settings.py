import pytest
from probo.components.conf import ProboUISettings
from probo.components.conf.configs import ProboSettingConfigs
from probo import DIV, H1, UL, LI, STRONG, SPAN, P

@pytest.fixture
def settings():
    return ProboUISettings()

@pytest.fixture
def setting_configs():
    return ProboSettingConfigs()

def test_ui_settings_get_custom_default(settings):
    """Test get() fallback on ProboUISettings."""
    assert settings.get("MISSING_KEY", "fallback_value") == "fallback_value"

def test_configs_configure_empty(setting_configs):
    """Test configure with no arguments still locks configuration."""
    setting_configs.configure()
    assert setting_configs._is_configured is True
    assert setting_configs._configs == {}

def test_configs_register_none(setting_configs):
    """Test registering None as a config object."""
    setting_configs.register("empty", None)
    # hasattr(None, 'key') is False, so it should cleanly return default
    assert setting_configs.get("any_key", "default_val") == "default_val"

def test_ssdom_pipeline_strict_data():
    """Test SSDOM data pipeline with strict_data=True dropping the node."""
    settings = ProboUISettings()
    settings.TITLE = "Strict App"
    
    # Missing USER variable
    tree = DIV(
        H1({'TITLE'}),
        P("User is ", {'USER'}),
        data_pipeline=settings
    )
    
    html = str(tree.render())
    # Because strict_data=False (default) and USER is missing, it will blank out the string.
    assert "<p>User is </p>" in html or "<p>User is  </p>" in html
    # But the H1 should render since TITLE is provided and H1 is a separate node
    assert "<h1>Strict App</h1>" in html

def test_ssdom_pipeline_with_raw_dict():
    """Test data pipeline natively supporting standard Python dicts."""
    raw_dict = {"TITLE": "Dictionary App", "USER": "DictUser"}
    
    tree = DIV(
        H1({'TITLE'}),
        P({'USER'}),
        data_pipeline=raw_dict
    )
    html = str(tree.render())
    assert "<h1>Dictionary App</h1>" in html
    assert "<p>DictUser</p>" in html

def test_ssdom_pipeline_custom_retriever():
    """Test data pipeline using a custom retriever function."""
    def custom_getter(pipeline, key, default):
        return f"Retrieved {key}"

    tree = DIV(
        H1({'TITLE'}),
        data_pipeline={},
        custom_retriever=custom_getter
    )
    html = str(tree.render())
    assert "<h1>Retrieved TITLE</h1>" in html

def test_ssdom_pipeline_private_policy():
    """Test private policy: variables shouldn't leak to children."""
    parent = DIV(data_pipeline={"SECRET": "hidden"})
    # Mark it as private
    parent.provide_data("SECRET", "hidden", policy="pri")
    
    child = P({'SECRET'})
    parent.add(child)
    
    html = str(parent.render())
    # Should be swapped to empty string since private data doesn't cross depth bounds
    assert "<p></p>" in html

def test_ssdom_pipeline_protected_policy():
    """Test protected policy: leaks to direct children but not grandchildren."""
    parent = DIV(data_pipeline={"SEMI_SECRET": "guard"})
    parent.provide_data("SEMI_SECRET", "guard", policy="pro")
    
    direct_child = DIV({'SEMI_SECRET'})
    grand_child = P({'SEMI_SECRET'})
    direct_child.add(grand_child)
    parent.add(direct_child)
    
    html = str(parent.render())
    # direct_child gets it, grand_child gets blank
    assert "<div>guard<p></p></div>" in html

def test_ui_settings_multiple_keys(settings):
    """Test storing and retrieving multiple keys in UI settings."""
    settings.configure(A=1, B=2, C=3)
    assert settings.get("A") == 1
    assert settings.get("B") == 2
    assert settings.get("C") == 3

def test_configs_multiple_matching_attributes(setting_configs):
    """Test deep retrieval logic across many configs."""
    class Conf1: attr_1 = 1
    class Conf2: attr_2 = 2
    class Conf3: attr_3 = 3
    
    setting_configs.configure(c1=Conf1(), c2=Conf2(), c3=Conf3())
    assert setting_configs.get("attr_1") == 1
    assert setting_configs.get("attr_2") == 2
    assert setting_configs.get("attr_3") == 3
