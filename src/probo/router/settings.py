from dataclasses import dataclass, field
from typing import Any, Dict, Optional

@dataclass
class RouterSettings:
    DEBUG: bool = field(default=True, metadata={"description": "Enable debug mode for detailed error messages and auto-reloading."})
    AUTO_RELOAD: bool = field(default=True, metadata={"description": "Enable auto-reloading of templates and components."})
    LOG_LEVEL: str = field(default="INFO", metadata={"description": "Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)."})
    ENABLE_GZIP: bool = field(default=False, metadata={"description": "Enable GZIP compression for HTTP responses."})
    HOST: str = field(default="127.0.0.1", metadata={"description": "The host address to bind the server to."})
    PORT: int = field(default=8080, metadata={"description": "The port number to listen on."})