from probo.styles.frameworks.bs5.components import BS5Card, BS5Modal, BS5Button
from probo.components.tag_functions import (
div,label,Input,img,nav
)

def test_card_grid_layout():
    """1. Grid of Cards."""
    cards = [BS5Card(card_body=f"Card {i}").render() for i in range(3)]
    html = div(*cards, Class="row row-cols-3")

    assert 'class="row row-cols-3"' in html
    assert html.count('class="card"') == 3

def test_modal_inside_card():
    """2. Button inside Card triggers Modal."""
    modal = BS5Modal(id="myModal", content="Details")
    btn = BS5Button("Open", data_bs_toggle="modal", data_bs_target="#myModal")
    card = BS5Card(card_body=btn.render() + modal.render())

    html = card.render()
    assert 'data-bs-toggle="modal"' in html
    assert 'id="myModal"' in html

def test_responsive_visibility():
    """3. Verify d-none d-md-block logic."""
    el = div("Mobile Hidden", Class="d-none d-md-block")
    assert "d-none d-md-block" in el

def test_flex_alignment_center():
    """4. Flexbox centering."""
    el = div("Center", Class="d-flex justify-content-center align-items-center")
    assert "justify-content-center" in el

def test_nested_rows_cols():
    """5. Row inside Column."""
    inner = div("Inner", Class="row")
    outer = div(inner, Class="col-6")
    assert '<div class="col-6"><div class="row">' in outer

def test_list_group_in_card():
    """6. List group flush in card."""
    # Assuming list group HTML structure
    lg = '<ul class="list-group list-group-flush"><li class="list-group-item">Item</li></ul>'
    card = BS5Card(card_body=lg)
    assert "list-group-flush" in card.render()

def test_input_group_layout():
    """7. Input group (Prepend + Input)."""
    # Manual construction using UI
    grp = div(
        label("@", Class="input-group-text") +
        Input(Class="form-control"),
        Class="input-group"
    )
    html = grp
    assert "input-group" in html
    assert "input-group-text" in html

def test_card_group_layout():
    """8. Card Group wrapper."""
    c1 = BS5Card("A").render()
    c2 = BS5Card("B").render()
    grp = div(c1+c2, Class="card-group")
    assert "card-group" in grp

def test_media_object_layout():
    """9. Media object (Flex pattern)."""
    img1 = img(Class="flex-shrink-0")
    body = div("Content", Class="flex-grow-1 ms-3")
    media = div(img1 + body, Class="d-flex")
    html = media
    assert "d-flex" in html
    assert "flex-shrink-0" in html

def test_sticky_top_layout():
    """10. Sticky positioning."""
    nav1 = nav("Nav", Class="sticky-top")
    assert "sticky-top" in nav1