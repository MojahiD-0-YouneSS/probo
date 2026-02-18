from probo.styles.frameworks.bs5.comp_enum import Carousel
from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5Carousel(BS5Component):
    """A high-level manager for Bootstrap 5 Carousel (slideshow) components.

    This class automates the complex markup required for carousels, including 
    the inner track (`carousel-inner`), item registration, navigation indicators, 
    and previous/next controls. It supports both dark and light variants.

    Attributes:
        carousel_items (list): A collection of rendered `BS5Element` instances 
            representing individual slides.
        variant (str): The visual theme ('light' or 'dark').
        carousel_control_prev (str): Rendered HTML for the 'previous' button.
        carousel_control_next (str): Rendered HTML for the 'next' button.
        carousel_indicators (str): Rendered HTML for the slide indicators.
    """
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
        """Creates and appends a new slide to the carousel.

        Args:
            content (Any): The primary content of the slide (usually an image).
            carousel_caption (str, optional): Heading or text to overlay on the slide.
            caption_attrs (dict, optional): Attributes for the caption container.
            return_item (bool): If True, returns the created BS5Element instead of self.
            **attrs: Attributes for the 'carousel-item' wrapper.

        Returns:
            Union[self, BS5Element]: The carousel instance for chaining or the new item.
        """
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
        """Generates the 'Previous' and 'Next' navigation buttons.

        This method populates `carousel_control_prev` and `carousel_control_next` 
        with the standard Bootstrap control markup, including SVG icons and 
        screen-reader text.

        Returns:
            self: Enables fluent method chaining.
        """

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
        """Generates the bottom navigation indicators (dashes/dots).

        This method calculates the number of indicators based on the current 
        length of `carousel_items` and assigns the 'active' state to the 
        appropriate index.

        Returns:
            self: Enables fluent method chaining.
        """
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