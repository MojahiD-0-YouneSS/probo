from mui import (
    div,img,a, p,h5
)

class DefaultCard:
    def __init__(self, is_card_group=False, **kwargs):
        self.is_card_group = is_card_group
        self.attrs = kwargs.get('attrs',{})
        self.contents = kwargs.get('contents',{})
   
    def __card(self,):        
        return div(self.contents.get('card', ''), Class='card', **self.attrs.get('card-attrs',{}))
    
    def __card_complete(self,):
        '''
            <div class="card" style="width: 18rem;">
            <div class="card-header">
                Featured
            </div>
            <img src="..." class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="card-link">Another link</a>
            </div>
            <div class="card-footer">
                Card footer
            </div>
            </div>
        '''
        return div(
            div(
                self.contents.get('card-header','Card Header'),
                Class='card-header',**self.attrs.get('card-header-attrs',{})
            ),
            img(
                Class='card-img-top',
                **self.attrs.get('img-attrs',{})
            ),
            div(
                self.contents.get('card-body',h5('Card title',Class='card-title')+p('Some quick example text to build on the card title and make up the bulk of the card\'s content.',Class='card-text')+a('Another link',href='#',Class='card-link'    )),
                Class='card-body',**self.attrs.get('card-body-attrs',{})
            ),
            div(
                self.contents.get('card-footer','Card Footer'),
                Class='card-footer',**self.attrs.get('card-footer-attrs',{})
            ),Class='card', **self.attrs.get('card-attrs',{})
        )

    def __card_group(self,):
        '''
            <div class="card-group">
            <div class="card">
                <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                </div>
                <div class="card-footer">
                <small class="text-muted">Last updated 3 mins ago</small>
                </div>
            </div>
            <div class="card">
                <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p>
                </div>
                <div class="card-footer">
                <small class="text-muted">Last updated 3 mins ago</small>
                </div>
            </div>
            <div class="card">
                <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
                </div>
                <div class="card-footer">
                <small class="text-muted">Last updated 3 mins ago</small>
                </div>
            </div>
            </div>
            '''
        return div(
            self.contents.get('cards',  div(
            div(
                self.contents.get('card-header','Card Header'),
                Class='card-header',**self.attrs.get('card-header-attrs',{})
            ),
            img(
                Class='card-img-top',
                **self.attrs.get('img-attrs',{})
            ),
            div(
                self.contents.get('card-body',h5('Card title',Class='card-title')+p('Some quick example text to build on the card title and make up the bulk of the card\'s content.',Class='card-text')+a('Another link',href='#',Class='card-link'    )),
                Class='card-body',**self.attrs.get('card-body-attrs',{})
            ),
            div(
                self.contents.get('card-footer','Card Footer'),
                Class='card-footer',**self.attrs.get('card-footer-attrs',{})
            )
        )),
            Class='card-group',
            **self.attrs.get('card-attrs',{})
        )
    
    def render(self):
        if self.is_card_group:
            return self.__card_group()
        elif self.contents.get('card-header') or self.contents.get('card-body') or self.contents.get('card-footer'):
            return self.__card_complete()
        else:
            return self.__card()
         

