# 🐘 Probo UI
![PyPI](https://img.shields.io/pypi/v/probo-ui)
![Python](https://img.shields.io/pypi/pyversions/probo-ui)
![License](https://img.shields.io/github/license/MojahiD-0-YouneSS/probo)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://MojahiD-0-YouneSS.github.io/probo/)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
[![Discord](https://img.shields.io/badge/chat-Discord-5865F2)](https://discord.gg/jnZRbVasgd)
![Last Commit](https://img.shields.io/github/last-commit/MojahiD-0-YouneSS/probo)
![Repo Size](https://img.shields.io/github/repo-size/MojahiD-0-YouneSS/probo)

Probo UI stands for Python Rendered Objects for Backend-Oriented UI is A Python-Native server-side Template Rendering Framework and Meta-framework for Django.Write Type-Safe Template Components, structure in HTML and styling in CSS with extra Logic in pure Python.that transforms Python objects into performant HTML/CSS with help with HTMX, creating a seamless bridge between Django's backend logic and the frontend interface. No context switching. No template spaghetti.

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

# Performance Tests

The following table demonstrates the **Linear Scaling ($O(n)$)** capability of the ProboUI engine. These benchmarks verify the efficiency of the "Unified Tree" architecture when handling massive data volumes.

### Benchmarking Environment
* **Environment:** GitHub Codespaces (Standard Tier)
* **Methodology:** Single-pass execution using `time.perf_counter()` to bypass `timeit` memory overhead at scale.
* **Operations:** Each test includes full Tree Build, a `find` operation, a `deep_remove` (Surgery), and a full `render`.

| Elements | Total String Length | Build Phase | Manipulation | Render Phase | Total Time |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **100** | 11,824 chars | 0.0009s | 0.0001s | 0.0031s | **0.0041s** |
| **1,000** | 119,824 chars | 0.0099s | 0.0001s | 0.0277s | **0.0377s** |
| **10,000** | 1,226,824 chars | 0.1421s | 0.0005s | 0.2677s | **0.4103s** |
| **100,000** | 12,566,824 chars | 1.5980s | 0.0027s | 2.8518s | **4.4525s** |
| **250,000** | 31,916,824 chars | 4.2229s | 0.0061s | 6.9578s | **11.1868s** |
| **500,000** | 64,166,824 chars | 8.4060s | 0.0104s | 14.5542s | **22.9706s** |
| **750,000** | 96,416,824 chars | 12.1594s | 0.0256s | 21.4920s | **33.6770s** |
| **1,000,000** | 128,666,824 chars | 14.9993s | 0.0214s | 28.2681s | **43.2888s** |

### Observations

* **Constant-Time Manipulation:** The "Surgery" phase (finding and removing nodes) remains consistently under **0.03s** even with 1 million nodes in memory.
* **Memory Threshold:** The engine successfully generated a **128.6 MB** HTML string. Scaling beyond 1.5 million elements typically hits the physical RAM limits of the containerized environment.
* **Linearity:** ProboUI scales linearly. Doubling the element count consistently doubles the time, with no exponential "cliffs," making it safe for enterprise-scale documents.

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
