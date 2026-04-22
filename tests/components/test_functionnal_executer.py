from src.probo.components.executer import ProboFunctionalExecuter, tuplizer as _
from src.probo import (div,h1,a,DIV)
from src.probo.components.light_tags import (l_div,Ldiv)
from probo.components.elements import Element
import pytest
import functools
# --- Test Suite ---


def test_root_initialization():
    """Verify the root nodecorrectly with default flags."""
    exe = ProboFunctionalExecuter(div, id="main")
    result = exe.execute()
    assert result == '<div id="main"></div>'


def test_basic_nesting():
    """Verify simple one-level nesting."""
    exe = ProboFunctionalExecuter(div, id="root")
    exe.nest("root", "body", div, Class="container")
    result = exe.execute()
    assert result == '<div id="root"><div class="container"></div></div>'


def test_anonymous_leaf_addition():
    """Verify add_to correctly appends leaf nodes."""
    exe = ProboFunctionalExecuter(div)
    exe.add_to("root", h1, "Hello World")
    result = exe.execute()
    assert "<h1>Hello World</h1>" in result


def test_dependency_injection_for_light_tags():
    """CRITICAL: Verify EL is automatically injected into l_ tags."""
    shared_el = Element()
    exe = ProboFunctionalExecuter(div).include_dependency(EL=shared_el)
    exe.add_to("root", l_div, "Light Content")

    result = exe.execute()
    # The second child (the l_div) should have the EL in its kwargs
    assert result == "<div><div>Light Content</div></div>"


def test_no_injection_for_heavy_tags():
    """Verify standard tags don't get EL injected."""
    shared_el = Element()
    exe = ProboFunctionalExecuter(div).include_dependency(EL=shared_el)
    exe.add_to("root", div, "Heavy Content")

    result = exe.execute()
    assert result == "<div><div>Heavy Content</div></div>"


def test_user_override_of_default_flags():
    """Verify users can override native flags like 'stream'."""
    exe = ProboFunctionalExecuter(div, stream=True)
    exe.add_to("root", div, "No Stream", stream=False)

    result = exe.execute()

    assert "".join(list(result)) == "<div><div>No Stream</div></div>"

def test_deep_nesting_paths():
    """Verify multi-level path resolution."""
    exe = ProboFunctionalExecuter(div, id="0")
    exe.nest("root", "1", div, id="1")
    exe.nest("root.1", "2", div, id="2")
    exe.add_to("root.1.2", div,"Terminal Leaf")

    result = exe.execute()
    assert (
        '<div id="0"><div id="1"><div id="2"><div>Terminal Leaf</div></div></div></div>'
        == result
    )


def test_multiple_children_at_same_path():
    """Verify paths can hold multiple leaf and branch children."""
    exe = ProboFunctionalExecuter(div)
    exe.add_to("root", h1, "First")
    exe.add_to("root", h1, "Second")
    result = exe.execute()
    assert result == "<div><h1>First</h1><h1>Second</h1></div>"


def test_invalid_path_raises_error():
    """Verify targeting a non-existent path raises ValueError."""
    exe = ProboFunctionalExecuter(div)
    with pytest.raises(ValueError, match="Path 'ghost' not found"):
        exe.add_to("ghost", div)


def test_chimera_paradigm_safety():
    """Verify mixing Heavy (div) and Light (l_div) functions works natively."""
    el = Element()
    exe = ProboFunctionalExecuter(div).include_dependency(EL=el)
    exe.nest("root", "heavy", div)
    exe.add_to("root.heavy", l_div, "I am light")

    result = exe.execute()
    # Path: root -> heavy (div) -> light (l_div)
    assert "div" in result
    assert result.count("div") == 6


def test_lazy_execution_via_partial():
    """Verify _prepare_node_callable returns a functools.partial object."""
    exe = ProboFunctionalExecuter(div)
    partial_obj = exe._prepare_node_callable(div, {"id": "test"})
    assert isinstance(partial_obj, functools.partial)
    # Execute the partial to ensure it produces the expected node
    node = partial_obj()
    assert node == """<div id="test"></div>"""
    assert node.count('div') == 2


def test_dependency_override():
    """Verify a user can override the natively injected EL."""
    shared_el = Element()
    custom_el = Element()
    exe = ProboFunctionalExecuter(div).include_dependency(EL=shared_el)
    exe.add_to("root", l_div, "Override", EL=custom_el)

    result = exe.execute()
    assert result == '<div><div>Override</div></div>'


def test_content_ordering():
    """Verify content passed at nest time and add_to time preserves order."""
    exe = ProboFunctionalExecuter(div, "Start")
    exe.add_to("root", "End")
    result = exe.execute()
    assert result == "<div> Start End</div>"


def test_root_attribute_persistence():
    """Verify root-level attributes are preserved."""
    exe = ProboFunctionalExecuter(div, Class="app-root")
    result = exe.execute()
    assert 'class="app-root"' in result


