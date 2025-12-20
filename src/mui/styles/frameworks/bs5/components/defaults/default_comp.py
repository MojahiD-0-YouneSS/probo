from enum import Enum
from mui.styles.frameworks.bs5.components.defaults.accordion import DefaultAccordion
from mui.styles.frameworks.bs5.components.defaults.alert import DefaultAlert
from mui.styles.frameworks.bs5.components.defaults.badge import DefaultBadge
from mui.styles.frameworks.bs5.components.defaults.breadcrumb import DefaultBreadcrumb
from mui.styles.frameworks.bs5.components.defaults.button import DefaultButton, DefaultButtonGroup,DefaultCloseButton
from mui.styles.frameworks.bs5.components.defaults.card import DefaultCard
from mui.styles.frameworks.bs5.components.defaults.carousel import DefaultCarousel
from mui.styles.frameworks.bs5.components.defaults.table import DefaultTable
from mui.styles.frameworks.bs5.components.defaults.collapse import DefaultCollapse
from mui.styles.frameworks.bs5.components.defaults.dropdowns import DefaultDropdown



class DefaultCompEnums(Enum):
    ACCORDION = DefaultAccordion
    ALERT = DefaultAlert
    BADGE = DefaultBadge
    BREADCRUMB = DefaultBreadcrumb 
    BUTTON = DefaultButton
    BUTTON_GROUP = DefaultButtonGroup
    CLOSE_BUTTON = DefaultCloseButton
    CARD = DefaultCard
    CAROUSEL=DefaultCarousel
    TABLE=DefaultTable
    COLLAPSE=DefaultCollapse
    DROPDOWN=DefaultDropdown