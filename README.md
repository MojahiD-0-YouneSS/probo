<a href="https://ko-fi.com/youness_mojahid" target="_blank"> <img src="./docs/assets/images/kofi_brandasset/kofi_logo.svg" alt="Buy Me a Coffee at ko-fi.com" height="36" style="border:0px;height:36px;" border="0" /> </a>
<p align="center"> 
<img src="./docs/assets/images/mastodon_ui.ico" alt="Probo UI Logo" width="200" height="200">
</p>

![PyPI](https://img.shields.io/pypi/v/probo-ui)
![Python](https://img.shields.io/pypi/pyversions/probo-ui)
![License](https://img.shields.io/github/license/MojahiD-0-YouneSS/probo)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://MojahiD-0-YouneSS.github.io/probo/)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
[![Discord](https://img.shields.io/badge/chat-Discord-5865F2)](https://discord.gg/jnZRbVasgd)
![Last Commit](https://img.shields.io/github/last-commit/MojahiD-0-YouneSS/probo)
![Repo Size](https://img.shields.io/github/repo-size/MojahiD-0-YouneSS/probo)


## 📣 Version 1.3.0 is Live!

# 🐘 Probo UI

Probo UI stands for Python Rendered Objects for Backend-Oriented UI is A Python-Native server-side Template Rendering Framework and Meta-framework for Django.Write Type-Safe Template Components, structure in HTML and styling in CSS with extra Logic in pure Python.that transforms Python objects into performant HTML/CSS with help with HTMX, creating a seamless bridge between Django's backend logic and the frontend interface. No context switching. No template spaghetti.

## 📣 Version 1.3.0 is Live!

Probo UI has officially reached stable v1 status. It is a backend-first framework that transforms Python objects into performant HTML/CSS, creating a seamless bridge between Django's backend logic and the frontend interface.

## 📚 Read the Full Sample Documentation

### Click the link above for deep dives into : <a href="./docs/simple_doc.md">view sample documentation</a>

The Component Architecture: Brain (State) / Body (Elements) / Skin (Style).

Shortcuts for building complex UIs.

Probo Forms: Automatic Django Form rendering.

JIT Styling: How the CSS engine works.

## ⚡ Purpose & Philosophy

Traditional Django development often requires context-switching between Python (views.py) and HTML/Jinja (templates/). Logic gets split, and typos in templates cause runtime errors.

Probo UI solves this by bringing the Frontend into Python:

🧠 Type-Safe UI: Write HTML in Python. If your code compiles, your HTML is valid.

🎨 Just-In-Time (JIT) CSS: Styles live with components. Probo UI scans your active components and generates a minified CSS bundle on the fly. No unused styles.

🛡️ Logic Gates: Built-in State Management. Components automatically hide themselves if required data (like user.is_authenticated) or permissions are missing.

🔌 Django Native: Deep integration with Django Forms and Requests via the RDT (Request Data Transformer).



# 📦 Installation

```bash 
pip install probo-ui
```

# 🚀 Quick Example

Here is how you build a reusable, styled component using the Flow API:

```python
def user_card(username):
    # 1. Define Logic (The Brain)
    # "Look for 'name' in dynamic data. If missing, don't render."
    user_id = 'User_789xyz1323'
    user_info = {'practical-info':['python','javascript','docker','django']}
    li_el = ElementState('li', d_state='practical-info',i_state=True, strict_dynamic=True,)
    user_comp_state = ComponentState(
        d_data=user_info,
        li_el,
    )
    # 2. Build Component (Structure + Style + Data)
    card = Component(
        name="UserCard",
        template=f"<div class='card'>{h1(username,strong(user_id))+ul(li_el.placeholder)}</div>",
        # Inject Data
        state=user_comp_state,
    )

    return card

# Render it
html= user_card("Admin").render()
print(html)
# Output: 
# <div class='card'><h1>Admin<strong>User_789xyz1323</strong></h1><ul><li>python</li><li>javascript</li><li>docker</li><li>django</li></ul></div>
```
💬 Community & Support Need help? Have a question that isn't a bug? Join our <a href='https://discord.gg/jnZRbVasgd'>Discord</a> Server to chat with other probo-ui developers.
