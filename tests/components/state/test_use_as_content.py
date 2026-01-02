from src.probo.components.state import ElementState



def test_render_static():
    """
    Scenario: Data exists, but display_it=False.
    Expected: Empty string (No Render).
    """
    # 1. Define Rules: explicit Kill Switch
    # 2. Define Element: Pointing to valid data
    es = ElementState(
        element="div",
        s_state="Hello Static",
        key_as_content=True,
    )
    result = es.render()
    assert result == "<div>Hello Static</div>"

def test_render_static_iterable():
    """
    Scenario: Data exists, but display_it=False.
    Expected: Empty string (No Render).
    """
    # 1. Define Rules: explicit Kill Switch
    # 2. Define Element: Pointing to valid data
    es = ElementState(
        element="div",
        s_state=["Hello","Static"],
        key_as_content=True,
        i_state=True
    )
    result = es.render()
    assert result == "<div>Hello</div><div>Static</div>"

def test_render_dynamic():
    """
    Scenario: Data exists, but display_it=False.
    Expected: Empty string (No Render).
    """
    # 1. Define Rules: explicit Kill Switch
    # 2. Define Element: Pointing to valid data
    es = ElementState(
        element="div",
        s_state="Admin User",
        key_as_content=True,
    )
    result = es.render()
    assert result == "<div>Admin User</div>"


def test_render_dynamic_iterable():
    """
    Scenario: Data exists, but display_it=False.
    Expected: Empty string (No Render).
    """
    # 1. Define Rules: explicit Kill Switch
    # 2. Define Element: Pointing to valid data
    es = ElementState(
        element="div",
        s_state=["Admin","User"],
        key_as_content=True,
        i_state=True
    )
    result = es.render()
    assert result == "<div>Admin</div><div>User</div>"

