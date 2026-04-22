from src.probo.templates import ProboTemplateParser
import pytest
from probo.components.elements import Element

# Assuming the resolver is placed in probo.templates.resolver

# =====================================================================
# 1. FIXTURES & TEST DATA
# =====================================================================

# Test scenarios: (Scenario Name, Raw HTML, Expected Root Tag, Expected Root Attrs)
TEMPLATE_INPUTS = [
    (
        "simple_text",
        '<p id="main" class="text-bold">Hello World</p>',
        "p",
        {"id": "main", "class": "text-bold"},
    ),
    (
        "void_self_closing",
        '<img src="logo.png" alt="logo"/>',
        "img",
        {"src": "logo.png", "alt": "logo"},
    ),
    (
        "nested_elements",
        '<div data-role="wrapper"><span>Child text</span></div>',
        "div",
        {"data-role": "wrapper"},
    ),
    (
        "svg_tree",
        '<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40"/></svg>',
        "svg",
        {"viewBox": "0 0 100 100"},
    ),
]


@pytest.fixture
def parser():
    """Provides a fresh instance of the blazing-fast AST Resolver."""
    return ProboTemplateParser()


@pytest.fixture
def shared_el():
    """Provides a fresh Element pipeline for testing Light Node rendering."""
    return Element(is_list=True, use_deque=True)


# =====================================================================
# 2. JSON / AST PARSING TESTS
# =====================================================================


@pytest.mark.parametrize("scenario, raw_html, exp_tag, exp_attrs", TEMPLATE_INPUTS)
def test_parser_json_mode(parser, scenario, raw_html, exp_tag, exp_attrs):
    """Tests the raw native Python dictionary AST generation."""
    ast = parser.parse(raw_html, mode="json")

    # Assert it returns a list of dictionaries
    assert isinstance(ast, list)
    assert len(ast) == 1

    root_node = ast[0]
    assert root_node["tag"] == exp_tag
    assert root_node["attrs"] == exp_attrs

    # Assert structural integrity based on scenario
    if scenario == "void_self_closing":
        assert root_node["content"] is None
    elif scenario == "simple_text":
        assert root_node["content"] == "Hello World"
    elif scenario in ["nested_elements", "svg_tree"]:
        assert isinstance(root_node["content"], list)
        assert len(root_node["content"]) > 0


# =====================================================================
# 3. HEAVY SSDOM COMPILATION TESTS
# =====================================================================


@pytest.mark.parametrize("scenario, raw_html, exp_tag, exp_attrs", TEMPLATE_INPUTS)
def test_parser_heavy_mode(parser, scenario, raw_html, exp_tag, exp_attrs):
    """Tests compiling HTML directly into Heavy OOP Nodes with parent tracking."""
    heavy_tree = parser.parse(raw_html, mode="heavy")

    # Assert Object instantiation
    assert type(heavy_tree).__name__ == "HeavyNodeProxy"
    assert getattr(heavy_tree, "parsed_tag", None) == exp_tag
    assert getattr(heavy_tree, "attributes", {}) == exp_attrs

    # Test execution engine (Eager Render)
    # Heavy nodes own their own EL, so we can render them directly
    output = heavy_tree.render()
    output_str = "".join(output) if isinstance(output, list) else str(output)

    # The output should exactly match the logical structure of the input
    assert f"<{exp_tag}" in output_str

    # Verify parent tracking exists on nested children
    if scenario == "nested_elements":
        child_span = heavy_tree.content[0]
        assert child_span.parent == heavy_tree


# =====================================================================
# 4. LIGHT SSDOM COMPILATION TESTS
# =====================================================================


@pytest.mark.parametrize("scenario, raw_html, exp_tag, exp_attrs", TEMPLATE_INPUTS)
def test_parser_light_mode(parser, shared_el, scenario, raw_html, exp_tag, exp_attrs):
    """Tests compiling HTML directly into high-performance Light Nodes."""
    light_tree = parser.parse(raw_html, mode="light")

    # Assert Object instantiation
    assert type(light_tree).__name__ == "LightNodeProxy"
    assert getattr(light_tree, "parsed_tag", None) == exp_tag
    assert getattr(light_tree, "attributes", {}) == exp_attrs

    # Light nodes strictly shouldn't have parent pointers to save memory
    assert hasattr(light_tree, "parent")

    # Test execution engine (Eager Render)
    # Light nodes require a shared Element pipeline
    output = light_tree.render(shared_el)
    output_str = "".join(output) if isinstance(output, list) else str(output)

    assert f"<{exp_tag}" in output_str


# =====================================================================
# 5. CALLABLE / FACTORY MODE TESTS
# =====================================================================


def test_parser_callable_factory(parser, shared_el):
    """Tests the deferred execution factory mode."""
    raw_html = '<div id="container"><ul><li>Item 1</li></ul></div>'

    # Parse ONCE into a factory
    template_factory = parser.parse(raw_html, mode="callable")

    assert callable(template_factory)

    # Execute the factory multiple times targeting different architectures
    heavy_instance = template_factory(target_mode="heavy")
    light_instance = template_factory(target_mode="light")

    assert type(heavy_instance).__name__ == "HeavyNodeProxy"
    assert type(light_instance).__name__ == "LightNodeProxy"

    # Both should render to identical HTML despite different underlying memory structures
    heavy_html = "".join(heavy_instance.render())
    light_html = "".join(light_instance.render(shared_el))

    assert heavy_html == light_html
    assert "<li>Item 1</li>" in heavy_html


# =====================================================================
# 6. POST-PARSE SSDOM MANIPULATION TESTS
# =====================================================================


def test_parsed_heavy_node_manipulation(parser):
    """Tests that a parsed HeavyNode can be manipulated like a native Probo object."""
    raw_html = '<div id="box">Original Text</div>'

    # Parse into a HeavyNode
    node = parser.parse(raw_html, mode="heavy")

    # 1. Modify an existing attribute
    node.attr_manager.set_id("modified-box")

    # 2. Add a new attribute
    node.attr_manager.set_data("state","active")

    # 3. Append new content
    node.content.append(" and Appended Text")

    # Verify the modifications were successful
    assert node.attributes["Id"] == "modified-box"
    assert node.attributes["data-state"] == "active"
    assert "Original Text" in node.content
    assert " and Appended Text" in node.content


def test_parsed_light_node_manipulation(parser):
    """Tests that a parsed LightNode can be manipulated."""
    raw_html = '<button class="btn">Click</button>'

    # Parse into a LightNode
    node = parser.parse(raw_html, mode="light")

    # 1. Modify attributes
    node.attributes["class"] += " btn-primary"

    # 2. Overwrite content completely
    node.content = ["Clicked!"]

    # Verify the modifications
    assert node.attributes["class"] == "btn btn-primary"
    assert len(node.content) == 1
    assert node.content[0] == "Clicked!"
