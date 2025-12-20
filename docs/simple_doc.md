# Mastodon UI (MUI) v1.0 Documentation

MUI allows you to build type-safe, server-side rendered HTML components in Python with built-in state management and JIT CSS generation.

## 1. Basic HTML Generation (Functional API)

The simplest way to use MUI is through its functional tags. This replaces writing raw HTML strings.

Goal: Create the "Logo Section" from your example.

```python
from mui import section, div, img, h2, span

def logo_component():
    return div(
        img(src="./user/Images/logo.jpg", alt="logo", width="80px"),
        h2(span("CLUB"), "BAC"),
        Class="log_logo"
    )

# Render to string
print(logo_component().render())


Output:

<div class="log_logo"><img src="./user/Images/logo.jpg" alt="logo" width="80px" /><h2><span>CLUB</span>BAC</h2></div>
```

## 2. The Component Class (Static)

For reusable UI parts, use the Component class. This allows you to manage templates and CSS boundaries.

Goal: Create the "Sign Up Form" container.
```python
from mui import Component, div, form, h2, Input, button, p, a

# 1. Define the internal structure (Template)
# We use Python functions to build the structure dynamically
def signup_template():
    return form(
        h2("Sign Up"),
        # Name Fields
        div(
            Input(type="text", placeholder="First Name", required=True),
            Input(type="text", placeholder="Last Name", required=True),
            Class="input-box1"
        ),
        # Submit
        button("Sign Up", type="submit", Class="btn", onclick="login()")
    )

# 2. Create the Component
# Passing the rendered string as the 'template'
signup_comp = Component(
    name="SignUpCard", 
    template=signup_template()
)

# 3. Add Root Styling (Optional)
signup_comp.set_root_element("div", Class="sign")

# 4. Render
html = signup_comp.render()
```

## 3. Adding State (Dynamic Components)

MUI Components become powerful when you add State. This allows you to inject data dynamically without string formatting hacks.

Goal: Make the "Welcome" header dynamic.

## Step 1: Define Element State

We use ElementState to create "Smart Placeholders" (<$...>...</$>) in our template.
```python
from mui import Component, ComponentState, ElementState, StateProps, section, h1, span

# 1. Define Logic Elements
# "Look for 'club_name' in static data (s_state)"
es_club_name = ElementState(
    'span', 
    s_state='club_name', 
    Class='highlight',
)

# "Look for 'welcome_msg' in dynamic data (d_state)"
# Strict Mode: If missing, don't render this H1 at all.
es_message = ElementState(
    element='h1', 
    d_state='welcome_msg', 
    strict_dynamic=True
)
# "Look for 'hello_1235' in dynamic data (d_state)"
# the hirarchy : d_state > s_state so in normal use if no d_stae found but s_state found the element will use the s_state value.
# Strict Mode: If missing, don't render this H1 at all.
es_message_both = ElementState(
    'h1', 
    s_state='welcome_879',
    d_state='hello_1235', 
    strict_dynamic=True
)

```
## Step 2: Create Component State

The ComponentState acts as the "Brain" holding the data.
```python
# 2. Define Data
state = ComponentState(
    # Static Data (Defaults)
    s_data={'club_name': 'The Biologists in Action Club'},
    
    # Dynamic Data (From Database/View)
    d_data={'welcome_msg': 'Jack the admin says: Welcome !!'},
    
    # Register elements so the State knows about them
    es_club_name, es_message, es_message_both,
)

```
## Step 3: Wire it Together

We construct the template using the elements' placeholders.
```python
# 3. Build Template using Placeholders
# <$ ... $> is automatically inserted by .placeholder
template_str = section(
    es_message.placeholder,  # <h1>Welcome to </h1>
    es_message_both.placeholder,  # <h1>Welcome to </h1>
    es_club_name.placeholder, # <span class="highlight">The Biologists...</span>
    Class="page"
)

# 4. Initialize Component
page_component = Component(
    name="HomePage",
    template=template_str,
    state=state
)

# 5. Render
# The Component automatically resolves data -> elements -> HTML
html = page_component.render()
print(html):
<section class="page"><span class="highlight">The Biologists in Action Club</span><h1>Jack the admin says: Welcome !!</h1></section>
```
## 4. Styling (JIT CSS)

MUI allows you to attach CSS rules directly to components. These are only rendered if the elements exist.
```python
from mui import CssRule, CssSelector

# Define Rules
btn_style = {CssSelector().cls('btn'):CssRule(background_color='blue', color='white')}
input_style = {CssSelector().cls('input-box'):CssRule(padding='40px', margin_bottom='10px')}

# Load into Component , this a binding css to component
signup_comp.load_css_rules(**{**btn_style, **input_style})
# setting root elemnt
signup_comp.set_root_element('main',Id="main")
# Changing Skins (Theming)
# You can swap styles entirely at runtime
signup_comp.change_skin(
    root_attr='class',
    root_attr_value='root_css',
    root_css={'background': '#f0f0f0', 'padding': '20px'} # Applied to root div
)
```

## 5. Full Architecture Example (The "shortcut")

For the best developer experience, use the shortcut to wire everything in one go.
```python
from mui.shortcuts import (component, ComponentConfig, StateConfig, StyleConfig,ElementStateConfig)
from mui import (ElementState, div, form,)

def build_signup_page():
    # 1. Logic
    title_state = ElementStateConfig(tag='h2', s_state='form_title')
    
    
    state_config = StateConfig(
        s_data={'form_title': 'Join the Club'},
        elements__state_config=[title_state,]
    )
    # 2. Style
    style_config = StyleConfig(
        css = {
            '.sign': {'background': '#fff', 'padding': '2px'},
            'input': {'width': '100%', 'padding': '10px'},#since no input element this is skipped
        }
    )
    config = ComponentConfig(
        name="SignUpPage",
        template=div(title_state.config_id,form('some form'),Class="sign"),
        # Configuration
        state_config=state_config,
        style_config=style_config,
    )
    # 3. Component
    return component(config)
print(build_signup_page())
('<div class="sign"><form>some form</form></div>', '.sign { background:#fff; padding:2px; }')
```