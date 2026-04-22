# CSS in SSDOM

Probo UI provides several ways to apply styling to your components. This page explains the current supported approaches.

---

## 1. Inline CSS

### A. Using `style` keyword argument (Recommended for simple cases)

Most UI functions and classes accept a `style` parameter:

```python
from probo import div, h1, button

card = div(
    h1("Hello Probo"),
    button("Click Me"),
    Class="card",
    style="background-color: #f8f9fa; padding: 20px; border-radius: 8px;"
)
```

# B. Using StyleManager (For dynamic / heavy styling)
```python
card = div(Class="card")

# Modify styles after creation
card.style_manager.add("background-color", "#ffffff")
card.style_manager.padding = "24px"
card.style_manager.margin = "16px"
card.style_manager.border_radius = "12px"

# You can also remove styles
card.style_manager.remove("margin")
```
### C. using Elementstyle
for sharable inline css use `elmnet_style(**css)` it returns inline css string syntax

```python

from probo.styles import element_style

shared_css = element_style(padding='4px',color="red",margin="1px 2px 0 0")
card1 = div(
    h1("styled Card1"),
    Class="card",
    style=shared_css
)
card2 = div(
    h1("styled Card2"),
    Class="card",
    style=shared_css
)

```

# 2. STYLE Object (For Animations & Complex CSS)
The STYLE object is designed for CSS that cannot be easily expressed as inline styles, such as:

- Keyframe animations
- Media queries
- Complex selectors
- Shared themes
## Note: use this like normal style tag.
```python

from probo.css import STYLE

# Define complex CSS (supports normal CSS syntax)
fade_animation = STYLE("""
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    
    .card {
        animation: fadeIn 0.4s ease-out forwards;
    }
""")
""""
this is the tree representation of probo.templates.default_templates.base_template_Tree
DOCTYPE (Root)
        └── HTML [lang="en"]
            ├── HEAD
            │   ├── META [charset="UTF-8"]
            │   ├── META [http-equiv="x-ua-compatible"]
            │   ├── META [viewport]
            │   ├── META [description]
            │   ├── META [author]
            │   ├── TITLE ("my project is cool")
            │   ├── LINK [favicon]
            │   ├── LINK [bootstrap.css]
            │   ├── STYLE               <======================= place it here is recommended
            │   ├── SCRIPT [htmx.js]
            │   ├── SCRIPT [bootstrap.js]
            │   └── SCRIPT [project.js]
            └── BODY
                ├── DIV [Class="mb-1"] (Navbar Wrapper)
                │   └── NAV [Class="navbar..."]
                │       └── DIV [Class="container-fluid"]
                │           ├── BUTTON (Navbar Toggler)
                │           │   └── SPAN [Class="navbar-toggler-icon"]
                │           ├── A [Class="navbar-brand"] ("mvp_base")
                │           └── DIV [Id="navbarSupportedContent"] (Collapse)
                │               └── UL [Class="navbar-nav mr-auto"]
                │                   ├── LI -> A ("home")
                │                   ├── LI -> A ("about")
                │                   └── LI -> A ("log in")
                ├── DIV [Class="container"] (Main Content Container)
                │   └── SPAN [hx-get="/contact"] ("click me")
                └── SCRIPT ("")
""""
```
### STYLE objects are ideal for animations and reusable advanced CSS rules.

# 3. Using .css Method (Recommended)
Currently, the cleanest and most recommended way to apply CSS in SSDOM is using the link/LINK
```python
from probo import LINK

# Link an external CSS file
custom_css = LINK(href="static/css/custom.css",rel="stylesheet")
main_css = LINK(href="/assets/styles/main.css",rel="stylesheet")

```
These are typically added to the HEAD section of your base template.

# 4. Advanced CSS: CSSRule, CSSSelector, CSSAnimation

These are powerful but still under active development. The Developer Experience (DX) is not yet optimal, so we recommend using .css() for most use cases at this stage.

### Important Note About JIT CSS
JIT (Just-In-Time) CSS currently works on rendered HTML strings, not directly on the SSDOM tree.
This means JIT optimization happens after calling .render() or during final output.
We are actively improving native JIT support for SSDOM objects.

# Best Practices (Current Version)

- Use inline style for simple, one-off styling
- Use `StyleManager` when you need to modify styles dynamically
- Use `STYLE` object for animations, keyframes, and complex non-inline CSS
- Use `LINK`/`link` for traditional external stylesheets
- Advanced objects (`CSSRule`, `CSSSelector`, `CSSAnimation`) are available but still maturing