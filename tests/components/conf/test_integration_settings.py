import pytest
from probo.components.conf.configs import ProboSettingConfigs
from probo import DIV

@pytest.fixture
def setting_configs():
    return ProboSettingConfigs()

# --- Advanced Integration Tests: ProboSettingConfigs x shortcuts.configs x SSDOM ---

def test_integration_theme_config_ssdom(setting_configs):
    """
    Test that shortcuts.configs (like ThemeConfig) can be registered into ProboSettingConfigs,
    and then seamlessly hydrate an SSDOM tree via the data pipeline.
    """
    from probo.shortcuts.configs import ThemeConfig
    
    # 1. Create a ThemeConfig and register it
    theme = ThemeConfig(spacing="2rem", border_radius="10px")
    setting_configs.register("site_theme", theme)
    
    # 2. Build an SSDOM tree that acts as a CSS variable injector, passing the config registry as the pipeline!
    tree = DIV("Spacing:", {'spacing'}, "; Radius:", {'border_radius'}, data_pipeline=setting_configs)
    
    # 3. Verify the pipeline successfully extracted the attributes from the ThemeConfig
    html = str(tree.render())
    assert "Spacing: 2rem ; Radius: 10px" in html

def test_integration_multiple_shortcut_configs_ssdom(setting_configs):
    """
    Test that SSDOM can pull variables from MULTIPLE different shortcut configs 
    simultaneously when the global config registry is used as the pipeline.
    """
    from probo.shortcuts.configs import ThemeConfig, PageConfig
    from probo import HTML, BODY
    
    # Register multiple distinct configs
    setting_configs.register("theme", ThemeConfig(spacing="1.5rem"))
    setting_configs.register("page", PageConfig(lang="fr"))
    
    # Build tree pulling 'lang' from PageConfig and 'spacing' from ThemeConfig
    tree = HTML(
        BODY("Global Spacing is ", {'spacing'}),
        lang={'lang'},
        data_pipeline=setting_configs
    )
    
    html = str(tree.render())
    assert "lang=\"fr\"" in html or "lang='fr'" in html
    assert "Global Spacing is  1.5rem" in html

def test_integration_hot_swapping_configs_ssdom(setting_configs):
    """
    Test that an SSDOM tree reacts dynamically to changes in the global config registry
    when rebuilt.
    """
    from probo.shortcuts.configs import ThemeConfig
    
    # Initial state
    setting_configs.register("theme", ThemeConfig(spacing="light-mode"))
    
    # Define a builder function that generates the tree (since render mutates internal state)
    def build_tree():
        return DIV({'spacing'}, data_pipeline=setting_configs)
    
    assert "light-mode" in str(build_tree().render())
    
    # Hot swap the config registry with a new object under the same key
    setting_configs.register("theme", ThemeConfig(spacing="dark-mode"))
    
    # Re-render a new instance
    assert "dark-mode" in str(build_tree().render())
