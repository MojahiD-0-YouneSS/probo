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
        self.content = []

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
    assert len(parent.node_children) == 3

def test_parent_linkage(complex_tree):
    """Verify child knows its parent and parent knows its child."""
    root, body, _, _ = complex_tree
    assert body.parent == root
    assert body in root.node_children

def test_migration_singleton(complex_tree):
    """CRITICAL: If a node is added to a new parent, it must leave the old one."""
    root, body, main, nav = complex_tree
    section = main.pop(main.node_children[0])
    
    nav.add(section) # Move section from main to nav
    
    assert section.parent == nav
    assert section not in main.node_children
    assert section in nav.node_children

def test_depth_logic(complex_tree):
    root, _, main, _ = complex_tree
    deep_child = main.node_children[0]
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
    assert len(body.node_children) == 2
    
    child = body.pop(body.node_children[0])
    assert child.parent is None
    assert len(body.node_children)==1

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
    assert len(n.node_children) == 0

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
    assert root.node_children[0].tag == "first"

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
    assert len(root.node_children) == 1000
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

def test_ssdom_navigation_properties(complex_tree):
    root, body, main, nav = complex_tree
    
    assert root.first_child == body
    assert root.last_child == body
    
    assert body.first_child == nav
    assert body.last_child == main
    
    assert nav.next_sibling == main
    assert main.previous_sibling == nav
    assert nav.previous_sibling is None
    assert main.next_sibling is None

def test_ssdom_ancestors(complex_tree):
    root, body, main, nav = complex_tree
    section = main.node_children[0]
    
    ancs = list(section.ancestors)
    assert ancs == [main, body, root]

def test_ssdom_append_prepend():
    parent = Node()
    child1 = Node("1")
    child2 = Node("2")
    child3 = Node("3")
    
    parent.append(child1, child2)
    assert parent.node_children == [child1, child2]
    
    parent.prepend(child3)
    assert parent.node_children == [child3, child1, child2]

def test_ssdom_insert_before_and_replace_with():
    parent = Node()
    c1 = Node("1")
    c3 = Node("3")
    parent.append(c1, c3)
    
    c2 = Node("2")
    parent.insert_before(c2, c3)
    assert parent.node_children == [c1, c2, c3]
    
    c4 = Node("4")
    c2.replace_with(c4)
    assert parent.node_children == [c1, c4, c3]
    assert c2.parent is None
    assert c4.parent == parent

def test_ssdom_clear_children():
    parent = Node()
    parent.append(Node("1"), Node("2"))
    assert len(parent.node_children) == 2
    parent.clear_children()
    assert len(parent.node_children) == 0

def test_ssdom_clone_node(complex_tree):
    root, body, main, nav = complex_tree
    
    # shallow clone
    cloned_nav = nav.clone_node(deep=False)
    assert cloned_nav is not nav
    assert cloned_nav.tag == nav.tag
    assert len(cloned_nav.node_children) == 0
    assert cloned_nav.parent is None
    
    # deep clone
    cloned_body = body.clone_node(deep=True)
    assert len(cloned_body.node_children) == len(body.node_children)
    assert cloned_body.node_children[0] is not nav
    assert cloned_body.node_children[0].tag == nav.tag

def test_ssdom_text_content():
    parent = Node()
    parent.append("Hello")
    child = Node()
    child.append("World!")
    parent.append(child)
    
    assert parent.text_content == "Hello World!"

def test_remove_with_callable():
    root = Node("root")
    target = Node("div")
    root.add(target)
    
    # Remove using a callable that finds the node by tag
    root.remove("div", lambda tag: root.find(lambda n: n.tag == tag))
    
    assert len(root.node_children) == 0
    assert target.parent is None

def test_pop_with_callable():
    root = Node("root")
    target = Node("span")
    root.add(target)
    
    # Pop using a callable
    popped = root.pop("span", lambda tag: root.find(lambda n: n.tag == tag))
    
    assert popped is target
    assert len(root.node_children) == 0
    assert target.parent is None

def test_ssdom_text_properties():
    parent = Node()
    parent.append("Direct text 1")
    child = Node()
    child.append("Inner text")
    parent.append(child)
    parent.append("Direct text 2")
    
    # text should only get direct string children
    assert parent.text == "Direct text 1Direct text 2"
    
    # inner_text should return a list of all texts recursively
    assert parent.inner_text == ["Direct text 1", "Inner text", "Direct text 2"]

def test_ssdom_creation_helpers():
    parent = Node()
    
    # create_element should instantiate an Element (or LightNode if is_light=True) and append it
    heavy_child = parent.create_element(tag="div", is_light=False)
    light_child = parent.create_element(tag="span", is_light=True)
    
    assert parent.get_child_count() == 2
    
    children_col = parent.get_children()
    assert len(children_col) == 2
    assert children_col.first is heavy_child
    assert children_col.last is light_child

def test_get_max_depth():
    root = Node("div")
    assert root.get_max_depth() == 0

    child1 = Node("span")
    child2 = Node("span")
    root.append(child1, child2)
    assert root.get_max_depth() == 1

    grandchild = Node("a")
    child1.append(grandchild)
    assert root.get_max_depth() == 2
    assert child1.get_max_depth() == 1
    assert child2.get_max_depth() == 0

    great_grandchild = Node("b")
    grandchild.append(great_grandchild)
    assert root.get_max_depth() == 3
