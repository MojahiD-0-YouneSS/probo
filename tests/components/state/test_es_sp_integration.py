import pytest
from src.probo.components.state import ElementState, StateProps, ComponentState

# --- FIXTURES ---


@pytest.fixture
def data_store():
    """Simulates ComponentState data (s_data/d_data)."""
    return {"static_title": "Hello Static", "dynamic_user": "Admin User"}


@pytest.fixture
def props_context():
    """Simulates Global Context (User, Flags)."""
    return {"is_logged_in": True, "role": "admin", "theme": "dark"}


# --- TESTS ---


def test_render_blocked_by_kill_switch(data_store, props_context):
    """
    Scenario: Data exists, but display_it=False.
    Expected: Empty string (No Render).
    """
    # 1. Define Rules: explicit Kill Switch
    rules = StateProps(display_it=False)
    # 2. Define Element: Pointing to valid data
    es = ElementState(
        element="div",
        s_state="static_title",
        props=rules,  # Attach rules
    )
    cs = ComponentState(
        es,
        s_data=data_store,
        **props_context,
    )
    # 3. Execute (Pass both Data Store and Props Context)
    # Assuming signature: resolve_content(s_data, d_data, context_props)
    result = cs.resolved_template(es.placeholder)
    assert result == ""  # Should be empty, not <div>Hello Static</div>


def test_render_blocked_by_requirement(data_store, props_context):
    """
    Scenario: Data exists, but a required prop is missing/wrong.
    Expected: Empty string.
    """
    # Rule: Render only if theme is 'light' (Context has 'dark')
    rules = StateProps(required=True, prop_equals={"theme": "light"})

    es = ElementState(element="span", s_state="", d_state="dynamic_user", props=rules)
    cs = ComponentState(
        es,
        s_data=data_store,
        **props_context,
    )
    result = cs.resolved_template(es.placeholder)

    assert result == ""  # Blocked by theme mismatch


def test_render_allowed_when_rules_met(data_store, props_context):
    """
    Scenario: Rules pass AND Data exists.
    Expected: Rendered HTML.
    """
    # Rule: Render if role is admin
    rules = StateProps(required=True, prop_equals={"role": "admin"})

    es = ElementState(element="h1", s_state="static_title", props=rules)

    cs = ComponentState(
        es,
        s_data=data_store,
        incoming_props=props_context,
    )
    # 3. Execute (Pass both Data Store and Props Context)
    # Assuming signature: resolve_content(s_data, d_data, context_props)
    result = cs.resolved_template(es.placeholder)
    assert result == "<h1>Hello Static</h1>"

    cs = ComponentState(
        es,
        s_data=data_store,
        **props_context,
    )
    # 3. Execute (Pass both Data Store and Props Context)
    # Assuming signature: resolve_content(s_data, d_data, context_props)
    result = cs.resolved_template(es.placeholder)
    assert result != "<h1>Hello Static</h1>"


def test_render_blocked_if_context_missing(data_store):
    """
    Scenario: Rules require a prop, but context is empty.
    Expected: Empty string.
    """
    rules = StateProps(required=True, prop_is_truthy=["is_logged_in"])
    es = ElementState(element="div", s_state="static_title", props=rules)

    # Pass EMPTY context
    cs = ComponentState(
        es,
        s_data=data_store,
    )
    # 3. Execute (Pass both Data Store and Props Context)
    # Assuming signature: resolve_content(s_data, d_data, context_props)
    result = cs.resolved_template(es.placeholder)

    assert result == ""


def test_strict_dynamic_vs_props_priority(data_store, props_context):
    """
    Scenario:
    1. Props say ALLOW (display_it=True).
    2. Strict Mode says BLOCK (Dynamic Key missing).
    Expected: Strict Mode wins (No Render).
    """
    # Rule: Always show
    rules = StateProps(display_it=True)

    es = ElementState(
        element="div",
        s_state="",  # Key doesn't exist
        d_state="missing_key",  # Key doesn't exist
        strict_dynamic=True,  # Strict Mode ON
        props=rules,
    )
    cs = ComponentState(
        es,
        s_data=data_store,
        **props_context,
    )
    # 3. Execute (Pass both Data Store and Props Context)
    # Assuming signature: resolve_content(s_data, d_data, context_props)
    result = cs.resolved_template(es.placeholder)

    assert result == ""  # Blocked by Data Logic, despite Props Logic passing
