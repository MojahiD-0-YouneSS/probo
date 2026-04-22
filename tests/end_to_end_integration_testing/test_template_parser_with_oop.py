import pytest
from probo.components.elements import Element
from probo import DIV
from probo.templates.parser import ProboTemplateParser
from probo.components.node import ProxyElement
from probo.components.light_tags import Ldiv
from probo.utility import ProboSourceString

# =====================================================================
# 1. GRAFTING TESTS (Injecting ASTs into SSDOM)
# =====================================================================


def test_ast_grafting_heavy_nodes():
    """Tests parsing HTML into HeavyNodes and appending them to an existing Heavy Tree."""
    # parser = ProboASTResolver()
    parser = ProboTemplateParser()

    # 1. Create living Root tree
    root_tree = DIV("Original Parent", id="root")

    # 2. Parse a raw string into Heavy SSDOM Nodes
    raw_html = '<div id="parsed-heavy">Parsed HTML</div>'
    parsed_ast_node = parser.parse(raw_html, mode="heavy")

    # 3. Graft it! (Append to the root tree's content)
    # Heavy Nodes use lists for content usually
    if isinstance(root_tree.content, tuple):
        root_tree.content = list(root_tree.content)
    root_tree.content.append(parsed_ast_node)

    # 4. Render the grafted tree
    output = "".join(root_tree.render())

    assert '<div id="root">' in output
    assert "Original Parent" in output
    assert '<div id="parsed-heavy">Parsed HTML</div>' in output


def test_ast_grafting_light_nodes():
    """Tests parsing HTML into LightNodes and appending them to a Light Tree."""
    shared_el = Element(is_list=True)
    # parser = ProboASTResolver()
    parser = ProboTemplateParser()

    # 1. Create living Light tree
    root_tree = Ldiv("Light Parent", id="root-light")

    # 2. Parse into Light SSDOM Nodes
    raw_html = '<div id="parsed-light">Parsed HTML</div>'
    parsed_ast_node = parser.parse(raw_html, mode="light")

    # 3. Graft it! (Light nodes use deques)
    root_tree.content.append(parsed_ast_node)

    # 4. Render with shared Element
    output = "".join(root_tree.render(shared_el))

    assert '<div id="root-light">' in output
    assert "Light Parent" in output
    assert '<div id="parsed-light">Parsed HTML</div>' in output


# =====================================================================
# 2. PROXY TEMPLATE ENGINE TESTS
# =====================================================================


def test_proxy_ast_lazy_evaluation():
    """
    Tests loading an AST callable into a ProxyElement.
    The proxy dynamically instantiates the AST and renders/streams it
    only when execution hits the proxy within the larger document.
    """
    parser = ProboTemplateParser()

    # 1. Parse an HTML template ONCE into a lazy factory (mode="callable")
    raw_html = '<div id="lazy-heavy">Lazy Parsed HTML</div>'
    ast_factory = parser.parse(raw_html, mode="callable")

    # 2. Setup the Proxy Element
    proxy = ProxyElement(tag="section",wrap_result=True)
    proxy.load_logic(ast_factory)

    # 3. Configure the Proxy to execute the factory and render the resulting SSDOM
    def _render_ast(factory):
        # Instantiate heavy nodes from the factory
        nodes = factory(target_mode="heavy")
        if not isinstance(nodes, list):
            nodes = [nodes]
        # Render the nodes and return the string
        return "".join("".join(n.render()) for n in nodes)

    proxy.load_render_logic(_render_ast)

    # 4. Configure the Proxy to execute the factory and yield the stream
    def _stream_ast(factory):
        nodes = factory(target_mode="heavy")
        if not isinstance(nodes, list):
            nodes = [nodes]
        for n in nodes:
            yield from n.stream() if hasattr(n, "stream") else n.render()

    proxy.load_stream_logic(_stream_ast)

    # 5. Drop the Proxy into a standard Heavy Page
    page = DIV(
        DIV("Header"),
        proxy,  # The proxy intercepts execution and translates the AST!
        DIV("Footer"),
        id="app",
    )
    # --- Test Eager Rendering ---
    render_output = page.render()
    assert "Header" in render_output
    assert "<section>" in render_output  # Proxy Wrapper Tag
    assert '<div id="lazy-heavy">Lazy Parsed HTML</div>' in render_output
    assert "</section>" in render_output
    assert "Footer" in render_output

    # --- Test Lazy Streaming ---
    stream_output = "".join(
        list(page.stream() if hasattr(page, "stream") else page.render())
    )
    assert "Header" in stream_output
    assert "<section>" in stream_output
    assert '<div id="lazy-heavy">Lazy Parsed HTML</div>' in stream_output
    assert "Footer" in stream_output

