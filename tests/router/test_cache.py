import pytest
import time
from probo.router.cache import CacheItem, ProboCache

# ==========================================
# TEST 1: CacheItem Data Structure
# ==========================================


def test_cache_item_initialization_finite():
    """Tests items with a standard Time-To-Live (TTL)."""
    now = time.time()
    item = CacheItem("data", ttl=60)

    assert item.value == "data"
    assert item.expires_at >= now + 60
    assert item.is_expired() is False


def test_cache_item_initialization_infinite():
    """Tests items with TTL of 0 or less (Immortal items)."""
    # 0 TTL
    item_zero = CacheItem("data", ttl=0)
    assert item_zero.expires_at == 0
    assert item_zero.is_expired() is False

    # Negative TTL
    item_negative = CacheItem("data", ttl=-50)
    assert item_negative.expires_at == 0
    assert item_negative.is_expired() is False


def test_cache_item_expiration(monkeypatch):
    """Mocks time to ensure expiration logic calculates correctly."""
    item = CacheItem("data", ttl=10)

    # Mock time to 20 seconds in the future
    original_time = time.time
    monkeypatch.setattr("probo.router.cache.time.time", lambda: original_time() + 20)

    assert item.is_expired() is True


# ==========================================
# TEST 2: ProboCache Core Operations
# ==========================================


@pytest.fixture
def cache():
    """Fixture to provide a clean cache instance for each test."""
    return ProboCache()


def test_cache_set_and_get_valid(cache):
    """Tests storing and retrieving a valid, unexpired item."""
    cache.set_cache("my_key", "my_value", ttl=60)
    assert cache.get("my_key") == "my_value"


def test_cache_get_missing_key(cache):
    """Tests retrieving a key that doesn't exist."""
    assert cache.get("missing_key") is None


def test_cache_get_expired_item(cache, monkeypatch):
    """
    Tests that requesting an expired item returns None
    AND automatically purges the dead item from the store.
    """
    cache.set_cache("stale_key", "stale_value", ttl=10)

    # Fast-forward time by 20 seconds
    original_time = time.time
    monkeypatch.setattr("probo.router.cache.time.time", lambda: original_time() + 20)

    # Accessing it should return None
    assert cache.get("stale_key") is None
    # It should have been deleted from the internal dictionary
    assert "stale_key" not in cache._store


def test_cache_clear(cache):
    """Tests flushing the entire cache map."""
    cache.set_cache("k1", "v1")
    cache.set_cache("k2", "v2")

    assert len(cache._store) == 2
    cache.clear()
    assert len(cache._store) == 0


# ==========================================
# TEST 3: Garbage Collection (Sweep)
# ==========================================


def test_cache_sweep(cache, monkeypatch):
    """Tests the background RAM-freeing task."""
    cache.set_cache("immortal", "val", ttl=0)  # Never expires
    cache.set_cache("survivor", "val", ttl=60)  # Expires in 60s
    cache.set_cache("dead", "val", ttl=10)  # Expires in 10s

    # Fast forward time by 20 seconds
    original_time = time.time
    monkeypatch.setattr("probo.router.cache.time.time", lambda: original_time() + 20)

    # Run the background sweeper
    cache.sweep()

    # Check internal store
    assert "immortal" in cache._store  # Kept (expires_at == 0)
    assert "survivor" in cache._store  # Kept (not expired yet)
    assert "dead" not in cache._store  # Swept away


# ==========================================
# TEST 4: The Walker Generator
# ==========================================


def test_cache_walk(cache):
    """Tests all boolean flag combinations of the walk() generator."""
    cache.set_cache("k1", "v1")
    cache.set_cache("k2", "v2")

    # 1. on_keys (Default behavior)
    keys = list(cache.walk())
    assert keys == ["k1", "k2"]

    # 2. on_values
    values = list(cache.walk(on_keys=False, on_values=True))
    assert len(values) == 2
    assert values[0].value == "v1"
    assert values[1].value == "v2"

    # 3. on_items
    items = list(cache.walk(on_keys=False, on_items=True))
    assert len(items) == 2
    assert items[0][0] == "k1"
    assert items[0][1].value == "v1"

    # 4. Multi-flag (edge case: someone turns on multiple flags)
    multi = list(cache.walk(on_keys=True, on_values=True))
    assert len(multi) == 4  # 2 keys + 2 value objects
    assert "k1" in multi
