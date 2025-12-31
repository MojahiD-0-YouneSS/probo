import pytest
from src.probo.components.state import ElementState, ComponentState


# --- FIXTURES ---
@pytest.fixture
def dynamic_db() -> dict[str, str]:
    return {
        "profile_url": "/users/123",
        "avatar_img": "avatar.jpg",
        "status_class": "active-user",
        "is_disabled": True,
    }


@pytest.fixture
def static_db():
    return {"default_url": "/home", "default_class": "btn btn-primary"}


# --- TESTS ---


def test_void_element_binding(dynamic_db):
    """
    Scenario: Bind dynamic data to 'src' on an <img> tag.
    Expected: <img src="avatar.jpg" class="profile" />
    """
    es = ElementState(
        element="img",
        d_state="avatar_img",
        bind_to="src",  # <--- The Feature
        is_void_element=True,
        **{
            "class": "profile",
            "src": "./myimg.png",
        },
    )
    cs = ComponentState(es, d_data=dynamic_db)
    result = cs.resolved_template(es.placeholder)

    # Verify src matches dynamic data
    assert 'src="avatar.jpg"' in result
    # Verify static attr is preserved
    assert 'class="profile"' in result
    # Verify self-closing
    assert "/>" in result


def test_non_void_binding_with_content(dynamic_db):
    """
    Scenario: Bind dynamic URL to 'href' on <a>, keep static text.
    Expected: <a href="/users/123">View Profile</a>
    """
    es = ElementState(
        element="a",
        d_state="profile_url",
        bind_to="href",  # Bind data to attribute
        c_state="View Profile",  # Keep this as content
        href="/",
    )
    cs = ComponentState(es, d_data=dynamic_db)
    result = cs.resolved_template(es.placeholder)

    assert 'href="/users/123"' in result
    assert ">View Profile</a>" in result


def test_dynamic_class_binding(dynamic_db, static_db):
    """
    Scenario: Toggle CSS class based on dynamic data.
    Expected: <div class="active-user">Content</div>
    """
    es = ElementState(
        element="div",
        d_state="status_class",
        bind_to="class",
        c_state="User Status",
        Class="btn",
    )

    cs = ComponentState(es, s_data=static_db, d_data=dynamic_db)
    result = cs.resolved_template(es.placeholder)

    # The class should come from dynamic_db['status_class']
    assert 'class="active-user"' in result
    assert ">User Status</div>" in result


def test_binding_fallback_to_static(static_db):
    """
    Scenario: Dynamic key missing, bind_to uses static fallback.
    Expected: <a href="/home">Home</a>
    """
    es = ElementState(
        element="a",
        s_state="default_url",
        d_state="missing_key",  # Missing
        bind_to="href",
        c_state="Home",
        href="/",
    )
    cs = ComponentState(
        es,
        s_data=static_db,
    )
    result = cs.resolved_template(es.placeholder)

    # Should fall back to s_state value
    assert 'href="/home"' in result
    assert '<a href="/home">Home</a>' == result


def test_strict_binding_hides_element(static_db):
    """
    Scenario: Strict Mode ON, Key missing.
    Expected: Empty string (Whole element hidden), even if static content exists.
    """
    es = ElementState(
        element="a",
        d_state="missing_key",
        bind_to="href",
        c_state="Click Me",
        strict_dynamic=True,  # <--- Strict Mode
        href="/",
    )

    cs = ComponentState(
        es,
        s_data=static_db,
    )
    result = cs.resolved_template(es.placeholder)

    assert result == ""  # Should NOT render <a>Click Me</a> with empty href


@pytest.fixture
def stores():
    return ({}, {"url": "/home", "img": "pic.jpg"})


def test_bind_valid_attribute(stores):
    """
    Scenario: Binding 'href' to an 'a' tag.
    Expected: Allowed.
    """
    s, d = stores
    es = ElementState(
        element="a",
        d_state="url",
        bind_to="href",  # Valid for <a>
        c_state="Link",
        href="/",
    )
    cs = ComponentState(es, s_data=s, d_data=d)
    result = cs.resolved_template(es.placeholder)

    assert 'href="/home"' in result
    assert '<a href="/home">Link</a>'


def test_bind_invalid_attribute_blocks_render(stores):
    """
    Scenario: Binding 'href' to a 'div' tag (Invalid).
    Expected: Empty string (Element is hidden to prevent bad HTML).
    """
    s, d = stores
    es = ElementState(
        element="div",
        d_state="url",
        bind_to="href",  # Invalid for <div>
        c_state="Content",
        href="/home",
    )
    cs = ComponentState(es, s_data=s, d_data=d)
    print("self.valid_element", es.valid_element)
    result = cs.resolved_template(es.placeholder)

    # The logic should catch that 'href' is not in ElementAttribute definitions for 'div'
    assert result == ""


def test_bind_wildcard_attribute(stores):
    """
    Scenario: Binding 'data-id' (Wildcard).
    Expected: Allowed on any tag.
    """
    s, d = stores
    es = ElementState(
        element="div",
        d_state="url",  # Just using as dummy data
        bind_to="data-user-id",  # Wildcard
        c_state="User",
        data_user_id="xyz",
    )
    cs = ComponentState(es, s_data=s, d_data=d)
    result = cs.resolved_template(es.placeholder)
    assert 'data-user-id="/home"' in result
    assert '<div data-user-id="/home">User</div>' in result