# =====================================================================
# 3. FUNCTIONAL GRAFTING & PROXY TESTS
# =====================================================================


def test_ast_grafting_heavy_func():
    """Tests parsing HTML into a Heavy Functional node and composing it."""
    from probo import div

    parser = ProboTemplateParser()

    # 1. Parse string into functional execution
    raw_html = '<div id="parsed-heavy-func">Parsed HTML</div>'
    parsed_ast_node = parser.parse(raw_html, mode="heavy")

    # 2. Graft it! (In functional API, we just pass the result as content)
    output = div("Original Parent", parsed_ast_node, id="root")
    output_str = "".join(output) if isinstance(output, list) else str(output)

    assert '<div id="root">' in output_str
    assert "Original Parent" in output_str
    assert '<div id="parsed-heavy-func">Parsed HTML</div>' in output_str


def test_ast_grafting_light_func():
    """Tests parsing HTML into Light Functional node and composing it."""
    from probo.components.light_tags import l_div

    shared_el = Element(is_list=True, use_deque=True)
    parser = ProboTemplateParser()

    # 1. Parse into light func node
    raw_html = '<div id="parsed-light-func">Parsed HTML</div>'
    parsed_ast_node = parser.parse(raw_html, mode="heavy")

    # 2. Graft via function composition
    output = l_div(shared_el, "Light Parent", parsed_ast_node, id="root-light")
    output_str = "".join(output) if isinstance(output, list) else str(output)

    assert '<div id="root-light">' in output_str
    assert "Light Parent" in output_str
    assert '<div id="parsed-light-func">Parsed HTML</div>' in output_str


def test_proxy_ast_functional_evaluation():
    """
    Tests loading an AST callable into a ProxyElement and rendering it
    inside a purely Functional SSDOM tree.
    """
    from probo import div

    parser = ProboTemplateParser()

    # 1. Parse ONCE into a lazy factory
    raw_html = '<div id="lazy-heavy-func">Lazy Parsed HTML</div>'
    ast_factory = parser.parse(raw_html, mode="callable")

    # 2. Setup the Proxy Element
    proxy = ProxyElement(tag="section",wrap_result=True)
    proxy.load_logic(ast_factory)

    # 3. Configure Proxy for functional rendering
    def _render_ast(factory):
        nodes = factory(target_mode="heavy")
        return ProboSourceString("".join(nodes)) if isinstance(nodes, list) else ProboSourceString(nodes.render())

    proxy.load_render_logic(_render_ast)
    print(type(proxy.render()))
    # 4. Drop the Proxy into a Functional page
    page_output = div(div("Header"), proxy, div("Footer"), id="app")

    # Verify the proxy dynamically executed the functional factory and merged perfectly
    render_output = (
        "".join(page_output) if isinstance(page_output, list) else str(page_output)
    )

    assert "Header" in render_output
    assert "<section>" in render_output
    assert '<div id="lazy-heavy-func">Lazy Parsed HTML</div>' in render_output
    assert "</section>" in render_output
    assert "Footer" in render_output

def test_proxy_ast_flight_unctional_evaluation():
    """
    Tests loading an AST callable into a ProxyElement and rendering it
    inside a purely Functional SSDOM tree.
    """
    from probo.components.light_tags import l_div
    shared_el = Element(is_list=True, use_deque=True)

    parser = ProboTemplateParser()

    # 1. Parse ONCE into a lazy factory
    raw_html = '<div id="lazy-heavy-func">Lazy Parsed HTML</div>'
    ast_factory = parser.parse(raw_html, mode="callable")

    # 2. Setup the Proxy Element
    proxy = ProxyElement(tag="section",wrap_result=True)
    proxy.load_logic(ast_factory)

    # 3. Configure Proxy for functional rendering
    def _render_ast(factory):
        nodes = factory(target_mode="heavy")
        return ProboSourceString("".join(nodes)) if isinstance(nodes, list) else ProboSourceString(nodes.render())

    proxy.load_render_logic(_render_ast)

    # 4. Drop the Proxy into a Functional page
    page_output = l_div(shared_el,l_div(shared_el,"Header"), proxy, l_div(shared_el,"Footer"), id="app")

    # Verify the proxy dynamically executed the functional factory and merged perfectly
    render_output = (
        "".join(page_output) if isinstance(page_output, list) else str(page_output)
    )

    assert "Header" in render_output
    assert "<section>" in render_output
    assert '<div id="lazy-heavy-func">Lazy Parsed HTML</div>' in render_output
    assert "</section>" in render_output
    assert "Footer" in render_output
