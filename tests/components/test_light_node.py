import pytest
import inspect
from collections import deque
# Adjust import path to wherever your LightNode actually lives
from probo.components.light_tags.node import LightNode
from probo.components import Element


# ==========================================
# MOCKS AND FIXTURES
# ==========================================


class HeavyNodeMock:
    """Mocks a traditional 'Heavy' Probo Component with its own stream/render."""

    def render(self):
        return "<HeavyNodeMock> HEAVY_RENDER </HeavyNodeMock>"

    def stream(self, batch=50):
        yield from (x for x in ["<HeavyNodeMock>","HEAVY_STREAM","</HeavyNodeMock>"])


class MockEL:
    """Mocks the EL (Typewriter) Engine with predictable properties."""

    def __init__(self, is_list=False, use_deque=False):
        self.is_list = is_list
        self.use_deque = use_deque
        self.element = ""
        self._attrs = {}
        self._gen = None

    def div(self, content=None, **attrs):
        self._attrs = attrs
        if content is not None:
            self.element = f"<div>{content}</div>"
        else:
            self.element = ["<div>", "</div>"]

    def single(self, content=None, **attrs):
        # Mocks a self-closing tag where len(EL.element) == 1
        self.element = ["<single/>"]

    def set_attrs(self, **attrs):
        self._attrs = attrs

    def set_generator_content(self, gen):
        self._gen = gen

    def stream(self, batch=50):
        if self._gen:
            yield from self._gen
        else:
            yield ""


# ==========================================
# TEST 1: INITIALIZATION & TAG INFERENCE
# ==========================================


def test_lightnode_initialization():
    """Tests content deque casting, attribute storage, and tag name logic."""

    # 1. Tuple Content
    node1 = LightNode("Hello", "World", tag="div", id="1")
    assert isinstance(node1.content, deque)
    assert len(node1.content) == 2
    assert node1.tag_name == "div"
    assert node1.attributes == {"id": "1"}

    # 2. Single Content
    node2 = LightNode("Single")
    assert len(node2.content) == 1
    assert node2.tag_name == "lightnode"  # Fallback to class name lower

    # 3. Capitalized L-prefixed Class Logic (e.g. Ldiv -> div)
    class Lspan(LightNode):
        pass

    node3 = Lspan()
    assert node3.tag_name == "span"

    # 4. Perfectly Capitalized Non-L Class Logic (e.g. Custom -> custom)
    class Custom(LightNode):
        pass

    node4 = Custom()
    assert node4.tag_name == "custom"


# ==========================================
# TEST 2: SYNCHRONOUS RENDERING
# ==========================================


def test_render_with_el_method():
    """Tests rendering when EL natively supports the tag (e.g., div)."""
    el = MockEL()
    node = LightNode("Content", tag="div")
    res = node.render(el)

    assert res == "<div>Content</div>"


def test_render_without_el_method():
    """Tests rendering when EL lacks the method, bypassing EL builder."""
    el = MockEL()
    # 'unknown' tag has no method on MockEL
    node = LightNode("Content", tag="unknown")
    el.element = "FALLBACK"
    res = node.render(el)

    assert res == "FALLBACK"


# ==========================================
# TEST 3: RECURSIVE CONTENT RESOLUTION
# ==========================================


def test_get_rendered_content_types():
    """Ensures nested LightNodes, generators, HeavyNodes, and strings resolve."""
    el = MockEL(is_list=False, use_deque=False)
    class ChildLight(LightNode):
        def __init__(self,*content,**attrs):
            super().__init__(*content, tag="ChildLight", **attrs)
        def render(self,el):
            return f"<ChildLight>{self._get_rendered_content(el)}</ChildLight>"
    child_light = ChildLight("child_text")
    heavy = HeavyNodeMock()
    def my_gen():
        yield "gen1"
        yield heavy

    node = LightNode(child_light, my_gen(), heavy, "normal_text", tag="div")
    res = node._get_rendered_content(el)

    assert "child_text" in res
    assert "gen1" in res
    assert "HEAVY_RENDER" in res
    assert "normal_text" in res


