from enum import Enum
from mui.styles.frameworks.bs5.utilities import Breakpoint, Color


class JavaScriptPlugins(Enum):
    Alerts='data-bs-dismiss="alert"'
    Buttons= 'data-bs-toggle="button"'
    Carousel= 'data-bs-ride="carousel", data-bs-slide, data-bs-slide-to, data-bs-interval'
    Collapse= 'data-bs-toggle="collapse", data-bs-target'
    Dropdowns= 'data-bs-toggle="dropdown"'
    Modals= 'data-bs-toggle="modal", data-bs-target, data-bs-backdrop, data-bs-keyboard'
    Offcanvas= 'data-bs-toggle="offcanvas", data-bs-target, data-bs-backdrop, data-bs-scroll'
    Popovers=' data-bs-toggle="popover", data-bs-trigger, data-bs-placement, data-bs-content, data-bs-animation'
    Scrollspy= 'data-bs-spy="scroll", data-bs-target, data-bs-offset'
    Toasts= 'data-bs-autohide, data-bs-delay'
    Tooltips=' data-bs-toggle="tooltip", data-bs-placement=[top|right|bottom|left], data-bs-trigger, data-bs-animation'

class RTL(Enum):
    RTL= '.rtl'

class Extend:
    java_script_plugin = JavaScriptPlugins
    rtl = RTL
    @property
    def values_as_list(self):
        vals = []
        vals.extend([x.value for x in self.java_script_plugin])
        vals.extend([x.value for x in self.rtl])
        return vals