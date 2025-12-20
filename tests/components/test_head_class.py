import pytest
from mui import Head  # Assuming this is where it lives
# You might need to import your specific tag helpers if Head uses them internally
# from mui import title, meta, link, script, style

@pytest.fixture
def header():
    """Returns a fresh Head instance."""
    return Head()

def test_head_initialization():
    """Test creating a head with initial content."""
    h = Head("<!-- Analytics -->")
    html = h.render()
    assert "<head>" in html
    assert "<!-- Analytics -->" in html
    assert "</head>" in html

def test_set_title(header):
    """Test adding a title."""
    header.set_title("My Awesome Site")
    
    html = header.render()
    assert "<title>My Awesome Site</title>" in html

def test_register_meta(header):
    """Test injecting meta tags."""
    header.register_meta(name="description", content="SEO Stuff")
    header.register_meta(charset="UTF-8")
    
    html = header.render()
    # Check standard meta
    assert '<meta name="description" content="SEO Stuff"' in html
    # Check charset (often void/self-closing depending on your renderer)
    assert 'charset="UTF-8"' in html

def test_register_link(header):
    """Test injecting CSS/Favicons."""
    header.register_link(rel="stylesheet", href="style.css")
    
    html = header.render()
    assert '<link rel="stylesheet" href="style.css"' in html

def test_register_script(header):
    """Test injecting JS files."""
    header.register_script(src="app.js", defer=True)
    
    html = header.render()
    assert '<script src="app.js" defer' in html
    # Scripts are not void, should close
    assert '</script>' in html

def test_register_inline_style(header):
    """Test injecting raw CSS."""
    css = "body { background: #000; }"
    header.register_style(css)
    
    html = header.render()
    assert f"<style>{css}</style>" in html

def test_head_accumulation(header):
    """
    Test that multiple registers accumulate correctly.
    This is critical for the 'Layout' use case.
    """
    header.set_title("Home")
    header.register_meta(name="author", content="Me")
    header.register_link(rel="canonical", href="/home")
    
    html = header.render()
    
    # Order might vary depending on implementation, but all must exist
    assert "<title>Home</title>" in html
    assert 'name="author"' in html
    assert 'rel="canonical"' in html

def test_head_overwrites_title():
    """
    Scenario: Base template sets title, Child template sets title.
    Expected: Only the LAST title renders.
    """
    h = Head()
    h.set_title("Default Title")
    h.set_title("New Page Title") # Should overwrite
    
    html = h.render()
    assert "<title>New Page Title</title>" in html
    assert "Default Title" not in html # Old one gone

def test_head_overwrites_meta():
    """
    Scenario: Overwriting a specific meta tag (description).
    """
    h = Head()
    h.register_meta(name="description", content="Old Desc")
    h.register_meta(name="author", content="Me") # Different key, should stay
    h.register_meta(name="description", content="New Desc") # Same key, overwrite
    
    html = h.render()
    assert 'content="New Desc"' in html
    assert 'content="Old Desc"' not in html
    assert 'name="author"' in html # Kept safe
