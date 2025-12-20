from mui.shortcuts.configs import ElementStateConfig
from mui.components.state.component_state import ElementState



def make_es_from_esc(config: ElementStateConfig) -> ElementState:
    """Helper to create ElementState from ElementStateConfig."""
    return ElementState(
        element=config.tag,
        s_state=config.s_state,
        d_state=config.d_state,
        c_state=config.c_state,
        hide_dynamic=config.hide_dynamic,
        is_void_element=config.is_void_element,
        attrs=config.attrs,
    )