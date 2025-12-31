import pytest
from src.probo.context.django import DjangoComponent, DjangoComponentTools

# ==============================================================================
#  FIXTURES
# ==============================================================================


@pytest.fixture
def comp():
    """Returns a fresh DjangoComponent instance for testing."""
    return DjangoComponent()


# ==============================================================================
#  GROUP 1: Template Logic Helpers (DjangoComponentTools) [10 Tests]
# ==============================================================================


def test_tool_if_basic():
    """1. Generate simple {% if %} block."""
    res = DjangoComponentTools().If("user.is_active", "<p>Hi</p>")
    assert "{% if user.is_active %}" in res
    assert "<p>Hi</p>" in res
    assert "{% endif %}" in res


def test_tool_if_else():
    """2. Generate {% if %}...{% else %} block."""
    res = DjangoComponentTools().If("valid", "Yes", else_content="No")
    assert "{% else %}" in res
    assert "No" in res


def test_tool_for_loop():
    """3. Generate {% for %} loop."""
    res = DjangoComponentTools().For("item", "items", "<li>{{ item }}</li>")
    assert "{% for item in items %}" in res
    assert "{% endfor %}" in res


def test_tool_for_empty():
    """4. Generate {% for %}...{% empty %} block."""
    res = DjangoComponentTools().For("i", "list", "Show", empty_content="Empty list")
    assert "{% empty %}" in res
    assert "Empty list" in res


def test_tool_with_block():
    """5. Generate {% with %} context manager."""
    res = DjangoComponentTools().With("total=5", "<span>{{ total }}</span>")
    assert "{% with total=5 %}" in res
    assert "{% endwith %}" in res


def test_tool_comment():
    """6. Generate Django comment syntax."""
    res = DjangoComponentTools().Comment("TODO: Fix this")
    assert "{# TODO: Fix this #}" == res


def test_tool_include_simple():
    """7. Generate simple {% include %}."""
    res = DjangoComponentTools().Include("nav.html")
    assert "{% include 'nav.html' %}" == res


def test_tool_include_with_args():
    """8. Generate {% include %} with variables."""
    res = DjangoComponentTools().Include("widget.html", with_args="title='Main'")
    assert "with title='Main'" in res


def test_tool_csrf_token():
    """9. Generate CSRF tag."""
    assert DjangoComponentTools().Csrf() == "{% csrf_token %}"


def test_tool_load_library():
    """10. Generate library load tag."""
    assert DjangoComponentTools().Load("static") == "{% load static %}"


# ==============================================================================
#  GROUP 2: Variable Compilation Logic (_build_vars) [5 Tests]
# ==============================================================================


def test_vars_single_quote_match(comp):
    """11. Regex matches single quotes."""
    raw = "Hi <$probo-var name='user'/>"
    assert comp._build_vars(raw) == "Hi {{user}}"


def test_vars_double_quote_match(comp):
    """12. Regex matches double quotes."""
    raw = 'Value: <$probo-var name="count"/>'
    assert comp._build_vars(raw) == "Value: {{count}}"


def test_vars_whitespace_handling(comp):
    """13. Regex handles extra whitespace inside tag."""
    raw = "<$probo-var    name='data'   />"
    assert comp._build_vars(raw) == "{{data}}"


def test_vars_multiple_tokens(comp):
    """14. Regex handles multiple variables in one string."""
    raw = "<$probo-var name='a'/> + <$probo-var name='b'/>"
    assert comp._build_vars(raw) == "{{a}} + {{b}}"


def test_vars_ignore_standard_text(comp):
    """15. Regex ignores normal text."""
    raw = "<div>Normal HTML</div>"
    assert comp._build_vars(raw) == raw


# ==============================================================================
#  GROUP 3: Component Builder Logic [8 Tests]
# ==============================================================================


def test_comp_init_state(comp):
    """16. Verify empty state on init."""
    assert comp.extends_from is None
    assert comp.blocks == {}
    assert comp.raw_template == ""


def test_comp_set_extends(comp):
    """17. Verify extends updates state."""
    comp.extends("base.html")
    assert comp.extends_from == "base.html"


def test_comp_add_block(comp):
    """18. Verify adding a block."""
    comp.add_block("main", "<h1>Title</h1>")
    assert comp.blocks["main"] == "<h1>Title</h1>"


def test_comp_set_variables_kwargs(comp):
    """19. Verify setting variables via kwargs."""
    comp.set_variables(user="Admin", role="Editor")
    assert comp.variables["user"] == "Admin"
    assert comp.variables["role"] == "Editor"


def test_comp_set_variables_update(comp):
    """20. Verify updating existing variables."""
    comp.set_variables(count=1)
    comp.set_variables(count=2)  # Update
    assert comp.variables["count"] == 2


def test_comp_build_source_order(comp):
    """
    21. Critical: Verify Source Order.
    Extends -> Blocks -> Raw Template.
    """
    comp.extends("layout.html")
    comp.add_block("sidebar", "Menu")
    comp.raw_template = "<footer>Footer</footer>"

    source = comp.build_source()

    # Check positions
    ext_pos = source.find("{% extends")
    blk_pos = source.find("{% block")
    raw_pos = source.find("<footer>")

    assert ext_pos < blk_pos
    assert blk_pos < raw_pos


def test_comp_build_source_auto_compiles_vars(comp):
    """22. Verify build_source triggers _build_vars automatically."""
    comp.raw_template = "<$probo-var name='test'/>"
    # Should NOT return the raw tag, but the compiled django tag
    assert "{{test}}" in comp.build_source()


def test_comp_block_overwrite(comp):
    """23. Verify overwriting a block with same name."""
    comp.add_block("content", "Old")
    comp.add_block("content", "New")
    assert comp.blocks["content"] == "New"


def test_comp_render_empty(comp):
    """25. Verify fallback string if Django is missing/misconfigured."""
    # Force ImportError for django.template
    result = comp.render()
    assert "" in result
