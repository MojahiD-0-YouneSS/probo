from typing import Any, Dict

class ProboSettingConfigs:
    """The global config registry for ProboUI (resolving around shortcuts.configs)."""
    
    def __init__(self):
        # Initialize the registry for config objects like FormConfig, StyleConfig, etc.
        self._configs: Dict[str, Any] = {}
        self._is_configured = False

    def configure(self, **configs: Any):
        """Allows the user to inject their project-specific config objects."""
        if self._is_configured:
            raise RuntimeError("ProboUI shortcut configs are already configured.")
        self._configs.update(configs)
        self._is_configured = True

    def register(self, key: str, config_obj: Any):
        """Dynamically register a config object."""
        self._configs[key] = config_obj

    def get(self, key: str, default: Any = None) -> Any:
        """Access registered shortcut configs by key."""
        for v in self._configs.values():
            if hasattr(v,key):
                return getattr(v,key)
        return default
def new_ui_configs()->ProboSettingConfigs:
    return ProboSettingConfigs()