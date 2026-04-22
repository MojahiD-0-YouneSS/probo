# Template to SSDOM

While writing UI entirely in pure Python is incredibly powerful, you may have an existing project with hundreds of .html files, or you might be working with frontend developers who prefer writing raw HTML.

Probo UI bridges this gap with its Template Parsing Engine. You can parse raw HTML strings—or fully rendered Jinja/Django templates—directly into a living Probo Server-Side Document Object Model (SSDOM). Once parsed, you can manipulate the tree using pure Python before sending it to the client.


# 1. The Core Engine: ProboTemplateParser

At the heart of this feature is the ProboTemplateParser. It takes standard HTML and meticulously converts every tag, attribute, and text node into Probo's Heavy / Light OOP Objects (DIV, SPAN, P, etc.).
```python
from probo.templates.parser import ProboTemplateParser
from probo import BUTTON

# Your raw HTML
html_content = """
<main id="app-root">
    <p class="text-muted">Loading complete.</p>
</main>
"""

# Convert HTML string into a Probo SSDOM Object
parser = ProboTemplateParser()
probo_dom = parser.parse(html_content,mode='heavy') # light for lighter ssdom or json as dict version

# The result is a native Probo node! You can append new Probo components to it:
probo_dom.add(BUTTON("Click Me!", Class="btn-primary"))

print(probo_dom.render()) # => <main id="app-root"><p class="text-muted">Loading complete.</p><button class="btn-primary">Click Me!</button></main>
```
- using a file:
```python
from probo.templates import ProboTemplateParser
from probo import BUTTON

# Your raw HTML

# Convert HTML string into a Probo SSDOM Object
parser = ProboTemplateParser('path/hero.html')
probo_dom = parser.parse(mode='heavy') # light for lighter ssdom or json as dict version

# The result is a native Probo node! You can append new Probo components to it:
probo_dom.add(BUTTON("Click Me!", Class="btn-primary"))

print(probo_dom.render()) # => <main id="app-root"><p class="text-muted">Loading complete.</p><button class="btn-primary">Click Me!</button></main>
```

# 2. Light Usage: TemplateProcessor

For lightweight HTML strings or simple variable injections, you don't need a heavy template engine like Jinja. Probo provides a built-in TemplateProcessor that handles basic variable replacement and parses the result into an SSDOM tree.
```python
from probo.context import TemplateProcessor
from probo.templates import ProboTemplateParser

def dynamic_welcome_banner(user_name: str):
    # 1. A simple HTML string with a variable placeholder
    raw_html = """
    <div class="banner">
        <h1 id="greeting">Welcome, {{ name }}!</h1>
    </div>
    """

    # 2. Initialize the processor with your data context
    processor = TemplateProcessor(data_context={"name": user_name})
    parser = ProboTemplateParser()
    # 3. Render and parse it into an SSDOM Tree
    ssdom_tree = parser.parse(
        processor.render_template(raw_html),
        mode="heavy",
        )

    # 4. Now you can mutate it just like a native Probo object!
    ssdom_tree.style_manager.background_color = "blue"

    return ssdom_tree.render()
```


# 3. Advanced Pipeline: Jinja & Django Integration

If your .html files contain complex template logic ({% for %}, {% if %}, custom template tags), Probo's parser should not try to parse the raw file directly.

Instead, you use a two-step pipeline:

Process: Let your native framework (Django or Jinja2) resolve the template logic into a standard HTML string.

Parse & Mutate: Pass that clean HTML string to ProboTemplateParser to generate your SSDOM, then apply your dynamic Python mutations.

This allows you to take legacy Django/Jinja templates and dynamically inject Probo components into them!

### "Django Pipeline"

```python
from django.template.loader import render_to_string
from django.http import HttpResponse
from probo.templates.parser import ProboTemplateParser
from probo import DIV, H2

def legacy_dashboard_view(request):
    # STEP 1: Process the Django Template Language (DTL)
    # This resolves all {% for %} and {{ variables }} into pure HTML
    rendered_html = render_to_string("legacy/dashboard.html", {
        "user": request.user,
        "stats": get_stats()
    })
    
    # STEP 2: Parse into Probo SSDOM
    parser = ProboTemplateParser()
    ssdom = parser.parse(rendered_html,mode='heavy')
    
    # STEP 3: Python DOM Manipulation!
    # Let's dynamically inject a new Probo component into the legacy layout
    alert_box = DIV(H2("System Maintenance at Midnight!"), Class="alert-danger")
    
    main_container = ssdom.find(lambda n: n.attr_manager.get_id() == "main-content")
    if main_container:
        main_container.add(alert_box)
        
    # STEP 4: Return the mutated tree
    return HttpResponse(ssdom.render())
```


### "Jinja2 Pipeline"

```python
from jinja2 import Environment, FileSystemLoader
from probo.templates.parser import ProboTemplateParser
from probo import P

# Setup Jinja Environment
env = Environment(loader=FileSystemLoader('templates/'))

def render_jinja_to_probo():
    # STEP 1: Process Jinja syntax
    template = env.get_template("invoice.html")
    rendered_html = template.render(invoice_id="INV-10294")
    
    # STEP 2: Parse to Probo SSDOM
    parser = ProboTemplateParser()
    ssdom = parser.parse(rendered_html)
    
    # STEP 3: Mutate using Probo
    footer = ssdom.find(lambda n: n.tag == "FOOTER")
    if footer:
        footer.add(P("Thank you for your business!"))
        
    return ssdom.render()
```


###  "The Best of Both Worlds"
By combining native template engines with Probo's `ProboTemplateParser`, you empower your frontend team to continue writing standard .html and `Jinja`/`Django` templates, while giving your backend team the ultimate power to intercept, mutate, and enhance those templates using pure Python before they ever reach the browser.