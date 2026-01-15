from probo.styles.frameworks.bs5.comp_enum import Carousel
from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Carousel(BS5Component):
    
    def __init__(self, *carousel_items,variant='light',render_constraints=None, **attrs):
        self.attrs = attrs
        self.variant=variant
        self.render_constraints=render_constraints
        self.carousel_items = list() if not carousel_items else [self.add_carousel_item(item,return_item=True) for item in carousel_items]
        if self.carousel_items:
            if 'active' not in self.carousel_items[0].classes:
                self.carousel_items[0].classes.append('active')
        # self.template = self._render_comp()
        self.btn_classes = [Carousel[self.variant.upper()].value if self.variant.upper() in Carousel else Carousel.CAROUSEL.value]
        self.carousel_control_prev=str()
        self.carousel_control_next=str()
        self.carousel_indicators=str()
        self.tag = 'div'

        super().__init__(name='BS5-carousel', state_props=self.render_constraints)
    
    def add_carousel_item(self,content,carousel_caption=None,caption_attrs=None,return_item=False,**attrs):
        item = BS5Element(
            'div',
            content,
            classes=['carousel-item'],
            **attrs
        )
        if carousel_caption:
            item_caption = BS5Element(
                'div',
                carousel_caption,
                classes=['carousel-caption'],
                **(caption_attrs if caption_attrs else dict())
            )
            item.include(item_caption)
        if return_item:
            return item
        self.carousel_items.append(item)
        return self

    def add_carousel_controls(self,):
        '''
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
        '''
        control_prev = BS5Element(
            'button',
            classes=['carousel-control-prev'],
            Type='button',
            data_bs_target='#carouselExampleDark',
            data_bs_slide='prev'
        )
        control_prev.include(BS5Element('span', classes=['carousel-control-prev-icon'], aria_hidden='true'))
        control_prev.include(BS5Element('span', 'Previous', classes=['visually-hidden']))
        
        control_next = BS5Element(
            'button',
            classes=['carousel-control-next'],
            Type='button',
            data_bs_target='#carouselExampleDark',
            data_bs_slide='next'
        )
        control_next.include(BS5Element('span', classes=['carousel-control-next-icon'], aria_hidden='true'))
        control_next.include(BS5Element('span', 'Next', classes=['visually-hidden']))
        
        self.carousel_control_prev = control_prev.render()
        self.carousel_control_next = control_next.render()
        
        return self

    def add_carousel_indicators(self,):
        '''
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        '''
        indicators = BS5Element(
            'div',
            classes=['carousel-indicators']
        )
        indicators_list = [
            BS5Element(
            'button',
            Type="button", data_bs_target=f"#{self.attrs.get('Id','')}", data_bs_slide_to=str(indx), aria_label=f"Slide {indx+1}",
        )
            for indx in range(len(self.carousel_items))
        ]
        indicators_list[0].attrs['class']="active"
        indicators.include(*indicators_list)
        self.carousel_indicators = indicators.render()
        return self

    def before_render(self, **props):
        carousel_inner = BS5Element(
            'div',
            classes=['carousel-inner'],
        ).include(*self.carousel_items).render()
        self.include_content_parts(self.carousel_indicators, carousel_inner,self.carousel_control_prev,self.carousel_control_next)


    def _render_comp(self):

        carousel = BS5Element(
            self.tag,
            classes=['carousel','slide'],
            data_bs_ride="carousel",**self.attrs
        )
        return carousel