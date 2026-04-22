# Proxies in SSDOM (`ProxyElement`)

When working with a Python-based UI, you inevitably need to inject external data structures, foreign framework objects (like Django Models), or native Python types into your layout.

However, standard Probo elements expect their children to either be strings or objects with a native `.render()` or `.stream()` method.

This is where **`ProxyElement`** comes in. A proxy in Probo is *not* the dynamic tag generation (`Element.div()`)—it is a dedicated adapter class used to safely link, process, and render objects that do not natively speak Probo's rendering language.

!!! tip "Quick Tip"
    For simple data types like numbers and lists, you don't even need special methods! You can just pass them directly to the proxy's constructor (e.g., `ProxyElement(404)`).

---

## 1. What does ProxyElement do?

The `ProxyElement` is a "smart wrapper." It inherits from `BaseHTMLElement` (meaning it acts exactly like a `DIV` or a `SPAN`), but its internal content is powered by whatever foreign object you load into it.

It serves three main purposes:

1. **Linking objects without a `.render()` method:** Using `load_logic()`, it adapts native Python iterables (lists, dictionaries, generators) or primitives so they can be injected into the SSDOM seamlessly.
2. **Pre-Processing Logic:** Hooking into foreign APIs (like a Jinja2 template returning `__html__()` or a Django Model returning `__str__()`) and formatting them right before the final render via `load_render_logic()`.
3. **Streaming Fallbacks:** If you inject an object that can `.render()` but cannot `.stream()`, the proxy will catch it, execute the render, and yield the string instantly into the pipeline so your streaming architecture doesn't crash.

---

## 2. Basic Usage

To use a proxy, you wrap your data in the `ProxyElement`, load the logic, and drop it into your tree. By default, proxies simply render their internal content without wrapping it in an HTML tag.

```python
from probo import DIV
from probo.components.node import ProxyElement

# A native dictionary does not have a .render() method!
raw_data = {"status": "active", "user": "admin"}

# 1. Create a Proxy wrapper
proxy = ProxyElement() 

# 2. Load the foreign logic and dictate how it should render
proxy.load_logic(raw_data)
proxy.load_render_logic(lambda n: str(n))

# 3. Mount it directly into the SSDOM tree
page = DIV(proxy, id="main-container")

print(page.render())
# Output: <div id="main-container">{'status': 'active', 'user': 'admin'}</div>
```
### .Showing the Wrapper Tag
If you want the proxy to physically render as an HTML tag (like a <span> or <div>), you must pass a tag name and explicitly set the wrap_result=True flag:
```python
proxy = ProxyElement(tag="span", wrap_result=True)
proxy.load_logic(raw_data)
proxy.load_render_logic(lambda n: str(n))

# Output: <div id="main-container"><span>{'status': 'active', 'user': 'admin'}</span></div>
```

## 3. Invisible Execution (Living Unseen)
The true power of ProxyElement is how it can perform `SSDOM` manipulations and regular Python processes without showing up in the final HTML output.

Because wrap_result defaults to False, proxies act as invisible logical nodes. This is perfect for injecting conditional text, running side-effects, or formatting data right before the render tree completes.

Example: A Conditional Message Injector
```python
from probo import DIV
from probo.components.node import ProxyElement

class MessageInjector:
    def __init__(self, data):
        self._data = data
        self._message = None
        
    def process_data(self):
        # Truthy check on the data
        self._message = "YaaY!!" if bool(self._data) else "BooO!!"
        
    def render(self):
        self.process_data()
        return self._message or ''

# The tag="div" is ignored because wrap_result=False by default!
message_proxy = ProxyElement(tag="div")
message_proxy.load_logic(MessageInjector([])) # Passing an empty list (Falsy)

page = DIV(message_proxy)

print(page.render())
# Output: <div>BooO!!</div>
```
## 4. SSDOM Mutability on Proxies
Because ProxyElement inherits from the standard Heavy OOP Node architecture, it has full access to the attr_manager and style_manager.

This means you can mutate the wrapper of the foreign object long after it was generated, dynamically changing its classes, IDs, and inline styles!

!!! warning "Important: `wrap_result=True` is Required! to render as wrapper"
You must declare `wrap_result=True` in the constructor if you want to use the attribute or style managers. Otherwise, there is no HTML tag for the classes and styles to attach to, and your changes won't reflect in the output.
```python
from probo.components.node import ProxyElement

# Wrap a raw integer directly in the constructor!
proxy = ProxyElement(404, tag="div", wrap_result=True)

# Use standard Probo Mixin methods on the proxy wrapper
proxy.attr_manager.add_class("error-text")
proxy.attr_manager.set_attr("data-code", "not-found")
proxy.style_manager.color = "red"

print(proxy.render())
# Output: <div class="error-text" data-code="not-found" style="color:red;">404</div>
```

## 5. ProxyElement in the wild
### 5.1 Example: The URL Interceptor

Proxies are exceptionally powerful when used as `UI middleware` to dynamically build/manipulate Heavy OOP SSDOM trees based on business logic.

Imagine you have a raw list of navigation links. You want a proxy that silently intercepts these links, checks if the URL matches a specific batch of "target" URLs, rewrites them to /admin routes, and then constructs a fully styled HTML navigation menu right before rendering.

