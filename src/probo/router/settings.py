from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List


@dataclass
class RouterSettings:
    # --- Core Mechanics ---
    DEBUG: bool = field(
        default=True,
        metadata={
            "description": "Enable debug mode for detailed error messages and auto-reloading."
        },
    )
    AUTO_RELOAD: bool = field(
        default=False,
        metadata={"description": "Enable auto-reloading of templates and components."},
    )
    LOG_LEVEL: str = field(
        default="INFO",
        metadata={
            "description": "Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)."
        },
    )
    ENABLE_GZIP: bool = field(
        default=False,
        metadata={"description": "Enable GZIP compression for HTTP responses."},
    )

    # --- Server Configuration ---
    HOST: str = field(
        default="127.0.0.1",
        metadata={"description": "The host address to bind the server to."},
    )
    PORT: int = field(
        default=8080, metadata={"description": "The port number to listen on."}
    )
    WORKERS: int = field(
        default=1,
        metadata={
            "description": "Number of worker processes for Gunicorn/Uvicorn deployments."
        },
    )
    MAX_REQUEST_SIZE: int = field(
        default=10485760,
        metadata={"description": "Max upload/request size in bytes (default 10MB)."},
    )

    # --- Security & Auth ---
    SECRET_KEY: str = field(
        default="probo-secret-key-change-me-in-production",
        metadata={
            "description": "The secret key used for signing cookies and sessions."
        },
    )
    ALLOWED_HOSTS: List[str] = field(
        default_factory=lambda: ["*"],
        metadata={"description": "List of hostnames the server is allowed to serve."},
    )
    CORS_ORIGINS: List[str] = field(
        default_factory=list,
        metadata={
            "description": "List of domains allowed to make cross-origin requests."
        },
    )
    SESSION_COOKIE_NAME: str = field(
        default="probo_session",
        metadata={"description": "The name of the session cookie."},
    )
    SESSION_MAX_AGE: int = field(
        default=31536000,
        metadata={"description": "Session duration in seconds (default 1 year)."},
    )

    # --- File System & Paths ---
    STATIC_FOLDER: str = field(
        default="static",
        metadata={"description": "Local directory containing static files."},
    )
    STATIC_URL: str = field(
        default="/static/",
        metadata={"description": "URL prefix for serving static files."},
    )
    MEDIA_FOLDER: str = field(
        default="media",
        metadata={"description": "Local directory for user-uploaded media."},
    )
    MEDIA_URL: str = field(
        default="/media/",
        metadata={"description": "URL prefix for serving media files."},
    )
    TEMPLATE_FOLDER: str = field(
        default="templates",
        metadata={"description": "Local directory containing raw HTML templates."},
    )

    # --- Database (Optional/Future-proofing) ---
    DATABASE_URI: Optional[str] = field(
        default=None,
        metadata={"description": "Connection string for the primary database."},
    )

    # --- Internal Protection ---
    _LOCKED: bool = field(default=False, init=False, repr=False)

    def freeze(self):
        """Make this specific instance read-only. Call this right before starting the web server."""
        object.__setattr__(self, "_LOCKED", True)

    def __setattr__(self, name, value):
        """Prevents mutation if the settings object has been locked."""
        if getattr(self, "_LOCKED", False):
            raise AttributeError(
                f"ProboSettings is frozen. Cannot modify '{name}' after server start."
            )
        # Use object.__setattr__ to bypass our custom lock check and avoid infinite recursion
        object.__setattr__(self, name, value)
