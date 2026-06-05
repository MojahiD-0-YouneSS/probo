---
name: "Doc Task: Light Functional"
about: Good first issue to document Light Functional tags
title: "[DOC Light Functional] implement google style doc strings on probo/components/light_tags/func/block_tags.py"
labels: good first issue, documentation
assignees: ''
---

We are updating our documentation to strictly use Google-style docstrings across the Probo UI framework!

This issue involves updating the docstrings for a batch of light functional HTML components located in `probo/components/light_tags/func/`.

### 🎯 Tags to update in this batch:
*(Maintainer will list the ~15 tags here)*

### 📝 Requirements
Your docstrings must include:
1. A brief description of the HTML element function.
2. Inherited API usage demonstrating `attr_manager` and the metaprogramming features of `style_manager`.
3. Args definition (`*content`, `**attrs`).
4. A short Python example.

### 💡 Example Docstring Format
Please use this exact structure for all functional tags:

```python
def a(*content: Any, **attrs: Any) -> Component:
    """
    Represents an HTML <a> (anchor) element in the SSDOM.

    This function creates hyperlinked elements. It utilizes the core 
    functionalities, including robust attribute and inline style management.

    Inherited API Usage:
        attr_manager (ElementAttributeManipulator):
            Used to safely mutate, retrieve, or delete HTML attributes for this tag 
            after initialization.
            Example:
                >>> my_link = a("Click here")
                >>> my_link.attr_manager.set_attr("href", "https://example.com")
                >>> my_link.attr_manager.set_attr("target", "_blank")
        
        style_manager (StyleManager):
            Utilizes Python metaprogramming to dynamically manage inline CSS styles 
            for this tag. You can use standard methods or dot-notation.
            Example:
                >>> my_link.style_manager.add_style("text_decoration", "none")
                >>> my_link.style_manager.color = "blue"

    Args:
        *content (str | Any): The inner text or child SSDOM nodes of the anchor tag.
        **attrs (Any): Standard HTML attributes to be passed into the element 
            (e.g., href="...", Class="nav-link").

    Example:
        >>> link = a("Probo UI", href="https://probo.dev", Class="link-primary")
        >>> link.style_manager.font_weight = "bold"
        >>> print(link.render())
        <a href="https://probo.dev" class="link-primary" style="font-weight: bold;">Probo UI</a>
    """
```
