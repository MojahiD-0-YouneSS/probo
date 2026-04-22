import pytest
import threading
from probo.context.context import ProboContextProvider


@pytest.fixture(autouse=True)
def reset_context():
    """
    Fixture to ensure a clean slate before and after every test.
    Prevents tests from accidentally sharing state.
    """
    ProboContextProvider.clear()
    yield
    ProboContextProvider.clear()


def test_bucket_initialization():
    """Test that the internal bucket initializes correctly if missing."""
    # Force delete the bucket attribute to simulate a fresh thread/start
    if hasattr(ProboContextProvider._storage, "bucket"):
        delattr(ProboContextProvider._storage, "bucket")

    bucket = ProboContextProvider._get_bucket()
    assert isinstance(bucket, dict)
    assert bucket == {}


def test_put_and_get():
    """Test single key insertion and retrieval, including default fallbacks."""
    ProboContextProvider.put("theme", "dark")

    assert ProboContextProvider.get("theme") == "dark"
    assert ProboContextProvider.get("missing_key") is None
    assert ProboContextProvider.get("missing_key", "fallback") == "fallback"


def test_push_bulk_data():
    """Test bulk injection using dicts and kwargs."""
    # 1. Test with dict only
    ProboContextProvider.push({"user_id": 1, "role": "admin"})
    assert ProboContextProvider.get("user_id") == 1

    # 2. Test with kwargs only
    ProboContextProvider.push(lang="en", status="active")
    assert ProboContextProvider.get("lang") == "en"

    # 3. Test with both
    ProboContextProvider.push({"dict_key": "dict_val"}, kwarg_key="kwarg_val")
    assert ProboContextProvider.get("dict_key") == "dict_val"
    assert ProboContextProvider.get("kwarg_key") == "kwarg_val"


def test_clear_specific_key():
    """Test clearing a single specific key from the context."""
    ProboContextProvider.put("keep_me", "yes")
    ProboContextProvider.put("remove_me", "no")

    ProboContextProvider.clear(key="remove_me")

    assert ProboContextProvider.get("keep_me") == "yes"
    assert ProboContextProvider.get("remove_me") is None


def test_clear_all_or_missing_key():
    """
    Test that calling clear() without a key, or with a missing key,
    clears the entire bucket (based on your specific logic flow).
    """
    ProboContextProvider.put("k1", "v1")
    ProboContextProvider.put("k2", "v2")

    # Path A: Clear without a key
    ProboContextProvider.clear()
    assert ProboContextProvider.get("k1") is None

    # Path B: Clear with a missing key (hits the 'else' block in clear)
    ProboContextProvider.put("k3", "v3")
    ProboContextProvider.clear(key="does_not_exist")
    assert ProboContextProvider.get("k3") is None


def test_clear_uninitialized_bucket():
    """Test that clearing an uninitialized storage doesn't throw an error."""
    if hasattr(ProboContextProvider._storage, "bucket"):
        delattr(ProboContextProvider._storage, "bucket")

    # This should pass silently, hitting the 'if hasattr' bypass
    ProboContextProvider.clear()


def test_context_manager_success():

    ProboContextProvider.put("global_var1", "active1")
    ProboContextProvider.put("global_var2", "active2")
    ProboContextProvider.put("global_var3", "active3")
    """Test the 'with Context():' scope pattern."""
    with ProboContextProvider() as ctx:
        ctx.put("scoped_var", "active")
        assert ctx.get("scoped_var") == "active"

    # The __exit__ method should have automatically cleared the context
    assert ProboContextProvider.get("scoped_var") is None
    assert ProboContextProvider.get("global_var1") == "active1"
    assert ProboContextProvider.get("global_var2") == "active2"
    assert ProboContextProvider.get("global_var3") == "active3"


def test_context_manager_exception():
    """
    Test that the context manager still clears the bucket
    if an exception occurs inside the 'with' block.
    This also covers the exc_type, exc_val, exc_tb variables in __exit__.
    """
    try:
        with ProboContextProvider() as ctx:
            ctx.put("error_scoped", "active")
            raise ValueError("Simulated Exception")
    except ValueError:
        pass

    # Must still be cleared despite the crash!
    assert ProboContextProvider.get("error_scoped") is None


def test_thread_safety():
    """
    Crucial Test: Ensure that the threading.local() storage isolates
    state between concurrent threads (simulating multiple web requests).
    """

    def worker(thread_name, results_dict):
        # Put data in this thread's local context
        ProboContextProvider.put("active_thread", thread_name)

        import time

        time.sleep(0.05)  # Force threads to overlap in time

        # Read it back and store it in the results map
        results_dict[thread_name] = ProboContextProvider.get("active_thread")

    results = {}

    # Spin up two concurrent "requests"
    t1 = threading.Thread(target=worker, args=("Thread-A", results))
    t2 = threading.Thread(target=worker, args=("Thread-B", results))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Thread A should only see Thread A's data, and same for B
    assert results["Thread-A"] == "Thread-A"
    assert results["Thread-B"] == "Thread-B"
