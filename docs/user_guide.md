# Probo UI User Guide

Welcome to Probo UI! This framework is designed for rapid, dynamic, and highly composable UI development using a Python-native Server-Side DOM (SSDOM).

# 🛠 Installation

Probo UI is designed to be lightweight with zero mandatory dependencies for its core rendering engine.

```bash
pip install probo-ui
```

# 🧱 Reusable Partial Templates

The power of Probo UI lies in Python's function-based composition. Because every component evaluates to a ProboSourceString (or an object that renders to one), you can nest them naturally just like HTML, but with the power of Python loops and variables.

Probo UI supports different paradigms for building partials based on your performance and manipulation needs.

### Functional (Fastest)

Function-based components use lowercase tags (e.g., `div`, `h3`). These are evaluated quickly into `ProboSourceString` formats. Because they return strings, they are extremely fast but cannot be mutated after creation.

```python
from probo import div, h3, p, section

def user_card(username: str, role: str = "Member")->str:
    """A reusable functional partial template"""
    return div(
        h3(username),
        p(f"Role: {role}", Class="text-muted"),
        Class="card"
    )

# Usage inside a list comprehension
def team_page() -> str:
    users = [("Alice", "Admin"), ("Bob", "Editor")]
    return section(*[
        user_card(name, role) for name, role in users
    ])
```


### OOP / SSDOM (Most Flexible)

Object-Oriented components use uppercase tags (e.g., `DIV`, `H3`). These create an efficient **Server-Side DOM (SSDOM)** tree in memory. 

This "lazy" approach means you can pass a complex UI tree through various logic checks to dynamically inject classes, IDs, or security tokens *before* rendering it to the client.

```python
from probo import DIV, P, H3, SECTION

def profile_widget():
    # 1. Create the base structure
    card = DIV(Class="card")
    
    # 2. Append children dynamically
    card.add(H3("Guest", Id="username"))

    # 3. SSDOM Manipulation: Change an attribute dynamically
    card.attributes.add_class("theme-dark")
    card.attr_manager.set_attr('Id', 'sub-container')
    
    # 4. SSDOM Manipulation: Add more children
    card.add(P("Logout"))
    
    container = SECTION(card)
    
    # Call .render() when you are finally ready to output the HTML!
    return container.render()
```


### Routing with ProboRouter
If you are using the built-in dual-engine ProboRouter, you don't even need to call .render(). The router handles it automatically!

```python

from probo.router.router import ProboRouter

app = ProboRouter('demo_app')

@app.page("/admin/widget")
def admin_widget():
    return profile_widget() # The router automatically calls .render() or .stream()
```


🔌 Integration with Other Frameworks

#### Probo UI works great as a view engine for popular Python web frameworks.

### FastAPI (ASGI)

Since FastAPI is built on ASGI, you can use Probo UI to generate the HTML and return it via FastAPI's native `HTMLResponse`.

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from probo import form, label, input_, button

api = FastAPI()

@api.get("/order", response_class=HTMLResponse)
async def order_form():
    # Build the UI
    form_string = form(
        label("Your Name:"),
        input_(type="text", name="user_name", required=True),
        label("Table Number:"),
        input_(type="number", name="table"),
        button("Submit Order", type="submit"),
        method="post",
        action="/order",
    )
    return form_string
```


### Django (WSGI)

Use Probo UI inside your Django views to bypass the slow Django Template Language (DTL) for high-performance dashboards and tables.

**Option 1: Direct HttpResponse (Pure Probo)**
```python
from django.http import HttpResponse
from probo import table, tr, td

def my_django_view(request):
    data_table = table(*[
        tr(td(f"Cell {i}")) for i in range(1000)
    ])
    return HttpResponse(data_table)
```

**Option 2: Hybrid Render (Probo + Django Templates)**
```python
from django.shortcuts import render
from probo import table, tr, td

def my_hybrid_view(request):
    # Generate the heavy table instantly in Python
    data_table = table(*[
        tr(td(f"Cell {i}")) for i in range(1000)
    ])
    # Pass the Probo string into a standard Django template!
    return render(request, 'pages/dashboard.html', {'sales_table': data_table})
```


### Flask (WSGI)

No more messy HTML strings everywhere! Keep your Flask views clean and entirely in Python.

```python
from flask import Flask
from probo import div, p, section, ul, li

app = Flask(__name__)

@app.route("/")
def index():
    view = section(
        "Welcome to Probo UI",
        p("This is the shorthand syntax demo."),
        div(
            p("Nested components feel natural:"),
            ul(
                li("Fast rendering"),
                li("Python-native syntax"),
                li("Zero context switching"),
            ),
            Class="content-box",
        ),
    )
    return view
```


🛡️ Native HTML Escaping & Security

Probo UI uses a strict ProboSourceString pattern. Any user-provided string passed as content is automatically escaped to prevent XSS attacks.

To bypass escaping for trusted HTML, you must explicitly wrap it in the ProboSourceString class, or use Probo's inline tag syntax.

1. Explicit Trusted Strings
```python

from probo.core import ProboSourceString
from probo import div

# The <strong> tags will NOT be escaped because we explicitly trusted them
nested = div(ProboSourceString("<strong>Already Escaped</strong>"))
```

2. Inline Tag Syntax (Safe)

If you don't want to import ProboSourceString, you can leverage Probo's built-in inline syntax. Probo understands strings acting as element wrappers.
```python
from probo import div

nested = div("hey div", "strong", "Already Escaped", {'id':'strong-id'}, Id='div-id') # recomend using this with functions only
# Output: 
# <div id="div-id">hey div<strong id="strong-id">Already Escaped</strong></div>
```
