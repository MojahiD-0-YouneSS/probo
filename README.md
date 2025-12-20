<a href="https://ko-fi.com/youness_mojahid" target="_blank"> <img src="https://github.com/MojahiD-0-YouneSS/mastodon-ui/blob/main/assets/images/kofi_brandasset/kofi_logo.svg" alt="Buy Me a Coffee at ko-fi.com" height="36" style="border:0px;height:36px;" border="0" /> </a>

<p align="center">
<img src="https://github.com/MojahiD-0-YouneSS/mastodon-ui/blob/main/assets/images/mastodon_ui.ico" alt="MUI Logo" width="200" height="200">
</p>

# 🐘 Mastodon UI (mui)

A Python-Native Template Rendering Framework and Meta-framework for Django.
Write Type-Safe HTML, CSS, and Logic in pure Python. No context switching. No template spaghetti.

## 📣 Version 1.0.0 is Live!

MUI has officially reached stable v1 status. It is a backend-first framework that transforms Python objects into performant HTML/CSS, creating a seamless bridge between Django's backend logic and the frontend interface.

## 📚 Read the Full Sample Documentation (v1.0)

### Click the link above for deep dives into : <a href="https://github.com/MojahiD-0-YouneSS/mastodon-ui/blob/main/docs/simple_doc.md">view sample documentation</a>

The Component Architecture: Brain (State) / Body (Elements) / Skin (Style).

Shortcuts for building complex UIs.

Mastodon Forms: Automatic Django Form rendering.

JIT Styling: How the CSS engine works.

## ⚡ Purpose & Philosophy

Traditional Django development often requires context-switching between Python (views.py) and HTML/Jinja (templates/). Logic gets split, and typos in templates cause runtime errors.

MUI solves this by bringing the Frontend into Python:

🧠 Type-Safe UI: Write HTML in Python. If your code compiles, your HTML is valid.

🎨 Just-In-Time (JIT) CSS: Styles live with components. MUI scans your active components and generates a minified CSS bundle on the fly. No unused styles.

🛡️ Logic Gates: Built-in State Management. Components automatically hide themselves if required data (like user.is_authenticated) or permissions are missing.

🔌 Django Native: Deep integration with Django Forms and Requests via the RDT (Request Data Transformer).



# 📦 Installation

```bash 
pip install mastodon-ui 
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
        s_data={},
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