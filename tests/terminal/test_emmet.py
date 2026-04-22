import pytest
from unittest.mock import MagicMock

# Import the module explicitly as a separate alias to avoid the name collision
import probo.terminal.emmet as emmet_module
from probo.terminal.emmet import emmet


# @pytest.fixture(autouse=True)
# def mock_tag_functions(monkeypatch):
#     """
#     Mocks the Probo tag_functions module.
#     Instead of returning real Probo Elements, it returns dictionaries
#     representing the exact state parsed by the Emmet engine.
#     """

#     class DummyTagFunctions:
#         @staticmethod
#         def div(content="", **kwargs):
#             return {"tag": "div", "content": content, "attrs": kwargs}

#         @staticmethod
#         def span(content="", **kwargs):
#             return {"tag": "span", "content": content, "attrs": kwargs}

#     # BUGFIX: Patch directly on the module object instead of using a string path!
#     monkeypatch.setattr(emmet_module, "tag_functions", DummyTagFunctions)


# ==========================================
# TESTS: Validation and Error Handling
# ==========================================


def test_emmet_invalid_shlex():
    """Tests that unclosed quotes trigger a ValueError in shlex and return None."""
    # An unclosed quote will crash shlex.split()
    assert emmet('div "unclosed string') is None


def test_emmet_empty_string():
    """Tests that empty strings or whitespace return None."""
    assert emmet("") is None
    assert emmet("   ") is None


def test_emmet_unknown_tag():
    """Tests that an invalid tag raises a ValueError."""
    with pytest.raises(ValueError, match="Unknown tag: unknown"):
        emmet("unknown #id")


# ==========================================
# TESTS: Argument Parsing
# ==========================================


def test_emmet_basic_tag():
    """Tests a bare tag with no attributes."""
    res = emmet("div")
    assert res == "<div></div>"


def test_emmet_id_and_classes():
    """Tests #id and .class parsing."""
    res = emmet("div #main .container .p-4")
    assert res== """<div id="main" class="container p-4"></div>"""


def test_emmet_kwargs_attributes():
    """Tests key=value attribute extraction."""
    res = emmet("Input type=text data-foo=bar")
    assert res == """<input type="text" data-foo="bar"/>"""


def test_emmet_styles():
    """Tests inline style parsing using the -s flag."""
    res = emmet("div -s color:red -s font-weight:bold")
    assert res == """<div style="color:red; font-weight:bold"></div>"""


def test_emmet_styles_boundary():
    """Tests edge cases where the -s flag is malformed or missing arguments."""
    # 1. Missing the colon (should ignore it)
    res_no_colon = emmet("div -s invalid_style")
    assert "style" not in res_no_colon
    assert "<div></div>" == res_no_colon

    # 2. Dangling flag at the end of the string
    res_dangling = emmet("div -s")
    assert "style" not in res_dangling


def test_emmet_content():
    """Tests the -c flag for content assignment."""
    res = emmet('div -c "Hello World" from probo')
    assert res == """<div>Hello World from probo</div>"""


def test_emmet_content_dangling():
    """Tests edge case where -c is the absolute last argument."""
    res = emmet("div -c")
    assert res == "<div></div>"


def test_emmet_flag_interruption():
    """Tests that the -c loop correctly yields to subsequent flag definitions."""
    # The `-c` collector should stop collecting at `-s`
    res = emmet('div -c "Hello" -s color:blue')
    assert res == """<div style="color:blue">Hello</div>"""


# ==========================================
# TESTS: The Complete Component Command
# ==========================================


def test_emmet_comprehensive():
    """Tests a fully loaded, complex Emmet command."""
    command = 'button #hero .badge .bg-primary type=button -s display:flex -c "Click Me!"'
    res = emmet(command)

    assert (
        res
        == """<button id="hero" type="button" class="badge bg-primary" style="display:flex">Click Me!</button>"""
    )
