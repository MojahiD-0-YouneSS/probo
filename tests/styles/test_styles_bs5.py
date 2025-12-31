import pytest
from src.probo.styles.frameworks.bs5.bs5 import (
    BS5,
    BS5ElementStyle,
    BS5Element,
)


# ==============================================================================
#  GROUP 1: BS5ElementStyle (The Configuration)
# ==============================================================================
def test_bs5_style_init():
    """1. Test initialization stores tag correctly."""
    style = BS5ElementStyle("button")
    assert style.tag == "button"
    assert style.classes == []


def test_bs5_style_add_single():
    """2. Test adding a single class."""
    style = BS5ElementStyle("div").add("container")
    assert "container" in style.classes


def test_bs5_style_add_multiple():
    """3. Test adding multiple classes at once."""
    style = BS5ElementStyle("div").add("row", "justify-content-center")
    assert len(style.classes) == 2
    assert "row" in style.classes


def test_bs5_style_chaining():
    """4. Test fluent API chaining."""
    style = BS5ElementStyle("span").add("badge").add("bg-primary")
    assert "badge" in style.classes
    assert "bg-primary" in style.classes


def test_bs5_style_duplicates():
    """5. Test behavior with duplicate classes (Should logically allow or dedup)."""
    # Lists allow duplicates, sets don't.
    # Assuming list implementation based on previous code, but checking presence.
    style = BS5ElementStyle("div").add("col", "col")
    assert "col" in style.classes


def test_bs5_style_none_handling():
    """6. Test adding None values (Should be safe/ignored or filtered later)."""
    # If your add method doesn't filter None, this tests robustness of render later.
    style = BS5ElementStyle("div")
    try:
        style.add(None)
        assert True  # Should not crash
    except Exception:
        pytest.fail("BS5ElementStyle.add(None) crashed.")


# ==============================================================================
#  GROUP 2: BS5 (The Bucket/Registry)
# ==============================================================================


@pytest.fixture
def populated_bucket():
    btn = BS5ElementStyle("button").add("btn", "btn-primary")
    card = BS5ElementStyle("div").add("card", "p-3")
    return BS5(
        btn_submit=btn,
        div__card=card,  # Simulating normalized key for div#card
    )


def test_bs5_bucket_init(populated_bucket):
    """7. Verify bucket stores styles."""
    assert "btn_submit" in populated_bucket.registry
    assert "div__card" in populated_bucket.registry


def test_bs5_bucket_get_classes_valid(populated_bucket):
    """8. Verify retrieval of class string."""
    classes = populated_bucket.get_cls_string("btn_submit")
    assert "btn" in classes
    assert "btn-primary" in classes


def test_bs5_bucket_get_classes_normalization(populated_bucket):
    """9. Verify key normalization (. -> _ and # -> __)."""
    # If  asks for 'div.card', bucket should look for 'div_card' (or similar logic)
    # Based on your previous code: clean_key = key.replace('#', '__').replace('.', '_')
    # Our fixture has 'div__card', so input 'div#card' should find it
    classes = populated_bucket.get_cls_string("div#card")
    assert "card" in classes


def test_bs5_bucket_get_classes_missing(populated_bucket):
    """10. Verify graceful failure for missing keys."""
    # Should return empty string, not crash
    assert populated_bucket.get_cls_string("missing_key") == ""


def test_bs5_bucket_get_element_success(populated_bucket):
    """11. Verify factory returns a BS5Element."""
    el = populated_bucket.get_element("btn_submit")
    assert isinstance(el, BS5Element)
    assert el.tag == "button"


def test_bs5_bucket_get_element_content(populated_bucket):
    """12. Verify passing content to the factory."""
    el = populated_bucket.get_element("btn_submit", content="Click Me")
    assert el.content == "Click Me"


def test_bs5_bucket_get_element_attrs(populated_bucket):
    """13. Verify passing extra attributes (kwargs)."""
    el = populated_bucket.get_element("btn_submit", id="my-btn")
    assert el.attrs["id"] == "my-btn"


def test_bs5_bucket_get_element_missing(populated_bucket):
    """14. Verify ValueError on missing key."""
    with pytest.raises(ValueError):
        populated_bucket.get_element("ghost_style")


