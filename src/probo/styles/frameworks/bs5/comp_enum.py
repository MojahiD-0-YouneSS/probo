from enum import Enum
from probo.styles.frameworks.bs5.utilities import Breakpoint, Color


class ProgressBar(Enum):
    PROGRESS = "progress"  # Container for progress bar
    PROGRESS_BAR = "progress-bar"  # Actual progress bar
    PROGRESS_BAR_STRIPED = "progress-bar-striped"  # Adds stripes
    PROGRESS_BAR_ANIMATED = "progress-bar-animated"

class Spinner(Enum):
    SPINNER_BORDER = "spinner-border"  # Default border spinner
    SPINNER_BORDER_SM = "spinner-border spinner-border-sm"  # Small border spinner
    SPINNER_GROW = "spinner-grow"  # Growing spinner
    SPINNER_GROW_SM = "spinner-grow spinner-grow-sm"  # Small growing spinner

class Pagination(Enum):
    PAGINATION = "pagination"  # Pagination container
    PAGINATION_LG = "pagination-lg"  # Large pagination
    PAGINATION_SM = "pagination-sm"  # Small pagination

    PAGE_ITEM = "page-item"  # Wrapper for each page link
    PAGE_LINK = "page-link"  # Actual page link

class Accordion(Enum):
    BASE = "accordion"
    ITEM = "accordion-item"
    HEADER = "accordion-header"
    BUTTON = "accordion-button"
    COLLAPSE = "accordion-collapse"
    FLUSH = "accordion-flush"
    BODY = "accordion-body"

class Alert(Enum):
    BASE = "alert"
    PRIMARY = "alert-primary"
    SECONDARY = "alert-secondary"
    SUCCESS = "alert-success"
    INFO = "alert-info"
    WARNING = "alert-warning"
    DANGER = "alert-danger"
    LIGHT = "alert-light"
    DARK = "alert-dark"
    DISMISSIBLE = "alert-dismissible"
    LINK = "alert-link"
    HEADING = "alert-heading"  # Adds heading to alert

class Badge(Enum):
    BASE = "badge"
    PRIMARY = "badge-primary"
    SECONDARY = "badge-secondary"
    SUCCESS = "badge-success"
    INFO = "badge-info"
    WARNING = "badge-warning"
    DANGER = "badge-danger"
    LIGHT = "badge-light"
    DARK = "badge-dark"

class Lists(Enum):
    """
    Bootstrap Lists classes.
    These are used for styling lists.
    """

    UNSTYLED = "list-unstyled"  # Unordered list without bullets
    INLINE = "list-inline"  # Inline ordered list
    INLINE_ITEM = "list-inline-item"  # Inline list item
    LIST_GROUP = "list-group"  # Main list group container
    LIST_GROUP_ITEM = "list-group-item"  # Basic list group item

    LIST_GROUP_ITEM_ACTIVE = "list-group-item active"  # Active list group item
    LIST_GROUP_ITEM_DISABLED = "list-group-item disabled"  # Disabled list group item

    LIST_GROUP_ITEM_ACTION = "list-group-item list-group-item-action"  # Actionable list group item (links or buttons)

    LIST_GROUP_FLUSH = (
        "list-group-flush"  # Flush list group (no borders and rounded corners)
    )

    LIST_GROUP_HORIZONTAL = (
        "list-group-horizontal"  # Horizontal list group (default breakpoint)
    )
    LIST_GROUP_HORIZONTAL_SM = "list-group-horizontal-sm"  # Horizontal on small devices
    LIST_GROUP_HORIZONTAL_MD = (
        "list-group-horizontal-md"  # Horizontal on medium devices
    )
    LIST_GROUP_HORIZONTAL_LG = "list-group-horizontal-lg"  # Horizontal on large devices
    LIST_GROUP_HORIZONTAL_XL = (
        "list-group-horizontal-xl"  # Horizontal on extra large devices
    )
    LIST_GROUP_HORIZONTAL_XXL = "list-group-horizontal-xxl"  # Horizontal on XXL devices

    LIST_GROUP_ITEM_PRIMARY = "list-group-item-primary"  # Contextual color variants
    LIST_GROUP_ITEM_SECONDARY = "list-group-item-secondary"
    LIST_GROUP_ITEM_SUCCESS = "list-group-item-success"
    LIST_GROUP_ITEM_DANGER = "list-group-item-danger"
    LIST_GROUP_ITEM_WARNING = "list-group-item-warning"
    LIST_GROUP_ITEM_INFO = "list-group-item-info"
    LIST_GROUP_ITEM_LIGHT = "list-group-item-light"
    LIST_GROUP_ITEM_DARK = "list-group-item-dark"

