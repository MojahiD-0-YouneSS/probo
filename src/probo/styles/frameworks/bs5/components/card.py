from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Cards
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Card(BS5Component):
    ''''''
    
    def __init__(self, card_header=None,card_image=None, card_body=None,card_footer=None, **attrs):
        self.attrs = attrs
        self.card_header=card_header
        self.card_body=card_body
        self.card_footer=card_footer
        # self.template = self._render_comp()
        self.card_image=card_image
        self.card_classes = [Cards.BASE.value]
        self.tag = 'div'
        self.body_children = []
        super().__init__(name='BS5-card', props={}, state=None)

    def add_card_title(self, title:str, tag='h1',**attrs):
        card_title = BS5Element(tag, title, classes=['card-title'],**attrs)
        self.body_children.append(card_title.render())
        return self

    def add_card_sub_title(self, sub_title:str, tag='h1',**attrs):
        card_sub_title = BS5Element(tag, sub_title, classes=['card-sub-title'],**attrs)
        self.body_children.append(card_sub_title.render())
        return self

    def add_card_text(self, text:str, tag='p',**attrs):
        card_text = BS5Element(tag, text, classes=['card-text'],**attrs)
        self.body_children.append(card_text.render())
        return self

    def add_card_link(self, link:str, tag='a',**attrs):
        card_link = BS5Element(tag, link, classes=['card-link'],**attrs)
        self.body_children.append(card_link.render())
        return self

    def add_card_body(self, card_body,**attrs):
        body = BS5Element(
            'div',
            card_body,
            classes=[Cards.BODY.value],
        )
        body.include(''.join(self.body_children))
        if self.card_body:
            self.card_body+=body.render()
        else:
            self.card_body=body.render()
        return self
    def add_card_header(self, card_header,**attrs):
        header = BS5Element(
            'div',
            card_header,
            classes=[Cards.HEADER.value],
        )
        self.card_header=header.render()
        return self
    def add_card_footer(self, card_footer,**attrs):
        footer = BS5Element(
            'div',
            card_footer,
            classes=[Cards.FOOTER.value],
        )
        self.card_footer=footer.render()
        return self
    
    def add_card_image(self,**attrs):
        img = BS5Element(
            'img',
            classes=[Cards.IMAGE.value],
        )
        self.card_image=img.render()
        return self
    def _render_comp(self):
        card_content = ''
        if self.card_header:
            card_content += self.card_header
        if self.card_image:
            card_content += self.card_image
        if self.card_body:
            card_content += self.card_body
        if self.card_footer:
            card_content += self.card_footer

        card = BS5Element(
            self.tag,
            card_content,
            classes=self.card_classes,**self.attrs
        )
        return card
    
class BS5CardGroup(BS5Component):
    
    def __init__(self, *cards, **attrs):
        self.attrs = attrs
        self.cards = list(cards)
        # self.template = self._render_comp()
        self.card_classes = [Cards.GROUP.value]
        self.tag = 'div'
        super().__init__(name='BS5-card', props={}, state=None)
    def add_card(self,card_header=None,card_image=None, card_body=None,card_footer=None, **attrs):
        card = BS5Card(card_header=card_header,card_image=card_image, card_body=card_body,card_footer=card_footer, **attrs).render()
        self.cards.append(card) 
        return self
    def _render_comp(self):
        card_group_content = ''.join(self.cards)
        card_group = BS5Element(
            self.tag,
            card_group_content,
            classes=self.card_classes,**self.attrs
        )
        return card_group