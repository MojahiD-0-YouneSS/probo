from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import Cards
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Card(BS5Component):
    ''''''
    
    def __init__(self, card_header=None,card_image=None, card_body=None,card_footer=None,render_constraints=None,is_image_bottom=False, **attrs):
        self.attrs = attrs
        self.is_image_bottom=is_image_bottom
        self.card_header=card_header
        self.card_body=card_body
        self.card_footer=card_footer
        self.render_constraints=render_constraints or {}
        # self.template = self._render_comp()
        self.card_image=card_image
        self.card_classes = [Cards.CARD.value]
        self.tag = 'div'
        self.body_children = []
        super().__init__(name='BS5-card', state_props=self.render_constraints)

    def add_card_title(self, title:str, tag='h1',**attrs):
        card_title = BS5Element(tag, title, classes=['card-title'],**attrs)
        self.body_children.append(card_title.render())
        return self

    def add_card_sub_title(self, sub_title:str, tag='h1',**attrs):
        card_sub_title = BS5Element(tag, sub_title, classes=['card-subtitle'],**attrs)
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

    def add_card_body(self, card_body,override=False,**attrs):
        body = BS5Element(
            'div',
            card_body,
            classes=[Cards.CARD_BODY.value],
        )
        body.include(''.join(self.body_children))
        if self.card_body and not override:
            self.card_body+=body.render()
        else:
            self.card_body=body.render()
        return self

    def add_card_header(self, card_header,override=False,**attrs):
        header = BS5Element(
            'div',
            card_header,
            classes=[Cards.CARD_HEADER.value],
        )
        self.card_header=header.render()
        return self

    def add_card_footer(self, card_footer,override=False,**attrs):
        footer = BS5Element(
            'div',
            card_footer,
            classes=[Cards.CARD_FOOTER.value],
        )
        self.card_footer=footer.render()
        return self
    
    def add_card_image(self,src_url,override=False,**attrs):
        img = BS5Element(
            'img',
            classes=[(Cards.CARD_IMG_BOTTOM.value if self.is_image_bottom else Cards.CARD_IMG_TOP.value)],src=src_url
        )
        self.card_image=img.render()
        return self

    def before_render(self, **props):
        if self.card_header:
            self.add_card_header(str(self.card_header),override=True)
        if self.card_image:
            self.add_card_image(str(self.card_image),override=True)
        if self.card_body:
            self.add_card_body(str(self.card_body),override=True)
            if not self.body_children:
                self.body_children.append(self.card_body)
        if self.card_footer:
            self.add_card_footer(str(self.card_footer),override=True)

        if self.is_image_bottom:
            parts = [x  for x in [self.card_header,*self.body_children,self.card_footer,self.card_image]if x is not None]
        else:
            parts = [x  for x in [self.card_header, self.card_image, *self.body_children, self.card_footer]if x is not None]
        self.include_content_parts(*parts)

    def _render_comp(self):
        card = BS5Element(
            self.tag,
            classes=self.card_classes,**self.attrs
        )
        return card
    
class BS5CardGroup(BS5Component):
    
    def __init__(self, *cards, render_constraints=None,**attrs):
        self.attrs = attrs
        self.render_constraints=render_constraints
        self.cards = list(cards)
        # self.template = self._render_comp()
        self.card_classes = [Cards.CARD_GROUP.value]
        self.tag = 'div'
        super().__init__(name='BS5-card', state_props=self.render_constraints)
    def add_card(self,card_header=None,card_image=None, card_body=None,card_footer=None, **attrs):
        card = BS5Card(card_header=card_header,card_image=card_image, card_body=card_body,card_footer=card_footer, **attrs).render()
        self.cards.append(card) 
        return self

    def before_render(self, **props):
        self.include_content_parts(*self.cards)
        return
    def _render_comp(self):
        card_group_content = ''.join(([x.render() if hasattr(x,'render') else str(x) for x in self.cards]))
        card_group = BS5Element(
            self.tag,
            card_group_content,
            classes=self.card_classes,**self.attrs
        )
        return card_group
