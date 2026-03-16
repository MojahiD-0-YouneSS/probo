# ProboUI User guide

Welcome to ProboUI, a Python-native SSR (Server-Side template Rendering) framework designed for rapid dynamic UI.

🛠 Installation

ProboUI is designed to be lightweight with zero mandatory dependencies for its core rendering engine.

# Install via pip
```bash
pip install probo-ui
```

# Reusable Partial Templates

The power of ProboUI lies in Python's function-based composition. Since every html_tag or Component returns a ProboSourceString object, you can nest them naturally.

## Creating a Partial

A partial is simply a Python function or class/object that performs a process defined by the developer that returns a HTML element as ProboSourceString format. ProboUI support diferent ways to make the partials based on developer need.

### function version
- function based uses tag function. mind that the returned value is string (ProboSourceString) so string processing is the way to perform modifications.
    - Quick example:

```python
from probo import (
    div, h3, p, section
)

def user_card(username, role="Member"):
    """A reusable partial template"""
    return div(
        h3(username),
        p(f"Role: {role}", Class="text-muted")
    , Class="card")

```
-  Usage in a page asuming using Bottle based ProboRouter
```python
@app.page("/team")
def team_page():
    users = [("Alice", "Admin"), ("Bob", "Editor")]
    return section(*[
        user_card(name, role) for name, role in users
    ])

```
### OOP version also reffered to as SSDOM

- ProboUI implements a Server-Side DOM (SSDOM). Unlike previous implementation that renders strings on fly, ProboUI creates an efficient tree of objects. This allows you to manipulate the structure of your UI after it has been defined but before it is rendered to the client.

    - Quick example:

You can access and modify attributes or children directly on the element object.

```python
from probo import (
    DIV, P, H3, SECTION
)

def profile_widget():
    # Create the structure

    card = DIV(
        H3("Guest", id="username")
    , Class="card")
    # also you do
    card = DIV(Class="card")
       card.add( H3("Guest", id="username"))

    # SSDOM Manipulation: Change an attribute dynamically
    card.attributes['Class'] += " theme-dark"
    card.attr_manger.set_attr('Id','sub-container')
    # SSDOM Manipulation: Modify children
    # You can append, remove, or replace elements in the tree
    card.add(P("Logout"))
    container = SECTION(card)
    return container
    # if u want string do
    return container.render()

```

- This "lazy" approach means you can pass a complex UI tree through various middleware or logic checks to inject classes, IDs, or security tokens without messy regex or string replacements.

## using Bottle based ProboRouter
   -  Usage in a page asuming using Bottle based ProboRouter
```python

from probo.router import ProboRouter

app = ProboRouter('demo_app')

@app.page("/admin/widget")
def admin_widget():
    # Just call .render() on oop version otherwise exclude it to get the final string
    return profile_widget().render()
    # in case returning rendered string
    return profile_widget()

```


# Integration with Other Frameworks

ProboUI is WSGI-compliant, making it the perfect "view engine" replacement for existing frameworks.

## FastAPI Integration

Since FastAPI is ASGI, use ProboUI to generate the HTML and return it as an HTMLResponse.
```python

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from probo import (
    label,
    Input,
    button,
)

api = FastAPI()

@api.get("/order", response_class=HTMLResponse)
async def order_form():
    form_string = form(
        label("Your Name:"),
        Input(type="text", name="user_name", required=True),
        label("Table Number:"),
        Input(type="number", name="table"),
        button("Submit Order", type="submit"),
        method="post",
        action="/order",
    )

    return layout("Place Order", form_string)

```

## Django Integration

Use ProboUI inside your Django views to bypass the slow Django Template Language (DTL) for high-performance sections.

- using HttpResponse
    - when using HttpResponse u have freedom to return any kind for template ether partial like this example or full page.

```python

from django.http import HttpResponse
from probo import (
    table,tr,td,
)

def my_django_view(request):

    table = table( *[
        tr( [td( f"Cell {i}")]) 
        for i in range(1000)
    ])
    return HttpResponse(table)

```
- using render
    - when using render it required to use a base or other html template and pass the generated partials as context variables

```python

from django.shortcuts import render
from probo import (
    table,tr,td,
)

def my_django_view(request):

    table = table( *[
        tr( [td( f"Cell {i}")]) 
        for i in range(1000)
    ])
    return render(request,'pages/user_dashboard.html',{'sales_table':table,})

```


## Flask Integration

```python

from flask import Flask
from probo import (
 div,
 p,
 section,
 ul,
 li,
)

app = Flask(__name__)

@app.route("/")
def index():
    # Look how clean this is! No more  everywherestrings    view = layout(
    view = section(
        "Welcome to ProboUI",
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

## Native HTML Escaping

ProboUI uses the ProboSourceString Container pattern. Any string passed as content is automatically escaped unless it is wrapped in the ProboSourceString class or is another ProboUI component.


- ProboSourceString handles nesting without double-escaping
```python

from probo.router import ProboSourceString
from probo import div

nested = div(ProboSourceString("<strong>Already Escaped</strong>"))

```
 - if u dont want to use ProboSourceString you can do
```python

from probo import div

nested = div("hey div","strong","Already Escaped",{'id':'strong-id'},Id='div-id')

#  output: <div id="div-id"> hey div<strong id="strong-id">Already Escaped</strong></div>

```