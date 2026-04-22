# DOM Manipulation (SSDOM API)

While Probo's functional tags (`div`, `span`) evaluate instantly for maximum speed, its Heavy OOP tags (`DIV`, `SPAN`) generate a living **Server-Side Document Object Model (SSDOM)**. 

Because this tree exists in memory before being sent to the browser, you have the power to traverse, query, and mutate it dynamically using pure Python. Probo's internal `ElementNodeMixin` provides necessary traversal API  with the power of Python.

---

## 1. Building the Tree

When you initialize a Heavy OOP component, you can pass children directly into the constructor, or build the tree step-by-step later in your code.

```python
from probo import DIV, H1, P

# Method 1: In the constructor
card = DIV(H1("User Profile"), Class="card")

# Method 2: Using .add() for dynamic insertion
card.add(P("Welcome back!"))

```
# 2. Traversing & Finding Nodes
Probo provides powerful traversal methods to find exactly what you need in the SSDOM tree. These are powered by Python lambda functions, giving you limitless querying flexibility without relying on complex string parsers.

- `find`(predicate) & `find_all`(predicate)

Searches the node and all of its descendants. find returns the first matching node, while find_all returns a list of all matches.

```python

from probo import DIV, BUTTON

ui = DIV(
    BUTTON("Submit", id="submit-btn", Class="btn-primary"),
    BUTTON("Cancel", id="cancel-btn", Class="btn-secondary")
)

# Find a single button by its ID
submit_btn = ui.find(lambda n: n.attr_manager.get_id() == "submit-btn")

# Find ALL buttons with the 'btn-secondary' class
secondary_btns = ui.find_all(lambda n: n.attr_manager.contains_class("btn-secondary"))
```
- `walk`

Generates a highly efficient, depth-first iteration of the SSDOM tree. Use this when you need to inspect or modify multiple nodes at once.
# Strip the 'hidden' class from all elements globally in the tree
```python

from probo import DIV, BUTTON

ui = DIV(
    BUTTON("Submit", id="submit-btn", Class="btn-primary"),
    BUTTON("Cancel", id="cancel-btn", Class="btn-secondary")
)

for node in ui.walk():
    if node.attr_manager.contains_class("hidden"):
        node.attr_manager.remove_class("hidden") #removes the class

```

# Removing & Extracting Nodes (remove, pop)
You can cleanly detach nodes from the SSDOM tree before rendering the final HTML.

- `remove` , `deep_remove`

`remove` Removes a specific child node instance from the current element.`deep_remove` locates the parent of a target child and removes it from child list

```python
from probo import DIV, BUTTON

ui = DIV(
    BUTTON("Submit", id="submit-btn", Class="btn-primary"),
    BUTTON("Cancel", id="cancel-btn", Class="btn-secondary")
)

# Find an unwanted paragraph and remove it
unwanted_node = ui.find(lambda n: n.tag == "P")

if unwanted_node:
    ui.remove(unwanted_node)
# deep_remove
ui.deep_remove(unwanted_node)

```
- `pop`,`deep_pop`

`pop` Removes and returns the child node  from the current element , `deep_pop` locates a the parent of target child to remove from child list.

```python
from probo import UL, LI

list_tree = UL(LI("First"), LI("Second"), LI("Third"))
child = list_tree.find(lambda n:'Third' in n.content)
# Remove and get the last item
last_item = list_tree.pop(child) 
last_item.inner_html('Forth')
# Remove and get the first item
first_item = list_tree.deep_pop(child)
```

# 4. Mutating Nodes (The Managers)
Every Heavy OOP node comes with dedicated managers for precise control over its HTML attributes and inline CSS styles.

- `attr_manager`

The Attribute Manager handles standard HTML attributes as well as custom data-* attributes.

```python
from probo import DIV

box = DIV("Content")

# Set a standard attribute
box.attr_manager.set_attr("role", "alert")
box.attr_manager.set_id("my-box")

# Set a data attribute (automatically prepends 'data-')
# This outputs: data-target="#modal"
box.attr_manager.set_data("target", "#modal")
box.attr_manager.add_class("container", "bg-primary")

# Remove an attribute
box.attr_manager.remove_attr("Class")
```

# style_manager
The Style Manager allows you to manipulate inline CSS using standard Python properties. ProboUI automatically translates Python's snake_case properties into valid CSS kebab-case properties!

```Python

from probo import DIV

box = DIV("Alert Content")

# Python attributes translate directly to CSS styles
box.style_manager.background_color = "#ff0000"
box.style_manager.color = "white"
box.style_manager.padding = "15px"
box.style_manager.border_radius = "5px"

print(box.render())

# Output: <div style="background-color: #ff0000; color: white; padding: 15px; border-radius: 5px;">Alert Content</div>
```