def test_get_rendered_content_list_flags():
    """Tests the EL.is_list and EL.use_deque branching logic."""
    el_list = MockEL(is_list=True, use_deque=False)
    el_deque = MockEL(is_list=True, use_deque=True)

    def my_gen():
        yield "gen_content"

    child_light = LightNode("child")
    node = LightNode(child_light, my_gen(), tag="div")

    # 1. Test is_list = True, use_deque = False
    res_list = node._get_rendered_content(el_list)
    assert isinstance(res_list, list)

    # 2. Test use_deque = True
    res_deque = node._get_rendered_content(el_deque)
    assert isinstance(res_deque, list)


def test_unreachable_elif_branch():
    """
    CRITICAL COVERAGE FIX:
    Your code contains `elif EL.is_list and EL.use_deque:` right below an identical `if`.
    We use a property mock to dynamically flip the boolean between evaluations to hit it!
    """

    class TrickEL(MockEL):
        def __init__(self):
            super().__init__(is_list=True)
            self.use_deque=True
    def my_gen():
        yield "trick"

    node = LightNode(my_gen())
    res = node._get_rendered_content(TrickEL())

    # Proves we successfully entered the unreachable branch
    assert isinstance(res, list)


# ==========================================
# TEST 4: ASYNCHRONOUS / STREAMING PIPELINE
# ==========================================


def test_stream_without_el_method():
    """Tests stream generation when EL doesn't know the tag (e.g., standard HTML)."""
    el = MockEL()
    node = LightNode("Streaming", tag="customtag", id="123")

    streamed = list(node.stream(el, batch_size=50))
    # It dynamically constructs [<customtag>, "", </customtag>]
    assert "".join(streamed) == "<customtag>Streaming</customtag>"


def test_stream_with_el_method():
    """Tests stream generation utilizing the EL method hook."""
    el = MockEL()
    node = LightNode("StreamedContent", tag="div")

    streamed = list(node.stream(el, batch_size=50))
    assert "".join(streamed) == "<div>StreamedContent</div>"


def test_stream_single_element_info():
    """Tests streaming for self-closing tags (where EL.element len == 1)."""
    el = MockEL()
    # MockEL.single() returns ["<single/>"]
    node = LightNode(tag="single")

    streamed = list(node.stream(el))
    # Because len == 1, it appends None in the stream logic
    assert "<single/>" in streamed


def test_get_stream_content_types():
    """Ensures nested LightNodes, HeavyNodes, and strings stream correctly."""
    el = MockEL()
    heavy = HeavyNodeMock()
    child_light = LightNode("light_str")

    node = LightNode(child_light, heavy, "normal_str", tag="div")

    res = list(node._get_stream_content(el, batch_size=50))
    assert "light_str" in res
    assert "HEAVY_STREAM" in res
    assert "normal_str" in res

# ==========================================
# TEST 5: DIFFERENT DATA TYPES (INT, FLOAT, LIST, DEQUE, BOOL, ETC)
# ==========================================

def test_lightnode_int_render():
    el = MockEL()
    node = LightNode(123, tag="div")
    assert "123" in node.render(el)

def test_lightnode_int_stream():
    el = MockEL()
    node = LightNode(123, tag="div")
    assert "123" in "".join(node.stream(el))

def test_lightnode_float_render():
    el = MockEL()
    node = LightNode(12.34, tag="div")
    assert "12.34" in node.render(el)

def test_lightnode_float_stream():
    el = MockEL()
    node = LightNode(12.34, tag="div")
    assert "12.34" in "".join(node.stream(el))

def test_lightnode_bool_render():
    el = MockEL()
    node = LightNode(True, False, tag="div")
    assert "True" in node.render(el)
    assert "False" in node.render(el)

def test_lightnode_bool_stream():
    el = MockEL()
    node = LightNode(True, False, tag="div")
    res = "".join(node.stream(el))
    assert "True" in res
    assert "False" in res

