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
                Type='button',
                data_bs_dismiss='alert',
                aria_label='Close'
            )
            alert.include(close_btn)
        return alert
    
'''
curent supported:
<svg class="bi" width="32" height="32" fill="currentColor">
  <use xlink:href="bootstrap-icons.svg#heart-fill"/>
</svg>
<i class="bi bi-heart-fill"></i>
not supported:
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:">
    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
  </svg>

<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
  <symbol id="check-circle-fill" fill="currentColor" viewBox="0 0 16 16">
    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
  </symbol>
  <symbol id="info-fill" fill="currentColor" viewBox="0 0 16 16">
    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/>
  </symbol>
  <symbol id="exclamation-triangle-fill" fill="currentColor" viewBox="0 0 16 16">
    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
  </symbol>
</svg>
'''