import threading
from typing import Any, Dict


class ProboContextProvider:
    """
    Global UI State Manager.
    Provides context to the SSDOM tree without prop-drilling.
    """

    def __init__(self, **inline_context: Any):
        """
        Initializes a scoped context.
        Accepts kwargs for immediate injection during the `with` block.
        """
        self._inline_context = inline_context
        # Define instance variables here to keep linters happy
        self._snapshot: Dict[str, Any] = {}
    # The 'Storage' part: thread-local prevents data leaking between concurrent users.
    _storage = threading.local()

    @classmethod
    def _get_bucket(cls) -> Dict[str, Any]:
        """Internal storage bucket initializer."""
        if not hasattr(cls._storage, "bucket"):
            cls._storage.bucket = {}
        return cls._storage.bucket

    @classmethod
    def put(cls, key: str, value: Any):
        """Inject a single variable into the UI state."""
        cls._get_bucket()[key] = value

    @classmethod
    def get(cls, key: str, default: Any = None) -> Any:
        """Read a variable from anywhere in the UI tree."""
        return cls._get_bucket().get(key, default)

    @classmethod
    def push(cls, context_dict: Dict[str, Any] = None, **kwargs):
        """
        Bulk insert data. Perfect for receiving Django/FastAPI contexts.
        Usage: Context.push(django_context) OR Context.push(user="Admin", theme="dark")
        """
        if context_dict:
            cls._get_bucket().update(context_dict)
        if kwargs:
            cls._get_bucket().update(kwargs)

    @classmethod
    def clear(cls, key:str|None=None):
        """
        Wipes the state. Must be called by the Router/Middleware
        at the end of the request.
        """
        if hasattr(cls._storage, "bucket"):
            if key in cls._storage.bucket.keys():
                del cls._storage.bucket[key]
            else:
                cls._storage.bucket.clear()
    #
    # def __enter__(self):
    #     """Allows scoped context injection using 'with Context():'"""
    #     # Snapshot the existing keys before entering the scope
    #     self._snapshot = set(self._get_bucket().keys())
    #     return self.__class__
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     """Automatically clears only the new keys added during the scope."""
    #     bucket = self._get_bucket()
    #     # Find and delete only the keys that were not in our snapshot
    #     keys_to_remove = [
    #         k for k in bucket.keys() if k not in getattr(self, "_snapshot", set())
    #     ]
    #     for k in keys_to_remove:
    #         del bucket[k]

    def __enter__(self):
        # 1. Take a SHALLOW COPY of the entire dictionary to preserve exact values
        self._snapshot = self._get_bucket().copy()

        # 2. Push any inline arguments passed during instantiation
        if self._inline_context:
            self.push(**self._inline_context)

        return self.__class__

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Completely restore the bucket to its exact state before the `with` block
        # This prevents both new keys from leaking AND existing keys from being permanently mutated.
        self._storage.bucket = self._snapshot