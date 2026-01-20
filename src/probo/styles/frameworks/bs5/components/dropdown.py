from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Dropdowns
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Dropdown(BS5Component):
    ''''''
    def __init__(self,render_constraints=None,is_btn_group=False,escape_btn=False, **attrs):
        self.attrs = attrs
        self.is_btn_group=is_btn_group
        self.render_constraints=render_constraints
        self.dropdown_btn = None
        self.escape_btn = escape_btn
        self.dropdown_menu = None
        self.tag = 'div'
        super().__init__(name='BS5-dropdown', state_props=self.render_constraints)
    def add_btn(self,content,**attrs):
        btn = BS5Element(
            'button',
            content,
            classes=[Dropdowns.DROPDOWN_TOGGLE.value,],
            Type="button",
            data_bs_toggle="dropdown",
            aria_expanded="false",
            **attrs
        )
        self.dropdown_btn=btn.render()
        return self
    def add_menu(self,*items_content,items_attrs=None,**attrs):
        '''items_attrs must be {index[int]:attrs_dict,}'''

        menu = BS5Element(
            'ul',
            classes=[Dropdowns.DROPDOWN_MENU.value,],
            **attrs
        )
        if items_attrs:

            items = [
                BS5Element(
                'li',
                content,
                classes=[Dropdowns.DROPDOWN_ITEM.value,],
                **items_attrs[indx]
            ) for indx,content in enumerate(items_content)]
        else:
            items = [
                BS5Element(
                'li',
                content,
                classes=[Dropdowns.DROPDOWN_ITEM.value,],
            ) for content in items_content]
        menu.include(*items)
        self.dropdown_menu =menu.render()
        return self

    def before_render(self, **props):
        if self.dropdown_btn and not self.escape_btn:
            self.include_content_parts(self.dropdown_btn,first=True)
        if self.dropdown_menu:
            self.include_content_parts(self.dropdown_menu)

    def _render_comp(self):
        dropdown = BS5Element(
            self.tag,
            classes=[(Dropdowns.DROPDOWN.value if not self.is_btn_group else 'btn-group'),],
            **self.attrs
        )
        if self.dropdown_btn:
            dropdown.include(self.dropdown_btn)
        if self.dropdown_menu:
            dropdown.include(self.dropdown_menu)
        return dropdown

'''class BS5Dropdown(BS5Component):
    """
    Bootstrap 5 Dropdown component.
    Supports toggle buttons, menu items, headers, dividers, and various configurations (split, dark, directions).
    """
    def __init__(self, label="Dropdown", items=None, split=False, direction="down", dark=False, btn_variant="secondary", btn_size="", render_constraints=None, **attrs):
        self.label = label
        self.split = split
        self.direction = direction
        self.dark = dark
        self.btn_variant = btn_variant
        self.btn_size = btn_size
        self.render_constraints = render_constraints
        
        # Determine wrapper class based on direction
        # direction: 'down' (default), 'up', 'end', 'start', 'center' (not standard BS class but logic handled)
        wrapper_class = "dropdown"
        if direction == "up": wrapper_class = "btn-group dropup"
        elif direction == "end": wrapper_class = "btn-group dropend"
        elif direction == "start": wrapper_class = "btn-group dropstart"
        elif split: wrapper_class = "btn-group" # Split buttons need btn-group wrapper
        
        self.root = BS5Element('div', classes=[wrapper_class], **attrs)
        
        # Build Toggle Button
        btn_classes = [f'btn btn-{btn_variant}']
        if btn_size: btn_classes.append(f'btn-{btn_size}')
        
        if split:
            # Split Button: Standard Button + Toggle Button
            main_btn = BS5Element('button', content=label, type='button', classes=btn_classes)
            self.root.include(main_btn)
            
            toggle_classes = btn_classes + ['dropdown-toggle', 'dropdown-toggle-split']
            self.toggle_btn = BS5Element(
                'button', type='button', 
                classes=toggle_classes, 
                data_bs_toggle="dropdown", 
                aria_expanded="false"
            )
            # Add screen reader text
            self.toggle_btn.include('<span class="visually-hidden">Toggle Dropdown</span>')
            self.root.include(self.toggle_btn)
        else:
            # Single Button
            btn_classes.append('dropdown-toggle')
            self.toggle_btn = BS5Element(
                'button', content=label, type='button', 
                classes=btn_classes, 
                data_bs_toggle="dropdown", 
                aria_expanded="false"
            )
            self.root.include(self.toggle_btn)
        
        # Build Menu
        menu_classes = ['dropdown-menu']
        if dark: menu_classes.append('dropdown-menu-dark')
        
        self.menu = BS5Element('ul', classes=menu_classes)
        
        # Add initial items if provided
        if items:
            for item in items:
                self.add_item(item)
                
        self.root.include(self.menu)
        
        super().__init__('BS5Dropdown', self.root)

    def add_item(self, content, href="#", active=False, disabled=False):
        """Adds a link item to the dropdown menu."""
        link_classes = ['dropdown-item']
        if active: link_classes.append('active')
        if disabled: link_classes.append('disabled')
        
        link = BS5Element('a', content=str(content), href=href, classes=link_classes).render()
        li = BS5Element('li', content=link)
        self.menu.include(li)
        return self

    def add_header(self, content):
        """Adds a header to the dropdown menu."""
        header = BS5Element('h6', content=str(content), classes=['dropdown-header']).render()
        li = BS5Element('li', content=header)
        self.menu.include(li)
        return self

    def add_divider(self):
        """Adds a divider line to the dropdown menu."""
        divider = BS5Element('hr', classes=['dropdown-divider']).render()
        li = BS5Element('li', content=divider)
        self.menu.include(li)
        return self

    def add_text(self, content):
        """Adds plain text to the dropdown menu."""
        # Typically wrapped in a p or span with padding
        text = BS5Element('span', content=str(content), classes=['dropdown-item-text']).render()
        li = BS5Element('li', content=text)
        self.menu.include(li)
        return self
    
    def render(self, override_props=None):
        if self.render_constraints:
            if not override_props: return ""
            for key, val in self.render_constraints.items():
                if override_props.get(key) != val: return ""
        return super().render(override_props)'''
