from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.bs5 import BS5Element
from probo.styles.frameworks.bs5.comp_enum import Accordion

class BS5Accordion(BS5Component):
    """A high-level component for generating Bootstrap 5 Accordions.

    This class automates the creation of multi-item collapsible containers. 
    It manages the generation of unique IDs for parent-child relationships, 
    ensuring that clicking a header correctly toggles the corresponding body 
    without affecting other items.

    Attributes:
        items (list): A collection of dictionaries containing the header 
            and body data for each accordion segment.
    """
    def __init__(self,*accordion_items,variant='base',render_constraints=None,**attrs):
        self.attrs = attrs
        self.tag='div'
        self.accordion_classes = [Accordion.BASE.value,(Accordion.FLUSH.value if variant == "flush" else ''),]
        self.variant = variant
        self.accordion_items = list(accordion_items)
        self.render_constraints=render_constraints

        super().__init__(name='BS5-accordion', state_props=self.render_constraints)

    def add_accordion_item(self,accordion_header:str,header_id:str,accordion_body:str,body_id:str):
        """Registers a new item to be rendered within the accordion.

        Args:
            accordion_header (str): The text or HTML to display in the 
                clickable header button.
            header_id (str): The unique HTML ID for the header element.
            accordion_body (str): The HTML content to display when expanded.
            body_id (str): The unique HTML ID for the collapsible body container.

        Returns:
            self: Enables fluent method chaining.
        """
        item =  BS5Element(
           'div',
          classes=[Accordion.ITEM.value]
        ) 
        item_header = BS5Element(
               'h2',
               BS5Element(
                   'button',
                   accordion_header,
                   classes=[Accordion.BUTTON.value],
                     **{
                          'type':'button',
                          'data-bs-toggle':'collapse',
                          'data-bs-target':f'#{body_id}',
                          'aria-expanded':'false',
                          'aria-controls':f'{body_id}',
                     }
               ),
               classes=[Accordion.HEADER.value],
               Id=header_id,
        )
        item_body = BS5Element(
               'div',
               BS5Element(
                   'div',
                   accordion_body,
                   classes=[Accordion.BODY.value]
               ),
               classes=[Accordion.COLLAPSE.value,'collapse'],
               Id=body_id,
               **{
                    'data-bs-parent':f'#{self.attrs.get("Id", "")}',
                    'aria-labelledby':header_id,
               }
        )
        item.include(item_header,item_body)
        self.accordion_items.append(item.render())
        return self

    def before_render(self,*args,**kwargs):
        self.include_content_parts(*self.accordion_items)
        return self

    def _render_comp(self):
        btn_grp = BS5Element(
            self.tag,
            ''.join(self.accordion_items),
            classes=self.accordion_classes,**self.attrs
        )
        return btn_grp
