from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Toast
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Toast(BS5Component):
    def __init__(self, header_content=None,body_content=None,btn_position='header',render_constraints=None,include_container=False, **attrs):
        self.render_constraints = render_constraints
        self.attrs = attrs
        self.btn_position=btn_position
        self.header_content = header_content
        self.body_content = body_content
        self.toast_items=[]
        self.toast=None
        self.include_container=include_container
        self.tag = 'div'
        self.close_btn=self.close_toast_btn()
        self.toast_classes = [Toast.TOAST.value]
        super().__init__(name='BS5-Toast', state_props=self.render_constraints)

    def close_toast_btn(self,):
        return BS5Element(
            'button',
            classes=['btn-close'],
            Type='button',
            data_bs_dismiss='toast',
            aria_label='close',
        )

    def add_toast(self,header_content=None,body_content=None,btn_position='header',**attrs):
        toast = BS5Element(
            self.tag,
            classes=self.toast_classes,
            role='alert',
            aria_live='assertive',
            aria_atomic='true',
        )
        toast.attr_manager.set_bulk_attr(**self.attrs)

        toast.attr_manager.set_bulk_attr(**attrs)
        if header_content:
            header = BS5Element(
                'div',header_content,classes=[Toast.TOAST_HEADER.value],
            )
        if body_content:
            body = BS5Element(
                'div',body_content,classes=[Toast.TOAST_BODY.value],
            )

        if header_content and btn_position=='header':
            header.include(self.close_btn)
            toast.include(header)

        if body_content and btn_position == 'body':
            body.include(self.close_btn)
            toast.include(body)

        if header_content and not btn_position=='header':
            toast.include(header)
        if body_content and not btn_position == 'body':
            toast.include(body)

        if self.include_container:
            self.toast_items.append(toast)
        else:
            self.toast=toast
        return self

    def before_render(self, **props):
        self.include_content_parts(*self.toast_items)

    def _render_comp(self,*args,**kwargs):
        if self.include_container:
            toast_container = BS5Element(
                self.tag,
                classes=[Toast.TOAST_CONTAINER.value],

            )
            toast_container.include(*self.toast_items)
            return toast_container
        else:
            self.add_toast(
                header_content=self.header_content,
                body_content=self.body_content,
                btn_position=self.btn_position,
            )

            return self.toast
