from probo.components.fragment import frag
from probo import div
def test_fragment_coverage():
    """Specifically targets the 0% fragment.py file."""
    # Test Eager Fragment
    f = frag("A", "B")
    assert f == "AB"

    # Test Streaming Fragment
    f_stream = frag("A", "B", stream=True)
    assert list(f_stream) == ["A", "B"]

def test_fragment_deep_resolution():
    """Hits the recursive streaming paths in fragment.py."""

    # Test nested fragments and generators
    def gen_content():
        yield "Chunk 1"
        yield "Chunk 2"

    f = frag(div("Parent"), frag(gen_content(), stream=True), stream=True)

    output = list(f)
    assert "<div>Parent</div>" in output
    assert "Chunk 1" in output
    assert "Chunk 2" in output

def test_fragment_one_tree_multiple_parts():
    from probo import DIV,P,I
    tree = DIV(
        DIV("Header",P('somthing'), id="h"),
        DIV("Content",I('other thing'), id="c"),
        DIV("Footer", id="f")
    )
    # Mark fragments
    tree.children_nodes[0].frag_header = True
    tree.children_nodes[1].frag_content = True

    result = frag(tree, fragments=[lambda n:n.element_tag == 'p', lambda n:n.element_tag == 'i',])
    assert '<div id="h">Header</div>' not in result
    assert '<p>somthing</p>' in result
    assert '<i>other thing</i>' in result
    assert '<div>Content</div>' not in result
    assert '<div>Footer</div>' not in result

def test_fragment_multiple_trees_multiple_parts():
    from probo import DIV, SECTION, P
    tree1 = DIV(
        DIV("T1 Header"),
        P("T1 Content")
    )
    tree1.children_nodes[0].target_frag = True
    
    tree2 = SECTION(
        DIV("T2 Header",Id='header2'),
        P("T2 Content")
    )
    tree2.children_nodes[1].target_frag2 = True

    result = frag(tree1, tree2, fragments=[lambda n:n.element_tag == 'p', lambda n:n.attr_manager.get_id() == 'header2'])
    assert "T1 Header" not in result
    assert "T2 Content" in result
    assert "T1 Content" in result
    assert "T2 Header" in result
    assert '<p>T1 Content</p>' in result
    assert '<p>T2 Content</p>' in result
    assert '<div>T1 Header</div>' not in result
    assert '<div id="header2">T2 Header</div>' in result
