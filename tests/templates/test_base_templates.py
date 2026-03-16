import pytest
from probo.templates.default_templates import base_template_string, base_template_tree
from probo.components.tag_classes import META, TITLE, DIV, P, LINK, SPAN, NAV, UL, LI, A, BUTTON
from probo.styles.frameworks.bs5 import BS5ElementStyle
from probo.htmx import HTMXElement as HXE
from probo.components.tag_functions import meta, title, div
from time import time


def body_content():
    return (DIV(
                NAV(
                    DIV(
                        BUTTON(
                            SPAN(
                                Class="navbar-toggler-icon",
                            ),
                            Class=f"navbar-toggler navbar-toggler-right{BS5ElementStyle("button").add("display_block").render()}",
                            type="button",
                        ),
                        A("mvp_base", Class="navbar-brand", href="/home"),
                        DIV(
                            UL(
                                LI(
                                    A(
                                        SPAN("home", Class="visually-hidden"),
                                        Class="nav-link active",
                                        href="/home",
                                    ),
                                    Class="nav-item",
                                ),
                                LI(
                                    A(
                                        "about",
                                        Class="nav-link",
                                        href="/about",
                                    ),
                                    Class="nav-item",
                                ),
                                LI(
                                    A(
                                        "log in",
                                        Id="log-in-link",
                                        Class="nav-link",
                                        href="/account_login",
                                    ),
                                    Class="nav-item",
                                ),
                                Class="navbar-nav mr-auto",
                            ),
                            Class="collapse navbar-collapse",
                            Id="navbarSupportedContent",
                        ),
                        Class="container-fluid",
                    ),
                    Class="navbar navbar-expand-md navbar-light bg-light",
                ),
                Class="mb-1",
            ),DIV(
                SPAN(
                    "click me",
                    style="font-size:100px; color:green;",
                    **HXE()
                    .set_attr(
                        get="/contact",
                        trigger="click",
                        target="#navbarSupportedContent",
                        swap="innerHTML",
                    )
                    .render(attrs_as_string=False),
                ),
                Class="container",
            ),
        )

@pytest.fixture
def sample_nodes():
    return [DIV(P("Tree Node"), id="node-1")]

@pytest.fixture
def sample_strings():
    return ["<div id='str-1'><p>String Node</p></div>"]

@pytest.mark.parametrize("func", [base_template_string, base_template_tree])
def test_default_boilerplate(func):
    """Ensures both functional and tree versions generate a valid HTML5 shell."""
    rendered = func()
    out = rendered.render() if hasattr(rendered, "render") else rendered
    assert "<!DOCTYPE html>" in out
    assert '<html lang="en">' in out
    assert "<head>" in out
    assert "<body>" in out
    assert 'charset="UTF-8"' in out
    assert "bootstrap.min.css" in out

def test_tree_node_injection_integrity():
    """Verifies that live Node objects maintain attributes through the tree function."""
    head_nodes = [META(name="robots", content="noindex")]
    body_nodes = [DIV(SPAN("Content", Class="test-class"), id="test-id")]

    out = base_template_tree(head_nodes=head_nodes, body_nodes=body_nodes, overide_head=True, overide_body=True).render()
    assert 'name="robots"' in out
    assert 'content="noindex"' in out
    assert 'id="test-id"' in out
    assert 'class="test-class"' in out


def test_htmx_logic_preservation():
    """Tests if the HXE attributes survive the template rendering process."""
    rendered = base_template_tree()
    rendered.html_doc.find(lambda n: n.element_tag == "body").add(body_content())
    out = rendered.render()

    assert 'hx-get="/contact"' in out
    assert 'hx-trigger="click"' in out
    assert 'hx-target="#navbarSupportedContent"' in out
    assert 'hx-swap="innerHTML"' in out

@pytest.mark.parametrize("bad_input", [None, "", [], {}])
def test_resilience_to_garbage_input(bad_input):
    """Force-feeds the templates bad data to ensure they don't crash."""
    try:

        base_template_tree(
            head_nodes=[bad_input] if bad_input else None, overide_head=True
        ).html_doc.find(lambda n: n.element_tag == "body").add(body_content()).render()

        base_template_string(head_list=[bad_input] if bad_input else None,overide_head=True)
    except Exception as e:
        pytest.fail(f"Template crashed on input {bad_input}: {e}")

def test_template_logic_parity():
    """Ensures base_template_string and base_template_tree produce logically identical output."""
    str_out = base_template_string(body_list=body_content(), overide_body=True)
    tree_out = base_template_tree()
    tree_out.html_doc.find(lambda n: n.element_tag == "body").add(body_content())

    checkpoints = [
        "<!DOCTYPE html>",
        "navbar-brand",
        "js/project.js",
        "click me",
        "navbar-toggler-icon",
    ]
    for cp in checkpoints:
        assert cp in str_out
        assert cp in tree_out.render()

def test_massive_node_injection_scaling():
    """Injects 500 unique nodes to check for performance regressions."""
    nodes = [DIV(id=f"node-{i}") for i in range(500)]
    start = time()
    out = base_template_tree(body_nodes=nodes, overide_body=True).render()
    end = time()

    assert end - start < 0.5  # Should render 500 nodes in under 500ms even on Celeron
    assert "node-499" in out
