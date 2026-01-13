from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Modal
from probo.styles.frameworks.bs5.bs5 import BS5Element
class BS5Modal():
    '''<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Open modal for @mdo</button>

    <div class="modal" id="exampleModal">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">New message</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
        </div>
    </div>
    </div>'''
    
    def __init__(self, content, **attrs):
        self.attrs = attrs
        self.content=content
        self.modal_parts=[]
        # self.template = self._render_comp()
        self.modal_classes = [Modal.BASE.value]
        self.tag = 'div'

        super().__init__(name='BS5-button', props={}, state=None)
    
    def add_trigger_btn(self,content,**attrs):
        trigger_btn = BS5Element(
            'button',
            content,
            classes=self.btn_classes,
            **attrs
        )
        self.triggers.append(trigger_btn)
        return self
    
    
    def add_modal_header(self,other_content,title=None,**attrs):
        header_content = ''
        if title:
            header_content += f'<h5 class="modal-title">{title}</h5>'
        header_content += other_content
        modal_header = BS5Element(
            'div',
            header_content,
            classes=[Modal.MODAL_HEADER.value],
            **attrs
        )
        self.modal_parts.append(modal_header.render())
        return self 
    def add_modal_body(self,content,**attrs):
        modal_body = BS5Element(
            'div',
            content,
            classes=[Modal.MODAL_BODY.value],
            **attrs
        )
        self.modal_parts.append(modal_body.render())
        return self 
    def add_modal_footer(self,content,**attrs):
        modal_footer = BS5Element(
            'div',
            header_content,
            classes=[Modal.MODAL_FOOTER.value],
            **attrs
        )
        self.modal_parts.append(modal_footer.render())
        return self 
    def _render_comp(self):
        self.content+=''.join(self.modal_parts)
        button = BS5Element(
            self.tag,
            self.content,
            classes=self.btn_classes,**self.attrs
        )
        return button
