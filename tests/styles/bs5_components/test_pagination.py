from probo.styles.frameworks.bs5.components.pagination import BS5Pagination

# ==============================================================================
#  BS5Pagination Tests
# ==============================================================================

def test_bs5_pagination_render_basic():
    """1. Render basic pagination structure with items."""
    # Usage: BS5Pagination("1", "2") or tuples ("1", "/page/1")
    # Assuming string inputs create simple items
    pag = BS5Pagination("1", "2", Id="page-nav",aria_label="Page navigation")
    html = pag.render()

    # Structure checks
    assert '<nav id="page-nav" aria-label="Page navigation"' in html
    assert '<ul class="pagination"' in html
    assert 'id="page-nav"' in html

    # Items
    assert '<li class="page-item"><a href="#" class="page-link">1</a></li>' in html
    assert '<li class="page-item"><a href="#" class="page-link">2</a></li>' in html

def test_bs5_pagination_render_sizing_fluent():
    """2. Render with size using fluent properties (.lg, .sm)."""
    # Test Large
    pag_lg = BS5Pagination("1").lg
    html_lg = pag_lg.render()
    assert 'class="pagination pagination-lg"' in html_lg

    # Test Small
    pag_sm = BS5Pagination("1").sm
    html_sm = pag_sm.render()
    assert 'class="pagination pagination-sm"' in html_sm

def test_bs5_pagination_controls():
    """3. Test add_controls method."""
    pag = BS5Pagination("1")

    # Add controls with custom text/links
    pag.add_controls(
        prev_conten="Back",
        prev_link="/prev",
        next_conten="Forward",
        next_link="/next"
    )

    html = pag.render()

    # Check Previous
    assert '<li class="page-item"><a href="/prev" class="page-link">Back</a></li>' in html
    # Check Next
    assert '<li class="page-item"><a href="/next" class="page-link">Forward</a></li>' in html

def test_bs5_pagination_positioning():
    """4. Test alignment/positioning classes."""
    # center -> justify-content-center
    pag_center = BS5Pagination(position='center')
    assert 'justify-content-center' in pag_center.render()

    # end -> justify-content-end
    pag_end = BS5Pagination(position='end')
    assert 'justify-content-end' in pag_end.render()

def test_bs5_pagination_state_blocking():
    """5. State: Pagination hidden when constraints not met."""
    pag = BS5Pagination(
        "1",
        "2",
        render_constraints={"has_multiple_pages": True}
    )

    # Render with False -> Hidden
    html = pag.render(override_props={"has_multiple_pages": False})

    assert not html

def test_bs5_pagination_state_passing():
    """6. State: Pagination visible when constraints met."""
    pag = BS5Pagination(
        "1",
        render_constraints={"is_visible": True}
    )
    pag.include_env_props(is_visible=True)
    # Render with True -> Visible
    html = pag.render()

    assert "pagination" in html
    assert "1" in html