```python
from probo import HEADER, NAV, UL, LI, A
from probo.components.node import ProxyElement

class AdminURLInterceptor:
    def __init__(self, raw_links, admin_targets):
        self.raw_links = raw_links
        self.admin_targets = admin_targets
        self._menu_tree = None

    def build_ssdom(self):
        # 1. Initialize a Heavy OOP unordered list
        self._menu_tree = UL(class_="nav-list")
        
        for label, url in self.raw_links:
            # 2. Intercept and rewrite the URL if it exists in the target batch
            final_url = f"/admin{url}" if url in self.admin_targets else url
            
            # 3. Construct the nested Heavy OOP elements
            link_item = A(label, href=final_url, class_="nav-link")
            list_item = LI(link_item, class_="nav-item")
            
            # 4. Attach to the living tree
            self._menu_tree.add(list_item)

    def render(self):
        self.build_ssdom()
        return self._menu_tree.render()


# --- USAGE ---

raw_site_links = [
    ("Home", "/home"),
    ("Users", "/users"),
    ("Settings", "/settings"),
    ("Contact", "/contact")
]

# URLs that should be restricted/rewritten to admin paths
restricted_batch = ["/users", "/settings"]

# Create the invisible proxy
menu_proxy = ProxyElement()
menu_proxy.load_logic(AdminURLInterceptor(raw_site_links, restricted_batch))

# Wrap it in a layout
header_layout = HEADER(
    NAV(menu_proxy, id="main-nav")
)

print(header_layout.render())
```
## Output:
```html

<header>
    <nav id="main-nav">
        <ul class="nav-list">
            <li class="nav-item">
                <a href="/home" class="nav-link">Home</a>
            </li>
            <li class="nav-item">
                <a href="/admin/users" class="nav-link">Users</a>
            </li>
            <li class="nav-item">
                <a href="/admin/settings" class="nav-link">Settings</a>
            </li>
            <li class="nav-item">
                <a href="/contact" class="nav-link">Contact</a>
            </li>
        </ul>
    </nav>
</header>
```
- As you can see, the `ProxyElement` vanishes completely, leaving behind a perfectly formed, logic-driven Heavy OOP layout!

### 5.2 Full Document Lifecycle: Pre-UI vs Post-UI Proxies

When building a complete `HTML` document using Heavy OOP components, the placement of your invisible `ProxyElement` within the tree dictates what it is capable of doing. Because Probo evaluates and renders the tree sequentially (top-to-bottom), proxies act as powerful lifecycle hooks.

### 5.3 Pre-UI Proxies (Before the BODY)
Placed immediately inside the `HTML` tag (or inside the `HEAD`), these proxies execute early. Because the UI has not been rendered or streamed yet, Pre-UI proxies can safely manipulate the SSDOM. You can use them to inject theme classes, validate auth state, or modify layout nodes dynamically.

### 5.4 Post-UI Proxies (After the BODY)
Placed at the very end of the `HTML` document, these proxies execute after the entire UI has been processed. Modifying the DOM here is useless (especially in a streaming pipeline, because the HTML has already been sent to the browser). Therefore, this location is strictly reserved for Side Effects.

### 5.5 Use Post-UI proxies for:

- Invoking background tasks (Celery/Redis)

- Caching the final rendered tree

- Making analytical UI snapshots

- Logging render completion times

- The Full Document Example
- and any other Python thing you can do

## 6. Scoped Proxies (Branch-Level Logic)

While global proxies sit at the document root to manage entire pages, you can also place `ProxyElement` instances deep inside your OOP tree to act as **Scoped Proxies**.

A Scoped Proxy lives inside a specific branch (like a `MAIN`, `SECTION`, or a custom component `DIV`) and applies its logic or side-effects *only* to that local area.

### 6.1 The Golden Rule of Top-Down Rendering
Because Probo streams and evaluates the `SSDOM` sequentially (top-to-bottom), a scoped proxy is bound by the laws of time:
* **✅ Allowed:** A proxy *can* mutate its children, its subsequent siblings, or trigger side-effects based on localized data.
* **❌ Forbidden:** A proxy *cannot* mutate its parent or its previous siblings. Once a parent or previous sibling has been processed by the streaming engine, and it will raise `RunTimeError`.

### 6.2 Example: A Component-Level Scoped Proxy

Imagine you have a specific `SECTION` on your page that needs to fetch its own localized data and dynamically style its children based on that data, without touching the rest of the global document.

```python
from probo import MAIN, SECTION, DIV, P
from probo.components.node import ProxyElement


class LocalDataInjector:
    def __init__(self, target_section):
        self.target_section = target_section

    def render(self):
        # Fetch data scoped only to this component
        local_status = "error"  # Imagine this came from a local DB check

        # Mutate the target section dynamically
        if local_status == "error":
            self.target_section.attr_manager.add_class("bg-danger text-white")

        return ""  # Render invisibly


# 1. Define the localized branch
user_dashboard = SECTION(P("User data goes here..."))
proxy = ProxyElement()
proxy.load_logic(LocalDataInjector(user_dashboard))
# 2. Build the Layout
page_layout = MAIN(
    DIV("Previous Sibling (Already rendered, cannot be touched by proxy)"),
    # Place the Scoped Proxy right before the target it needs to manipulate
    proxy, # <--------- mutates user_dashboard before it gets rendered and proxy never shows up afterwards
    user_dashboard,
    DIV("Next Sibling (Safe to render)"),
)

print(page_layout.render())

# output: <main><div>Previous Sibling (Already rendered, cannot be touched by proxy)</div><section class="bg-danger text-white"><p>User data goes here...</p></section><div>Next Sibling (Safe to render)</div></main>

```
- By scoping your proxies, you can build highly modular, self-contained UI components that manage their own internal state and side-effects without cluttering the global document root!