class Cards(Enum):
    CARD = "card"  # Card container
    CARD_BODY = "card-body"  # Card body container
    CARD_TITLE = "card-title"  # Card title
    CARD_SUBTITLE = "card-subtitle"  # Card subtitle
    CARD_TEXT = "card-text"  # Card text content
    CARD_LINK = "card-link"  # Card link
    CARD_HEADER = "card-header"  # Card header section
    CARD_FOOTER = "card-footer"  # Card footer section
    CARD_IMG_TOP = "card-img-top"  # Image at top of card
    CARD_IMG_BOTTOM = "card-img-bottom"  # Image at bottom of card
    CARD_IMG = "card-img"  # Image inside card (not top or bottom)
    CARD_GROUP = "card-group"  # Group multiple cards together
    CARD_DECK = "card-deck"  # Deprecated in Bootstrap 5, was used for card decks
    CARD_COLUMNS = (
        "card-columns"  # Deprecated in Bootstrap 5, was used for card columns
    )
    CARD_BODY_TEXT = "card-body text-center"  # Centered text in card body
    CARD_IMG_OVERLAY = "card-img-overlay"  # Overlay text on top of an image in the card
    CARD_ROUNDED = "rounded"  # Rounded corners for card image or card
    CARD_SHADOW = "shadow"  # Add shadow to the card

class Dropdowns(Enum):
    DROPDOWN = "dropdown"  # Dropdown container
    DROPDOWN_TOGGLE = "dropdown-toggle"  # Toggle button for dropdown
    DROPDOWN_MENU = "dropdown-menu"  # Dropdown menu container
    DROPDOWN_ITEM = "dropdown-item"  # Dropdown menu item
    DROPDOWN_DIVIDER = "dropdown-divider"  # Divider line in dropdown menu
    DROPDOWN_HEADER = "dropdown-header"  # Header text in dropdown menu
    DROPDOWN_MENURIGHT = "dropdown-menu-end"  # Align dropdown menu to right
    DROPDOWN_SHOW = "show"  # Show dropdown menu (used to toggle visibility)
    DROPDOWN_ITEM_ACTIVE = "active"  # Active dropdown item
    DROPDOWN_ITEM_DISABLED = "disabled"  # Disabled dropdown item
    DROPDOWN_SM = "dropdown-menu-sm"  # Small dropdown menu size
    DROPDOWN_LG = "dropdown-menu-lg"  # Large dropdown menu size
    DROPDOWN_XL = "dropdown-menu-xl"  # Extra large dropdown menu size

class Collapse(Enum):
    COLLAPSE = "collapse"  # Collapse container (hidden content)
    COLLAPSE_SHOW = "show"  # Show collapsed content
    COLLAPSE_HORIZONTAL = "collapse-horizontal"  # Horizontal collapse
    COLLAPSE_MULTI = "multi-collapse"  # Accordion collapse container
   
class Nav(Enum):
    NAV = "nav"  # Base nav component
    NAV_ITEM = "nav-item"  # Nav item container
    NAV_LINK = "nav-link"  # Nav link
    NAV_LINK_ACTIVE = "nav-link active"  # Active nav link
    NAV_FILL = "nav-fill"  # Nav fills the width
    NAV_JUSTIFYIED = "nav-justified"  # Nav justified
    NAV_TABS = "nav-tabs"  # Tabs style navigation
    NAV_PILLS = "nav-pills"  # Pills style navigation
    TAB_CONTENT = "tab-content"  # Container for tab content
    TAB_PANE = "tab-pane"  # Single tab content pane
    TAB_PANE_ACTIVE = "tab-pane active"  # Active tab pane

class Navbar(Enum):
    NAVBAR = "navbar"  # Base navbar component
    NAVBAR_BRAND = "navbar-brand"  # Navbar brand/logo
    NAVBAR_NAV = "navbar-nav"  # Container for navigation links
    NAV_ITEM = "nav-item"  # Individual nav item
    NAV_LINK = "nav-link"  # Navigation link
    NAV_LINK_ACTIVE = "nav-link active"  # Active navigation link
    NAVBAR_TOGGLER = "navbar-toggler"  # Navbar toggle button (for collapsible)
    NAVBAR_COLLAPSE = "navbar-collapse"  # Collapsible navbar content
    NAVBAR_EXPAND = "navbar-expand"  # Responsive expand (auto)
    NAVBAR_EXPAND_SM = "navbar-expand-sm"  # Expand navbar on small screens and up
    NAVBAR_EXPAND_MD = "navbar-expand-md"  # Expand navbar on medium screens and up
    NAVBAR_EXPAND_LG = "navbar-expand-lg"  # Expand navbar on large screens and up
    NAVBAR_EXPAND_XL = "navbar-expand-xl"  # Expand navbar on extra-large screens and up
    NAVBAR_EXPAND_XXL = (
        "navbar-expand-xxl"  # Expand navbar on extra-extra-large screens and up
    )
    NAVBAR_LIGHT = "navbar-light"  # Light color scheme for navbar
    NAVBAR_DARK = "navbar-dark"  # Dark color scheme for navbar

