import pytest
from probo.components.base import BaseHTMLElement
from probo.components.node import ProxyElement
from probo.components.power_node import PowerNode
from probo import DIV, P
from probo.exceptions.components_error import TargetNotFound


class ColorPowerNode(PowerNode):
    def execute(self, target):
        target.style_manager.color="red"

class BackNode(PowerNode):
    def execute(self, target):
        data_pipeline = self.parent.get_data_pipeline

        data_pipeline['p']=789

        data_pipeline['a']=456

        data_pipeline['i']=123

class ContentProxy(ProxyElement):
    def exe(self):
        self.attr_manager.add_class("proxy-executed")

def test_power_node_registration_via_kwargs():
    pnode = ColorPowerNode(lambda n: n.tag == 'P', hook='on_mount')
    container = DIV(P("Hello",{'p'}), power_nodes=[pnode,BackNode(lambda n:n, hook='on_mount')],data_pipeline={'p':1,'a':7,'i':8})

    # Check registration
    assert pnode in container._power_node_registry
    
    # Trigger the fallback phase manually since render() no longer triggers phases automatically
    # container.before_target()
    # # prnd = container.get_power_node(all_nodes=True)
    # #
    # # for p in prnd:
    # #     p.exe()
    html = container.render()
    assert "color:red;" in html
    assert "Hello 789" in html

def test_power_node_registration_via_children():
    pnode = ColorPowerNode(lambda n: getattr(n, 'tag', None) == 'P', hook='on_mount')
    # Passed directly as child
    container = DIV(P("Hello"), pnode)
    
    # Should not be in content
    assert pnode not in container.content
    assert pnode in container._power_node_registry

    html = container.render()
    assert "color:red;" in html

def test_proxy_element_hook_phase():
    # Proxy executes in background at specific phase
    proxy = ContentProxy(tag='span', run_in_background=False, wrap_result=True, hook="on_mount")
    container = DIV(proxy, Class="box")

    assert proxy in container._proxy_registry

    html = container.render()
    # If it was executed before target, the class proxy-executed should be present
    assert "proxy-executed" in html
    
def test_power_node_target_not_found():
    # Searching for H1 but none exists
    pnode = ColorPowerNode(lambda n: getattr(n, 'tag', None) == 'H1', hook='on_mount')
    with pytest.raises(TargetNotFound):

        container = DIV(P("Hello"), pnode)
        container.render()

def test_power_node_before_render_hook():
    class RenderTrackingPowerNode(PowerNode):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.before_render_called = False
            self.execute_called = False

        def before_render(self):
            self.before_render_called = True

        def execute(self, target):
            self.execute_called = True
            target.style_manager.color = "blue"

    pnode = RenderTrackingPowerNode(lambda n: getattr(n, 'tag', None) == 'P', hook='before_render')
    container = DIV(P("Hello"), pnode)

    assert not pnode.before_render_called
    assert not pnode.execute_called

    html = container.render()

    assert "color:blue;" in html
    assert pnode.execute_called
    assert pnode.before_render_called

def test_proxy_element_before_render_hook():
    class RenderTrackingProxy(ProxyElement):
        def __init__(self, *content, tag='div', wrap_result=False, **attrs):
            super().__init__(*content, tag=tag, wrap_result=wrap_result, **attrs)
            self.before_render_called = False
            self.execute_called = False

        def before_render(self):
            print('why???')
            self.before_render_called = True

        def exe(self):
            self.execute_called = True
            self.attr_manager.add_class("before-render-proxy")

    proxy = RenderTrackingProxy(tag='span', run_in_background=False, wrap_result=True, hook="before_render")
    container = DIV(proxy)

    assert not proxy.before_render_called
    assert not proxy.execute_called

    html = container.render()

    assert "before-render-proxy" in html
    assert proxy.execute_called
    assert proxy.before_render_called

