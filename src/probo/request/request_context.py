from typing import Any, List


class ComponentRequestContext:
    """
    This class handles injecting global/context properties into Component objects
    that are not directly tied to a request lifecycle (e.g., static components needing context).
    """

    def __init__(self, *components_objs, **context_props):
        self.context_props = context_props
        self.components = list(components_objs)
        self.processed_components = []

    def process_components(self, *extra_component_objs, **extra_props) -> List[Any]:
        """
        Applies the stored context_props (plus any extra_props) to all components.
        """
        # 1. Prepare Context (Merge defaults with extras)
        current_context = self.context_props.copy()
        if extra_props:
            current_context.update(extra_props)

        # 2. Prepare Targets (Merge defaults with extras)
        targets = self.components.copy()
        if extra_component_objs:
            targets.extend(extra_component_objs)

        # 3. Apply Context to Components
        self.processed_components = []
        for obj in targets:
            # We assume obj has a 'props' dictionary
            if hasattr(obj, "props") and isinstance(obj.props, dict):
                obj.props.clear()
                obj.props.update(current_context)
            self.processed_components.append(obj)

        return self.processed_components
