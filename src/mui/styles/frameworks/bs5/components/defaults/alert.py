from mui.components.elements import Element as EL
from mui.components.tag_functions.self_closing import (
    hr, 
)
from mui.components.tag_functions.inline_tags import (
    strong,
    a,
)
from mui.components.tag_functions.block_tags import (
    div, 
    h4, 
    p, 
    button,
)
from mui.styles.frameworks.bs5.components.comp_enum import Alert

class DefaultAlert:
    def __init__(self,content,path,color,link_content, heading_content):
        self.content=content
        self.path=path
        self.color=color.upper()
        self.link_content=link_content
        self.heading_content=heading_content
        self.selected_icon = None
        self.icon_dict = self.__icon_dict_gen()
    
    def __icon_dict_gen(self,):
        return {
            'exclamation-triangle': EL().custom_element('svg', EL().custom_element('path', d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z",is_void_element=True,).element, xmlns="http://www.w3.org/2000/svg", width="24", height="24", fill="currentColor", Class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2", viewBox="0 0 16 16", role="img", aria_label="Warning:").element,

            'info-fill': EL().custom_element('svg', EL().custom_element('path', d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z",is_void_element=True,).element, xmlns="http://www.w3.org/2000/svg", width="24", height="24", fill="currentColor", Class="bi bi-info-circle-fill flex-shrink-0 me-2", viewBox="0 0 16 16", role="img", aria_label="Info:").element,

            'check-circle-fill': EL().custom_element('svg', EL().custom_element('path', d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z",is_void_element=True,).element, xmlns="http://www.w3.org/2000/svg", width="24", height="24", fill="currentColor", Class="bi bi-check-circle-fill flex-shrink-0 me-2", viewBox="0 0 16 16", role="img", aria_label="Success:").element,

        }

    def __base(self,):
        content = self.content if self.content else "A simple primary alert—check it out!"
        return div(
            content,
            Class=f"""{Alert.BASE.value} {Alert.PRIMARY.value}""",
            role="alert"
        )

    def __link(self,):
        link_content = a(self.link_content if self.link_content else "an example link", href=self.path if self.path else "#", Class="alert-link")
        content =  self.content if self.content else  f'A simple primary alert with {link_content} Give it a click if you like.'
        return div(
            content,
            Class=f"""{Alert.BASE.value} {Alert[self.color].value if self.color else Alert.PRIMARY.value}""",
            role="alert"
        )
   
    def __heading(self,):
        content = self.content if self.content else p("Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.")+ hr()+ p("Whenever you need to, be sure to use margin utilities to keep things nice and tidy.", Class="mb-0")
        heading_content = self.heading_content if self.heading_content else "Well done!"
        return div(
            h4(heading_content, Class=Alert.HEADING.value),
            content,
            Class=f"""{Alert.BASE.value} {Alert[self.color].value if self.color else Alert.SUCCESS.value}""",
            role="alert"
        )
   
    def __icons(self,):
        content = self.content if self.content else div('An example alert with an icon')
        icon = self.icon_dict.get(self.selected_icon,'exclamation-triangle')
        return div(
            icon, content,
            Class=f"""{Alert.BASE.value} {Alert[self.color].value if self.color else Alert.PRIMARY.value} d-flex align-items-center""",
            role="alert"
        )
   
    def __local_svg(self,):
        return div(EL().custom_element('svg',"""<use xlink:href="#check-circle-fill"/>""",Class="bi flex-shrink-0 me-2" ,width="24" ,height="24", role="img" ,aria_label="Success:"),
            div("An example success alert with an icon"),
            Class=f"""{Alert.BASE.value} {Alert[self.color].value if self.color else Alert.SUCCESS.value } d-flex align-items-center""",
            role="alert"
        ) 
   
    def __dismissible(self,):
        content = self.content if self.content else strong("Holy guacamole!")+" You should check in on some of those fields below."
        return div(
            content,
            button(Type="button", Class="btn-close" ,data_bs_dismiss="alert" ,aria_label="Close"),
            Class=f"""{Alert.BASE.value} {Alert.DISMISSIBLE.value} {Alert[self.color].value if self.color else Alert.WARNING.value} fade show""",
            role="alert"
        )
   
 
    def render(self,Type='Base',icon_type='exclamation-triangle'):
        self.selected_icon = icon_type
        type_dict = {
            'base': self.__base,
            'link': self.__link,
            'heading': self.__heading,
            'icons': self.__icons,
            'local_svg': self.__local_svg,
            'dismissible': self.__dismissible
        }
        return type_dict.get(Type.lower(), self.__base)()


DefaultAlertObject = DefaultAlert

