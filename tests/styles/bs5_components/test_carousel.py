from probo.styles.frameworks.bs5.components import (
    BS5Carousel
)


# ==============================================================================
#  BS5Carousel Tests
# ==============================================================================

def test_bs5_carousel_render_basic():
    """1. Render basic carousel with items via init."""
    # Assuming items can be strings or tuples
    car = BS5Carousel("Slide 1", "Slide 2", Id="basicCarousel")
    html = car.render()

    assert 'id="basicCarousel"' in html
    assert 'class="carousel slide"' in html
    assert 'class="carousel-inner"' in html

    # Check items
    assert 'class="carousel-item active"' in html  # First item should be active
    assert 'Slide 1' in html
    assert 'class="carousel-item"' in html  # Second item
    assert 'Slide 2' in html


def test_bs5_carousel_render_fluent_items_and_captions():
    """2. Render using add_carousel_item with captions."""
    car = BS5Carousel(Id="captionCarousel")

    car.add_carousel_item("Image 1", carousel_caption="Caption 1")
    car.add_carousel_item("Image 2", carousel_caption="Caption 2")

    html = car.render()

    assert 'class="carousel-caption"' in html
    assert 'Caption 1' in html
    assert 'Caption 2' in html
    # Ensure structure nesting
    assert html.find('Caption 1') > html.find('Image 1')


def test_bs5_carousel_render_controls_indicators():
    """3. Render with Controls and Indicators."""
    car = BS5Carousel("A", "B", Id="ctrlCarousel")

    car.add_carousel_controls()
    car.add_carousel_indicators()

    html = car.render()

    # Controls
    assert 'class="carousel-control-prev"' in html
    assert 'class="carousel-control-next"' in html
    assert 'data-bs-target="#ctrlCarousel"' in html

    # Indicators
    assert 'class="carousel-indicators"' in html
    assert 'data-bs-slide-to="0"' in html
    assert 'data-bs-slide-to="1"' in html
    assert 'class="active"' in html  # First indicator active


def test_bs5_carousel_render_attributes():
    """4. Render with custom attributes (e.g. crossfade, dark variant)."""
    # 'carousel-fade' and 'carousel-dark' are common BS5 modifiers
    car = BS5Carousel("S1", Id="attrCarousel", Class="carousel-fade carousel-dark")

    html = car.render()

    assert 'carousel-fade' in html
    assert 'carousel-dark' in html
    assert 'data-bs-ride="carousel"' in html  # Standard attribute usually added


def test_bs5_carousel_state_constraints_blocking():
    """5. State: Carousel hidden when constraints not met."""
    car = BS5Carousel(
        "Promo Slide",
        Id="promo",
        render_constraints={"has_promo": True}
    )

    # Render with False -> Hidden
    html = car.render(override_props={"has_promo": False})

    assert not html


def test_bs5_carousel_state_constraints_passing():
    """6. State: Carousel visible when constraints met."""
    car = BS5Carousel(
        "Promo Slide",
        Id="promo",
        render_constraints={"has_promo": True}
    )

    html = car.render(override_props={"has_promo": True},add_to_global=True)

    assert "carousel" in html
    assert "Promo Slide" in html
