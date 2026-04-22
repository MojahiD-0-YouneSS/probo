import pytest
import sys
from types import ModuleType
from unittest.mock import MagicMock

# Assuming your mixin is saved here, adjust if needed
from probo.components.node import ElementMutatorMixin


# ==========================================
# MOCKS AND FIXTURES
# ==========================================


class DummyNode(ElementMutatorMixin):
    """A concrete class to test the mixin behaviors."""

    pass


@pytest.fixture
def mock_element_engine(monkeypatch):
    """
    Mocks the heavy 'Element' class from probo.components.elements
    so we can test the fallback 'Root Spawning' logic without loading
    the entire typewriter engine.
    """

    class MockElement:
        def __init__(self, is_list=False):
            self.is_list = is_list
            self.deque_called = False

        def use_deque(self):
            self.deque_called = True

    # Ensure the target module exists in sys.modules to prevent ImportError
    if "probo.components.elements" not in sys.modules:
        sys.modules["probo.components.elements"] = ModuleType(
            "probo.components.elements"
        )

    # Patch the Element class inside that module
    monkeypatch.setattr("probo.components.elements.Element", MockElement, raising=False)

    return MockElement


# ==========================================
# TESTS
# ==========================================


def test_initialization():
    """Tests the default state of the mutator."""
    node = DummyNode(use_list=True, custom_data="test")

    assert node._el_instance is None
    assert node.use_list is True
    assert node.use_deque is False
    assert node._share_element is True
    assert node.element_data == {"custom_data": "test"}


def test_el_is_attached_and_bind_unbind():
    """Tests binding, unbinding, and checking attachment status."""

    class MockParentEngine:
        is_list = True
        _use_deque = True  # Note the underscore to match your getattr logic

    node = DummyNode()
    assert node.el_is_attached() is False

    # Bind
    node.bind_element(MockParentEngine())
    assert node.el_is_attached() is True
    assert node.use_list is True
    assert node.use_deque is True
    assert node._el_instance.__class__ == MockParentEngine

    # Unbind
    node.unbind()
    assert node.el_is_attached() is False
    assert node._el_instance is None


def test_bind_element_no_deque_flag():
    """Tests binding an element that does not have the _use_deque attribute."""

    class MockParentEngineBasic:
        is_list = False
        # No _use_deque defined

    node = DummyNode(use_deque=True)  # Start True
    node.bind_element(MockParentEngineBasic())

    # Should default to False based on your getattr fallback
    assert node.use_deque is False


def test_toggle_share_element():
    """Tests the fluid API for toggling the share element flag."""
    node = DummyNode()
    res = node.toggle_share_element(False)

    assert res == node  # Verifies method chaining works
    assert node._share_element is False


def test_delegate_render_conditions_full_tree():
    """Tests broadcasting flags down to children and resetting caches."""
    child1 = DummyNode()

    # A mock child that DOES NOT have delegate_render_conditions
    # This hits the 'if hasattr' bypass branch in your loop
    child2 = object()

    root = DummyNode()
    root.node_children = [child1, child2]
    root._el_instance = "Stale_Engine"

    # Act
    res = root.delegate_render_conditions(use_list=True, use_deque=True)

    # Assert Root
    assert res == root
    assert root.use_list is True
    assert root.use_deque is True
    assert root._el_instance is None  # Cache must be cleared

    # Assert Child 1 (Recursive)
    assert child1.use_list is True
    assert child1.use_deque is True


def test_delegate_render_conditions_missing_attrs():
    """
    CRITICAL COVERAGE: Tests the edge case where the node is missing
    its expected attributes to ensure the hasattr() checks work safely.
    """
    node = DummyNode()

    # Delete attributes to force the hasattr checks to fail
    del node.use_list
    del node.use_deque
    del node._el_instance

    node.delegate_render_conditions(use_list=True, use_deque=True)

    # Attributes should not have been recreated
    assert not hasattr(node, "use_list")
    assert not hasattr(node, "use_deque")
    assert not hasattr(node, "_el_instance")


# ==========================================
# EL PROPERTY (LAZY PROPAGATION) TESTS
# ==========================================


def test_el_property_returns_cached():
    """Tests Condition 1: Returning the existing instance if sharing is enabled."""
    node = DummyNode()
    node._el_instance = "Cached_Engine"

    assert node.EL == "Cached_Engine"


def test_el_property_skips_cache_if_not_sharing(mock_element_engine):
    """
    Tests that turning off _share_element bypasses the cache
    and spawns a brand new root instance.
    """
    node = DummyNode()
    node._el_instance = "Cached_Engine"
    node.toggle_share_element(False)

    el = node.EL

    # Should NOT be the cached one
    assert el != "Cached_Engine"
    assert isinstance(el, mock_element_engine)

    # Root Spawning logic toggles sharing back to True at the end
    assert node._share_element is True


def test_el_property_climbs_to_parent():
    """Tests Condition 2: Climbing up to the parent's EL property."""

    class MockParent(DummyNode):
        @property
        def EL(self):
            return "Parents_Engine"

    parent = MockParent(use_list=True, use_deque=True)

    child = DummyNode(use_list=False, use_deque=False)
    child.parent = parent  # Attach parent

    el = child.EL

    assert el == "Parents_Engine"
    # Child should inherit the high-performance flags from the parent
    assert child.use_list is True
    assert child.use_deque is True
    assert child._el_instance == "Parents_Engine"


def test_el_property_parent_has_no_el(mock_element_engine):
    """
    Tests Condition 2 Edge Case: Parent exists but lacks the EL property.
    Should fallback to Condition 3 (Root Spawning).
    """
    child = DummyNode()
    child.parent = object()  # Has no EL property

    el = child.EL
    assert isinstance(el, mock_element_engine)


def test_el_property_spawns_root_node(mock_element_engine):
    """
    Tests Condition 3: No parent, no cache. Must spawn the Engine.
    Tests both use_list and use_deque triggers.
    """
    node = DummyNode(use_list=True, use_deque=True)

    # Act
    el = node.EL

    # Assert
    assert isinstance(el, mock_element_engine)
    assert el.is_list is True
    assert el.deque_called is True
    assert node._share_element is True
    assert node._el_instance == el
