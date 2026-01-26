# 🐘 Probo UI
![PyPI](https://img.shields.io/pypi/v/probo-ui)
![Python](https://img.shields.io/pypi/pyversions/probo-ui)
![License](https://img.shields.io/github/license/MojahiD-0-YouneSS/probo)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://MojahiD-0-YouneSS.github.io/probo/)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
[![Discord](https://img.shields.io/badge/chat-Discord-5865F2)](https://discord.gg/jnZRbVasgd)
![Last Commit](https://img.shields.io/github/last-commit/MojahiD-0-YouneSS/probo)
![Repo Size](https://img.shields.io/github/repo-size/MojahiD-0-YouneSS/probo)

A Python-Native server-side Template Rendering Framework and Meta-framework for Django.Write Type-Safe Template Components, structure in HTML and styling in CSS with extra Logic in pure Python.that transforms Python objects into performant HTML/CSS with help with HTMX, creating a seamless bridge between Django's backend logic and the frontend interface. No context switching. No template spaghetti.

## 📣 Version 1.2.1 is Live!

Probo UI has officially reached stable v1.2 status. It is a backend-first framework.

    ```python
    from probo import (
        div, span
    )
    div(span("Hello, Probo",Class='badge'))
    ```

## Why Probo?

- use your python skill in making dynamic UI templates.
- Explicit, readable ad reusable layout
- Easier refactoring than HTML templates (it's python)
- IDE-friendly & type-safe

*For the deeper reasoning behind these choices, see Purpose & Philosophy ↓*

## ⚡ Purpose & Philosophy

Traditional Django development often requires context-switching between Python (views.py) and HTML/Jinja (templates/). Logic gets split, and typos in templates cause runtime errors.

Probo UI solves this by bringing the Frontend into Python:

🧠 Type-Safe UI: Write HTML in Python. If your code compiles, your HTML is valid.

🎨 Just-In-Time (JIT) CSS: Styles live with components. Probo UI scans your active components and generates a minified CSS bundle on the fly. No unused styles.

🛡️ Logic Gates: Built-in State Management. Components automatically hide themselves if required data (like user.is_authenticated) or permissions are missing.

🔌 Django Native: Deep integration with Django Forms and Requests via the RDT (Request Data Transformer).

# 📦 Installation

```bash 
        pip install probo-ui
```

# 🚀 Quick Example

Here is how you build a reusable component:

```python
from probo import (
    li,div,h1,ul,strong,
)
def user_card(username):
    user_id = f'User_789{username}1323'
    user_info = {'practical-info':['python','javascript','docker','django']}
    li_el = [li(info) for info in user_info['practical-info']]
    # 2. Build Component (Structure + Style + Data)
    card = div(
        h1(username,strong(user_id)),
        ul(*li_el)
        Class='card',
        style='color:red;'
    )
    return card

# Render it
html= user_card("Admin")
print(html)
# Output: 
# <div class='card'><h1>Admin<strong>User_789xyz1323</strong></h1><ul><li>python</li><li>javascript</li><li>docker</li><li>django</li></ul></div>
```
in case of permission
```python
from probo.components import (
    Component,ComponentState, ElementState,StateProps,
)
from probo import (
    div,h1,strong,ul,
)

def user_card(username):
    props = StateProps(required=True,prop_equal_to={'username':'admin'})
    user_id = f'User_789{username}1323'
    user_info = {'practical-info':['python','javascript','docker','django']}
    li_el = ElementState('li', d_state='practical-info',i_state=True, strict_dynamic=True,props=props,)
    user_comp_state = ComponentState(
        d_data=user_info,
        li_el,
    )
    # 2. Build Component (Structure + Style + Data)
    card = Component(
        name="UserCard",
        template=div(
            h1(username,strong(user_id)),
            ul(li_el.placeholder)},
            Class='card'),
        # Inject Data
        state=user_comp_state,
        props={'username':username}
    )

    return card

# Render it
html= user_card("Admin").render()
print(html)
# Output: 
# <div class='card'><h1>Admin<strong>User_789xyz1323</strong></h1><ul></ul></div>
html2= user_card("admin").render()
print(html2)
# Output: 
# <div class='card'><h1>Admin<strong>User_789xyz1323</strong></h1><ul><li>python</li><li>javascript</li><li>docker</li><li>django</li></ul></div>
```
[ 🚀 Get Started → ](user_guide.md)

💬 Community & Support Need help? Have a question that isn't a bug? Join our <a href='https://discord.gg/jnZRbVasgd'>Discord</a> Server to chat with other probo-ui developers.
