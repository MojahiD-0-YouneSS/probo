from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Offcanvas
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Offcanvas(BS5Component):

    def __init__(self, *content, render_constraints=None,position='start', **attrs):
        self.attrs = attrs
        self.render_constraints=render_constraints
        self.position=position
        self.content=''.join(content)
        self.offcanvas_items=list()
        # self.template = self._render_comp()
        self.offcanvas_classes = [Offcanvas.OFFCANVAS.value,Offcanvas[f'offcanvas_{self.position}'.upper()].value]
        self.tag = 'div'
        super().__init__(name='BS5-offcanvas', state_props=self.render_constraints)

    def add_trigger(self,target,content,tag='button',**attrs):
        trigger = BS5Element(
            tag,
            content,
            data_bs_toggle='offcanvas',
            aria_controls=target,
            **({'type':'button'} if tag == 'button' else {'role':'button', 'href':f'#{target}'})
        )

        trigger.attr_manager.set_bulk_attr(**attrs)
        return self

    def add_offcanvas_header(self,content,tag='h1',**attrs):
        title = BS5Element(
            tag,
            content,
            classes=[Offcanvas.OFFCANVAS_TITLE.value,]
            ,**attrs,
        )
        if not attrs.get('Id', None) and self.attrs.get('Id', None):
            title.attr_manager.set_attr('Id',f"{self.attrs.get('Id', None)}Label")
        close_btn = BS5Element(
            'button',
            classes=['btn-close',]
        )
        close_btn.attr_manager.set_bulk_attr(
            Type='button',data_bs_dismiss='offcanvas',aria_label="close"
        )
        header = BS5Element(
            'div',classes=[Offcanvas.OFFCANVAS_HEADER.value,],
        )
        if attrs.get('Id', None):
            self.template.attr_manager.set_attr('aria_labelledby', attrs['Id'])
        header.include(title,close_btn)

        self.offcanvas_items.append(header)
        return self
    def add_offcanvas_body(self,content,**attrs):
        item = BS5Element(
                'div',
                content,classes=[Offcanvas.OFFCANVAS_BODY.value],
            **attrs)
        self.offcanvas_items.append(item)
        return self

    def before_render(self, **props):
        self.include_content_parts(*self.offcanvas_items)

    def _render_comp(self):
        offcanvas = BS5Element(
            self.tag,
            self.content,
            classes=self.offcanvas_classes,**self.attrs
        )
        offcanvas.attr_manager.set_bulk_attr(
            tabindex=-1,
        )
        return offcanvas

