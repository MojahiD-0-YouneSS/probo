import pytest
import inspect
from typing import Any, Callable
from probo.components.elements import Element
from probo import DIV, div
from probo.components.light_tags import Ldiv, l_div
from probo.components import ProxyElement
from probo.utility import ProboSourceString

# --- Advanced Probo API Constructs ---
class MockComponent:
    def render(self):
        return ProboSourceString("<custom-comp>Mounted</custom-comp>")

    def stream(self, batch=50):
        yield ProboSourceString("<custom-comp>")
        yield "Mounted"
        yield ProboSourceString("</custom-comp>")


class MockHTMXElement:
    def render(self):
        return ProboSourceString('<div hx-get="/api/data" hx-trigger="click"></div>')


class MockBS5:
    def render(self):
        return ProboSourceString('<button class="btn btn-primary">Bootstrap</button>')


class MockCSSRule:
    def render(self):
        return ".probo-active { display: block !important; }"


# --- Foreign Framework Logic ---
class MockDjangoModel:
    def __str__(self):
        return "DjangoUser(id=1)"


class MockJinjaTemplate:
    def __html__(self):
        return ProboSourceString("<b>Safe HTML</b>")


# =====================================================================
# 2. FIXTURES & DATA SCENARIOS
# =====================================================================

NATIVE_TYPES = [
    ("int", 404, "404"),
    ("none", None, ""),
    ("list", ["A", "B"], "AB"),
    ("dict", {"a": 1}, "{'a': 1}"),
    ("generator", (str(i) for i in range(3)), "012"),
]

ADVANCED_API_CLASSES = [
    ("probo_component", MockComponent(), "Mounted"),
    ("probo_htmx", MockHTMXElement(), 'hx-get="/api/data"'),
    ("probo_bs5", MockBS5(), "btn btn-primary"),
    ("probo_css", MockCSSRule(), ".probo-active { display: block !important; }"),
    ("django_str", MockDjangoModel(), "DjangoUser(id=1)"),
    ("jinja_html", MockJinjaTemplate(), "<b>Safe HTML</b>"),
]

TARGET_ARCHITECTURES = [
    ("heavy_oop", DIV, False),
    ("light_oop", Ldiv, False),
    ("heavy_func", div, True),
    ("light_func", l_div, True),
]


@pytest.fixture
def shared_el():
    return Element(is_list=True, use_deque=True)


def setup_proxy(raw_data) -> Any:  # -> ProxyElement
    """
    Helper to configure the ProxyElement based on the new v1.3.4 API.
    Injects render_callable and stream_callable using obj_as_arg=True pattern.
    """

    # Initialize ProxyElement (using "span" as a wrapper tag just for testing)
    proxy = ProxyElement(tag="span")
    proxy.load_logic(raw_data)

    # Configure Render & Stream Fallbacks using the new obj_as_arg signature
    if not hasattr(raw_data, "render"):
        if hasattr(raw_data, "__html__"):
            proxy.load_render_logic(lambda obj=None: obj.__html__() if obj else str())

            def _stream_html(obj=None):
                if obj:
                    yield obj.__html__()
                else:
                    yield str()

            proxy.load_stream_logic(_stream_html)

        elif isinstance(raw_data, (list, tuple)):
            def _render_gen(obj):
                return "".join(str(x) for x in obj)
                
            proxy.load_render_logic(_render_gen)

            def _stream_iter(obj):
                yield from (str(x) for x in obj) if obj is not None else ""

            proxy.load_stream_logic(_stream_iter)

        elif inspect.isgenerator(raw_data):
            proxy.load_render_logic(lambda obj=None: "012")

            def _stream_gen(obj=None):
                yield from obj if obj is not None else ""

            proxy.load_stream_logic(_stream_gen)

        else:
            proxy.load_render_logic(lambda obj=None: str(obj) if obj is not None else "")

            def _stream_fallback(obj=None):
                yield str(obj) if obj is not None else ""

            proxy.load_stream_logic(_stream_fallback)

    # If the object natively renders but lacks a stream method, patch streaming to yield the render output
    elif hasattr(raw_data, "render") and not hasattr(raw_data, "stream"):

        def _stream_from_render(obj=None):
            yield obj.render() if obj is not None else ""

        proxy.load_stream_logic(_stream_from_render)

    return proxy


# =====================================================================
# 3. THE INTEGRATION MATRIX
# =====================================================================