class Carousel(Enum):
    CAROUSEL = "carousel"  # Base carousel container
    CAROUSEL_SLIDE = "slide"  # Carousel with slide animation
    CAROUSEL_FADE = "carousel-fade"  # Carousel with fade animation
    CAROUSEL_INNER = "carousel-inner"  # Wrapper for carousel items
    CAROUSEL_ITEM = "carousel-item"  # Active carousel item
    CAROUSEL_DARK = "carousel-dark"  #dark carousel
    CAROUSEL_CONTROL_PREV = "carousel-control-prev"  # Previous control
    CAROUSEL_CONTROL_NEXT = "carousel-control-next"  # Next control
    CAROUSEL_CONTROL_PREV_ICON = "carousel-control-prev-icon"  # Previous icon
    CAROUSEL_CONTROL_NEXT_ICON = "carousel-control-next-icon"  # Next icon
    CAROUSEL_INDICATORS = "carousel-indicators"  # Carousel indicators container
    CAROUSEL_INDICATOR = "carousel-indicator"  # Individual indicator (usually a button)

class Modal(Enum):
    MODAL = "modal"  # Modal container
    MODAL_DIALOG = "modal-dialog"  # Modal dialog wrapper
    MODAL_CONTENT = "modal-content"  # Modal content wrapper
    MODAL_HEADER = "modal-header"  # Modal header section
    MODAL_TITLE = "modal-title"  # Modal title text
    MODAL_BODY = "modal-body"  # Modal body section
    MODAL_FOOTER = "modal-footer"  # Modal footer section
    MODAL_FADE = "modal fade"  #  Modal with fade effect
    MODAL_SHOW = "modal show"  # Modal shown state
    MODAL_BACKDROP = "modal-backdrop"  # Modal backdrop overlay
    BUTTON_CLOSE = "btn-close"  # Close button for modal

class Popover(Enum):
    POPOVER = "popover"  # Popover container
    POPOVER_HEADER = "popover-header"  # Popover header
    POPOVER_BODY = "popover-body"  # Popover body/content
    POPOVER_TOP = "popover bs-popover-top"  # Popover positioned on top
    POPOVER_BOTTOM = "popover bs-popover-bottom"  # Popover positioned at bottom
    POPOVER_LEFT = "popover bs-popover-start"  # Popover positioned on left/start
    POPOVER_RIGHT = "popover bs-popover-end"  # Popover positioned on right/end

class Toast(Enum):
    TOAST = "toast"  # Toast container
    TOAST_HEADER = "toast-header"  # Header section of toast
    TOAST_BODY = "toast-body"  # Body/content section of toast
    TOAST_CONTAINER = "toast-container"  # Container for toasts

class Scrollspy(Enum):
    SCROLLSPY = "scrollspy"  # Enable scrollspy behavior

class Offcanvas(Enum):
    OFFCANVAS = "offcanvas"  # Main offcanvas container
    OFFCANVAS_START = "offcanvas-start"  # Offcanvas from left side
    OFFCANVAS_END = "offcanvas-end"  # Offcanvas from right side
    OFFCANVAS_TOP = "offcanvas-top"  # Offcanvas from top
    OFFCANVAS_BOTTOM = "offcanvas-bottom"  # Offcanvas from bottom
    OFFCANVAS_HEADER = "offcanvas-header"  # Header of offcanvas
    OFFCANVAS_TITLE = "offcanvas-title"  # Title in header
    OFFCANVAS_BODY = "offcanvas-body"  # Body content of offcanvas

class DarkMode(Enum):
    BODY_DARK = "bg-dark text-white"
    BODY_LIGHT = "bg-light text-dark"
    BG_DARK = "bg-dark"
    BG_LIGHT = "bg-light"

    TEXT_WHITE = "text-white"
    TEXT_LIGHT = "text-light"
    TEXT_BODY = "text-body"
    TEXT_MUTED = "text-muted"
    TEXT_BLACK_50 = "text-black-50"
    TEXT_WHITE_50 = "text-white-50"

    LINK_LIGHT = "link-light"
    LINK_DARK = "link-dark"

    BTN_DARK = "btn-dark"
    BTN_LIGHT = "btn-light"

    TABLE_DARK = "table-dark"

    NAVBAR_DARK = "navbar-dark"
    NAVBAR_LIGHT = "navbar-light"

    BG_BODY = "bg-body"

    BG_TRANSPARENT = "bg-transparent"

    data_bs_theme = 'data-bs-theme="dark"'