def test_complex_tree_snapshot():
    """A full integration snapshot test."""
    el = Element()
    builder = ProboFunctionalExecuter(div, id="app")
    builder.include_dependency(EL=el)

    builder.nest("root", "nav", div, Class="navbar")
    builder.add_to("root.nav", h1, "Probo")

    builder.nest("root", "main", l_div, Class="container")
    builder.add_to("root.main", "Hello from Light Node")

    result = builder.execute()
    expected = (
        '<div id="app">'
        '<div class="navbar"><h1>Probo</h1></div>'
        '<div class="container">Hello from Light Node</div>'
        "</div>"
    )
    # Note: Mock tag order of attrs depends on dict order; we check for components
    assert '<div id="app"' in result
    assert '<div class="navbar"' in result
    assert '<div class="container"' in result
    assert "Hello from Light Node" in result
    assert expected == result


def test_node_reusability():
    """Verify we can execute the same builder multiple times."""
    exe = ProboFunctionalExecuter(div)
    exe.add_to("root", "Hi")
    res1 = exe.execute()
    res2 = exe.execute()
    assert res1 == res2 == "<div>Hi</div>"


def test_nested_path_validity_on_multiple_branches():
    """Verify we can nest multiple branches under the same parent."""
    exe = ProboFunctionalExecuter(div)
    exe.nest("root", "left", div)
    exe.nest("root", "right", div)
    exe.add_to("root.left", "L")
    exe.add_to("root.right", "R")
    result = exe.execute()
    assert "<div>L</div><div>R</div>" in result


def test_large_flat_path_list():
    """Ensure the flat dictionary approach handles many paths efficiently."""
    exe = ProboFunctionalExecuter(div)
    for i in range(100):
        exe.nest("root", f"n{i}", div)
    result = exe.execute()
    assert result.count('<div>') == 101 # plus root


def test_tag_name_deduction():
    """Ensure the injector correctly identifies l_ tags even if they are partials."""
    # This tests the logic: hasattr(tag, '__name__')
    exe = ProboFunctionalExecuter(div)
    assert exe._prepare_node_callable(l_div, {}).func == l_div
    assert exe._prepare_node_callable(div, {}).func == div


def test_empty_content_handling():
    """Verify nodes with no contentorrectly."""
    exe = ProboFunctionalExecuter(div)
    exe.nest("root", "empty", div)
    result = exe.execute()
    assert "<div><div></div></div>" == result


def test_nested_path_validity_on_multiple_branches_using_magic_methods():
    """Verify we can nest multiple branches under the same parent."""
    exe = ProboFunctionalExecuter(div)
    exe / ("root", "left", div)
    exe / ("root", "right", div)
    exe + ("root.left", "L")
    exe + ("root.right", "R")
    result = exe.execute()
    assert "<div>L</div><div>R</div>" in result


def test_dsl_tuplizer_basic_addition():
    """Verify that `+ _(...)` successfully adds an element to the root."""
    exe = ProboFunctionalExecuter(div, id="app")

    # Notice how clean this is! No dictionaries.
    exe += _(h1, "Welcome to Probo", Class="header", data_id="123")

    result = exe.execute()
    assert (
        '<div id="app"><h1 class="header" data-id="123">Welcome to Probo</h1></div>'
        == result
    )


def test_dsl_tuplizer_smart_nesting():
    """Verify that `/ _('path', 'name', tag)` correctly creates a nested branch."""
    exe = ProboFunctionalExecuter(div)

    # 1. Smart Nesting: 3+ arguments with a string name -> calls .nest()
    exe /= _("root", "sidebar", div, id="side")

    # 2. Smart Adding: 2+ arguments with a tag -> calls .add_to()
    exe /= _("root.sidebar", a, "Home", href="/home")

    result = exe.execute()
    assert '<div><div id="side"><a href="/home">Home</a></div></div>' == result


def test_dsl_tuplizer_chaining():
    """Verify that the operators can be cleanly chained together."""
    shared_el = Element()
    exe = ProboFunctionalExecuter(div, id="main").include_dependency(EL=shared_el)

    (
        exe
        + _(h1, "Title")
        / _("root", "nav", div, Class="navbar")
        / _("root.nav", l_div, "Light Link", Class="nav-item")
    )

    result = exe.execute()
    # verify heavy title, heavy nav, light nested child
    assert (
        '<div id="main"><h1>Title</h1><div class="navbar"><div class="nav-item">Light Link</div></div></div>'
        == result
    )


def test_init_content_handling():
    """Verify that content passed directly into __init__ is preserved."""
    exe = ProboFunctionalExecuter(div, h1("Init Title"), id="app")
    exe += _(div, "Appended Content")

    result = exe.execute()
    assert (
        '<div id="app"><h1>Init Title</h1><div>Appended Content</div></div>' == result
    )


