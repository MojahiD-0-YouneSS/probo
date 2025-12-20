from mui.styles.frameworks.bs5.components.comp_enum import Carousel
from mui.styles.frameworks.bs5.bs5 import (
    BS5,
    BS5ElementStyle,
)

from mui import (
    div,
    img,
    video,
    audio,
    button,
    span,
)


class DefaultCarousel:
    def __init__(self,Type='base',*crsl_items, **kwargs):
        self.attrs = kwargs.get('attrs',{})
        self.contents = kwargs.get('contents',{})
        self.crsl_type = Type
        self.crsl_items=crsl_items
    
    def __base(self,):
        '''
        base Carousel format
            <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                <img src="..." class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                <img src="..." class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                <img src="..." class="d-block w-100" alt="...">
                </div>
            </div>
            </div>
        '''
        dflt_crsl_bs5_css = BS5()
        dflt_crsl_bs5_css.add_new('div #carouselExampleSlidesOnly',
                BS5ElementStyle('div').add('carousel','slide').render()
            )

        dflt_crsl_bs5_css.add_new('div c-inner',
            BS5ElementStyle('div',).add('carousel-inner').render()
        )

        dflt_crsl_bs5_css.add_new('div',
            BS5ElementStyle('div',).add('carousel-item').render()
        )

        dflt_crsl_bs5_css.add_new('img',
            BS5ElementStyle('img',).add('d-block','w-100',).render()
        )
        
        carousel = div(
            div(
                div(
                    *self.crsl_items if self.crsl_items else img(
                        src= self.attrs.get('img-attrs',{}).get('src', '...'),
                        alt=self.attrs.get('img-attrs',{}).get('alt', '...'),
                        Class=dflt_crsl_bs5_css.elements.get('img')
                    ),
                    Class=dflt_crsl_bs5_css.elements.get('div',),
                ),
                Class=dflt_crsl_bs5_css.elements.get('div c-inner',),
            ),
            Id='carouselExampleSlidesOnly',
            Class=dflt_crsl_bs5_css.elements.get('div #carouselExampleSlidesOnly'),
            data_bs_ride=Carousel.CAROUSEL.value,
        )
        return carousel

    def __with_cotrols(self,):
        '''
         <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="..." class="d-block w-100" alt="...">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
        '''
        dflt_crsl_bs5_css = BS5()
        dflt_crsl_bs5_css.add_new('div #carouselExampleControls',

                BS5ElementStyle('div').add('carousel','slide').render(),
            )

        dflt_crsl_bs5_css.add_new('div c-inner',
            BS5ElementStyle('div',).add('carousel-inner').render()
        )

        dflt_crsl_bs5_css.add_new('div',
            BS5ElementStyle('div',).add('carousel-item').render()
        )

        dflt_crsl_bs5_css.add_new('img',
            BS5ElementStyle('img',).add('d-block','w-100',).render()
        )
        
        dflt_crsl_bs5_css.add_new('btn p',
            BS5ElementStyle('btn',).add('carousel-control-prev',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span p',
            BS5ElementStyle('span',).add('visually-hidden',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span p-icon',
            BS5ElementStyle('span',).add('carousel-control-prev-icon',).render()
        )
        
        dflt_crsl_bs5_css.add_new('btn n',
            BS5ElementStyle('btn',).add('carousel-control-next',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span n',
            BS5ElementStyle('span',).add('visually-hidden',).render()
        )
        dflt_crsl_bs5_css.add_new('span n-icon',
            BS5ElementStyle('span',).add('carousel-control-next-icon',).render()
        )
        
        crsl_w_ctrls = div(
            div(
                div(
                    div(
                        *self.crsl_items if self.crsl_items else img(
                            src= self.attrs.get('img-attrs',{}).get('src', '...'),
                            alt=self.attrs.get('img-attrs',{}).get('alt', '...'),
                            Class=dflt_crsl_bs5_css.elements.get('img',''),
                        ),
                        Class=dflt_crsl_bs5_css.elements.get('div',''),
                    ),
                    Class=dflt_crsl_bs5_css.elements.get('div c-inner',''),
                ),
                Class=dflt_crsl_bs5_css.elements.get('div #carouselExampleControls',''),Id="carouselExampleControls", data_bs_ride="carousel",
                
            ),
            button(
                span(
                    
                ),
                span(
                    'Previous',
                    Class=dflt_crsl_bs5_css.elements.get('span p',''),

                ),
                Class=dflt_crsl_bs5_css.elements.get('btn p',''), type="button", data_bs_target="#carouselExampleControls", data_bs_slide="prev",
            ),
            button(
                span(
                ),
                span(
                    'Next',
                    Class=dflt_crsl_bs5_css.elements.get('span n',''),
                ),
            ), Class=dflt_crsl_bs5_css.elements.get('btn n',''), type="button", data_bs_target="#carouselExampleControls", data_bs_slide="next"

        )
        return crsl_w_ctrls
   
    def __with_indicators(self,):
        '''
            <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                    <img src="..." class="d-block w-100" alt="...">
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        '''
        dflt_crsl_bs5_css = BS5()
        dflt_crsl_bs5_css.add_new('div #carouselExampleIndicators',

                BS5ElementStyle('div').add('carousel','slide',).render(),
            )

        dflt_crsl_bs5_css.add_new('div c-inner',
            BS5ElementStyle('div',).add('carousel-inner').render()
        )

        dflt_crsl_bs5_css.add_new('div',
            BS5ElementStyle('div',).add('carousel-item').render()
        )

        dflt_crsl_bs5_css.add_new('img',
            BS5ElementStyle('img',).add('d-block','w-100',).render()
        )
        
        dflt_crsl_bs5_css.add_new('btn p',
            BS5ElementStyle('btn',).add('carousel-control-prev',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span p',
            BS5ElementStyle('span',).add('visually-hidden',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span p-icon',
            BS5ElementStyle('span',).add('carousel-control-prev-icon',).render()
        )
        
        dflt_crsl_bs5_css.add_new('btn n',
            BS5ElementStyle('button',).add('carousel-control-next',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span n',
            BS5ElementStyle('span',).add('visually-hidden',).render()
        )
        dflt_crsl_bs5_css.add_new('span n-icon',
            BS5ElementStyle('span',).add('carousel-control-next-icon',).render()
        )
        dflt_crsl_bs5_css.add_new('div c-indicators',
            BS5ElementStyle('div',).add('carousel-indicators',).render()
        )
        dflt_crsl_bs5_css.add_new('btn c-indicators',
            BS5ElementStyle('button',).add('active',).render()
        )
        
        
        crsl_w_indctrs = div(
            div(
                *[
                    button(
                        type="button",
                        data_bs_target="#carouselExampleIndicators",
                        data_bs_slide_to=f"{x}",
                        Class=dflt_crsl_bs5_css.elements.get('btn c-indicators',''),
                        aria_current="true",
                        aria_label=f"Slide {x+1}",
                    ) for x in range(len(self.crsl_items))],
                Class=dflt_crsl_bs5_css.elements.get('div c-indicators','')
            ),
            div(
                *self.crsl_items if self.crsl_items else div(
                     img(
                            src= self.attrs.get('img-attrs',{}).get('src', '...'),
                            alt=self.attrs.get('img-attrs',{}).get('alt', '...'),
                            Class=dflt_crsl_bs5_css.elements.get('img',''),
                        ),
                        Class=dflt_crsl_bs5_css.elements.get('div',''),
                    ),
                    Class=dflt_crsl_bs5_css.elements.get('div c-inner',''),
                
            ),
            button(
                span(
                    Class=dflt_crsl_bs5_css.elements.get('span p-icon',''),
                ),
                span(
                    'Previous',
                    Class=dflt_crsl_bs5_css.elements.get('span p',''),

                ),
                Class=dflt_crsl_bs5_css.elements.get('btn p',''), type="button", data_bs_target="#carouselExampleIndicators", data_bs_slide="prev",
            ),
            button(
                span(
                    Class=dflt_crsl_bs5_css.elements.get('span n-icon',''),
                ),
                span(
                    'Next',
                    Class=dflt_crsl_bs5_css.elements.get('span n',''),
                ),Class=dflt_crsl_bs5_css.elements.get('btn n',''), type="button", data_bs_target="#carouselExampleIndicators", data_bs_slide="next"
            ), 
                Class=dflt_crsl_bs5_css.elements.get('div #carouselExampleIndicators',''),Id="carouselExampleIndicators", data_bs_ride="carousel",
            
        )
        return crsl_w_indctrs
   
    def __with_crossfade(self,):
        '''<div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
            <img src="..." class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="..." class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="..." class="d-block w-100" alt="...">
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
        </div>'''
        
        dflt_crsl_bs5_css = BS5()
        dflt_crsl_bs5_css.add_new('div #carouselExampleFade',

                BS5ElementStyle('div').add('carousel','slide','carousel-fade').render(),
            )

        dflt_crsl_bs5_css.add_new('div c-inner',
            BS5ElementStyle('div',).add('carousel-inner').render()
        )

        dflt_crsl_bs5_css.add_new('div',
            BS5ElementStyle('div',).add('carousel-item').render()
        )

        dflt_crsl_bs5_css.add_new('img',
            BS5ElementStyle('img',).add('d-block','w-100',).render()
        )
        
        dflt_crsl_bs5_css.add_new('btn p',
            BS5ElementStyle('btn',).add('carousel-control-prev',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span p',
            BS5ElementStyle('span',).add('visually-hidden',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span p-icon',
            BS5ElementStyle('span',).add('carousel-control-prev-icon',).render()
        )
        
        dflt_crsl_bs5_css.add_new('btn n',
            BS5ElementStyle('btn',).add('carousel-control-next',).render()
        )
        
        dflt_crsl_bs5_css.add_new('span n',
            BS5ElementStyle('span',).add('visually-hidden',).render()
        )
        dflt_crsl_bs5_css.add_new('span n-icon',
            BS5ElementStyle('span',).add('carousel-control-next-icon',).render()
        )
        dflt_crsl_bs5_css.add_new('div c-indicators',
            BS5ElementStyle('div',).add('carousel-indicators',).render()
        )
        dflt_crsl_bs5_css.add_new('btn c-indicators',
            BS5ElementStyle('btn',).add('active',).render()
        )
        
        crsl_w_crssfd = div(
            div(
                button(
                    type="button",
                    data_bs_target="#carouselExampleFade",
                    data_bs_slide_to="0",
                    Class=dflt_crsl_bs5_css.elements.get('btn c-indicators',''),
                    aria_current="true",
                    aria_label="Slide 1",
                ),
                Class=dflt_crsl_bs5_css.elements.get('div c-indicators','')
            ),
            div(
                div(
                    div(
                       *self.crsl_items if self.crsl_items else img(
                            src= self.attrs.get('img-attrs',{}).get('src', '...'),
                            alt=self.attrs.get('img-attrs',{}).get('alt', '...'),
                            Class=dflt_crsl_bs5_css.elements.get('img',''),
                        ),
                        Class=dflt_crsl_bs5_css.elements.get('div',''),
                    ),
                    Class=dflt_crsl_bs5_css.elements.get('div c-inner',''),
                ),
                Class=dflt_crsl_bs5_css.elements.get('div #carouselExampleFade',''),Id="carouselExampleFade", data_bs_ride="carousel",
                
            ),
            button(
                span(
                    
                ),
                span(
                    'Previous',
                    Class=dflt_crsl_bs5_css.elements.get('span p',''),

                ),
                Class=dflt_crsl_bs5_css.elements.get('btn p',''), type="button", data_bs_target="#carouselExampleIndicators", data_bs_slide="prev",
            ),
            button(
                span(
                ),
                span(
                    'Next',
                    Class=dflt_crsl_bs5_css.elements.get('span n',''),
                ),
            ), Class=dflt_crsl_bs5_css.elements.get('btn n',''), type="button", data_bs_target="#carouselExampleIndicators", data_bs_slide="next"
            
        )
        return crsl_w_crssfd
    
    def __with_item_interval(self,):
        '''
            <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active" data-bs-interval="10000">
                <img src="..." class="d-block w-100" alt="...">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
            </div>
        '''
        dflt_crsl_bs5_css = BS5()
        dflt_crsl_bs5_css.add_new('div #carouselExampleInterval',
                BS5ElementStyle('div').add('carousel','slide').render()
            )

        dflt_crsl_bs5_css.add_new('div c-inner',
            BS5ElementStyle('div',).add('carousel-inner').render()
        )

        dflt_crsl_bs5_css.add_new('div',
            BS5ElementStyle('div',).add('carousel-item').render()
        )

        dflt_crsl_bs5_css.add_new('img',
            BS5ElementStyle('img',).add('d-block','w-100',).render()
        )
        
        carousel = div(
            div(
                *self.crsl_items if self.crsl_items else div(
                    img(
                        src= self.attrs.get('img-attrs',{}).get('src', '...'),
                        alt=self.attrs.get('img-attrs',{}).get('alt', '...'),
                        Class=dflt_crsl_bs5_css.elements.get('img'),
                        data_bs_interval="10000",
                    ),
                    Class=dflt_crsl_bs5_css.elements.get('div',),
                ),
                Class=dflt_crsl_bs5_css.elements.get('div c-inner',),
            ),
            Id='carouselExampleInterval',
            Class=dflt_crsl_bs5_css.elements.get('div #carouselExampleInterval'),
            data_bs_ride=Carousel.CAROUSEL.value,
        )
        return carousel
   
    def __dark_mode(self,):
        '''
            <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div class="carousel-inner">
                    <div class="carousel-item active" data-bs-interval="10000">
                    <img src="..." class="d-block w-100" alt="...">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>First slide label</h5>
                        <p>Some representative placeholder content for the first slide.</p>
                    </div>
                    </div>
                    <div class="carousel-item" data-bs-interval="2000">
                    <img src="..." class="d-block w-100" alt="...">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Second slide label</h5>
                        <p>Some representative placeholder content for the second slide.</p>
                    </div>
                    </div>
                    <div class="carousel-item">
                    <img src="..." class="d-block w-100" alt="...">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Third slide label</h5>
                        <p>Some representative placeholder content for the third slide.</p>
                    </div>
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
                </div>
        '''
   
    def render(self,):
        Type_dict = {
            'base':self.__base,
            'controls':self.__with_cotrols,
            'indicators':self.__with_indicators,
            'crossfade':self.__with_crossfade,
            'item_interval':self.__with_item_interval,
            'dark_mode':self.__dark_mode,
        }
        
        return Type_dict.get(self.crsl_type,self.__base)()

'''
Disable touch swiping
    <div id="carouselExampleControlsNoTouching" class="carousel slide" data-bs-touch="false" data-bs-interval="false">
    <div class="carousel-inner">
        <div class="carousel-item active">
        <img src="..." class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
        <img src="..." class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
        <img src="..." class="d-block w-100" alt="...">
        </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
    </div>
'''