class Table(Enum):
    """
    Bootstrap Table classes.
    These are used for styling tables.
    """

    STRIPED = "table-striped"  # Striped table rowsk
    BORDERED = "table-bordered"  # Bordered table
    BORDERLESS = "table-borderless"  # Borderless table
    HOVER = "table-hover"  # Hover effect on table rows
    RESPONSIVE = "table-responsive"  # Responsive table
    DARK = f"table-{Color.DARK.value}"  # Dark themed table
    LIGHT = f"table-{Color.LIGHT.value}"  # Light themed table
    PRIMARY = f"table-{Color.PRIMARY.value}"  # Primary themed table
    SECONDARY = f"table-{Color.SECONDARY.value}"  # Secondary themed table
    SUCCESS = f"table-{Color.SUCCESS.value}"  # Success themed table
    DANGER = f"table-{Color.DANGER.value}"  # Danger themed table
    WARNING = f"table-{Color.WARNING.value}"  # Warning themed table
    INFO = f"table-{Color.INFO.value}"  # Info themed table
    WHITE = f"table-{Color.WHITE.value}"  # White themed table
    MUTED = f"table-{Color.MUTED.value}"  # Muted themed table
    ACTIVE = "table-active"
    TABLE = "table"
    SM = f"table-{Breakpoint.SM.value}"
    MD = f"table-{Breakpoint.MD.value}"  #  table for large screens
    LG = f"table-{Breakpoint.LG.value}"  #  table for large screens
    XL = f"table-{Breakpoint.XL.value}"  #  table for extra large screens
    XXL = f"table-{Breakpoint.XXL.value}"  #  table for extra extra large screens
    RESPONSIVE_SM = f"table-responsive-{Breakpoint.SM.value}"  # Responsive table for small screens
    RESPONSIVE_MD = f"table-responsive-{Breakpoint.MD.value}"  # Responsive table for large screens
    RESPONSIVE_LG = f"table-responsive-{Breakpoint.LG.value}"  # Responsive table for large screens)
    RESPONSIVE_XL = f"table-responsive-{Breakpoint.XL.value}"  # Responsive table for extra large screens
    RESPONSIVE_XXL = f"table-responsive-{Breakpoint.XXL.value}"  # Responsive table for extra extra large screens
    CAPTION = "caption-top"
    TABLE_GROUP_DIVIDER = "table-group-divider"

class Breadcrumb(Enum):
    BASE = "breadcrumb"
    ITEM="breadcrumb-item"
class Components:
    PROGRESSBAR = ProgressBar
    SPINNER = Spinner
    PAGINATION = Pagination
    ACCORDION = Accordion
    ALERT = Alert
    LISTS = Lists
    CARDS = Cards
    DROPDOWNS = Dropdowns
    COLLAPSE = Collapse
    NAV = Nav
    NAVBAR = Navbar
    CAROUSEL = Carousel
    MODAL = Modal
    POPOVER = Popover
    TOAST = Toast
    SCROLLSPY = Scrollspy
    OFFCANVAS = Offcanvas
    DARKMODE = DarkMode
    TABLE = Table
    BADGE = Badge
    BREADCRUMB = Breadcrumb
    @property
    def values_as_list(self):
        vals = []
        vals.extend([x.value for x in self.PROGRESSBAR])
        vals.extend([x.value for x in self.SPINNER])
        vals.extend([x.value for x in self.PAGINATION])
        vals.extend([x.value for x in self.ACCORDION])
        vals.extend([x.value for x in self.ALERT])
        vals.extend([x.value for x in self.LISTS])
        vals.extend([x.value for x in self.CARDS])
        vals.extend([x.value for x in self.DROPDOWNS])
        vals.extend([x.value for x in self.COLLAPSE])
        vals.extend([x.value for x in self.NAV])
        vals.extend([x.value for x in self.NAVBAR])
        vals.extend([x.value for x in self.CAROUSEL])
        vals.extend([x.value for x in self.MODAL])
        vals.extend([x.value for x in self.POPOVER])
        vals.extend([x.value for x in self.TOAST])
        vals.extend([x.value for x in self.SCROLLSPY])
        vals.extend([x.value for x in self.OFFCANVAS])
        vals.extend([x.value for x in self.DARKMODE])
        vals.extend([x.value for x in self.TABLE])
        vals.extend([x.value for x in self.BADGE])
        vals.extend([x.value for x in self.BREADCRUMB])
        return vals
