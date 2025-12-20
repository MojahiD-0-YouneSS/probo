import pytest
from mui.request.request_context import ComponentRequestContext

# ==============================================================================
#  MOCKS
# ==============================================================================

class MockComponent:
    """Simulates the Component Lifecycle API."""
    def __init__(self, name="Mock"):
        self.name = name
        self.props = {}
        
        # Lifecycle Flags
        self.init_called = False
        self.before_render_called = False
        self.last_render_props = None
        
        # Trigger Init Hook
        self.on_init()

    def on_init(self):
        """Lifecycle Hook: Called after __init__"""
        self.init_called = True

    def before_render(self, props):
        """Lifecycle Hook: Called before render logic"""
        self.before_render_called = True
        self.last_render_props = props
        if props:
            self.props.update(props)

    def render(self, override_props=None):
        """Simulate render flow"""
        self.before_render(override_props)
        return f"<div>{self.name}</div>"

# ==============================================================================
#  PART 1: ComponentRequestContext Tests (5 Tests)
# ==============================================================================

def test_crc_initialization_storage():
    """1. Test that components and props are stored correctly on init."""
    c1 = MockComponent("C1")
    ctx = ComponentRequestContext(c1, theme="dark", user="admin")
    
    assert c1 in ctx.components
    assert ctx.context_props['theme'] == "dark"
    assert ctx.context_props['user'] == "admin"

def test_crc_process_applies_props():
    """2. Test applying stored props to registered components."""
    c1 = MockComponent("C1")
    # Pre-existing props should be cleared based on your logic
    c1.props = {'garbage': 'value'}
    
    ctx = ComponentRequestContext(c1, theme="light")
    ctx.process_components()
    
    assert 'garbage' not in c1.props
    assert c1.props['theme'] == "light"

def test_crc_process_with_extra_components():
    """3. Test processing transient components passed at runtime."""
    c1 = MockComponent("Stored")
    c2 = MockComponent("Extra")
    
    ctx = ComponentRequestContext(c1, mode="read")
    # Pass c2 only during processing
    results = ctx.process_components(c2)
    
    assert c1 in results
    assert c2 in results
    assert c1.props['mode'] == "read"
    assert c2.props['mode'] == "read"

def test_crc_process_with_extra_props():
    """4. Test overriding/adding props at runtime."""
    c1 = MockComponent("C1")
    ctx = ComponentRequestContext(c1, color="blue")
    
    # Runtime override: color=red
    ctx.process_components(color="red", size="lg")
    
    assert c1.props['color'] == "red"
    assert c1.props['size'] == "lg"

def test_crc_isolation():
    """5. Test that processing does not mutate the original definition permanently."""
    c1 = MockComponent("C1")
    ctx = ComponentRequestContext(c1, base="original")
    
    # Run A with extras
    ctx.process_components(extra="A")
    assert c1.props['extra'] == "A"
    
    # Run B without extras (should revert to base context + clear)
    # Note: Your logic clears props every time, so it resets state
    ctx.process_components()
    assert 'extra' not in c1.props
    assert c1.props['base'] == "original"


# ==============================================================================
#  PART 2: Component Lifecycle Tests (5 Tests)
# ==============================================================================

def test_lifecycle_on_init_execution():
    """1. Verify on_init is called automatically during instantiation."""
    comp = MockComponent("Life")
    assert comp.init_called is True

def test_lifecycle_before_render_execution():
    """2. Verify before_render is called when render() is invoked."""
    comp = MockComponent("RenderTest")
    assert comp.before_render_called is False # Not yet
    
    comp.render()
    assert comp.before_render_called is True

def test_lifecycle_before_render_receives_overrides():
    """3. Verify before_render receives arguments passed to render()."""
    comp = MockComponent("Args")
    overrides = {'active': True}
    
    comp.render(override_props=overrides)
    
    assert comp.last_render_props == overrides
    assert comp.props['active'] is True

def test_lifecycle_subclass_hook_override():
    """4. Verify a subclass can effectively override the hook."""
    class CustomComp(MockComponent):
        def on_init(self):
            super().on_init()
            self.props['setup_complete'] = True

    comp = CustomComp()
    assert comp.init_called is True
    assert comp.props.get('setup_complete') is True

def test_lifecycle_state_flow():
    """5. Verify the order of operations (Init -> Props -> Render)."""
    # Define a component that tracks order
    class OrderComp(MockComponent):
        def __init__(self):
            self.history = []
            super().__init__()
            self.history.append("init_finished")
        
        def on_init(self):
            self.history = ["on_init"] # Initializer runs before init finishes
            
        def before_render(self, props):
            self.history.append("before_render")
            
    comp = OrderComp()
    comp.render()
    
    # Expected: on_init -> init_finished -> before_render
    assert comp.history == ["on_init", "init_finished", "before_render"]