<a href="https://ko-fi.com/youness_mojahid" target="_blank"> <img src="./docs/assets/images/kofi_brandasset/kofi_logo.svg" alt="Buy Me a Coffee at ko-fi.com" height="36" style="border:0px;height:36px;" border="0" /> </a>

# <img src="./docs/assets/images/mastodon_ui.ico" align="center" alt="Probo UI Logo" width="200" height="200"/>  Probo UI : Future of Python based UI

<div align="center">
  <video src="./docs/assets/videos/video_1.mp4" autoplay loop muted playsinline width="100%" title="Probo UI Syntax Transition"></video>
  <br/>
  <em>Seamlessly transition from HTML strings to Python-Native SSDOM.</em>
</div>

# Python Rendered Objects for Backend-Oriented User Interfaces (Probo-UI). 

![PyPI](https://img.shields.io/pypi/v/probo-ui)
![Python](https://img.shields.io/pypi/pyversions/probo-ui)
![License](https://img.shields.io/github/license/MojahiD-0-YouneSS/probo)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://MojahiD-0-YouneSS.github.io/probo/)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
[![Discord](https://img.shields.io/badge/chat-Discord-5865F2)](https://discord.gg/jnZRbVasgd)
![Last Commit](https://img.shields.io/github/last-commit/MojahiD-0-YouneSS/probo)
![Repo Size](https://img.shields.io/github/repo-size/MojahiD-0-YouneSS/probo)
![Tests](https://img.shields.io/badge/Tests-1444%20Passed-brightgreen?style=flat-square&logo=github)
[![APIs](https://img.shields.io/badge/APIs-580+%20Ready-blue?style=flat-square&logo=python&logoColor=white)](https://MojahiD-0-YouneSS.github.io/probo/)

Probo UI (Python Rendered Objects for Backend-Oriented UI) is a Python-native server-side template rendering framework. Write type-safe template, components. structuring your HTML and styling your CSS with pure Python logic. It transforms Python objects into performant HTML/CSS (with native HTMX support), creating a seamless bridge between your backend logic and frontend interface.

## Version 1.4.4 is Live!

Probo UI has officially reached **stable v1.4.4**. Designed from the ground up as a backend-first UI meta-framework, Probo allows you to build robust, dynamic, and secure web interfaces without ever leaving your Python environment.

## The Probo UI Experience: Ease of Use

Probo UI removes the headache of string-based templating and brings the frontend directly to your backend.

- **Highly Modular & Reusable:** It is incredibly easy to customize components. Build your UI as modular building blocks that encapsulate structure and state.
- **100% Python Native:** If you know Python, you already know how to build a Probo UI. Leverage native list comprehensions, loops, and logic.
- **Complete Type Safety:** Enjoy full IDE autocompletion, static type checking, and real-time error highlighting.
- **Object-Oriented UI:** Rename tags, move components, and restructure layouts just like any other Python object.

---

## Framework-Agnostic Integration

Probo UI is designed to be highly flexible and non-blocking.

- **Unmatched Drop-in Support:** Use Probo UI natively within **Django, FastAPI, Flask**, and more!
- **Native HTMX Integration:** Generate blazing-fast partial page updates and SPA-like interactions right out of the box, with zero custom JavaScript required.
- **⏱Async & Await Capabilities:** Probo tags are natively awaitable! This allows you to resolve database queries, fetch external APIs, and render **multiple UIs concurrently** at the same time without blocking your async web frameworks.

---

## 📦 Installation

Get up and running in seconds:

```bash 
pip install probo-ui
```

---

## Show Me The Code: High-Quality Examples

Probo’s syntax is designed to be instantly readable. Data merges elegantly with structure.

### Example 1: The "Pythonic" Component

You can build components structurally via functions, or robustly via pure Object-Oriented Python.

**A. Functional Component**
```python
from probo import div, h1, ul, li, strong

def generate_user_badge(username: str, role: str):
    skills = ['Python', 'JavaScript', 'Docker']
    
    # Generate UI elements natively using Python list comprehensions!
    skill_tags = [li(skill, Class="text-sm border-b") for skill in skills]

    return div(
        h1(username, strong(f"({role})")),
        ul(*skill_tags),
        Class='card shadow-lg p-4 rounded-md',
    )
```

**B. OOP Component**
```python
from probo import DIV, H1, UL, LI, STRONG

def generate_user_badge(username: str, role: str):
    skills = ['Python', 'JavaScript', 'Docker']

    # Generate UI elements natively using Python list comprehensions!
    skill_tags = [LI(skill, Class="text-sm border-b") for skill in skills]

    return DIV(
        H1(username, STRONG(f"({role})")),
        UL(*skill_tags),
        Class='card shadow-lg p-4 rounded-md',
    ).render()
```

### Example 2: Optional Rendering (Logic Gates)

In secure applications, your UI must react dynamically to state. With Probo, you can easily use `add_render_constraints` to act as a **state guard**, conditionally hiding entire trees if data or security rules don't match.

**Note**: you would need to add data as dict and pass it as **data_pipeline** attribute in any element and pass the variable as **set** data type
```python
from probo import DIV, H1, UL, LI, STRONG

def generate_user_badge(username: str, role: str):
    skills = ['Python', 'JavaScript', 'Docker']
    data = {
        'username':username,
        'role':role,
    }
    # Generate UI elements natively using Python list comprehensions!
    skill_tags = [LI(skill, Class="text-sm border-b") for skill in skills]

    return DIV(
        H1({'username'}, STRONG("(",{'role'},")")), # <----- {'variable'}
        UL(*skill_tags).add_render_constraints(username='admin'),
        Class='card shadow-lg p-4 rounded-md',
        data_pipeline=data,
    ).render()
```
## Advanced Usage: Async, Dynamic Mutations & PowerNodes
Probo UI isn't just for static template generation; it's a living DOM. You can fetch data asynchronously, dynamically alter attributes and styles on the fly, and use PowerNodes to mutate the tree before it serializes.

### Example 1: Async Data, Dynamic Styles & Root Proxies

Because Probo tags natively support await, you can resolve database queries directly inside your component definition. You can also dynamically proxy the root element and inject Just-In-Time (JIT) CSS based on live data.

```python
import asyncio
from probo import DIV, H1, P,ARTICLE

async def fetch_user_prefs(user_id: int):
    # Simulate an async database or API call
    await asyncio.sleep(0.1)
    return {"username": "Youness", "role": "admin", "theme": "dark"}

async def dynamic_user_card(user_id: int):
    # 1. Await data directly in the component scope
    data = await fetch_user_prefs(user_id)
    template=DIV(
        H1({'username'}),
        P(f"System Role:",{'role'}),
        Class='user-card'
    )
    # 3. Dynamic Root Proxy & Attributes
    # Wraps the component in an <article> tag and injects dynamic data attributes
    article = ARTICLE(template,data_pipeline=data,data_theme={'theme'}, data_role={'role'})

    return article
```

### 2. Deep DOM Manipulation with `PowerNode`
Sometimes you need to mutate elements deep within a complex tree without breaking encapsulation. `PowerNode` acts as a targeted mutation pipeline. It searches for specific elements using a predicate and executes heavy logic or attribute changes directly on the target before the final string is rendered.

```python
from probo.components.power_node import PowerNode
from probo import SECTION, DIV, BUTTON


class PrivilegeEscalationNode(PowerNode):
    """
    A PowerNode that hunts down elements with a specific class
    and dynamically alters their attributes and styles.
    """

    def execute(self, target, *args, **kwargs):
        # Mutate the target node dynamically
        target.attr_manager.add_class("admin-unlocked")
        target.attr_manager.set_bulk_attr(**{
            'disabled' : False,
            'hx-post' : '/api/admin/override',
        })


def admin_control_panel(is_admin: bool):
    # The PowerNode targets any button marked 'restricted'
    modifier = PrivilegeEscalationNode(
        target_predicate=lambda node: node.element_tag == 'button' and node.attr_manager.contains_class('restricted'),
        hook='on_mount'
    )

    panel = SECTION(
            DIV("Standard Controls"),
            BUTTON("Delete Database", Class="btn restricted", disabled=True),
        )

    # If the user is an admin, append the PowerNode to the tree.
    # It will traverse the DOM, find the target, and execute the mutation pipeline.
    if is_admin:
        panel.add_power_node(modifier)

    return panel

```
### 3. Serving in Any Web Framework

Because Probo UI components render down to string-like objects, you can return them directly in **ANY** Python web framework. Here is how seamless it is to serve the exact same component across four popular backends.

#### FastAPI
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ui.components import admin_control_panel
from probo.components import frag

app = FastAPI()

@app.get("/")
async def home():
    # Render your Probo component directly into an HTML response!
    return HTMLResponse(content=frag(admin_control_panel(is_admin=True)))
```

#### Flask
```python
from flask import Flask
from ui.components import admin_control_panel
from probo.components import frag

app = Flask(__name__)

@app.route("/")
def home():
    return frag(admin_control_panel(is_admin=True))
```

#### Django
```python
from django.http import HttpResponse
from ui.components import admin_control_panel
from probo.components import frag

def home(request):
    return HttpResponse(frag(admin_control_panel(is_admin=True)))
```

#### CherryPy
```python
import cherrypy
from ui.components import admin_control_panel
from probo.components import frag

class HelloWorld:
    @cherrypy.expose
    def index(self):
        return frag(admin_control_panel(is_admin=True))

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
```

## Purpose & Philosophy

Traditional Django development often requires context-switching between Python (views.py) and HTML/Jinja (templates/). Logic gets split, and typos in templates cause runtime errors.

Probo UI solves this by bringing the Frontend into Python:

* Type-Safe UI: Write HTML in Python. If your code compiles, your HTML is valid.

* Just-In-Time (JIT) CSS: Styles live with components. Probo UI scans your active components and generates a minified CSS bundle on the fly. No unused styles.

* Logic Gates: Built-in State Management. Components automatically hide themselves if required data (like user.is_authenticated) or permissions are missing.

* Framework-Agnostic & Django-Ready: Build your UI completely standalone, or drop it into a Django project. When Django is present, Probo UI automatically enables deep integration with Django Forms and Requests via the RDT.

## Some ProboUI Architecture & Concepts

- **Push & Clear**: When creating HTML elements via the ```Element``` object, the final output is pushed to the ```element``` attribute. The content and attributes used in that specific session are then cleared to maintain a clean state. To allow for cumulative processing, arguments can be passed to the class to "stash" previous results, serving as the content for the subsequent execution chain.

- **SSDOM (Server-Side DOM)**: Unlike traditional string-based templates, ProboUI treats HTML as a live object tree in Python. This allows for direct manipulation of the structure, attributes, and children of a component after its definition but before it is finalized into a string.

- **State Management**: Enforces strict rendering constraints on components and elements via ```ComponentState``` and ```ElementState```. To render an element, a props dictionary must be passed and validated against the expected schema; the rendering only proceeds if the state is valid.

- **CSS Sharing**: Performance optimization where components can share the same CSS objects. This prevents the definition of redundant style objects and reduces memory overhead during large-scale renders.

- **Shared Execution**: An internal efficiency pattern where every HTML tag is generated by the same unified logic under the hood, ensuring zero logic duplication and a consistent output format across the entire framework.

- **Head Registry**: Instead of manually managing meta, link, and script tags, ProboUI uses a centralized registry. Developers use dedicated methods to register head elements, which the engine then constructs and optimizes automatically.

- **Template Switching**: The ```Template``` engine allows you to construct a page and then dynamically modify or rebase its structure based on an entirely different template hierarchy, providing extreme flexibility in multi-layout applications.

- **Base Template**: Provides a standardized, overrideable page structure that facilitates rapid development by allowing developers to inherit and manipulate a global foundation without starting from scratch.

- **Attribute Managers**: Utilizes the ```ElementAttributeManipulator``` to manage an element's attributes. This creates a clean separation of concerns between the element's core logic and its HTML attribute state.

- **SDH (Static/Dynamic Hierarchy)**: Employs ```StaticData``` and ```DynamicData``` classes to resolve content within ```ElementState```. The hierarchy prioritizes data in the order of Dynamic > Static > Content, which is used when binding these values to specific attribute values.

- **URL Component Mapping**: Implemented via the ```TemplateComponentMap``` (TCM), this concept maps components to specific URLs. It allows for effortless discovery and access via URL names or slugified versions, bypassing manual route registration.

- **Django Syntax**: Provides the ability to generate ProboUI output formatted as standard Django template syntax, allowing ProboUI components to be seamlessly embedded into existing .html templates within a Django environment.

- **HTMX Integration**: Native support for creating HTMX-based elements, enabling high-speed, dynamic UX updates (partial page refreshes) without writing custom JavaScript.

- **Routing Engine**: A built-in, Bottle-based server designed for rapid prototyping and testing of Python-based static web pages before production deployment.

- **Configs & Shortcuts**: Utilizes specialized data classes to group configuration info for each shortcut execution, streamlining the API and reducing repetitive boilerplate code.

- **Component Styling**: By linking CSS selectors directly to components and verifying their existence in the template, ProboUI prevents the delivery of "dead CSS" while still fully supporting standard CSS cascading.

- **Bootstrap 5 Support**: Native integration for BS5 design tokens and components, allowing developers to implement professional layouts using familiar utility classes and components with zero extra configuration.

- **Probo-CLI**: A command-line interface used to scaffold custom ProboUI packages as static web apps. It also enables "Django Mutation," automatically injecting the necessary Probo directories (components/, pages/, probo_tcm.py) into existing Django projects.

- **Proxy Element**: The ```ProxyElement``` provides a mechanism to embed external logic or third-party objects directly into the SSDOM. It facilitates the integration of arbitrary objects by accepting the object and an optional render callable, which is utilized if the object does not possess a native ```render``` method.

- **Style Manager**: The ```StyleManager``` helps adding inline styling to HTML objects like in js style with remove_style/add_style methods.


## Explore More

If you enjoy the backend-first, Python-native approach of Probo UI, you might find these related resources and tools useful:

* 📖 [**Full Documentation & User Guide**](https://mojahid-0-youness.github.io/probo/) - Dive deeper into Server-Side DOM (SSDOM), async rendering, and dynamic routing. (V 1.4.3) 1.4.4 is still in the making.

*    [ 🚀 Get Started → ](https://mojahid-0-youness.github.io/probo/user_guide/)

* 💬 Community & Support Need help? Have a question that isn't a bug? Join our <a href='https://discord.gg/jnZRbVasgd'>Discord</a> Server to chat with other probo-ui developers.
