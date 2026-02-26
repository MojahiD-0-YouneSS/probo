import pytest
from probo.components.node import ComponentNode
from probo.components.component import Component


# Mock Component for testing if necessary,
# or use your actual Component class if already integrated.

@pytest.fixture
def root_node():
    return Component(name="Root")


@pytest.fixture
def child_node():
    return Component(name="Child")


# --- Tree Structure & Relationship Tests ---

def test_initial_node_state(root_node):
    """Verifies that a new node has no parent and depth 0."""
    assert root_node.get_parent is None
    assert root_node.depth == 0
    assert root_node.children_count == 0


def test_single_parent_child_linking(root_node, child_node):
    """Ensures setting a parent correctly updates depth and parent count."""
    child_node._set_parent(root_node)
    assert child_node.get_parent == root_node
    assert child_node.depth == 1
    assert root_node.children_count == 1


def test_multi_level_depth(root_node):
    """Validates depth propagation across multiple generations."""
    child = Component(name="Child")
    grandchild = Component(name="Grandchild")

    child._set_parent(root_node)
    grandchild._set_parent(child)

    assert root_node.depth == 0
    assert child.depth == 1
    assert grandchild.depth == 2


def test_children_count_accumulation(root_node):
    """Ensures the children_count reflects the number of direct children."""
    for i in range(5):
        c = Component(name=f"Child_{i}")
        c._set_parent(root_node)

    assert root_node.children_count == 5


def test_get_root_method(root_node):
    """Tests the ability to find the top-level node from any depth."""
    child = Component(name="C")
    grandchild = Component(name="GC")

    child._set_parent(root_node)
    grandchild._set_parent(child)

    assert grandchild.get_root() == root_node
    assert child.get_root() == root_node


# --- Hierarchy & Safety Tests ---

def test_is_descendant_of(root_node):
    """Verifies hierarchy checking logic."""
    child = Component(name="C")
    grandchild = Component(name="GC")

    child._set_parent(root_node)
    grandchild._set_parent(child)

    assert grandchild.is_descendant_of(root_node) is True
    assert grandchild.is_descendant_of(child) is True
    assert child.is_descendant_of(root_node) is True
    assert root_node.is_descendant_of(child) is False


def test_self_parenting_prevention(root_node):
    """Ensures a node cannot be its own parent."""
    root_node._set_parent(root_node)
    assert root_node.get_parent is None
    assert root_node.children_count == 0


def test_depth_is_read_only(root_node):
    """Ensures depth cannot be modified directly (it should be internal logic)."""
    with pytest.raises(AttributeError):
        root_node.depth = 10


# --- Integration Tests (Simulating add_child) ---

def test_add_child_updates_node_tree(root_node, child_node):
    """Simulates your Component.add_child logic to ensure integration works."""
    # This assumes your add_child calls child._set_parent(self)
    root_node.add_child(child_node)

    assert child_node.get_parent == root_node
    assert root_node.children_count == 1


def test_multiple_parents_scenario(root_node):
    """Tests if moving a node to a new parent updates correctly."""
    # Note: Current logic increments parent. Check if you need a "remove_child"
    # logic if you plan on moving nodes between parents dynamically.
    new_root = Component(name="NewRoot")
    child = Component(name="MovingChild")

    child._set_parent(root_node)
    child._set_parent(new_root)

    assert child.get_parent == new_root
    assert child.depth == 1
    assert new_root.children_count == 1