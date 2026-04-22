# O(1) Memory Streaming

One of Probo UI’s most powerful features is its ability to **stream HTML directly to the browser** with almost zero memory overhead.

Traditional template engines (Jinja2, Django Templates, etc.) build the entire HTML string in memory before sending it. This causes high RAM usage and slow Time-to-First-Byte (TTFB) when rendering large datasets.

Probo UI solves this with **true O(1) memory streaming** using Python generators.


---

## Why Streaming Matters

Rendering a table with 50,000+ rows using `.render()` can:
- Spike your server’s RAM
- Delay the first byte sent to the user
- Make your application feel slow

Probo’s `.stream()` method fixes this by yielding HTML in small chunks as it’s generated.

---

## Standard vs Streaming Approach

### ❌ Using `.render()` (High Memory)

```python
from probo import ul, li

# This loads everything into memory at once
users = get_all_users()                    # Big list in RAM
ui = ul(*[li(user.name) for user in users]) # Another huge list + HTML string

html = ui.render()                         # Server freezes
```
### ✅ Using .stream() (O(1) Memory)


```python
from probo import ul, li

# This loads everything into memory at once
users = get_all_users()                    # Big list in RAM
ui = ul(*[li(user.name,return_list=True,stream=True) for user in users],return_list=True,stream=True) # Another huge list + HTML string

# Stream chunks to the client
for chunk in ui:
    send_to_client(chunk)

```

### Using .stream() in wild
```python
from probo import TABLE,tr,td
from .models import User

def gen_user_table(*args,**kwargs):
    users = User.objects.all().iterator()
    
    lazy_rows = (tr(td(u.id), td(u.name)) for u in users)
    
    ui = TABLE(lazy_rows)
    return ui

```
- Memory usage stays low because rows are processed and sent one batch at a time.

# Integration with Web Frameworks
- Django Example (Using StreamingHttpResponse)
```python

from django.http import StreamingHttpResponse
from .components.users import gen_user_table

def streamed_users_view(request):
    ui = gen_user_table()
    ui.style_manager.table_layout= "fixed"
    ui.style_manager.width= "100%"
    
    return StreamingHttpResponse(
        ui.stream(batch=50),
        content_type="text/html"
    )

```
