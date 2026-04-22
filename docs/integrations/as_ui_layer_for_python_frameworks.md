# Probo as a UI Layer for Python Frameworks

Probo UI is designed to act as a **drop-in UI rendering layer** for any Python web framework.  
You can keep your existing backend logic, routing, and database handling while using Probo UI to generate the HTML frontend in pure Python.

This approach gives you the best of both worlds: powerful Python components with full type safety and IDE support, without forcing you to rewrite your entire application.

---

## Supported Frameworks

Probo UI currently integrates well with the following Python web frameworks:

| Framework       | Type     | Integration Level | 
|-----------------|----------|-------------------|
| **Django**      | WSGI     | Excellent         |
| **FastAPI**     | ASGI     | Excellent         |
| **Flask**       | WSGI     | Very Good         |
| **Bottle**      | WSGI     | Good              |
| **Starlette**   | ASGI     | Good              |
| **Quart**       | ASGI     | Good              |
| **Tornado**     | Async    | Basic             |
| **Sanic**       | Async    | Basic             |
| **CherryPy**    | WSGI     | Basic             |

---

## 1. Django Integration

### Using `HttpResponse`

```python
from django.http import HttpResponse
from probo import div, h1, button
from probo.components import Component

class Dashboard(Component):
    def render(self):
        return div(
            h1("Welcome to Dashboard"),
            button("Refresh", hx_get="/refresh", hx_swap="outerHTML"),
            Class="dashboard"
        )

def dashboard_view(request):
    return HttpResponse(Dashboard().render())
```
# Using Django `render()` with base template

```python
from django.shortcuts import render
from probo import div, h1

def dashboard_view(request):
    content = div(
        h1("Dashboard Content"),
        Class="main-content"
    )
    
    return render(request, 'base.html', {
        'probo_content': content
    })
```
# 2. FastAPI Integration
```Python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from probo import div, h1, button

app = FastAPI()

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    content = div(
        h1("FastAPI + Probo UI"),
        button("Click Me", Class="btn btn-primary"),
        Class="container"
    )
    return content.render()
```
# 3. Flask Integration
```Python
from flask import Flask
from probo import div, h1, p, section

app = Flask(__name__)

@app.route("/")
def index():
    return section(
        h1("Hello from Flask + Probo"),
        p("This page is rendered entirely with Probo UI"),
        Class="hero"
    ).render()
```
# 4. Bottle Integration (ProboRouter)
```python
from probo.router import ProboRouter

app = ProboRouter("my_app")

@app.page("/")
def home():
    return div(
        h1("Welcome"),
        Class="home-page"
    )
```
# Best Practices

- Keep UI components in a dedicated components/ folder
- Use a base_template() for consistent layout across all pages
- Prefer HttpResponse / HTMLResponse when returning Probo-rendered content
- Use .stream() for large pages or data-heavy views
- Combine Probo with HTMX for highly interactive interfaces without heavy JavaScript

## When to Use Probo as UI Layer

**Use this approach when you:**
- Want to keep your existing framework and business logic
- Want to gradually migrate away from template files
- Want better type safety and IDE support for your frontend
- Want to reduce context switching between Python and HTML
