from mui import (
    nav,
    ol,
    li,
    a
)

class DefaultBreadcrumb:
    def __init__(self,url_path_dict=None):
        self.url_path_dict = url_path_dict if url_path_dict is not None else {}
        
    def render(self,):
        breadcrumb = nav(
            ol(
                *[li(a(k, href=f'{v}', ),Class='breadcrumb-item', aria_current="page") for k,v in self.url_path_dict.items()],
                Class='breadcrumb'
            ),
            aria_label="breadcrumb",
        )
        return breadcrumb