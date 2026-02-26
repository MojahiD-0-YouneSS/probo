import pytest
from probo.components.base import BaseHTMLElement
from probo.components.node import ElementNodeMixin
from probo.utility import render_attributes

# Mocking the required tags for testing
class MockDIV(BaseHTMLElement, ElementNodeMixin):
    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
    def render(self): return f"<Mockdiv>{self._get_rendered_content()}</Mockdiv>"

class MockSPAN(BaseHTMLElement, ElementNodeMixin):
    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
        
    def render(self): return f"<Mockspan>{self._get_rendered_content()}</Mockspan>"

def test_initialization_vs_manual_add():
    """Verify MockDIV(MockSPAN()) is equivalent to Mockdiv.add(Mockspan)."""
    # Pattern A: Initialization
    Mockspan_a = MockSPAN("Hello")
    Mockdiv_a = MockDIV(Mockspan_a)

    # Pattern B: Manual Add
    Mockspan_b = MockSPAN("Hello")
    Mockdiv_b = MockDIV()
    Mockdiv_b.add(Mockspan_b)

    assert len(Mockdiv_a.node_children) == len(Mockdiv_b.node_children)
    assert Mockdiv_a.node_children[0].tag == Mockdiv_b.node_children[0].tag
    assert Mockspan_a.parent == Mockdiv_a
    assert Mockspan_b.parent == Mockdiv_b

def test_mixed_content_initialization():
    """Verify strings are ignored by the tree but kept in content, 
    while Tags are linked."""
    container = MockDIV(
        "Raw Text",
        MockSPAN("Nested Tag"),
        "More Text"
    )

    # The tree should only care about the MockSPAN node
    assert len(container.node_children) == 1
    assert isinstance(container.node_children[0], MockSPAN)
    
    # But rendering should include everything
    rendered = container.render()
    assert "Raw Text" in rendered
    assert "<Mockspan>Nested Tag</Mockspan>" in rendered

def test_deep_initialization_chain():
    """Test deep nesting in a single constructor call."""
    tree = MockDIV(MockDIV(MockDIV(MockSPAN("Deep"))))
    
    # Traverse down
    level_1 = tree.node_children[0]
    level_2 = level_1.node_children[0]
    level_3 = level_2.node_children[0]

    assert level_3.get_tree_depth() == 3
    assert isinstance(level_3, MockSPAN)

def test_find_works_on_tag_classes():
    """Verify that search logic works on real Tag instances."""
    app = MockDIV(
        MockDIV(id="header"),
        MockDIV(MockSPAN("Target"), id="main"),
        MockDIV(id="footer")
    )

    found = app.find(lambda n: n.attributes.get("id") == "main")
    assert found is not None
    assert isinstance(found.node_children[0], MockSPAN)

# --- advanced Tests ---

class IMG(BaseHTMLElement, ElementNodeMixin):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
    def render(self):
        return f"<img {render_attributes('img',self.attributes)}/>"

class SVG(BaseHTMLElement, ElementNodeMixin):
    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
    def render(self):
        return f"<svg {render_attributes('svg', self.attributes)}>{self._get_rendered_content()}</svg>"

