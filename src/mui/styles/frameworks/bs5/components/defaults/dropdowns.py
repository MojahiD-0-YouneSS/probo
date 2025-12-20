from mui import (
    div,
    button,
    ul,
    li,a,
)

class DefaultDropdown:
    def __init__(self,Type='base', **kwargs):
        self.contents  = kwargs.get('drp-down-contents',{})
        self.kwargs=kwargs
        self.Type=Type
        self.btn_type  = 'btn'
        
    def __base(self,):
        '''
        <div class="dropdown">
        <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
            Dropdown button
        </button>
        <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Link 1</a></li>
            <li><a class="dropdown-item" href="#">Link 2</a></li>
            <li><a class="dropdown-item" href="#">Link 3</a></li>
        </ul>
        </div>
        '''
        ''
        items = [li(a('Link 1',Class="dropdown-item", href="#")) if self.contents.get('item',None)  else li(a(x.get('content',f'Link {y}') ,Class="dropdown-item", href=x.get('content',f'#'))) for x,y in zip( self.contents.get('item',None), range(len( self.contents.get('item',None))))]
               
        drpdwn = div(
            button(
                'Dropdown button',
                type="button",
                Class="btn btn-primary dropdown-toggle",
                data_bs_toggle="dropdown",
            ) if self.btn_type  == 'btn' else a(
                Class="btn btn-secondary dropdown-toggle",
                href= self.kwargs.get('btn-link',"#"), role="button",
                data_bs_toggle="dropdown",
                aria_expanded="false"
                ),
            ul(
                *items
                ,Class="dropdown-menu"
            ),Class='dropdown',
        )
        return drpdwn
    
    def render(self,):
        if self.Type:
            return self.__base()
        return
    
'''
header : <li><h5 class="dropdown-header">Dropdown header 1</h5></li>

divider : <li><hr class="dropdown-divider"></hr></li>

<div class="dropdown dropend">

<div class="dropdown dropstart">

<div class="dropdown-menu dropdown-menu-end">

<div class="dropup">

<li><span class="dropdown-item-text">Just Text</span></li>

<div class="btn-group">
    <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">Sony</button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Tablet</a></li>
      <li><a class="dropdown-item" href="#">Smartphone</a></li>
    </ul>
  </div>
</div>
'''