def test_bs5_bucket_immutability(populated_bucket):
    """15. Verify getting an element doesn't mutate the registry."""
    el1 = populated_bucket.get_element("btn_submit")
    el1.add("extra-class")  # Modify the INSTANCE

    el2 = populated_bucket.get_element("btn_submit")  # Get a NEW instance
    # el2 should NOT have 'extra-class'
    # This ensures your .copy() logic works
    rendered2 = el2.render()
    assert "extra-class" not in rendered2


# ==============================================================================
#  GROUP 3: BS5Element (The Renderer)
# ==============================================================================


def test_bs5_element_render_basic():
    """16. Basic render with tag and classes."""
    el = BS5Element("div", classes=["container"])
    html = el.render()
    assert '<div class="container"></div>' == html


def test_bs5_element_fluent_add():
    """17. Fluent API .add()."""
    el = BS5Element("span").add("badge").add("bg-secondary")
    html = el.render()
    assert 'class="badge bg-secondary"' in html


def test_bs5_element_include_string():
    """18. Include string content."""
    el = BS5Element("h1").include("Title")
    html = el.render()
    assert "<h1>Title</h1>" in html


def test_bs5_element_include_nesting():
    """19. Recursive nesting of BS5Elements."""
    child = BS5Element("span", content="Icon").add("icon")
    parent = BS5Element("button").add("btn").include(child)

    html = parent.render()
    # <button class="btn"><span class="icon">Icon</span></button>
    assert '<button class="btn">' in html
    assert '<span class="icon">Icon</span>' in html


def test_bs5_element_merge_attrs_class():
    """20. Merging 'class_' kwarg with internal classes."""
    # If user does BS5Element(..., class_='extra')
    el = BS5Element("div", classes=["row"], class_="gap-3")
    html = el.render()
    assert "row" in html
    assert "gap-3" in html


def test_bs5_element_handle_none_class():
    """21. Filter None values from class list during render."""
    el = BS5Element("div", classes=["valid", None, "also-valid"])
    # The render method usually joins with space. 'None' might become string "None" if not filtered.
    # Ideally, your BS5Element should filter: [c for c in classes if c]
    # Let's see if your implementation handles it.
    html = el.render()
    # Ensure "None" string is NOT in class list
    assert 'class="valid also-valid"' in html or "None" not in html


def test_bs5_element_void_tag():
    """22. Rendering a void element (hr)."""
    # Assuming Element() handles void logic correctly based on tag name
    el = BS5Element("hr").add("my-3")
    html = el.render()
    assert '<hr class="my-3"/>' in html


def test_bs5_element_mixed_content_types():
    """23. Include int and float content."""
    el = BS5Element("span").include(123, 4.5)
    html = el.render()
    assert "<span>1234.5</span>" in html


def test_bs5_element_empty_classes():
    """24. Rendering with no classes."""
    el = BS5Element("div")
    html = el.render()
    # Should be <div></div> or <div class=""></div>
    # Ideally clean: <div></div>
    assert "<div" in html


def test_bs5_element_attribute_passthrough():
    """25. Verify standard attributes (id, data-*) pass through."""
    el = BS5Element("div", id="main", data_bs_toggle="modal")
    html = el.render()
    assert 'id="main"' in html
    assert 'data-bs-toggle="modal"' in html
    """25. Verify standard attributes (id, data-*) pass through."""
    el = BS5Element("div", id="main", data_bs_toggle="modal")
    html = el.render()
    assert 'id="main"' in html
    assert 'data-bs-toggle="modal"' in html


# ==============================================================================
#  GROUP 4: Integration Scenarios (BS5 + BS5ES + BS5E)
# ==============================================================================


@pytest.fixture
def full_theme():
    """A complex registry representing a full component library."""
    return BS5(
        # div#card -> div__card
        div__card=BS5ElementStyle("div").add("card", "shadow-sm"),
        # div.card-body -> div_card_body
        div_card_body=BS5ElementStyle("div").add("card-body", "p-3"),
        # h5.card-title -> h5_card_title
        h5_card_title=BS5ElementStyle("h5").add("card-title", "mb-2"),
        # p.card-text -> p_card_text
        p_card_text=BS5ElementStyle("p").add("card-text", "text-muted"),
        # btn#primary -> btn__primary
        btn__primary=BS5ElementStyle("button").add("btn", "btn-primary"),
        # btn#link -> btn__link
        btn__link=BS5ElementStyle("a").add("btn", "btn-link"),
    )