class MockG(BaseHTMLElement, ElementNodeMixin):
    def __init__(self, *content, **attrs):
        super().__init__(*content, **attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children(content)
    def render(self):
        return f"<g {render_attributes('g', self.attributes)}>{self._get_rendered_content()}</g>"

class PATH(BaseHTMLElement, ElementNodeMixin):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        ElementNodeMixin.__init__(self)
        self._set_node_children([],True)
    def render(self):
        # SVG paths are often self-closing
        return f"<path {render_attributes('path', self.attributes)} />"

def test_void_tag_initialization():
    """1. Ensure void tags like IMG initialize without children."""
    image = IMG(src="logo.png")
    assert len(image.node_children) == 0
    assert image.parent is None

def test_void_tag_in_tree():
    """2. Ensure void tags can be children of standard tags."""
    container = MockDIV(IMG(src="thumb.jpg"))
    assert isinstance(container.node_children[0], IMG)
    assert container.node_children[0].parent == container

def test_void_tag_depth():
    """3. Verify depth logic works for void tags."""
    tree = MockDIV(MockDIV(IMG()))
    assert tree.node_children[0].node_children[0].get_tree_depth() == 2

def test_svg_tree_structure():
    """4. Test complex SVG nesting (SVG -> G -> PATH)."""
    # Assuming G and PATH classes exist similarly to SVG
    icon = SVG(
        PATH(d="M10 10L20 20")
    )
    assert len(icon.node_children) == 1
    assert icon.node_children[0].parent == icon

def test_svg_multiple_children():
    """5. SVG with multiple shapes."""
    icon = SVG(PATH(id="p1"), PATH(id="p2"))
    assert len(icon.node_children) == 2
    assert icon.find(lambda n: n.attributes.get("id") == "p2") is not None

def test_illegal_nesting_logic():
    """6. What happens if we try to add a child to a void tag? 
    (Technically possible in the tree, but should be handled in ProboUI)."""
    image = IMG()
    image.add(MockDIV())
    assert len(image.node_children) == 0# The tree allows it; render() decides the output.
    assert image.render() == "<img />" # The tree allows it; render() decides the output.

def test_find_all_svg_paths():
    """7. Find all paths inside a complex document."""
    doc = MockDIV(
        SVG(PATH(id="1")),
        MockDIV(SVG(PATH(id="2")))
    )
    paths = doc.find_all(lambda n: n.__class__.__name__ == "PATH")
    assert len(paths) == 2

def test_self_closing_svg_in_Mockdiv():
    """8. Ensure SVG components render correctly inside standard tags."""
    ui = MockDIV(SVG(PATH()))
    rendered = ui.render()
    assert "<svg" in rendered
    assert "<path" in rendered

def test_void_tag_sibling_migration():
    """9. Move an IMG from one MockDIV to another."""
    img = IMG()
    d1, d2 = MockDIV(img), MockDIV()
    d2.add(img)
    assert img.parent == d2
    assert len(d1.node_children) == 1
    img2 = IMG()
    d3, d4 = MockDIV(img2), MockDIV()
    d4.add(d3.pop(img2))
    assert img2.parent == d4
    assert len(d3.node_children) == 0

def test_svg_namespace_attributes():
    """10. Test SVG specific attributes like viewBox."""
    icon = SVG(viewBox="0 0 100 100")
    assert icon.attributes["viewBox"] == "0 0 100 100"

def test_br_tag_repetition():
    """11. Test multiple BR tags as siblings."""
    # Assuming BR class exists
    line_break = MockDIV("Text", MockSPAN(), MockSPAN(), "More Text")
    # Tree only tracks the 2 BR nodes
    assert len(line_break.node_children) == 2

def test_mixed_standard_and_svg_search():
    """12. Search for a specific class that exists in both HTML and SVG."""
    ui = MockDIV(
        MockDIV(classes=["icon-wrapper"]),
        SVG(PATH(classes=["icon-wrapper"]))
    )
    matches = ui.find_all(lambda n: "icon-wrapper" in n.attributes.get("classes", []))
    assert len(matches) == 2

def test_svg_text_content():
    """13. SVG tags can contain text (e.g., <text> tags)."""
    # Assuming TEXT class for SVG exists
    svg_text = SVG("Hello SVG")
    assert "Hello SVG" in svg_text.render()

def test_remove_svg_node():
    """14. Remove a path from an SVG."""
    p = PATH()
    icon = SVG(p)
    icon.remove(p)
    assert len(icon.node_children) == 0
    assert p.parent is None

def test_deep_svg_nesting_depth():
    """15. Extremely deep SVG nesting."""
    root = SVG()
    curr = root
    for _ in range(10):
        new_g = MockG() # Group tag
        curr.add(new_g)
        curr = new_g
    assert curr.get_tree_depth() == 10

def test_void_tag_with_id_search():
    """16. Find an IMG by ID."""
    doc = MockDIV(IMG(id="hero-img"))
    found = doc.find(lambda n: n.attributes.get("id") == "hero-img")
    assert isinstance(found, IMG)

def test_svg_fragment_rendering():
    """17. Render just the SVG part of a larger tree."""
    doc = MockDIV(id="wrapper")
    icon = SVG(id="my-svg")
    doc.add(icon)
    assert "<svg" in icon.render()
    assert "<Mockdiv" not in icon.render()

def test_complex_document_integrity():
    """18. One massive test: Nesting everything."""
    page = MockDIV(
        MockDIV(IMG(id="avatar")),
        SVG(PATH(), PATH()),
        MockDIV(MockSPAN())
    )
    # Total nodes: 1(MockDIV) + 1(IMG) + 1(SVG) + 1(G) + 2(PATH) + 1(MockDIV) + 1(BR) = 8
    # find_all(True) returns the caller + all descendants
    assert len(page.find_all(lambda n: True)) == 8

def test_void_tag_illegal_nesting_integrity():
    """
    Test that adding content to a void tag (IMG) updates the tree 
    but does not affect the final rendered HTML.
    """
    # 1. Setup a void tag and a block element
    image = IMG(src="probo.png", id="hero")
    illegal_child = MockDIV("I should not be here", id="ghost")
    
    # 2. Attempt to add the block to the void tag
    image.add(illegal_child)
    
    # --- Tree Check ---
    # The Mixin should still track the relationship (DOM-like behavior)
    assert len(image.node_children) == 0
    assert illegal_child.parent != image
    
    # --- Search Check ---
    # You should still be able to find the ghost element via the tree
    found = image.find(lambda n: getattr(n, "id", None) == "ghost")
    assert found is None
    
    # --- Render Check (The Truth) ---
    # The render method of IMG must be strict and ignore self.node_children
    rendered_html = image.render()
    # The output should be a clean void tag, ignoring the nested DIV
    assert rendered_html == '<img src="probo.png" id="hero"/>'
    assert "I should not be here" not in rendered_html
    assert "<div" not in rendered_html