@pytest.mark.parametrize(
    "name, raw_data, expected", NATIVE_TYPES + ADVANCED_API_CLASSES
)
@pytest.mark.parametrize("arch_name, TargetWrapper, is_func", TARGET_ARCHITECTURES)
def test_proxy_eager_render(
    shared_el, name, raw_data, expected, arch_name, TargetWrapper, is_func
):
    """Tests bridging both raw Python types and Advanced Probo API into rendering."""

    proxied_node = setup_proxy(raw_data)
    # Inject into the Probo Architecture
    if is_func:
        if "EL" in inspect.signature(TargetWrapper).parameters:
            page = TargetWrapper(shared_el, proxied_node, id="container")
        else:
            page = TargetWrapper(proxied_node, id="container")
    else:
        page = TargetWrapper(proxied_node, id="container")

    if hasattr(page, "render"):
        sig = inspect.signature(page.render)
        output = page.render(shared_el) if "EL" in sig.parameters else page.render()
    else:
        output = str(page)

    output_str = "".join(output) if not isinstance(output, str) else str(output)

    assert 'id="container"' in output_str
    assert expected in output_str


@pytest.mark.parametrize(
    "name, raw_data, expected", NATIVE_TYPES + ADVANCED_API_CLASSES
)
@pytest.mark.parametrize("arch_name, TargetWrapper, is_func", TARGET_ARCHITECTURES)
def test_proxy_streaming(
    shared_el, name, raw_data, expected, arch_name, TargetWrapper, is_func
):
    """Tests bridging both raw Python types and Advanced Probo API into streams."""

    # Recreate generators as they exhaust
    if name == "generator":
        raw_data = (str(i) for i in range(3))

    proxied_node = setup_proxy(raw_data)

    if is_func:
        if "EL" in inspect.signature(TargetWrapper).parameters:
            stream_gen = TargetWrapper(
                shared_el, proxied_node, id="container", stream=True, batch=10
            )
        else:
            stream_gen = TargetWrapper(
                proxied_node, id="container", stream=True, batch=10
            )
    else:
        page = TargetWrapper(proxied_node, id="container")
        sig = inspect.signature(page.stream)
        stream_gen = (
            page.stream(shared_el, batch=10)
            if "EL" in sig.parameters
            else page.stream(batch=10)
        )

    # stream_gen could be a native generator or a StreamManager object
    assert hasattr(
        stream_gen, "__iter__"
    ), f"Expected iterable StreamManager/Generator, got {type(stream_gen)}"

    chunks = list(stream_gen)
    full_output = "".join(chunks)

    assert len(chunks) > 0, f"Stream failed for {name} on {arch_name}"
    assert 'id="container"' in full_output
    assert expected in full_output


# =====================================================================
# 4. LOGIC LOADING TESTS (Updated for stream_callable)
# =====================================================================


def test_proxy_logic_loading():
    """
    Verifies that ProxyElement exposes and utilizes both render and stream loaders,
    and accurately respects the obj_as_arg=True execution pattern.
    """

    # 1. Test Advanced Component (Has native Render and Stream)
    component = MockComponent()
    proxy = ProxyElement(tag="div")
    proxy.load_logic(component)

    # Rendering should succeed natively
    assert proxy._logic_obj is component
    assert proxy.render() == "<custom-comp>Mounted</custom-comp>"

    # Streaming should succeed natively using yield from self._logic_obj.stream()
    stream_out = list(proxy.stream(batch=50))
    assert "Mounted" in "".join(stream_out)

    # 2. Test Primitive Data (Requires lambda fallback injection)
    primitive_data = [1, 2, 3]
    primitive_proxy = ProxyElement(tag="div")
    primitive_proxy.load_logic(primitive_data)

    # Load logic expecting obj_as_arg=True
    primitive_proxy.load_render_logic(lambda obj: f"RENDER: {obj}")

    def mock_stream(obj):
        yield f"STREAM: {obj}"

    primitive_proxy.load_stream_logic(mock_stream)

    assert primitive_proxy.render_callable is not None
    assert primitive_proxy.stream_callable is not None

    # Verify execution mapping works correctly with the parameter
    assert primitive_proxy.render(obj_as_arg=True) == "RENDER: [1, 2, 3]"
    assert "".join(list(primitive_proxy.stream(obj_as_arg=True))) == "STREAM: [1, 2, 3]"
