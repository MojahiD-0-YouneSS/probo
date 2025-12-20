from mui import (
    div,
    a,
    button,
    p,
)

class DefaultCollapse:
    def __init__(self, Type='base', **kwargs) -> None:
        self.Type=Type
        self.contents=kwargs.get('collapse-contents',{})
        self.attrs=kwargs.get('collapse-attrs',{})
    def __base(self,):
        '''
        <p>
            <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
                Link with href
            </a>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                Button with data-bs-target
            </button>
        </p>
        <div class="collapse" id="collapseExample">
            <div class="card card-body">
                Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
            </div>
        </div>
        '''
        button_sction = p(
            a(
                'Link with href',
                Class="btn btn-primary", 
                data_bs_toggle="collapse",
                href="#collapseExample",
                role="button",
                aria_expanded="false",
                aria_controls="collapseExample"
            ),
            button(
                'Button with data-bs-target',
                Class="btn btn-primary",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target="#collapseExample",
                aria_expanded="false",
                aria_controls="collapseExample",
            )
        )
        collapse = div(
            div(
            'Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.',
            Class="card card-body",
            ),
            Class="collapse", id="collapseExample"
        )
        return button_sction + collapse
    
    def __multiple_targets(self,):
        '''
        <p>
            <a class="btn btn-primary" data-bs-toggle="collapse" href="#multiCollapseExample1" role="button" aria-expanded="false" aria-controls="multiCollapseExample1">Toggle first element</a>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample2" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target=".multi-collapse" aria-expanded="false" aria-controls="multiCollapseExample1 multiCollapseExample2">Toggle both elements</button>
        </p>
        <div class="row">
            <div class="col">
                <div class="collapse multi-collapse" id="multiCollapseExample1">
                <div class="card card-body">
                    Some placeholder content for the first collapse component of this multi-collapse example. This panel is hidden by default but revealed when the user activates the relevant trigger.
                </div>
                </div>
            </div>
            <div class="col">
                <div class="collapse multi-collapse" id="multiCollapseExample2">
                <div class="card card-body">
                    Some placeholder content for the second collapse component of this multi-collapse example. This panel is hidden by default but revealed when the user activates the relevant trigger.
                </div>
                </div>
            </div>
        </div>
        '''
        btns = p(
            a(
                'Toggle first element',
                Class="btn btn-primary",
                data_bs_toggle="collapse",
                href="#multiCollapseExample1",
                role="button",
                aria_expanded="false",
                aria_controls="multiCollapseExample1",
            ),
            button(
                'Toggle second element',
                Class="btn btn-primary",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target="#multiCollapseExample2",
                aria_expanded="false",
                aria_controls="multiCollapseExample2",
            ),
            button(
                'Toggle both elements',
                Class="btn btn-primary",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=".multi-collapse",
                aria_expanded="false",
                aria_controls="multiCollapseExample2",
            )
        )
        collapse = div(
            div(
                div(
                    div(
                        'Some placeholder content for the first collapse component of this multi-collapse example. This panel is hidden by default but revealed when the user activates the relevant trigger.',
                   Class="card card-body"
                    ),
                    Class="collapse multi-collapse",
                    Id="multiCollapseExample1",
                ),
                Class="col"
            ),
            div(
                div(
                    div(
                        'Some placeholder content for the first collapse component of this multi-collapse example. This panel is hidden by default but revealed when the user activates the relevant trigger.',
                   Class="card card-body"
                    ),
                    Class="collapse multi-collapse",
                    Id="multiCollapseExample2",
                ),
                Class="col"
            ),Class="row"
        )
        return btns + collapse
    
    def render(self,):
        if self.Type == 'base':
          return self.__base()
        else:
          return self.__multiple_targets()
