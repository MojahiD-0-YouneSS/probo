from mui import (
    button,
    Element as EL,
    div,
    input as input_tag,
    label
)

class DefaultButton:
    def __init__(self, btn_content,**args):
        self.btn_content = btn_content
        self.args = args
    
    def __button(self,):
        return button(self.btn_content, **self.args)

    def __any_tag(self,tag):
        return EL( self.btn_content, **self.args).custom_element(tag).element

    def render(self,tag=None,):

        if tag:
            return self.__any_tag(tag)
        return self.__button()

class DefaultCloseButton:
    def __init__(self, btn_state=None,**args):
        self.btn_state = btn_state
        self.args = args
    
    def __base(self,):
        '''
            <button type="button" class="btn-close" aria-label="Close"></button>
            <button type="button" class="btn-close" disabled aria-label="Close"></button>
        '''
        if self.btn_state =='disabled':
            return button(type="button", Class="btn-close",disabled='true', aria_label="Close")
        else:
            return button(type="button", Class="btn-close", aria_label="Close")

    def __white(self,):
        '''
            <button type="button" class="btn-close btn-close-white" aria-label="Close"></button>
            <button type="button" class="btn-close btn-close-white" disabled aria-label="Close"></button>
        '''
        if self.btn_state =='disabled':
            return button(type="button", Class="btn-close  btn-close-white",disabled='true', aria_label="Close")
        else:
            return button(type="button", Class="btn-close  btn-close-white", aria_label="Close")

    def render(self,Type='base',):
        Type_dict = {
            'base':self.__base,
            'white':self.__white,
        }
        return Type_dict.get(Type,self.__base)()

class DefaultButtonGroup:
    def __init__(self, btn_grp_cntnt:dict,is_vertical=False,**args):
        self.btn_grp_cntnt = btn_grp_cntnt
        self.args = args
        self.is_vertical = is_vertical

    def __button(self,):
        return div(
            *[button(k, **v) for k,v in self.btn_grp_cntnt.items() if k !='aria_label'],
            **self.args,
            Class=f'btn-group{"-vertical" if self.is_vertical else ""}',role="group", aria_label=self.btn_grp_cntnt.get('aria_label',"Basic example"),
        )
    
    def __any_tag(self,tag):
        return div(
            *[EL(k, **self.args).custom_element(tag).element for k,v in self.btn_grp_cntnt.items() if k !='aria_label'],
            **self.args,
            Class=f'btn-group{"-vertical" if self.is_vertical else ""}',role="group", aria_label=self.btn_grp_cntnt.get('aria_label',"Basic example"),
        )

    def __Checkbox_and_radio(self,):
        return div(
            *[
                input_tag(**v.get('input_attrs'))+label(k, **v.get('label_attrs'))
                for k,v in self.btn_grp_cntnt.items() if k !='aria_label'
            ],
            **self.args,
            Class=f'btn-group{"-vertical" if self.is_vertical else ""}',role="group", aria_label=self.btn_grp_cntnt.get('aria_label',"Basic checkbox toggle button group"),
        )

    def __btn_toolbar(self,):
        return div(
            *[
                div(
                    *[button(k2, **v2) for k2,v2 in v.get('buttons',{}).items()],
                    Class=f'btn-group{"-vertical" if self.is_vertical else ""} me-2', role="group", aria_label=v.get('aria_label',"Button group")
                )
                for k,v in self.btn_grp_cntnt.items() if k !='aria_label'
            ],
            **self.args.get('btn_grp_attrs',{}),
            Class='btn-toolbar', role="toolbar", aria_label=self.args.get('btn-toolbar',{}).get('aria_label',"Toolbar with button groups"),
        )
        
    def render(self,tag=None,btn_grp_type='btn',):
        btn_grp_dict = {
            'btn': self.__button,
            'custom_tag': self.__any_tag,
            'checkbox_radio': self.__Checkbox_and_radio,
            'toolbar': self.__btn_toolbar,
        }
        if tag:
            return btn_grp_dict['custom_tag'](tag)
        else:
            return btn_grp_dict.get(btn_grp_type,self.__button)()
