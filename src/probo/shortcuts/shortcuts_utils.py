from probo.shortcuts.configs import ElementStateConfig
from probo.components.state.component_state import ElementState


def make_es_from_esc(config: ElementStateConfig) -> ElementState:
    """Factory function that transforms an ElementStateConfig blueprint into an ElementState instance.

    This utility acts as a translator within the ProboUI compiler pipeline. It 
    extracts the declarative metadata from the configuration object (ESC) and 
    hydrates a new stateful element (ES) that can be manipulated by the 
    component's logic.

    Args:
        config (ElementStateConfig): The configuration object containing 
            tag name, state identifiers, and attributes.

    Returns:
        ElementState: A live state object initialized with the configuration's 
            parameters, ready for rendering or data binding.
    """
   
    return ElementState(
        element=config.tag,
        s_state=config.s_state,
        d_state=config.d_state,
        c_state=config.c_state,
        hide_dynamic=config.hide_dynamic,
        is_void_element=config.is_void_element,
        attrs=config.attrs,
    )
