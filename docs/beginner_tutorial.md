# Beginner Tutorial

Learn how to build modern UIs with **Probo UI** in under 20 minutes.

This tutorial assumes you have basic Python knowledge and want to create dynamic web interfaces without writing HTML templates.

---

## 1. Installation
- Create a simple file named main.py to start coding. (any name can used!) 

```bash
mkdir my_probo_app

cd my_probo_app

python -m venv venv

source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install probo-ui
```

## 2. Your First Component
In Probo UI, everything is Python.
Let's create a simple greeting card:
```python

from probo import div, h1, p, button

def greeting_card(name: str) -> str|list[str]|deque[str]|StreamManager:
    return div(
        h1(f"Hello, {name}!"),
        p("Welcome to Probo UI — the future of backend UI development."),
        button("Learn More", Class="btn btn-primary"),
        Class="card"
    )

# Render it instantly by calling the function

card = greeting_card("John Doe")
print(card)

```

- Expected Output:
```
<div class="card">
    <h1>Hello, John Doe!</h1>
    <p>Welcome to Probo UI — the future of backend UI development.</p>
    <button class="btn btn-primary">Learn More</button>
</div>
```

# 3. Understanding the Two Main Ways to Build UI

### Style A: Functional Style (Simple & Fast)
```Python
from probo import div, h2, p

def hero_section(title: str, subtitle: str) -> str|list[str]|deque[str]:
    return div(
        h2(title),
        p(subtitle),
        Class="hero"
    )
```
### !! tip Controlling the Output:

For Functional tags, you can pass return_list=True or return_deque=True as kwargs if you want the engine to return a list of tags instead of a flattened string. This is useful for high-performance streaming pipelines!

### Style B: OOP / SSDOM Style (More Power)

from probo import DIV, H2, P

```python
from probo import DIV, H2, P

def hero_section(title: str, subtitle: str) -> DIV:
    # initialasation
    hero = DIV(Class="hero",Id="hero")
    hero.add(H2(title))
    hero.add(P(subtitle))

    # basic manipulation
    hero.attr_manager.set_data('trget',"#hero")
    hero.style_manager.color = "red"
    hero.style_manager.top = "50%"

    return hero
```
# 4. Creating Interactive Components with State
- Let's make a simple Counter component:
### Problem:
- If you use this directly in a view/route, the counter resets on every page refresh.
- Why? Because a new Counter() instance is created on every request.
- Correct Ways to Handle State
- In Probo UI, you have several options for real state:

- Use HTMX + backend session / database (Recommended for real apps)
- Use Probo’s global cache / context provider (new in 1.4.0)
- Store state in Django session or a simple in-memory store for demos

Simple HTMX + Session Example (Best for beginners)
```python
from probo import div, h1, button

def counter_component(count: int) -> str:
    return div(
        h1(f"Count: {count}"),
        button(
            "Increment",
            # Native HTMX Integration!
            hx_get=f"/count/{count + 1}",
            hx_swap="outerHTML",
            hx_target="#counter-container",
        ),
        Class="counter",
        Id="counter-container",
    )
```
- Then in your request/cached data:
```python
# Example with Django
def counter_view(request, count):
    # Update the session state
    request.session["count"] = count
    
    # Pass the new count back into our functional component
    new_ui = counter_component(count=count)
    return HttpResponse(new_ui)
```
- in urls.py
```python
    path("count/<int:count>", views.counter_view, name="count"),
```
# Summary — What You Learned

- How to create simple components using functions (def)
- How to use class-based components (Component)
- Why component state doesn't persist between requests by default
- Basic rendering with .render()
