from typing import Any, List


class ComponentRequestContext:
    """Handles the bulk injection of context data into ProboUI components.

    This class provides a mechanism to hydrate component objects with global 
    or request-specific properties. It is designed to bridge the gap between 
    static component definitions and dynamic request data, ensuring that 
    components have access to required 'props' before rendering.

    Attributes:
        context_props (Dict[str, Any]): The default key-value pairs to be 
            injected into components.
        components (List[Any]): A registry of component objects targeted 
            for context injection.
        processed_components (List[Any]): A cache of components that have 
            already undergone context application.
    """

    def __init__(self, *components_objs, **context_props):
        self.context_props = context_props
        self.components = list(components_objs)
        self.processed_components = []

    def process_components(self, *extra_component_objs, **extra_props) -> List[Any]:
        """Applies context data to the stored and extra component targets.

        This method merges stored properties with any one-time extra properties, 
        then iterates through the target components. For each component with 
        a `props` attribute, it clears existing data and performs a bulk update 
        with the current context.

        Args:
            *extra_component_objs: Additional components to process in 
                this specific call.
            **extra_props: Additional context properties to merge with 
                the stored defaults.

        Returns:
            A list of components that have been updated with the merged context.

        Examples:
            >>> ctx = ComponentRequestContext(user_bar, sidebar, theme="dark")
            >>> # Hydrate components with theme + dynamic user data
            >>> hydrated_list = ctx.process_components(user_id=123)
            >>> print(user_bar.props['theme'])
            'dark'
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
