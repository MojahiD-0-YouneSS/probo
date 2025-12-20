import pytest
from mui.components.component import Component
from mui.components.state.component_state import ComponentState

# ==============================================================================
#  HELPER SUBCLASSES (Spying on the Real Component)
# ==============================================================================

class SpyInitComponent(Component):
    """Subclass to verify on_init is called by the parent __init__."""
    def on_init(self):
        # Determine if this ran
        self.init_was_called = True
        # Verify state exists at this point
        self.init_state_check = self.comp_state is not None

class SpyRenderComponent(Component):
    """Subclass to verify before_render receives data."""
    def before_render(self, **props):
        self.render_was_called = True
        self.received_props = props
        # Mutate props to prove we can affect the render
        if props:
            self.props.update(props)
            self.props['injected_by_hook'] = True

class OrderTrackingComponent(Component):
    """Tracks the sequence of events."""
    def __init__(self, name, **kwargs):
        self.history = []
        super().__init__(name, **kwargs)
        self.history.append("init_finished")

    def on_init(self):
        self.history.append("on_init")

    def before_render(self, **props):
        self.history.append("before_render")

# ==============================================================================
#  THE 5 LIFECYCLE TESTS
# ==============================================================================

def test_real_component_on_init_auto_call():
    """
    1. Verify on_init is triggered automatically during instantiation.
    """
    # We pass minimal valid args to the real Component constructor
    comp = SpyInitComponent(name="TestInit", template="<div></div>")
    
    # Check if the hook ran
    assert getattr(comp, 'init_was_called', False) is True
    # Check if the component was fully set up when the hook ran
    assert comp.init_state_check is True

def test_real_component_before_render_call():
    """
    2. Verify before_render is triggered when .render() is called.
    """
    comp = SpyRenderComponent(name="TestRender", template="<div></div>")
    
    # Hook shouldn't have run yet
    assert getattr(comp, 'render_was_called', False) is False
    
    # Run render
    comp.render()
    
    # Now it should have run
    assert comp.render_was_called is True

def test_real_component_before_render_receives_overrides():
    """
    3. Verify before_render receives the specific props passed to render().
    """
    comp = SpyRenderComponent(name="TestArgs", template="<div></div>")
    
    overrides = {'theme': 'dark', 'user_id': 99}
    comp.render(override_props=overrides)
    
    # Check if the hook got the exact dictionary object (or copy)
    assert comp.received_props == overrides
    assert comp.received_props['theme'] == 'dark'

def test_real_component_hook_modifies_state():
    """
    4. Verify that logic inside before_render actually changes the Component's props.
    This is the primary use case (e.g., calculating data before render).
    """
    comp = SpyRenderComponent(name="TestMutation", template="<div></div>")
    
    # Verify pre-state
    assert 'injected_by_hook' not in comp.props
    
    # Render with some props
    comp.render(override_props={'trigger': True})
    
    # Verify post-state (The hook modified self.props)
    assert comp.props['injected_by_hook'] is True
    assert comp.props['trigger'] is True

def test_real_component_lifecycle_order():
    """
    5. Verify the strict order of operations.
    Expected: on_init -> (constructor finishes) -> before_render -> render output
    """
    comp = OrderTrackingComponent(name="OrderTest", template="<div></div>")
    
    # At this point, init is done
    assert comp.history == ["on_init", "init_finished"]
    
    # Now render
    comp.render()
    
    # Check full timeline
    assert comp.history == ["on_init", "init_finished", "before_render"]