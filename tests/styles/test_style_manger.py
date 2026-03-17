import pytest
from probo.styles.style_manager import StyleManager
from probo import DIV


def test_direct_assignment():
    """Test basic property assignment and hyphen conversion."""
    attrs = {}
    sm = StyleManager(attrs)
    sm.color = "red"
    sm.background_color = "blue"
    sm.font_size = "16px"
    
    # Check internal storage
    assert sm.color == "red"
    assert sm.background_color == "blue"
    assert sm.font_size == "16px"
    
    # Check rendered output
    render = sm.render
    assert "color:red" in render
    assert "background-color:blue" in render
    assert "font-size:16px" in render

def test_bi_directional_sync():
    """Verify that StyleManager updates the owner's attribute dictionary."""
    attrs = {"id":"test"}
    sm = StyleManager(attrs)
    sm.display = "flex"
    sm.render # Trigger sync
    
    assert "style" in attrs
    assert "display:flex" in attrs["style"]

def test_parsing_existing_style_string():
    """Test that the manager correctly imports existing style strings."""
    attrs = {"style":"color:green; margin-top:10px;"}
    sm = StyleManager(attrs)
    
    assert sm.color == "green"
    assert sm.margin_top == "10px"
    
    # Add new and check merge
    sm.padding = "5px"
    assert "color:green" in sm.render
    assert "padding:5px" in sm.render

def test_parsing_messy_strings():
    """Test robustness against malformed or messy style strings."""
    attrs = {"style":" color:red ;;  background:blue; invalid_pair ; "}
    sm = StyleManager(attrs)
    
    assert sm.color == "red"
    assert sm.background == "blue"
    # Verify it didn't crash on invalid_pair or double semicolons
    assert len(sm._styles) == 2

def test_removal_and_chaining():
    """Test property removal and fluid API chaining."""
    attrs = {}
    sm = StyleManager(attrs)
    sm.color = "white"
    sm.opacity = "0.5"
    sm.render
    sm.remove("color").remove("opacity")
    assert sm.render == ""
    assert attrs["style"] == ""

def test_tag_class_integration():
    """Test usage inside a real ProboUI Tag class."""
    node = DIV("Content", Id="btn")
    node.style_manager.background_color = "black"
    node.style_manager.color = "white"
    node.style_manager.render
    print(node.attributes)
    print(node.style_manager._styles)
    print(node.style_manager._owner_attrs)

    html = node.render()
    assert 'id="btn"' in html
    assert 'style="background-color:black; color:white;"' in html

def test_complex_values():
    """Test handling of complex CSS values like calc, variables, and quotes."""
    sm = StyleManager({})
    sm.width = "calc(100% - 20px)"
    sm.font_family = "'Roboto', sans-serif"
    sm.box_shadow = "0 2px 4px rgba(0,0,0,0.1)"
    
    render = sm.render
    assert "width:calc(100% - 20px)" in render
    assert "font-family:'Roboto', sans-serif" in render

def test_overriding_behavior():
    """Test that re-setting a property updates the existing one."""
    sm = StyleManager({})
    sm.margin = "10px"
    sm.margin = "20px"
    
    assert sm.margin == "20px"
    assert sm.render.count("margin:") == 1

def test_empty_manager_sync():
    """Verify that an empty manager clears the style attribute."""
    attrs = {"style":"color:red;"}
    sm = StyleManager(attrs)
    sm.remove("color")
    sm.render # Sync
    
    assert attrs["style"] == ""

def test_attribute_access_consistency():
    """Ensure both snake_case and hyphenated-case work for removal/access."""
    sm = StyleManager({})
    sm.background_color = "red"
    
    assert sm.background_color == "red"
    assert sm._styles["background-color"] == "red"
    
    sm.remove("background-color")
    assert "background-color" not in sm._styles


def test_node_style_override():
    """Test overriding initial styles via the manager (Scenario 1)."""
    # Start with blue color
    node = DIV("Content", style="color:blue;")
    
    # Override via manager
    node.style_manager.color = "red"
    
    html = node.render()
    # Verify the new style is present and the old one is gone
    assert 'style="color:red;"' in html
    assert 'color:blue' not in html

def test_node_style_clearance():
    """Test adding/removing styles until empty (Scenario 2)."""
    node = DIV("Content")
    
    # Add style
    node.style_manager.margin = "10px"
    assert 'style="margin:10px;"' in node.render()
    
    # Remove style
    node.style_manager.remove("margin")
    
    html = node.render()
    # The style attribute should be empty or entirely removed from the tag
    assert 'style="margin:10px;"' not in html
    assert 'style=""' in html