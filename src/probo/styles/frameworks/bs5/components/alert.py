from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element
from probo.styles.frameworks.bs5.comp_enum import Alert

class BS5Alert(BS5Component):
    def __init__(self, content, color_variant="primary", is_dismissible=False,has_icon=False,render_constraints=None, **attrs):
        self.variant = color_variant
        self.attrs = attrs
        self.attrs.update({'role':'alert'})
        self.content=content
        self.is_dismissible=is_dismissible
        self.has_icon=has_icon
        self.render_constraints=render_constraints
        # self.template = self._render_comp()
        self.alert_classes = ['alert', Alert[self.variant.upper()].value]
        self.tag = 'div'
        self.alert_items = []
        if is_dismissible:
            self.alert_classes.append(Alert.DISMISSIBLE.value)
        if has_icon:
            self.content=f'<div>{self.content}</div>'
        super().__init__(name='BS5-alert', state_props=render_constraints)
        self.attr_manager.root={'role':'alert',}
        self.attr_manager.root.update(self.attrs)

    def add_svg_icon(self,bs_icon_id,path_d=None, **svg_attrs):
        path_element=None
        if not path_d:
            svg_attrs.update({
                'width':'24',
                'height':'24',
                'role':'img',
                'aria_label':f'{self.variant.capitalize()}',
                'class':'flex-shrink-0 me',
            })
        if path_d:
            svg_attrs.update({'xmlns':"http://www.w3.org/2000/svg", 'class':f'{bs_icon_id}'})
            path_element=BS5Element(
                'path',
                d=path_d
            )
        else:
            
            use_element = BS5Element(
                'use',
                '',
                **{'xlink:href':f'bootstrap-icons.svg#{bs_icon_id}'}
            )
        icon_svg = BS5Element(
            'svg',
            '',
            classes=['bi',],**svg_attrs
        )
        if path_element:
            icon_svg.include(path_element)
        else:
            icon_svg.include(use_element)
        self.template.include(icon_svg,first=True)
        return self

    def add_svg_symbol_icon(self, symbol_attrs:dict=None,**symbol_d):
        svg_items = []
        default_attrs={
                'fill':"currentColor", 'viewBox':"0 0 16 16"
            }
        if symbol_attrs:
            default_attrs.update(symbol_attrs)
        icon_svg = BS5Element(
            'svg',
            '',
            classes=['bi', 'flex-shrink-0', 'me-2'],
            xmlns="http://www.w3.org/2000/svg",
            style="display: none;",
        )
        if symbol_d:
            for smbl_Id,d in symbol_d.items():
                symbol_element=BS5Element(
                    'symbol',
                    Id=smbl_Id,
                    **default_attrs
                )
                path_element=BS5Element(
                    'path',
                    d=d
                )
                symbol_element.include(path_element)
                svg_items.append(symbol_element)
        icon_svg.include(*svg_items)
        self.template.include(icon_svg,first=True)
        return self

    def add_alert_link(self,content,):
        link = BS5Element(
            'a',content,
        )
        link.attr_manager.add_class('alert_link')
        self.template.include(link)
        return self

    def add_font_icon(self,icon_class,**attr):
        icon_svg = BS5Element(
            'i',
            classes=['icon_class'],**attr
        )
        self.template.include(icon_svg,first=True)
        return self

    def add_additional_content(self, content,overite=False,alert_heading=''):
        
        alert_heading= BS5Element('h4',alert_heading,classes=["alert-heading"])
        content += alert_heading.render() if alert_heading else ''
        if overite:
            
            self.template.content = content
        else:
            self.template.content += content
        return self

    def before_render(self, **props):
        self.template.attrs=self.attr_manager.root

    def _render_comp(self):
        alert = BS5Element(
            self.tag,
            self.content,
            classes=self.alert_classes,
            **self.attrs
        )
        if self.is_dismissible:
            close_btn = BS5Element(
                'button',
                '',
                classes=['btn-close'],
            )
            close_btn.attr_manager.set_bulk_attr(Type='button',
                data_bs_dismiss='alert',
                aria_label='Close')
            alert.include(close_btn)
        return alert
