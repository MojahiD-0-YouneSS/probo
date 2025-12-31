import pytest
from src.probo.components.elements import Template
from src.probo import (
    div,
    span,
)
from src.probo.components.component import Component


# --- FIXTURES ---
@pytest.fixture
def base_layout():
    """
    Returns a standard Template with default slots.
    Structure: Header - Main - Footer
    """
    return Template(
        # Default components
        header=div("Default Header", id="header"),
        main=div("Default Content", id="main"),
        footer=div("Default Footer", id="footer"),
        # Separator for pretty printing (optional)
        separator="\n",
    )


# --- TESTS ---


def test_template_structure(base_layout):
    """
    Scenario: Render default template.
    Expected: DOCTYPE + html + head + body + components.
    """
    html = base_layout.render()

    assert "<!DOCTYPE html>" in html
    assert '<html lang="en">' in html
    assert "<head>" in html
    assert "<body>" in html

    # Check defaults
    assert "Default Header" in html
    assert "Default Content" in html
    assert "Default Footer" in html
    assert "</html>" in html


def test_swap_component(base_layout):
    """
    Scenario: Swap the 'main' slot with a new Component.
    Expected: Header/Footer remain, Main is replaced.
    """
    # New component to inject
    new_page = Component(name="Dashboard", template=div("Dashboard Stats"), state=None)

    # Perform the swap
    base_layout.swap_component(main=new_page)

    html = base_layout.render()

    assert "Default Header" in html  # Kept
    assert "Dashboard Stats" in html  # Swapped
    assert "Default Content" not in html  # Removed
    assert "Default Footer" in html  # Kept


def test_head_integration():
    """
    Scenario: Accessing and modifying the internal Head object.
    Expected: Meta tags added to the rendered head.
    """
    tmpl = Template()

    # Template should expose its Head object
    tmpl.head.set_title("My App")
    tmpl.head.register_meta(name="theme", content="dark")

    html = tmpl.render()
    assert "<title>My App</title>" in html
    assert 'name="theme"' in html


def test_swap_invalid_slot(base_layout):
    """
    Scenario: Trying to swap a slot that doesn't exist (e.g. 'sidebar').
    Expected: Should either raise error OR add it (depending on your design).
    Recommendation: Add it (Flexible Layouts).
    """
    sidebar = div("Sidebar Menu")
    base_layout.swap_component(sidebar=sidebar)

    html = base_layout.render()
    assert "Sidebar Menu" in html


def test_custom_separator():
    """
    Scenario: Using a custom separator (e.g. <hr>) between components.
    """
    tmpl = Template(item1=span("A"), item2=span("B"), separator="<hr>")

    # Render just the body content to check separator
    # (Assuming render logic puts separator between items)
    html = tmpl.render()
    assert "<span>A</span><hr><span>B</span>" in html
