import pytest
from probo.components.node import ElementNodeMixin, DataPipeLineMixin, ElementMutatorMixin
from probo.components.base import BaseHTMLElement

class MockNode(DataPipeLineMixin,ElementNodeMixin,  ElementMutatorMixin,BaseHTMLElement):
    def __init__(self, *content, **kwargs):
        # Extract data_pipeline, strict_data, custom_retriever out of kwargs

        # Now kwargs is safe to pass down to BaseHTMLElement as HTML attributes
        super().__init__(*content, **kwargs)
        self.extract_pipeline_args(kwargs)
        self._set_node_children(content)

        self.resolve_pipeline_variables()
    def render(self):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                return ""
        # Simple mock render that just joins string content
        return "".join(str(c) for c in self.content)

    def stream(self,batch=50):
        if self.has_unresolved_pipeline_vars:
            if not self.resolve_pipeline_variables(swap_vars=True):
                return ""
        # Simple mock render that just joins string content
        yield "".join(str(c) for c in self.content)

def test_data_pipeline_initialization():
    node = MockNode(data_pipeline={"theme": "dark", "version": 1})
    assert node.get_data("theme") == "dark"
    assert node.get_data("version") == 1
    assert node.get_data("non_existent") is None

def test_data_pipeline_policies():
    root = MockNode(data_pipeline={"root_var": "root_val"})
    root.provide_data("public_key", "pub_val", policy="pub")
    root.provide_data("private_key", "pri_val", policy="pri")
    root.provide_data("protected_key", "pro_val", policy="pro")

    child = MockNode()
    root.add(child)

    grandchild = MockNode()
    child.add(grandchild)

    # 1. Public policy (accessible everywhere)
    assert root.get_data("public_key") == "pub_val"
    assert child.get_data("public_key") == "pub_val"
    assert grandchild.get_data("public_key") == "pub_val"

    # 2. Private policy (accessible only by the node itself)
    assert root.get_data("private_key") == "pri_val"
    assert child.get_data("private_key") is None
    assert grandchild.get_data("private_key") is None

    # 3. Protected policy (accessible by self and direct children, but not grandchildren)
    assert root.get_data("protected_key") == "pro_val"
    assert child.get_data("protected_key") == "pro_val"
    assert grandchild.get_data("protected_key") is None

def test_variable_swapping_in_content():
    root = MockNode(data_pipeline={"username": "Alice", "role": "Admin"})
    
    # We use a set containing a single string for pipeline variable replacement
    child = MockNode("Hello, ", {"username"}, " - ", {"role"})
    root.add(child)
    
    # Before rendering, the content contains the sets
    assert {"username"} in child.content
    assert child.has_pipeline_vars is True

    # Render triggers the variable replacement
    html = child.render()
    
    # Output should substitute the variables
    assert "Hello," in html
    assert "Alice" in html
    assert "Admin" in html
    
    # The original content is modified, replacing the set with the string
    assert {"username"} not in child.content

def test_variable_swapping_missing_data_default():
    # strict_data=False (Default): variable replaced with empty string
    root = MockNode(data_pipeline={"username": "Alice"})
    child = MockNode("Hello, ", {"username"}, " (", {"missing_var"}, ")")
    root.add(child)
    
    html = child.render()
    assert "Alice" in html
    assert "()" in html  # missing_var should be replaced with ""

def test_variable_swapping_missing_data_strict_mode():
    # strict_data=True: drop the whole node if a variable is missing
    root = MockNode(data_pipeline={"username": "Alice"})
    child = MockNode("Hello, ", {"missing_var"}, strict_data=True)
    root.add(child)
    
    html = child.render()
    
    # Because 'missing_var' is missing and strict_data=True, ProxyElement aborts render 
    # and returns empty string.
    assert html == ""
    
def test_fetching_data_from_ancestor_nodes():
    # Explicit test for getting data from other nodes up the tree
    root = MockNode(data_pipeline={"global_theme": "dark", "app_name": "ProboUI"})
    parent = MockNode(data_pipeline={"section": "dashboard"})
    child = MockNode()
    
    root.add(parent)
    parent.add(child)
    
    # Child should be able to get data from its parent
    assert child.get_data("section") == "dashboard"
    
    # Child should also be able to get data from the root (grandparent)
    assert child.get_data("global_theme") == "dark"
    assert child.get_data("app_name") == "ProboUI"
    
    # Data not in the tree should return None
    assert child.get_data("non_existent") is None
