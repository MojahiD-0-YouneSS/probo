from probo.styles.frameworks.bs5.components.base import BS5Component
from probo.styles.frameworks.bs5.comp_enum import ProgressBar
from probo.styles.frameworks.bs5.bs5 import BS5Element

class BS5ProgressBar(BS5Component):
    def __init__(self, render_constraints=None,is_striped=False,is_animated=False, **attrs):
        self.render_constraints = render_constraints
        self.attrs = attrs
        self.is_striped = is_striped
        self.is_animated = is_animated
        self.tag = 'div'
        self.progress_bars = []
        self.progressbar_classes = [ProgressBar.PROGRESS.value]
        super().__init__(name='BS5-ProgressBar', state_props=self.render_constraints)

    def add_progress_bar(self,width,optional_content=None,**attr):

        progress_bar = BS5Element(
            self.tag,
            classes=[ProgressBar.PROGRESS_BAR.value,]
        )
        if self.is_striped:
            progress_bar.classes.append(ProgressBar.PROGRESS_BAR_STRIPED.value)
        if self.is_animated:
            progress_bar.classes.append(ProgressBar.PROGRESS_BAR_ANIMATED.value)
        if optional_content:
            progress_bar.include(optional_content)
        progress_bar.attr_manager.set_bulk_attr(
            role='progressbar',
            aria_valuenow=width,
            aria_valuemin=0,
            aria_valuemax=100,
            style=f'width:{width}%;',
        )
        progress_bar.attrs.update(**attr)
        self.progress_bars.append(progress_bar)
        return self
    def before_render(self, **props):
        self.include_content_parts(*self.progress_bars)

    def _render_comp(self,*args,**kwargs):
        progress = BS5Element(
            self.tag,
            classes=self.progressbar_classes,
            **self.attrs
        )
        return progress
