# Usage & Best Practices

You know the syntax. You know how to render a div. But how do you architect a scalable, maintainable application using Probo UI?

Because Probo brings UI generation into pure Python, it is easy to accidentally mix backend business logic with frontend rendering. This guide outlines the golden rules and best practices for building enterprise-grade Probo applications.

# 1. Separation of Concerns (Views vs. Components)

The Rule: Your HTTP routing views should never contain complex DOM trees.

Just like in django where you separate settings/configs from rest of project, you should keep your Probo UI components in dedicated files (e.g., components/,pages/) and simply import them into your router/views.

### ❌ Anti-Pattern (The Messy View)
```python

from django.http import HttpResponse
from probo import div, h1, p, table, tr, td

def user_dashboard(request):
    # Mixing DB logic with a massive UI tree
    users = User.objects.all()
    
    ui = div(
        h1("Dashboard"),
        p("Welcome back!"),
        table(*[tr(td(u.name), td(u.email)) for u in users], Class="table"),
        id="main-dash"
    )
    return HttpResponse(ui)
```

### ✅ Best Practice (The Probo Way)
- Organize your project like this:
```text
myproject/
├── components/
│   └── dashboard.py
├── pages/
│   ├── base.py
│   └── home.py
├── views.py
# rest of structure
```
#### component layer
- components/dashboard.py

```python
from probo import div, h1, p, table, tr, td

def dashboard_ui(users):
    """Pure presentational component."""
    return div(
        h1("Dashboard"),
        p("Welcome back!"),
        table(*[tr(td(u.name), td(u.email)) for u in users], Class="table"),
        id="main-dash"
    )
```
###  page layer
- pages/home.py
### !! tip: 
- use a base.py as inheritance for rest of pages 
- when accessing derect document (DOCTYPE object) access the "html" object via html_doc 
```python
# pages/base.py
from probo.templates import base_template_tree

def base_page(*children):
    """Reusable base template"""
    base = base_template_tree(override_body=True, override_head=True)
    body = base.html_doc.find(lambda n: n.tag == "BODY")
    if body:
        body.add(*children)
    return base

```

```python

from probo import div, h1, p, table, tr, td
from myproject.myapp.pages import base_template
from myproject.myapp.components import dashboard_ui

def order_page(*args,**kwargs):
    users = kwargs.get('users',[])
    dashboard = dashboard_ui(users)
    base = base_template(dashboard)
    title_obj =base.html_doc.find(lambda n:n.tag == 'TITLE')
    if title_obj:
        title_obj.inner_html('dashboard page')
    return base

```
# views.py
## !! tip:
- if you are using a base.html just import the components directly intop a container then pass it ascontext via render otherwise use Http class.
```python

from django.http import HttpResponse
from myproject.myapp.pages import order_page

def user_dashboard(request):
    # 1. Fetch Data
    users = User.objects.all()
    
    # 2. Pass to Component
    return HttpResponse(order_page(users=users).render())

```
# 2. Managing State & Context

When dealing with deep component trees, passing standard variables (prop-drilling) through 10 layers of functions becomes exhausting.

### ✅ Best Practice: Use ProboContextProvider

Instead of passing the request or session down manually, push it into Probo's thread-safe global context at the very top of your view.

```python
from myproject.context import ProboContextProvider as Context
from components.navbar import navbar_ui

def my_django_view(request):
    # Inject the session/user globally for this specific request thread
    with Context() as ctx:
        ctx.push(user=request.user, theme=request.session.get("theme", "light"))
        
        # navbar_ui can now call Context.get("user") directly!
        return HttpResponse(navbar_ui().render())

```
# 3. Choosing the Right Architecture

Probo offers multiple ways to build UI. Choosing the wrong one for your specific task will lead to unnecessary memory overhead or code verbosity.

| Scenario | Recommended Paradigm | Why? |
| :--- | :--- | :--- |
| Standard Layouts / Forms |Heavy Functional (div, p) | Fast, clean syntax. Eagerly evaluates to strings. |
| Dynamic Mutation | Heavy OOP (DIV, P) | Allows you to use .modify(), style_manager, and attr_manager before calling .render().|
| Massive Data Tables | Light Tags (l_div, l_tr) | Shares a single memory pipeline. Prevents RAM spikes when rendering 10,000+ elements.|
| Deeply Nested Pages | ProboFunctionalExecuter DSL |  Keeps your Python code perfectly flat (no indentation hell) using + and / operators.|
| .html files | ProboTemplateParser  | Parses your templates into SSDOM (Server-Side Document Object Model) consisting of Light/Heavy OOP trees.|

# 4. Streaming Massive Payloads

If your UI tree contains thousands of elements (like a massive report or data grid), never use .render(). .render() forces the server to concatenate the entire string or buid list/deque in memory before sending it to the user.

### ✅ Best Practice: O(1) Memory Streaming

Always use .stream() paired with a streaming HTTP response (like Django's StreamingHttpResponse or FastAPI's StreamingResponse).
```python
# in myproject/myapp/components/streamed_component.py
from probo import table, tr, td

def data_report(*args,**kwargs):
    # Assuming 'get_millions_of_rows()' is a Python generator
    lazy_rows = (tr(td(row.id), td(row.data)) for row in get_millions_of_rows())
    
    report_ui = table(lazy_rows, style="table-layout: fixed; width: 100%;")
    return report_ui
# in myproject/myapp/views
from django.http import StreamingHttpResponse
from  myproject.myapp.components import data_report

def massive_report_view(request):
    report_ui = data_report()
    # Stream chunks of 50 elements instantly to the browser!
    return StreamingHttpResponse(report_ui.stream(batch=100))

```
# 5. Security: Trusting Raw HTML

Probo automatically escapes all strings passed into components to prevent Cross-Site Scripting (XSS) attacks.

If you are fetching raw, pre-rendered HTML from a trusted source (like a Markdown-to-HTML database column) and want Probo to render it as actual HTML instead of escaped text, you must explicitly tell Probo it is safe.

### ✅ Best Practice: The Escape Hatch
```python
from probo import div
from probo.shortcuts import raw

def blog_post(post):
    return div(
        h1(post.title),
        # raw() marks the string as safe, preventing auto-escaping
        div(raw(post.html_content), Class="prose")
    )
# OR
from probo import div
from probo.utility import ProboSourceString

def blog_post(post):
    return div(
        h1(post.title),
        # raw() marks the string as safe, preventing auto-escaping
        div(ProboSourceString(post.html_content), Class="prose")
    )

```
# Quick Tips

- Keep components small and focused (single responsibility).
- Use base_page() for consistent layout across your app.
- Prefer functional style unless you need deep mutation.
- Use Context instead of passing request everywhere.
- Always stream large responses.