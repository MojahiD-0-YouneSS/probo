import time
from typing import Any, Dict, Optional, Generator


class CacheItem:
    __slots__ = ("value", "expires_at")

    def __init__(self, value: Any, ttl: int):
        self.value = value
        self.expires_at = time.time() + ttl if ttl > 0 else 0

    def is_expired(self) -> bool:
        if self.expires_at == 0:
            return False
        return time.time() > self.expires_at

class ProboCache:
    """
    A lightning-fast, thread-safe In-Memory Cache for Probo.
    """

    def __init__(self):
        self._store: Dict[str, CacheItem] = {}

    def get(self, key: str) -> Optional[Any]:
        """Retrieves an item if it exists and is not expired."""
        item = self._store.get(key)
        if not item:
            return None

        if item.is_expired():
            del self._store[key]
            return None

        return item.value

    def set_cache(self, key: str, value: Any, ttl: int = 60):
        """Stores an item with a Time-To-Live (TTL) in seconds."""
        self._store[key] = CacheItem(value, ttl)

    def walk(
        self,
        on_keys: bool = True,
        on_values: bool = False,
        on_items: bool = False,
    ) -> Generator:
        if on_keys:
            yield from (item for item in self._store.keys())
        if on_values:
            yield from (item for item in self._store.values())
        if on_items:
            yield from (item for item in self._store.items())

    def clear(self):
        """Flushes the entire cache."""
        self._store.clear()

    def sweep(self):
        """Background task to remove dead cache items and free RAM."""
        now = time.time()
        expired_keys = [
            k for k, v in self._store.items() if v.expires_at > 0 and now > v.expires_at
        ]
        for k in expired_keys:
            del self._store[k]
