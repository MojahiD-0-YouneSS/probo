import pytest
from probo.components import ElementNodeMixin
import uuid
from typing import List, Optional, Callable, Any
# --- Test Infrastructure ---
class Node(ElementNodeMixin):
    def __init__(self, tag="div", id=None, classes=None):
        super().__init__()
        self.tag = tag
        self.id = id or str(uuid.uuid4())[:8]
        self.classes = classes or []

# --- Pytest Suite ---
@pytest.fixture
def complex_tree():
    """Builds a multi-branch tree for searching."""
    root = Node("html")
    body = Node("body")
    main = Node("main", id="main-content")
    nav = Node("nav", classes=["sidebar"])
    
    root.add(body)
    body.add(nav).add(main)
    
    for i in range(3):
        main.add(Node("section", id=f"sec-{i}"))
    
    return root, body, main, nav

def test_chaining_integrity():
    """Test if .add().add() actually builds a flat list of siblings."""
    parent = Node()
    parent.add(Node("a")).add(Node("b")).add(Node("c"))
    assert len(parent.children) == 3

def test_parent_linkage(complex_tree):
    """Verify child knows its parent and parent knows its child."""
    root, body, _, _ = complex_tree
    assert body.parent == root
    assert body in root.children

def test_migration_singleton(complex_tree):
    """CRITICAL: If a node is added to a new parent, it must leave the old one."""
    root, body, main, nav = complex_tree
    section = main.pop(main.children[0])
    
    nav.add(section) # Move section from main to nav
    
    assert section.parent == nav
    assert section not in main.children
    assert section in nav.children

def test_depth_logic(complex_tree):
    root, _, main, _ = complex_tree
    deep_child = main.children[0]
    assert root.get_tree_depth() == 0
    assert deep_child.get_tree_depth() == 3

def test_find_by_id(complex_tree):
    root, _, _, _ = complex_tree
    found = root.find(lambda n: n.id == "sec-2")
    assert found is not None
    assert found.tag == "section"

def test_find_all_by_tag(complex_tree):
    root, _, _, _ = complex_tree
    sections = root.find_all(lambda n: n.tag == "section")
    assert len(sections) == 3

def test_remove_orphan_logic(complex_tree):
    root, body, _, _ = complex_tree
    body.remove(root) # Attempt to remove something not there (should fail silently)
    assert len(body.children) == 2
    
    child = body.pop(body.children[0])
    assert child.parent is None
    assert len(body.children)==1

def test_find_non_existent(complex_tree):
    root = complex_tree[0]
    assert root.find(lambda n: n.tag == "blink") is None

def test_find_returns_first_occurrence():
    root = Node("div")
    root.add(Node("p", id="1")).add(Node("p", id="2"))
    found = root.find(lambda n: n.tag == "p")
    assert found.id == "1"

def test_self_reference_prevention():
    """Prevent a node from adding itself as a child."""
    n = Node()
    n.add(n)
    assert len(n.children) == 0

def test_complex_predicate(complex_tree):
    """Search using multiple attributes."""
    root = complex_tree[0]
    found = root.find(lambda n: n.tag == "nav" and "sidebar" in n.classes)
    assert found is not None

def test_deep_recursion():
    """Test 100 level deep nesting."""
    root = Node("0")
    current = root
    for i in range(1, 101):
        new_node = Node(str(i))
        current.add(new_node)
        current = new_node
    
    found = root.find(lambda n: n.tag == "100")
    assert found.get_tree_depth() == 100

def test_sibling_insertion():
    root = Node()
    root.add(Node("last"))
    root.add(Node("first"), index=0)
    assert root.children[0].tag == "first"

def test_find_all_empty_tree():
    n = Node()
    res = n.find_all(lambda x: False)
    assert res == []

def test_parent_of_root():
    root = Node()
    assert root.parent is None

def test_find_with_no_id_attribute():
    """Ensure search doesn't crash if an object lacks an attribute."""
    class WeirdObject: pass
    root = Node()
    root.add(WeirdObject())
    # Should handle objects without find/find_all methods gracefully
    assert root.find(lambda n: False) is None

def test_root_is_found_by_find_all():
    root = Node("html")
    assert root in root.find_all(lambda n: n.tag == "html")

def test_tree_breadth_stress():
    """1000 siblings at one level."""
    root = Node()
    for i in range(1000):
        root.add(Node(id=str(i)))
    assert len(root.children) == 1000
    assert root.find(lambda n: n.id == "999") is not None

def test_removing_already_removed_node():
    root = Node()
    c = Node()
    root.add(c)
    root.remove(c)
    root.remove(c) # Second time
    assert c.parent is None

def test_find_all_multiple_branches():
    root = Node("root")
    left = Node("div")
    right = Node("div")
    root.add(left).add(right)
    assert len(root.find_all(lambda n: n.tag == "div")) == 2
