import pytest
from probo import DIV, P, SPAN, BUTTON, INPUT, FORM

def test_random_custom_attrs():
    """Test custom_attrs=True (immediate children) and custom_attrs='global' (whole tree) for random attributes"""
    # Immediate children
    container = DIV(
        P("Child 1", **{"data-random-xyz": "value1"}),
        SPAN("Child 2", **{"data-another": "value2"}),
        DIV("Child 3", P("Deep child", **{"data-ignored": "should-fail-if-not-global"})),
        custom_attrs=True,
        **{"data-parent": "parent-val"}
    )
    
    html = container.render()
    assert 'data-parent="parent-val"' in html
    assert 'data-random-xyz="value1"' in html
    assert 'data-another="value2"' in html
    
    # Global tree
    root = DIV(
        DIV(
            P("Deep child", **{"data-deep": "deep-val"}),
        ),
        custom_attrs='global',
        **{"data-root": "root-val"}
    )
    
    html_root = root.render()
    assert 'data-root="root-val"' in html_root
    assert 'data-deep="deep-val"' in html_root

def test_alpinejs_attributes():
    """Test using custom_attrs='global' for Alpine.js attributes"""
    component = DIV(
        BUTTON("Toggle", **{"@click": "open = !open"}),
        DIV(
            SPAN("Content to toggle"),
            **{"x-show": "open", "x-transition": ""}
        ),
        INPUT(**{"x-model": "searchQuery"}),
        custom_attrs='global',
        **{"x-data": "{ open: false, searchQuery: '' }"}
    )
    
    html = component.render()
    assert 'x-data="{ open: false, searchQuery: \'\' }"' in html
    assert '@click="open = !open"' in html
    assert 'x-show="open"' in html
    assert 'x-transition' in html
    assert 'x-model="searchQuery"' in html

def test_hyperscript_attributes():
    """Test using custom_attrs='global' for Hyperscript attributes"""
    ui = DIV(
        BUTTON("Click Me", **{"__": "on click toggle .active on #target"}),
        DIV("Target", id="target", **{"__": "on intersection(intersecting) having intersecting then add .visible"}),
        custom_attrs='global',
        **{"__": "on load log 'loaded'"}
    )
    
    html = ui.render()
    assert '_="on load log \'loaded\'"' in html
    assert '_="on click toggle .active on #target"' in html
    assert '_="on intersection(intersecting) having intersecting then add .visible"' in html

def test_unpoly_attributes():
    """Test using custom_attrs='global' for Unpoly attributes"""
    ui = DIV(
        FORM(
            INPUT(type="text", name="query"),
            **{"up-submit": "", "up-target": ".result"}
        ),
        DIV("Result here", Class="result", **{"up-hungry": ""}),
        custom_attrs='global',
    )
    
    html = ui.render()
    assert 'up-submit' in html
    assert 'up-target=".result"' in html
    assert 'up-hungry' in html
