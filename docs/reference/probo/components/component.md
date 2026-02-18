# Component

The `Component` class is the heart of Probo UI. It manages state, rendering, and context.

---

::: probo.components.component
    options:
      # 1. VISUAL STRUCTURE
      heading_level: 2          # Start headers at H2 (##) instead of H1 (#)
      show_root_heading: true   # Show the name "Component" at the top
      show_root_full_path: false # Show "Component" instead of "probo.components.component.Component"

      # 2. CONTENT CONTROL
      show_source: false        # Hide the "View Source" button (keep it clean)
      show_category_heading: true # Group things by "Methods", "Attributes", etc.
      
      # 3. FILTERING (Pick what to show)
      members:                  # Only show these specific methods
        - __init__
        - render
        - get_context
      
      # OR use filters (uncomment to use)
      # filters:
      #   - "!^_"               # Exclude anything starting with "_" (private methods)