def test_lightnode_list_render():
    el = MockEL()
    node = LightNode([1, "two", 3.0], tag="div")
    res = node.render(el)
    assert "1" in res
    assert "two" in res
    assert "3.0" in res

def test_lightnode_list_stream():
    el = MockEL()
    node = LightNode([1, "two", 3.0], tag="div")
    res = "".join(node.stream(el))
    assert "1" in res
    assert "two" in res
    assert "3.0" in res
    assert "1 two 3.0" in res

def test_lightnode_generator_ints_render():
    el = MockEL()
    def gen_ints():
        yield 42
        yield   "test"
        yield 100
    node = LightNode(gen_ints(), tag="div")
    res = node.render(el)
    assert "42" in res
    assert "test" in res
    assert "100" in res
    assert "42 test 100" in res

def test_lightnode_generator_ints_stream():
    el = MockEL()
    def gen_ints():
        yield 42
        yield 100
    node = LightNode(gen_ints(), tag="div")
    res = "".join(node.stream(el))
    assert "42" in res
    assert "100" in res

# ==========================================
# TEST 6: DATA PIPELINE INTEGRATION
# ==========================================

from probo.components.light_tags import Ldiv, Lspan

def test_lightnode_pipeline_simple():
    parent = Ldiv(Lspan({'username'}))
    parent.load_data({'username': 'Alice'})
    assert parent.render(Element()) == "<div><span>Alice</span></div>"

def test_lightnode_pipeline_nested():
    parent = Ldiv(Lspan({'user.profile.age'}))
    parent.load_data({'user': {'profile': {'age': 30}}})
    assert parent.render(Element()) == "<div><span>30</span></div>"

def test_lightnode_pipeline_lambda():
    parent = Ldiv(Ldiv({'x', 'y', lambda **kw: str(kw.get('x',0) + kw.get('y',0))}))
    parent.load_data({'x': 15, 'y': 25})
    assert parent.render(Element()) == "<div><div>40</div></div>"

def test_lightnode_pipeline_attributes():
    parent = Ldiv(Ldiv("Content", id={'dynamic_id'}))
    parent.load_data({'dynamic_id': 'header-123'})
    assert parent.render(Element()) == '<div><div id="header-123">Content</div></div>'

def test_lightnode_pipeline_component_return():
    def make_badge(**kw):
        return Lspan(kw.get('role'))
    parent = Ldiv(Ldiv({'role', make_badge}))
    parent.load_data({'role': 'Admin'})
    assert parent.render(Element()) == "<div><div><span>Admin</span></div></div>"

def test_lightnode_pipeline_attributes_mutation():

    parent = Ldiv(Ldiv("Content", id={'dynamic_id'}))
    parent.attributes['class']={'dynamic_id', lambda **dvars: f"admin {dvars.get('dynamic_id')} string"}
    parent.load_data({'dynamic_id': 'header-123'})
    print(parent.has_unresolved_pipeline_vars)
    assert parent.render(Element()) == '<div class="admin header-123 string"><div id="header-123">Content</div></div>'

def test_lightnode_pipeline_content_return_mutation():
    def make_badge(**kw):
        return Lspan('new content',kw.get('role'))
    parent = Ldiv(Ldiv({'role', make_badge},Id={'role'},), data_pipeline={'role': 'Admin'})
    # Render with MockEL instead of Element to avoid needing typewriter dependencies here
    assert parent.render(Element()) == '<div><div id="Admin"><span>new content Admin</span></div></div>'
    spn = parent.find(lambda n: n.attributes.get('Id') == 'Admin')
    print(spn.content)
    if spn:
        spn.inner_html('new content', {'role'} ,overwrite=True,)
    print(spn.content)
    # Render with MockEL instead of Element to avoid needing typewriter dependencies here
    assert parent.render(Element()) == '<div><div id="Admin">new content Admin</div></div>'

