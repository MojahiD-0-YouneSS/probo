from probo.components.conf.configs import ProboSettingConfigs
from probo.components.conf.ui_settings import ProboUISettings
# Instantiate the global settings objects
settings = ProboUISettings()
configs = ProboSettingConfigs()

__all__ = [
    "settings",
    "ProboSettingConfigs",
    "ProboUISettings",
    "configs",
]