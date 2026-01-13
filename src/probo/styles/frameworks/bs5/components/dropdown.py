from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Dropdowns
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Dropdown(BS5Component):
    ''''''
    def __init__(self, **attrs):
        self.attrs = attrs
        self.dropdown_btn = None
        self.dropdown_menu = None
        self.tag = 'div'
        super().__init__(name='BS5-dropdown', props={}, state=None)
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
    def add_menu(self,*items_content,**attrs):
        menu = BS5Element(
            'ul',
            classes=[Dropdowns.DROPDOWN_MENU.value,],
            **attrs
        )
        items = [
            BS5Element(
            'li',
            content,
            classes=[Dropdowns.DROPDOWN_ITEM.value,],
        ) for content in items_content]
        menu.include(*items)
        self.dropdown_menu =menu.render()
        return self
    def _render_comp(self):
        dropdown = BS5Element(
            self.tag,
            classes=[Dropdowns.DROPDOWN.value,],
            **self.attrs
        )
        if self.dropdown_btn:
            dropdown.include(self.dropdown_btn)
        if self.dropdown_menu:
            dropdown.include(self.dropdown_menu)
        return dropdown
