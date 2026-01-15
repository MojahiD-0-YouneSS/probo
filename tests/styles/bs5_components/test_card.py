from probo.styles.frameworks.bs5.components import (
    BS5Card, BS5CardGroup
)
    # ==============================================================================
    #  BS5Card Tests
    # ==============================================================================


def test_bs5_card_render_basic():
    """1. Render basic card with body content via init."""
    card = BS5Card(card_body="Simple Content")

    html = card.render()

    assert '<div class="card">' in html
    assert '<div class="card-body">' in html
    assert 'Simple Content' in html


def test_bs5_card_render_full_structure():
    """2. Render full structure (Header, Image, Body, Footer) via init."""
    card = BS5Card(
        card_header="Header",
        card_image="img.jpg",
        card_body="Body",
        card_footer="Footer"
    )
    html = card.render()

    assert 'class="card-header"' in html
    assert 'Header' in html
    assert 'class="card-img-top"' in html
    assert 'src="img.jpg"' in html
    assert 'class="card-body"' in html
    assert 'class="card-footer"' in html


def test_bs5_card_fluent_methods():
    """3. Render using fluent add_* methods for Title, Text, and Links."""
    card = BS5Card()  # Init empty

    card.add_card_body("Main Content")
    card.add_card_title("My Title", tag="h2")
    card.add_card_sub_title("Subtitle", tag="h3",Class='mb-2 text-muted')
    card.add_card_text("Some detail text.")
    card.add_card_link("Click here", href="#")

    html = card.render()

    # Check classes added by methods
    assert '<h2 class="card-title">My Title</h2>' in html
    assert '<h3 class="card-subtitle mb-2 text-muted">Subtitle</h3>' in html  # Standard BS5
    assert '<p class="card-text">Some detail text.</p>' in html
    assert 'class="card-link"' in html


def test_bs5_card_render_attributes():
    """4. Render root card with custom attributes."""
    card = BS5Card(card_body="Info", Id="profile-card", style="width: 18rem;")
    html = card.render()

    assert 'id="profile-card"' in html
    assert 'style="width: 18rem;"' in html


def test_bs5_card_state_blocking():
    """5. State: Card hidden when constraints not met."""
    # API implies inheritance from Component, so standard constraint logic applies
    card = BS5Card(
        card_body="Secret Info",
        render_constraints={"is_visible": True}
    )

    # Render with False -> Hidden
    html = card.render(override_props={"is_visible": False})
    assert not html


def test_bs5_card_state_passing():
    """6. State: Card visible when constraints met."""
    card = BS5Card(
        card_body="Public Info",
        render_constraints={"is_visible": True}
    )

    html = card.render(override_props={"is_visible": True},add_to_global=True)
    assert "card-body" in html
    assert "Public Info" in html

    # ==============================================================================
    #  BS5CardGroup Tests
    # ==============================================================================


def test_bs5_card_group_render_container():
    """1. Render basic card group container."""
    group = BS5CardGroup()
    html = group.render()

    assert '<div class="card-group">' in html


def test_bs5_card_group_init_with_cards():
    """2. Render group initialized with existing Card objects."""
    c1 = BS5Card(card_body="Card 1")
    c2 = BS5Card(card_body="Card 2")

    group = BS5CardGroup(c1, c2)
    html = group.render()

    assert 'class="card-group"' in html
    assert html.count('class="card"') >= 2
    assert "Card 1" in html
    assert "Card 2" in html


def test_bs5_card_group_fluent_add():
    """3. Render using add_card method (creating cards internally)."""
    group = BS5CardGroup()

    # Add a card via method args
    group.add_card(card_header="New Card", card_body="Created via group")

    html = group.render()

    assert 'class="card"' in html
    assert 'class="card-header"' in html
    assert "Created via group" in html


def test_bs5_card_group_attributes():
    """4. Render group with custom attributes."""
    group = BS5CardGroup(id="my-group", class_="mb-4")
    html = group.render()

    assert 'id="my-group"' in html
    assert 'mb-4' in html


def test_bs5_card_group_state_blocking():
    """5. State: Group hidden via constraints."""
    group = BS5CardGroup(render_constraints={"show_group": True})
    group.add_card(card_body="Content")

    html = group.render(override_props={"show_group": False})
    assert not html


def test_bs5_card_group_state_passing():
    """6. State: Group visible via constraints."""
    group = BS5CardGroup(render_constraints={"show_group": True})
    group.add_card(card_body="Content")

    html = group.render(override_props={"show_group": True},add_to_global=True)
    assert "card-group" in html
    assert "Content" in html