def test_heavy_func_with_return_flags():
    """
    Verify that heavy functions correctly accept custom flags like
    return_list and return_deque, and that they don't leak into the HTML.
    """
    exe = ProboFunctionalExecuter(div, id="main-app")

    # Pass the internal rendering flags using the DSL kwargs
    exe + _(div, "List Mode Content", return_list=True)
    list_div = exe.find(div, attrs={"return_list": True})

    exe + _(div, "Deque Mode Content", return_deque=True)
    deque_div = exe.find(div,attrs={'return_deque':True})

    # Add a control node for comparison
    exe + _(div, "Standard Content")
    standard_div = exe.find(div,content="Standard Content")

    result = exe.execute()
    # 1. Verify the Executer passed the kwargs perfectly to the node
    child_list = list_div[0]["node"]
    child_deque = deque_div[0]["node"]
    child_standard = standard_div[0]["node"]

    assert child_list['attrs'].get("return_list") is True, "return_list flag not passed!"
    assert (
        child_deque['attrs'].get("return_deque") is True
    ), "return_deque flag not passed!"
    assert child_standard['attrs'].get("return_list") is None, "Default should be False!"

    assert "return-list" not in result
    assert "return-deque" not in result
    assert "List Mode Content" in result
    assert "Deque Mode Content" in result


def test_ast_find_and_mutate_utility():
    """
    Verify that the `find()` utility successfully locates nodes by tag, attrs,
    and content, and that modifying the returned results mutates the AST safely.
    """
    exe = ProboFunctionalExecuter(div, id="main-app")

    # Setup some nodes
    exe += _(div, "List Mode Content", return_list=True, Class="test-flag-list")
    exe += _(div, "Deque Mode Content", return_deque=True, Class="test-flag-deque")
    exe += _(div, "Standard Content")

    # Deeply nested nodes
    exe /= _("root", "sidebar", div, Class="sidebar-dark")
    exe /= _("root.sidebar", a, "Home Link", href="/")

    # 1. Find by Attributes
    list_nodes = exe.find(attrs={"return_list": True})
    assert len(list_nodes) == 1
    assert "List Mode Content" in list_nodes[0]["node"]["content"]
    assert list_nodes[0]["type"] == "anonymous"

    # 2. Find by Tag (using the actual function)
    a_nodes = exe.find(tag=a)
    assert len(a_nodes) == 1
    assert a_nodes[0]["node"]["attrs"]["href"] == "/"

    # 3. Find by Content Substring
    deque_nodes = exe.find(content="Deque Mode")
    assert len(deque_nodes) == 1
    assert deque_nodes[0]["node"]["attrs"]["return_deque"] is True

    # 4. Find Named Branch by String Name
    sidebar_nodes = exe.find(tag="div", attrs={"Class": "sidebar-dark"})
    assert len(sidebar_nodes) == 1
    assert sidebar_nodes[0]["type"] == "branch"
    assert sidebar_nodes[0]["path"] == "root.sidebar"

    # 5. MUTATION TEST: Alter the AST via the found reference
    list_nodes[0]["node"]["attrs"]["class"] = "mutated-via-find"
    a_nodes[0]["node"]["content"] = ["Mutated Home Link"]

    result = exe.execute()

    # Verify mutations took effect before the final render
    assert 'class="mutated-via-find"' in result
    assert "Mutated Home Link" in result


def test_executer_with_heavy_class_tag():
    """Verify that Heavy OOP classes work seamlessly in the Executer."""
    exe = ProboFunctionalExecuter(DIV, id="root-class")
    exe += _(DIV, "Nested Heavy Class", Class="nested")

    result = exe.execute()
    rendered = result.render()

    assert '<div id="root-class">' in rendered
    assert '<div class="nested">Nested Heavy Class</div>' in rendered


def test_executer_with_div_tag():
    """Verify that Light OOP classes work in the Executer and render correctly when EL is provided."""
    shared_el = Element()
    exe = ProboFunctionalExecuter(div, id="main").include_dependency(EL=shared_el)

    exe /= _("root", "light_branch", Ldiv, data_id="light-1")
    exe /= _("root.light_branch", DIV, "Inner Heavy")

    result = exe.execute()

    # Ldiv requires EL during render

    assert '<div data-id="light-1">' in result
    assert "<div>Inner Heavy</div>" in result


def test_class_and_func_hybrid_dsl():
    """Verify the DSL effortlessly mixes functions, heavy classes, and light classes."""
    exe = ProboFunctionalExecuter(div, use_EL=True,id="hybrid-root")

    (
        exe
        + _(div, "Func Child")
        / _("root", "light_wrap", Ldiv, Class="light",)
        / _("root.light_wrap", h1, "Title inside Light")
    )

    result = exe.execute()

    assert '<div id="hybrid-root">' in result
    assert "<div>Func Child</div>" in result
    assert (
        '<div class="light"><h1>Title inside Light</h1></div>'
        in result

    )
