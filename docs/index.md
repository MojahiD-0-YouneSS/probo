

# <img src="./assets/images/mastodon_ui.ico" align="center" alt="Probo UI Logo" width="200" height="200"/> Probo UI : Python Rendered Objects for Backend-Oriented User Interfaces.
![PyPI](https://img.shields.io/pypi/v/probo-ui)
![Python](https://img.shields.io/pypi/pyversions/probo-ui)
![License](https://img.shields.io/github/license/MojahiD-0-YouneSS/probo)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://MojahiD-0-YouneSS.github.io/probo/)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
[![Discord](https://img.shields.io/badge/chat-Discord-5865F2)](https://discord.gg/jnZRbVasgd)
![Last Commit](https://img.shields.io/github/last-commit/MojahiD-0-YouneSS/probo)
![Repo Size](https://img.shields.io/github/repo-size/MojahiD-0-YouneSS/probo)
![Tests](https://img.shields.io/badge/Tests-1210%20Passed-brightgreen?style=flat-square&logo=github)
[![APIs](https://img.shields.io/badge/APIs-550%20Ready-blue?style=flat-square&logo=python&logoColor=white)](https://MojahiD-0-YouneSS.github.io/probo/)

Python Rendered Objects for Backend-Oriented User Interfaces.

Probo UI is a Python-Native, server-side Template Rendering Framework and micro web-framework. It allows you to write Type-Safe template components, structure HTML, and apply CSS styling using pure Python.

By transforming Python objects into highly performant HTML/CSS (with native HTMX support), Probo creates a seamless bridge between your backend logic and frontend interface. No context switching. No template spaghetti.

# 📣 Version 1.4.0 Architecture is Live!"
Probo UI has officially reached its stable, highly-optimized release. It is ready to act as the backend-first UI framework for your next massive application.

Why Probo?

#### 1. 🐍 Use your Python skills: Build dynamic UI templates without leaving Python.

#### 2. 📖 Explicit & Readable: Create highly reusable and composable layouts.

#### 3. 🛠️ Easy Refactoring: Because your UI is just Python objects, refactoring is infinitely easier than dealing with raw HTML strings.

#### 4. ✅ IDE-Friendly & Type-Safe: Catch UI errors at compile-time, not run-time.

# ⚡ Purpose & Philosophy

Traditional backend development (like Django or FastAPI) often requires context-switching between Python (views.py) and HTML/Jinja (templates/). Logic gets split, typos in templates cause hidden runtime errors, and performance suffers due to massive string concatenations.

## Probo UI solves this by bringing the Frontend directly into Python:

#### 1.  🧠 Type-Safe UI: Write HTML in Python. If your code compiles, your HTML is valid.

#### 2. 🎨 Just-In-Time (JIT) CSS: Styles live with components. Probo UI scans your active components and generates minified CSS bundles on the fly. No unused styles.

#### 3.🛡️ Logic Gates: Built-in State Management. Components automatically hide themselves if required data (like user.is_authenticated) or permissions are missing.

#### 4. 🔌 Ecosystem Native: Deep integrations with Django Forms, ASGI/WSGI engines, and Request Transformers.

# 🧬 Choose Your Chimera (Flexible Paradigms)

Probo UI supports multiple architectural paradigms for building UIs. You can strictly follow one, or mix them together to create a flexible "Chimera" architecture tailored to your specific needs.

### Reserved Python Keywords !!
All reserved Python keywords are mapped to capitalized notations (e.g., id -> Id, class -> Class, map -> Map). During the render phase, the appropriate lowercase HTML attributes are automatically applied!

Supported Paradigms (Ranked by speed: fastest to most feature-rich):

- Light Functional (l_div, l_span): Blistering speed, minimal memory overhead.

- Pure Functional (div, span): Fast, function-based HTML tags.

- Light OOP (Ldiv, Lspan): Object-oriented structures with a lightweight footprint.

- Pure OOP / Heavy (DIV, SPAN): Full feature set including state management, CSS binding, and deep tree traversal.

📦 Installation
```bash

pip install probo-ui
```

🚀 Quick Examples

## Basic Component

Here is how you implement a fast, reusable component using a mix of OOP and Functional Probo components.

```python
from probo import li, div, h1, ul, strong, DIV

def user_card(username):
    user_id = f'User_789{username}1323'
    user_info = {'practical-info': ['python', 'javascript', 'docker', 'django']}
    
    # Generate list items functionally
    li_el = [li(info) for info in user_info['practical-info']]

    # Compose the final card
    card = DIV(
        h1(username, strong(user_id)),
        ul(*li_el),
        Class='card',
        style='color:red;'
    )
    return card

html = user_card("Admin")
# style it
html.style_manager.margin = "4px"
html.style_manager.padding = "5px"
# Render it
html_string = httml.render()

```

**Output:**
```html 
<div class='card' style='color:red; margin:4px; padding:5px;'>
    <h1>Admin<strong>User_789Admin1323</strong></h1>
    <ul>
        <li>python</li>
        <li>javascript</li>
        <li>docker</li>
        <li>django</li>
    </ul>
</div>
```


##  State/Permission Component

Probo includes a powerful state engine. Here, the `li` tags will only render if the username passed to the props is strictly `"admin"`.

```python
from probo.components import Component, ComponentState, ElementState, StateProps
from probo import div, h1, strong, ul

def user_card(username):
    # 1. Define Props (Must be 'admin' to pass)
    props = StateProps(required=True, prop_equals={'username': 'admin'})
    
    user_id = f'User_789{username}1323'
    user_info = {'practical-info': ['python', 'javascript', 'docker', 'django']}
    
    # 2. Define Stateful Element
    li_el = ElementState(
        'li', 
        d_state='practical-info',
        i_state=True, 
        hide_dynamic=True,
        props=props,
    )
    
    # 3. Create Component State
    user_comp_state = ComponentState(d_data=user_info, li_el)

    # 4. Compose the Smart Component
    card = Component(
        name="UserCard",
        template=div(
            h1(username, strong(user_id)),
            ul(li_el.placeholder),
            Class='card'
        ),
        state=user_comp_state,
        props={'username': username}  # Inject Data here!
    )
    return card

# Render outputs
html_denied = user_card("Guest").render()
html_allowed = user_card("admin").render()
```

**Output (Guest):**
```html
<div class='card'><h1>Guest<strong>User_789Guest1323</strong></h1><ul></ul></div>
```

**Output (Admin):**
```html
<div class='card'><h1>admin<strong>User_789admin1323</strong></h1><ul><li>python</li><li>javascript</li><li>docker</li><li>django</li></ul></div>
```


💬 Community & Support

Ready to start building?

[ 🚀 Get Started → ](user_guide.md)

💬 Community & Support Need help? Have a question that isn't a bug? Join our [Discord](https://discord.gg/jnZRbVasgd) Server to chat with other probo-ui developers.

Need help? Have a question that isn't a bug? Join our Discord Server to chat with other Probo UI developers and share your creations!