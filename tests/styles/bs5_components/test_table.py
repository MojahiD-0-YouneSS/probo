from probo.styles.frameworks.bs5.components.table import (
    BS5TableRow,
    BS5Table,
)


# ==============================================================================
#  BS5TableRow Tests
# ==============================================================================

def test_bs5_table_row_render_basic():
    """1. Render basic table row with color variant."""
    # Usage: BS5TableRow(color='info')
    row = BS5TableRow(color='info', id="row-1")
    html = row.render()

    # Should render <tr class="table-info" id="row-1"></tr>
    assert '<tr' in html
    assert 'class="table-info"' in html
    assert 'id="row-1"' in html


def test_bs5_table_row_add_cells():
    """2. Render row with standard data cells (td)."""
    row = BS5TableRow()

    # Add cells
    row.add_table_cel(content="Cell 1")
    row.add_table_cel(content="Cell 2", colspan="2", Class="text-center")

    html = row.render()

    assert '<td>Cell 1</td>' in html
    assert '<td colspan="2" class="text-center">Cell 2</td>' in html


def test_bs5_table_row_add_headers():
    """3. Render row with header cells (th) - used inside thead."""
    row = BS5TableRow()

    # Add headers
    row.add_table_head(content="#", scope="col")
    row.add_table_head(content="Name")

    html = row.render()

    assert '<th scope="col">#</th>' in html
    assert '<th>Name</th>' in html


def test_bs5_table_row_mixed_content():
    """4. Render row with mixed th (row header) and td."""
    row = BS5TableRow()

    # First cell is header for the row
    row.add_table_head("Row 1", scope="row")
    row.add_table_cel("Data")

    html = row.render()
    assert '<th scope="row">Row 1</th>' in html
    assert '<td>Data</td>' in html


def test_bs5_table_row_state_blocking():
    """5. State: Row hidden when constraints not met."""
    row = BS5TableRow(
        color="danger",
        render_constraints={"is_deleted": True}
    )
    row.include_env_props(is_deleted=False)
    # Render with False -> Hidden
    html = row.render()

    assert not html


def test_bs5_table_row_state_passing():
    """6. State: Row visible when constraints met."""
    row = BS5TableRow(
        color="success",
        render_constraints={"is_active": True}
    )
    row.include_env_props(is_active=True)
    # Render with True -> Visible
    html = row.render()

    assert "table-success" in html


# ==============================================================================
#  BS5Table Tests
# ==============================================================================

def test_bs5_table_render_basic():
    """1. Render basic table wrapper with caption."""
    table = BS5Table(caption="List of Users", id="user-table")
    html = table.render()

    assert '<table id="user-table" class="table"' in html
    assert 'id="user-table"' in html
    assert '<caption>List of Users</caption>' in html


def test_bs5_table_render_variants():
    """2. Render table with variants (striped, hover, bordered)."""
    # Assuming variants are passed via Class or specific kwargs mapped to classes
    # If variant='striped' maps to table-striped
    table = BS5Table(variant='striped', Class="table-hover table-bordered")
    html = table.render()

    assert 'table-striped' in html
    assert 'table-hover' in html
    assert 'table-bordered' in html


def test_bs5_table_add_head_body_footer():
    """3. Render full table structure (thead, tbody, tfoot)."""
    table = BS5Table()

    # Create Rows
    head_row = BS5TableRow()
    head_row.add_table_head("Col 1")

    body_row = BS5TableRow()
    body_row.add_table_cel("Data 1")

    foot_row = BS5TableRow()
    foot_row.add_table_cel("Total")

    # Add Sections
    table.add_table_head(head_row, Class="table-dark")
    table.add_table_body(body_row)
    table.add_table_footer(foot_row)

    html = table.render()

    # Check Head
    assert '<thead class="table-dark">' in html
    assert '<th>Col 1</th>' in html

    # Check Body
    assert '<tbody>' in html
    assert '<td>Data 1</td>' in html

    # Check Footer
    assert '<tfoot>' in html
    assert '<td>Total</td>' in html


def test_bs5_table_multiple_rows():
    """4. Render multiple rows in body."""
    table = BS5Table()

    r1 = BS5TableRow().add_table_cel("A")
    r2 = BS5TableRow().add_table_cel("B")

    table.add_table_body(r1, r2)

    html = table.render()

    # Verify both rows present
    assert '<td>A</td>' in html
    assert '<td>B</td>' in html
    # Verify order
    assert html.find('A') < html.find('B')


def test_bs5_table_state_blocking():
    """5. State: Table hidden when constraints not met."""
    table = BS5Table(
        caption="Secret Data",
        render_constraints={"has_access": True}
    )
    table.include_env_props(has_access=False)
    html = table.render()

    assert not html


def test_bs5_table_state_passing():
    """6. State: Table visible when constraints met."""
    table = BS5Table(
        caption="Public Data",
        render_constraints={"is_public": True}
    )
    table.include_env_props(is_public=True)
    html = table.render()

    assert "<table" in html
    assert "Public Data" in html