from mui.components.tag_functions.block_tags import (
    div,
    h2,
    button,
)
from mui.components.tag_functions.inline_tags import (
    strong,
)
from mui.styles.frameworks.bs5.components.comp_enum import Accordion

class DefaultAccordion:
    def __init__(self, btn_string=None, abody_string=None):
        self.btn_string = btn_string
        self.abody_string = abody_string
        self.a_type_dict = {
            'base': self.__base_accordion,
            'flush': self.__flush_accordion,
            }

    def __base_accordion(self, a_content):
        return div(
                a_content,
                Class=Accordion.BASE.value,
                Id="accordionExample",
            )
    def __flush_accordion(self, a_content):
        return div(
                a_content,
                Class= Accordion.BASE.value + Accordion.FLUSH.value,
                Id="accordionFlushExample",
            )   
    def render(self,a_type='base', Always_open=False):
        btn_string = self.btn_string if self.btn_string else "Accordion Item #1"
        abody_string = self.abody_string if self.abody_string else "This is the first item’s accordion body. It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It’s also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow."
        a_content =  div(
                    h2(
                        button(
                            btn_string,
                            type="button",
                            data_bs_toggle= "collapse",
                            data_bs_target= "#collapseOne",
                            aria_expanded= "true",
                            aria_controls= "collapseOne",
                            Class=Accordion.BUTTON.value,
                            Type="button",
                        ),
                    Class=Accordion.HEADER.value
                    ),
                Class=Accordion.ITEM.value
                )
        a_content += div(
                    div(
                        strong(
                            abody_string,
                        ),
                        Class=Accordion.BODY.value,
                    ),
                    Id="collapseOne",
                    Class=Accordion.COLLAPSE.value + " collapse show",
                    data_bs_parent= "#accordionExample" if not Always_open else None,
                )
        das = self.a_type_dict.get(a_type, self.__base_accordion)(a_content)
        return das

DefaultAccordionObject = DefaultAccordion