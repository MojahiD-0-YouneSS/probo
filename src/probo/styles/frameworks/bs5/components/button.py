from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.layout import Button
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Button(BS5Component):
    
    def __init__(self, content, variant="primary", size='default',render_constaints:dict=None, **attrs):
        self.variant = variant
        self.size = size
        self.attrs = attrs
        self.content=content
        self.render_constaints=render_constaints or {}
        # self.template = self._render_comp()
        self.btn_classes = [Button.BTN.value,Button.get(variant)]
        self.tag = 'button'
        if self.size in ['sm','lg']:
            self.btn_classes.append(Button.get(size))
        super().__init__(name='BS5-button', state_props=self.render_constaints,)
    
    @property    
    def lg(self):
        self.btn_classes.append(Button.LG.value)
        self.template.add(Button.LG.value)
        return self
    
    @property
    def sm(self):
        self.btn_classes.append(Button.SM.value)
        self.template.add(Button.SM.value)
        return self
    
    
    
    def _render_comp(self):
        
        button = BS5Element(
            self.tag,
            self.content,
            classes=self.btn_classes,**self.attrs
        )
        return button

class BS5CloseButton(BS5Component):
    '''
        <button type="button" class="btn-close" aria-label="Close"></button>
        <button type="button" class="btn-close" disabled aria-label="Close"></button>
    
        <button type="button" class="btn-close btn-close-white" aria-label="Close"></button>
        <button type="button" class="btn-close btn-close-white" disabled aria-label="Close"></button>
    '''
    def __init__(self, variant="base", render_constaints=None, **attrs):
        self.variant = variant
        self.attrs = attrs
        self.render_constaints=render_constaints
        self.btn_classes = ['btn-close']
        self.attrs.update({"type": "button", "aria-label": "Close"})
        if variant == 'white':
            self.btn_classes.append('btn-close-white')
        self.tag = 'button'
        super().__init__(name='BS5-close-button',  state_props=self.render_constaints)
 
    def _render_comp(self):
        button = BS5Element(
            self.tag,
            # self.content,
            classes=self.btn_classes,**self.attrs
        )
        return button

class BS5ButtonGroup(BS5Component):
    
    def __init__(self,*btns,variant='horizontal',size='default',render_constaints=None,**attrs):
        self.btn_grp_cntnt = {}
        self.attrs = attrs
        self.attrs.update({'role':"group"})
        self.size=size
        self.render_constaints=render_constaints
        self.tag='div'
        self.btn_group_classes = [("btn-group-vertical" if variant == "vertical" else "btn-group"),]
        self.variant = variant
        self.btns = list(btns)
        if self.size in ['sm','lg']:
            self.btn_group_classes.append(Button[f'group_{self.size}'.upper()].value)

        super().__init__(name='BS5-button-group', state_props=self.render_constaints)

    @property
    def lg(self):
        self.btn_group_classes.append(Button.LG.value)
        self.template.add(Button.LG.value)
        return self

    @property
    def sm(self):
        self.btn_group_classes.append(Button.SM.value)
        self.template.add(Button.SM.value)
        return self

    def before_render(self,*args,**kwargs):
        self.include_content_parts(*self.btns)
        return self

    def add_btn(self,content, variant="primary",size='default', **attrs):
        
        btn = BS5Button(content, variant=variant, size=size, **attrs)
        self.btns.append(btn.render())
        return self
    def add_check_box_btn(self,content, variant="primary",size='default',override_input_attr:dict[str,str]=dict(), **attrs):
        '''
        <input type="checkbox" class="btn-check" id="btncheck1" autocomplete="off">
        <label class="btn btn-outline-primary" for="btncheck1">Checkbox 1</label>
        '''
        if not override_input_attr:
            bs5_input_attrs = {"type": "checkbox", "id": attrs.get('for',None), "autocomplete": "off"}
        else:
            
            override_input_attr.update({"type": "checkbox", "id": attrs.get('for',None), "autocomplete": "off"})
            bs5_input_attrs = override_input_attr

        bs5_input = BS5Element(
            'input',
            classes=["btn-check"],
            **bs5_input_attrs
        )
        
        btn = BS5Button(content, variant=variant, size=size, **attrs)
        btn.swap_element('label')
        self.btns.append(f'{bs5_input.render()}{btn.render()}')
        return self
    
    def _render_comp(self):
        btn_grp = BS5Element(
            self.tag,
            ''.join(self.btns),
            classes=self.btn_group_classes,**self.attrs
        )
        return btn_grp
    
class BS5ButtonToolbar(BS5Component):
    def __init__(self,*btn_grps,render_constaints=None, **attrs):
        self.btn_grps = [btn_g.render() if not isinstance(btn_g,str) else str(btn_g) for btn_g in btn_grps]
        self.attrs = attrs
        self.attrs.update({'role':"toolbar"})
        self.tag='div'
        self.btn_toolbar_classes = ['btn-toolbar',]
        self.render_constaints=render_constaints
        super().__init__(name='BS5-button-toolbar',  state_props=self.render_constaints)

    def add_btn_grp(self,btn_grp:BS5ButtonGroup):
        self.btn_grps.append(btn_grp.render())
        return self
    def before_render(self,*args,**kwargs):
        self.include_content_parts(*self.btn_grps)
        return self

    def _render_comp(self):
        btn_toolbar = BS5Element(
            self.tag,
            ''.join(self.btn_grps),
            classes=self.btn_toolbar_classes,**self.attrs
        )
        return btn_toolbar

