# 📚 Probo UI API Reference

## Welcome to the engine room.

The Probo UI API Reference provides complete, low-level technical documentation for every class, method, and function within the framework. Use the sidebar navigation to explore the specific modules, architectures, and methods that power Probo UI.

## 🧭 Navigating the API

The API documentation is generated directly from the framework's source code and docstrings. Each module page contains:

- Signatures: Exact arguments, defaults, and type hints (e.g., def find(self, predicate: Callable) -> Element).

- Returns: What the method yields (e.g., Self for method chaining, or str for eager rendering).

- Source: Direct links to view the exact implementation in the Probo GitHub repository.

## ⚡ Quick Import Cheatsheet

Forget where a specific tag or tool lives? Here is the global import cheatsheet for your daily workflow:

| Paradigm / Tool | Import Path | Example|
|--------|--------|-------|
| Heavy OOP (Classes) | from probo import ... | `DIV`, `SPAN`, `FORM`|
| Heavy Func (Functions) | from probo import ... | `div`, `span`, `form`|
| Light tags (oop/functionnal)|from probo.components.light_tags import ...| `l_div`, `l_span`, `Ltr`, `Lp`|
|Executer DSL| from probo.components import ...|`ProboFunctionalExecuter`, `tuplizer as _` | 
|Template Engine| from probo.templates import ...| `ProboTemplateParser`|
| String Processor| from probo.context.context_logic import ...| `TemplateProcessor`|
| Router & HTTP| from probo.router import ...| `ProboRouter`, `Context`| 

# 🚀 Quick API Example

Here is a minimal example showing how these tools and imports come together to build a routed, hybrid SSDOM component:
```python

from probo.router import ProboRouter
from probo import DIV, H1, l_div

app = ProboRouter("API_Demo")

@app.page("/dashboard")
def dashboard():
    # 1. Heavy OOP for stateful layout & manipulation
    layout = DIV(H1("Dashboard"), id="main-layout")
    
    # 2. Light Functional for fast, memory-efficient data strings
    fast_data = [
        l_p(f"{num} rows could go here...", class_=f"data-grid-{x}")
        for num in range(301)
        ]
    
    # 3. Hybrid Merge (Grafting the fast string into the live DOM tree)
    layout.add(DIV(*fast_data))
    
    return layout

app.runt()

```