import pytest
from probo.components.conf import settings, configs
from probo.components.conf.configs import ProboSettingConfigs
from probo.components.conf.ui_settings import ProboUISettings
from probo.components.tag_classes.block_tags import DIV


def test_probo_ui_settings():
    """Test the text-based global UI settings."""
    # Reset settings for isolated testing if needed, though it's a singleton
    settings.TITLE = "Test Title"
    assert settings.TITLE == "Test Title"
    
    settings.configure(SECTION_I="PP", OTHER="ZZ")
    assert settings.get("SECTION_I") == "PP"
    assert settings.get("OTHER") == "ZZ"
    assert settings.get("NON_EXISTENT", "fallback") == "fallback"


def test_probo_setting_configs():
    """Test the shortcut configs registry."""
    class MockFormConfig:
        form_submit_btn = "Submit Form"

    # Register a config object
    configs.register("main_form", MockFormConfig())
    
    # Retrieve it
    retrieved_config = configs.get("form_submit_btn")
    assert retrieved_config == "Submit Form"
    
    assert configs.get("non_existent_key") is None


def test_data_pipeline_integration():
    """
    Test that global settings are automatically integrated into the Data Pipeline.
    When a component resolves `{'TITLE'}`, it should fall back to settings.TITLE.
    """
    settings.TITLE = "Global Probo Title"
    settings.SECTION_I = "Hero Section"

    # Create a simple element that requests 'TITLE' and 'SECTION_I' from the data pipeline
    # The `{}` set notation is how Probo components request pipeline variables
    test_node = DIV({'TITLE'}, " - ", {'SECTION_I'},data_pipeline=settings)
    
    # Before rendering, it has unresolved pipeline vars
    assert test_node.has_pipeline_vars is True

    # Render it
    html_output = test_node.render()
    
    # The variables should be successfully pulled from the global settings
    assert "Global Probo Title" in html_output
    assert "Hero Section" in html_output
    assert html_output == "<div>Global Probo Title  -  Hero Section</div>"


def test_settings_frozen_state():
    """Test that settings cannot be modified after freezing."""
    # Create an isolated instance so we don't freeze the global one
    local_settings = ProboUISettings()
    local_settings.TITLE = "Before Freeze"
    
    local_settings.freeze()
    
    with pytest.raises(AttributeError, match="ProboUISettings is frozen"):
        local_settings.TITLE = "After Freeze"
