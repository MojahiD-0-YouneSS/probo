from probo.styles.frameworks.bs5.components.list_group import (
    BS5ListGroup,
)


# ==============================================================================
#  BS5ListGroup Tests
# ==============================================================================

def test_bs5_listgroup_render_basic():
    """1. Render basic list group with text items."""
    # Usage: BS5ListGroup("Item 1", "Item 2", content="", id="my-list")
    lg = BS5ListGroup("Item 1", "Item 2", content="", Id="my-list")
    html = lg.render()

    # Container check (ul is default usually)
    assert '<ul id="my-list" class="list-group"' in html or '<div class="list-group"' in html
    assert 'id="my-list"' in html

    # Items check
    assert '<li class="list-group-item">Item 1</li>' in html
    assert '<li class="list-group-item">Item 2</li>' in html


def test_bs5_listgroup_render_links_and_buttons():
    """2. Render actionable items (links/buttons) using add_list_item."""
    lg = BS5ListGroup(content="")

    # Add Link
    lg.add_list_item("Link Item", tag="a", href="/path")

    # Add Button via generic add
    lg.add_list_item("Button Item", tag="button", type="button")

    # Test specific helper if available or standard rendering
    html = lg.render()

    # Links should automatically get 'list-group-item-action' logic
    assert '<a href="/path" class="list-group-item list-group-item-action">Link Item</a>' in html
    assert '<button type="button" class="list-group-item">Button Item</button>' in html


def test_bs5_listgroup_render_modifiers():
    """3. Render with modifiers (flush, numbered, horizontal)."""
    # Flush remove borders
    lg_flush = BS5ListGroup(content="", Class="list-group-flush")
    assert "list-group-flush" in lg_flush.render()

    # Numbered (requires ol tag usually)
    lg_num = BS5ListGroup(content="",  Class="list-group-numbered")
    lg_num.swap_element('ol')
    html = lg_num.render()
    assert "<ol" in html
    assert "list-group-numbered" in html

    # Horizontal
    lg_horiz = BS5ListGroup(content="", Class="list-group-horizontal")
    assert "list-group-horizontal" in lg_horiz.render()

def test_bs5_listgroup_state_constraints_blocking():
    """5. State: List group hidden when constraints not met."""
    lg = BS5ListGroup(
        "Secure Item",
        content="",
        render_constraints={"show_list": True}
    )

    # Render with False -> Hidden
    html = lg.render(override_props={"show_list": False})

    assert not html


def test_bs5_listgroup_state_dynamic_content():
    """6. State: List items populated by Dynamic Data (Iterative)."""
    # 1. Define Logic Element for the list items
    # i_state=True means we loop over the data
    items = ['Alert 1', 'Alert 2']

    # 2. Inject into Component
    # We pass the placeholder as the content for the ListGroup
    lg = BS5ListGroup(content='')
    for item in items:
        lg.add_list_item(item)

    html= lg.render()

    # The placeholder should be replaced by the iterated items
    assert '<li class="list-group-item">Alert 1</li>' in html
    assert '<li class="list-group-item">Alert 2</li>' in html
    assert '<$' not in html