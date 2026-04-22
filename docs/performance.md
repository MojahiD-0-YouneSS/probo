# Performance & Benchmarks

Probo UI is designed to be as fast as the underlying Python interpreter allows. Because there is no external template engine to initialize and no separate .html files to read from the disk during execution, Probo natively eliminates the standard I/O bottlenecks of web rendering.

However, rendering 100 elements requires a very different approach than rendering 150,000 elements. This guide explains how to scale Probo using the Chimera Architecture.

# 1. The Rendering Scale (100 to 150,000 Elements)

Probo UI provides four different syntaxes (Functional, Light Functional, Heavy OOP, Light OOP). Depending on which you choose, the performance profile changes drastically.

Here is a general benchmark guide of how Probo handles generating nested HTML elements (like table rows and cells):

| Element Count | Heavy OOP (DIV, TR)| Functional (div, tr) | Light Functional (l_div, l_tr) |
|--------|--------|--------|--------|       
|100 Elements |⚡ Instant (< 1ms) |⚡ Instant (< 0.5ms) |⚡ Instant (< 0.2ms) |
|10,000 Elements | 🟡 Moderate (~50-100ms) | 🟢 Fast (~15-30ms) | ⚡ Ultra Fast (< 10ms) |
|150,000 Elements|❌ High RAM / Slow| 🟡 High CPU|🟢 Safe (When Streamed)|

### The 150,000 Element Rule

If you attempt to render 150,000 DIV objects into memory at once and call .render(), your server will experience a massive RAM spike. Python objects take up memory.

- To render at this massive scale, you must use Light Functional tags combined with .stream() (or return_list=True).

# 2. The "Chimera" Architecture (Best Practice)

You don't have to choose just one paradigm. The most performant Probo applications use a "Chimera" architecture: mixing Heavy OOP for the layout, and Light Functional for the heavy data.

- Heavy OOP (DIV, BODY, NAV): Used for the page skeleton. You want the attr_manager and style_manager here so you can dynamically mutate the layout, change the theme, or inject auth tokens.

- Light Functional(l_tr, l_td) and heavy func (tr, td): Used inside the Heavy OOP layout for massive data loops. These are evaluated instantly into string/list/deque, taking up almost zero memory.

- also you can use light OOP (Ltr, Ltd) : Used inside the Heavy OOP layout for massive data loops. These are evaluated in lazy way into string/list/deque, taking up some zero memory.

# 🥇 Example: The Chimera Pattern

```python

from probo import DIV, TABLE, THEAD, TBODY, TR, TH # Heavy OOP (Layout)
from probo.components.light_tags import l_tr, l_td # Light Functional (Data)

def massive_dashboard(user_preferences:UserPreferences, million_row_generator:Generator[str,Any,None]):
    
    # 1. THE SKELETON (Heavy OOP)
    # We use OOP here so we can mutate it based on user_preferences
    layout = DIV(Id="dashboard-container")

    if user_preferences.theme == "dark":
        layout.style_manager.background_color = "#111"
        layout.style_manager.color = "#eee"

    data_table = TABLE(
        THEAD(TR(TH("ID"), TH("Value"))),
        Class="data-grid"
    )
    
    # 2. THE MASSIVE DATA (Light Functional)
    # We use lowercase light tags inside a generator. No Python objects are stored!
    lazy_rows = (
        l_tr(l_td(str(row.id)), l_td(row.value)) 
        for row in million_row_generator
    )
    
    # 3. COMBINE THE CHIMERA
    # We attach the lightweight data stream into our heavy layout
    tbody = TBODY(lazy_rows)
    data_table.add(tbody)
    layout.add(data_table)
    
    # Return as a stream!
    return layout.stream(batch_size=100)

```

# 3. String Concatenation vs. Deques vs. Lists

When using Functional tags (div()), the default behavior is to concatenate the strings immediately

In Python, string concatenation is highly optimized, but doing it 150,000 times in a deep loop can cause memory fragmentation.

To squeeze out the maximum possible performance, use Probo's list/deque return arguments. This tells Probo to append strings to an array instead of concatenating them, which is significantly faster in Python.

- Optimizing Functional Tags

```python
from probo import div, ul, li

def ultra_fast_list(items):
    # return_list=True prevents immediate string concatenation inside the loop
    list_items = [
        li(item.name, return_list=True) for item in items
    ]
    
    # The parent 'ul' tag then joins the list all at once (C-level optimization)
    return ul(*list_items)

```
For absolute bleeding-edge performance on massive datasets, you can use `return_deque=True`. collections.deque has $O(1)$ append performance in Python, making it the fastest possible way to build a massive UI tree before rendering.

# 4. Summary: How to Optimize

- For Layouts: Use Heavy OOP (DIV, SECTION). The memory overhead is negligible for 50-100 elements, and the mutation APIs are incredibly powerful.

- For Data (100 - 5,000 items): Use Functional tags (div, tr).

- For Massive Data (10,000+ items): Use Light Functional tags (l_div, l_tr) combined with return_list=True or Python Generators.

- For Network delivery: Always use .stream() for anything over a few thousand elements to ensure an instant Time-to-First-Byte (TTFB).

Template Parsing: Only use ProboTemplateParser for static files. Do not run a massive 10,000-row HTML string through the parser; parsing strings back into Python objects is the most expensive operation in the framework.