from probo.styles.frameworks.bs5.components.progress import BS5ProgressBar

# ==============================================================================
#  BS5ProgressBar Tests
# ==============================================================================

def test_bs5_progress_render_basic():
    """1. Render basic progress container and a bar."""
    # Usage: BS5ProgressBar() -> add_progress_bar(width)
    prog = BS5ProgressBar()
    prog.add_progress_bar(width=50)
    html = prog.render()

    # Container
    assert '<div class="progress"' in html
    # Bar
    assert 'class="progress-bar"' in html
    assert 'role="progressbar"' in html  # Standard accessibility
    assert 'style="width:50%"' in html or 'width:50%' in html


def test_bs5_progress_render_striped_animated():
    """2. Render striped and animated variant (via init flags)."""
    # Assuming flags in init apply to the bars created
    prog = BS5ProgressBar(is_striped=True, is_animated=True)
    prog.add_progress_bar(width=75)
    html = prog.render()

    assert 'progress-bar-striped' in html
    assert 'progress-bar-animated' in html


def test_bs5_progress_render_stacked_bars():
    """3. Render multiple bars (stacked progress)."""
    prog = BS5ProgressBar(style="height:30px;")

    # Add bars with different colors
    prog.add_progress_bar(width=10, Class="bg-success")
    prog.add_progress_bar(width=20, Class="bg-warning")
    prog.add_progress_bar(width=30, Class="bg-danger")

    html = prog.render()

    assert 'style="height:30px;"' in html
    # Verify count
    assert html.count('class="progress-bar') >= 3
    # Verify Variants
    assert 'bg-success' in html
    assert 'bg-warning' in html
    assert 'bg-danger' in html


def test_bs5_progress_render_with_labels():
    """4. Render bar with internal text label."""
    prog = BS5ProgressBar()
    prog.add_progress_bar(width=25, optional_content="25% Complete")

    html = prog.render()

    assert '>25% Complete</div>' in html


def test_bs5_progress_state_blocking():
    """5. State: Progress hidden when constraints not met."""
    prog = BS5ProgressBar(
        id="task-progress",
        render_constraints={"show_progress": True}
    )
    prog.add_progress_bar(width=100)
    prog.include_env_props(show_progress=False)
    # Render with False -> Hidden
    html = prog.render()

    assert not html


def test_bs5_progress_state_passing():
    """6. State: Progress visible when constraints met."""
    prog = BS5ProgressBar(
        id="upload-progress",
        render_constraints={"is_uploading": True}
    )
    prog.add_progress_bar(width=40)
    prog.include_env_props(is_uploading=True)
    # Render with True -> Visible
    html = prog.render()

    assert 'class="progress"' in html
    assert 'width:40%' in html
