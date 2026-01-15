from probo.styles.frameworks.bs5.components.spinner import BS5Spinner

# ==============================================================================
#  BS5Spinner Tests
# ==============================================================================

def test_bs5_spinner_render_basic_border():
    """1. Render basic border spinner (default)."""
    # Usage: BS5Spinner(content="Loading...")
    spinner = BS5Spinner(content="Loading...")
    html = spinner.render()

    # Check default class and role
    assert '<div' in html
    assert 'class="spinner-border"' in html
    assert 'role="status"' in html
    # Content usually wrapped or placed inside
    assert 'Loading...' in html


def test_bs5_spinner_render_grow_variant():
    """2. Render 'grow' variant."""
    spinner = BS5Spinner(content="Loading...", variant="grow")
    html = spinner.render()

    assert 'class="spinner-grow"' in html
    assert 'spinner-border' not in html


def test_bs5_spinner_render_colors_and_size():
    """3. Render with color utilities and size modifier."""
    # BS5 uses text-{color} for spinners and spinner-border-sm for size
    spinner = BS5Spinner(
        content="Processing",
        Class="text-primary spinner-border-sm",
        id="my-spinner"
    )
    html = spinner.render()

    assert 'text-primary' in html
    assert 'spinner-border-sm' in html
    assert 'id="my-spinner"' in html


def test_bs5_spinner_accessibility_wrapper():
    """4. Verify content handling (Visually Hidden)."""
    # Ideally, spinner text is hidden for sighted users but available for screen readers
    # Assuming BS5Spinner handles wrapping content in 'visually-hidden' span, or user does it.
    # If the component is simple, it just puts content inside.
    # We check if the content exists inside the div.
    spinner = BS5Spinner(content='<span class="visually-hidden">Loading...</span>')
    html = spinner.render()

    assert 'class="visually-hidden"' in html
    assert 'Loading...' in html


def test_bs5_spinner_state_blocking():
    """5. State: Spinner hidden when constraints not met."""
    spinner = BS5Spinner(
        content="Loading...",
        id="load-spin",
        render_constraints={"is_loading": True}
    )

    # Render with False -> Hidden
    html = spinner.render(override_props={"is_loading": False})

    assert not html


def test_bs5_spinner_state_passing():
    """6. State: Spinner visible when constraints met."""
    spinner = BS5Spinner(
        content="Saving...",
        render_constraints={"is_saving": True}
    )
    spinner.include_env_props(is_saving=True)
    # Render with True -> Visible
    html = spinner.render()

    assert "spinner-border" in html
    assert "Saving..." in html