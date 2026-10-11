import os
import ast
from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class ProboUISettings:
    config: Dict[str, Any] = field(default_factory=dict)
    _LOCKED: bool = field(default=False, init=False, repr=False)

    def freeze(self):
        object.__setattr__(self, "_LOCKED", True)

    def __setattr__(self, name: str, value: Any):
        if getattr(self, "_LOCKED", False):
            raise AttributeError(f"ProboUISettings is frozen. Cannot modify '{name}'.")
        object.__setattr__(self, name, value)

    def __getitem__(self, key: str) -> Any:
        value = self.get(key)
        if value is None:
            raise KeyError(f"Setting '{key}' not found.")
        return value

    def __setitem__(self, key: str, value: Any):
        setattr(self, key, value)

    def configure(self, **kwargs):
        """
        Utility to set multiple settings at once.
        Example: settings.configure(TITLE="My App", OTHER_VAR=123)
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get(self, key: str, default: Any = None, from_env:bool=False) -> Any:
        """
        PRODUCTION SECURE GETTER:
        1. Falls back to internal configuration
        2. Checks OS Environment Variables first (Docker/Cloud priority) if the from_env
        3. Returns default if neither exists
        """
        # Fall back to internal state parsed from files or set via code
        if hasattr(self, key):
            return getattr(self, key)
        # Cloud/Docker environments take absolute priority
        if from_env:
            env_val = os.getenv(key)
            if env_val is not None:
                # Safely attempt to parse the env string into int/bool/etc.
                try:
                    return ast.literal_eval(env_val)
                except (ValueError, SyntaxError):
                    return env_val # Return as string if it's just text
            
        return default

    def from_file(self, filepath: str):
        """Loads local configurations. (Values here will be overridden by OS Env Vars)"""
        if not os.path.exists(filepath):
            return # Fail silently so production servers don't crash if the file is missing
            
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                
                key, value = line.split('=', 1)
                key, value = key.strip(), value.strip()
                
                # Safely parse python literals (True, 1, 3.14, 'string')
                try:
                    parsed_value = ast.literal_eval(value)
                except (ValueError, SyntaxError):
                    parsed_value = value # Keep as string if it's an unquoted word
                    
                setattr(self, key, parsed_value)

# Instantiate the global settings objects
def new_ui_settings()->ProboUISettings:
    return ProboUISettings()