def test_integration_basic_retrieval(full_theme):
    """26. Basic Fetch & Render: Get element from bucket and render it immediately."""
    # Scenario: user.py -> bs5.get('div#card')
    el = full_theme.get_element("div#card")
    html = el.render()

    assert "<div" in html
    assert 'class="card shadow-sm"' in html
    assert "</div>" in html


def test_integration_content_injection(full_theme):
    """27. Content Injection: Fetch element and inject string content."""
    # Scenario: .include('hello')
    el = full_theme.get_element("h5.card-title").include("Hello World")
    html = el.render()

    assert "<h5" in html
    assert 'class="card-title mb-2"' in html
    assert ">Hello World</h5>" in html


def test_integration_attribute_override(full_theme):
    """28. Attribute Override: Fetch element but add specific attributes (ID/Style)."""
    # Scenario: overriding ID on the fly
    el = full_theme.get_element("btn#primary", id="submit-btn", type="submit")
    html = el.render()

    assert 'id="submit-btn"' in html
    assert 'type="submit"' in html
    assert 'class="btn btn-primary"' in html


def test_integration_fluent_class_extension(full_theme):
    """29. Fluent Extension: Fetch element and add context-specific classes."""
    # Scenario: Adding 'active' state to a standard button
    el = full_theme.get_element("btn#primary").add("active", "w-100")
    html = el.render()

    assert 'class="btn btn-primary active w-100"' in html


def test_integration_nested_structure(full_theme):
    """30. Deep Nesting: Card > Body > Title + Text."""
    # Scenario: Building a full card component using registry items

    # 1. Prepare children
    title = full_theme.get_element("h5.card-title").include("Card Title")
    text = full_theme.get_element("p.card-text").include("Some detail text.")

    # 2. Prepare Body
    body = full_theme.get_element("div.card-body").include(title, text)

    # 3. Prepare Card (Parent)
    card = full_theme.get_element("div#card").include(body)

    html = card.render()

    # Verify Hierarchy
    assert '<div class="card shadow-sm">' in html
    assert '<div class="card-body p-3">' in html
    assert '<h5 class="card-title mb-2">Card Title</h5>' in html
    assert '<p class="card-text text-muted">Some detail text.</p>' in html


def test_integration_mixed_content_types(full_theme):
    """31. Mixed Content: Including strings, BS5Elements, and raw HTML."""
    # Scenario: Button with Icon (raw html) and Text
    btn = full_theme.get_element("btn#primary").include(
        "<span>Icon</span>",  # Raw HTML string
        " Save Changes",  # Text
    )
    html = btn.render()

    assert "<span>Icon</span>" in html
    assert " Save Changes" in html


def test_integration_tag_switching_via_registry():
    """32. Registry Logic: Ensure different tags are respected."""
    # Setup specific registry
    theme = BS5(
        link=BS5ElementStyle("a").add("text-decoration-none"),
        span=BS5ElementStyle("span").add("badge"),
    )

    link_html = theme.get_element("link", href="/home").include("Go").render()
    span_html = theme.get_element("span").include("New").render()

    assert '<a href="/home" class="text-decoration-none">Go</a>' == link_html
    assert '<span class="badge">New</span>' == span_html


def test_integration_legacy_hybrid_mode(full_theme):
    """33. Hybrid Mode: Using registry classes with manual Element instantiation."""
    # Scenario: User wants just the classes string to use in a non-BS5Element
    classes = full_theme.get_cls_string("btn#primary")

    # Simulate manual usage
    assert classes == "btn btn-primary"
    # Ensure it didn't crash and returned a string


def test_integration_immutability_complex(full_theme):
    """34. Complex Immutability: Ensure modifying a retrieved nested tree doesn't break registry."""
    # Get a button, modify it heavily
    btn1 = full_theme.get_element("btn#primary").add("danger-mode").include("Delete")

    # Get original again
    btn2 = full_theme.get_element("btn#primary")

    html1 = btn1.render()
    html2 = btn2.render()

    assert "danger-mode" in html1
    assert "danger-mode" not in html2
    assert "Delete" not in html2


def test_integration_empty_hydration(full_theme):
    """35. Empty Hydration: Getting an element defined with NO classes."""
    # Add an empty style to the existing theme
    full_theme.registry["div__plain"] = BS5ElementStyle("div")

    el = full_theme.get_element("div#plain").include("Content")
    html = el.render()

    # Should render standard div without class attribute (or empty class)
    # Using 'in' allows for flexible attribute ordering/presence
    assert "<div>Content</div>" in html
