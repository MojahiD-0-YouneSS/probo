from enum import Enum


class Breakpoint(Enum):
    XS = "xs"
    SM = "sm"
    MD = "md"
    LG = "lg"
    XL = "xl"
    XXL = "xxl"

    @classmethod
    def get(cls, name):
        try:
            return cls[name]
        except KeyError:
            return None


class Tooltip(Enum):
    TOOLTIP = "tooltip"  # Tooltip container
    TOOLTIP_TOP = "tooltip bs-tooltip-top"  # Tooltip positioned on top
    TOOLTIP_BOTTOM = "tooltip bs-tooltip-bottom"  # Tooltip positioned at bottom
    TOOLTIP_LEFT = "tooltip bs-tooltip-start"  # Tooltip positioned on the left/start
    TOOLTIP_RIGHT = "tooltip bs-tooltip-end"  # Tooltip positioned on the right/end
    TOOLTIP_ARROW = "tooltip-arrow"  # Tooltip arrow element
    TOOLTIP_INNER = "tooltip-inner"  # Tooltip inner content


class Flex(Enum):
    FLEX = "d-flex"
    INLINE_FLEX = "d-inline-flex"
    FLEX_ROW = "flex-row"
    FLEX_ROW_REVERSE = "flex-row-reverse"
    FLEX_COLUMN = "flex-column"
    FLEX_COLUMN_REVERSE = "flex-column-reverse"
    FLEX_WRAP = "flex-wrap"
    FLEX_NOWRAP = "flex-nowrap"
    FLEX_WRAP_REVERSE = "flex-wrap-reverse"
    FLEX_GROW_0 = "flex-grow-0"
    FLEX_GROW_1 = "flex-grow-1"
    FLEX_SHRINK_0 = "flex-shrink-0"
    FLEX_SHRINK_1 = "flex-shrink-1"
    FLEX_BASIS_AUTO = "flex-basis-auto"
    FLEX_BASIS_0 = "flex-basis-0"


class Order(Enum):
    ORDER_FIRST = "order-first"
    ORDER_LAST = "order-last"
    ORDER_0 = "order-0"
    ORDER_1 = "order-1"
    ORDER_2 = "order-2"
    ORDER_3 = "order-3"
    ORDER_4 = "order-4"
    ORDER_5 = "order-5"
    ORDER_6 = "order-6"
    ORDER_7 = "order-7"
    ORDER_8 = "order-8"
    ORDER_9 = "order-9"
    ORDER_10 = "order-10"
    ORDER_11 = "order-11"
    ORDER_12 = "order-12"


class ZIndex(Enum):
    DROPDOWN = "zindex-dropdown"
    STICKY = "zindex-sticky"
    FIXED = "zindex-fixed"
    OFFCANVAS_BACKDROP = "zindex-offcanvas-backdrop"
    OFFCANVAS = "zindex-offcanvas"
    MODAL_BACKDROP = "zindex-modal-backdrop"
    MODAL = "zindex-modal"
    POPOVER = "zindex-popover"
    TOOLTIP = "zindex-tooltip"
    AUTO = "z-auto"
    N1 = "z-n1"

    @classmethod
    def get(cls, name):
        try:
            return cls[name]
        except KeyError:
            return None


class Offset(Enum):
    """Bootstrap offset classes for grid columns.

    Provides offset classes to create space between columns in Bootstrap's grid system.
    Supports responsive offsets for all breakpoints.
    """

    # Base offsets
    OFFSET_1 = "offset-1"
    OFFSET_2 = "offset-2"
    OFFSET_3 = "offset-3"
    OFFSET_4 = "offset-4"
    OFFSET_5 = "offset-5"
    OFFSET_6 = "offset-6"
    OFFSET_7 = "offset-7"
    OFFSET_8 = "offset-8"
    OFFSET_9 = "offset-9"
    OFFSET_10 = "offset-10"
    OFFSET_11 = "offset-11"

    # Responsive offsets - SM
    SM_OFFSET_1 = "offset-sm-1"
    SM_OFFSET_2 = "offset-sm-2"
    SM_OFFSET_3 = "offset-sm-3"
    SM_OFFSET_4 = "offset-sm-4"
    SM_OFFSET_5 = "offset-sm-5"
    SM_OFFSET_6 = "offset-sm-6"
    SM_OFFSET_7 = "offset-sm-7"
    SM_OFFSET_8 = "offset-sm-8"
    SM_OFFSET_9 = "offset-sm-9"
    SM_OFFSET_10 = "offset-sm-10"
    SM_OFFSET_11 = "offset-sm-11"

    # Responsive offsets - MD
    MD_OFFSET_1 = "offset-md-1"
    MD_OFFSET_2 = "offset-md-2"
    MD_OFFSET_3 = "offset-md-3"
    MD_OFFSET_4 = "offset-md-4"
    MD_OFFSET_5 = "offset-md-5"
    MD_OFFSET_6 = "offset-md-6"
    MD_OFFSET_7 = "offset-md-7"
    MD_OFFSET_8 = "offset-md-8"
    MD_OFFSET_9 = "offset-md-9"
    MD_OFFSET_10 = "offset-md-10"
    MD_OFFSET_11 = "offset-md-11"

    # Responsive offsets - LG
    LG_OFFSET_1 = "offset-lg-1"
    LG_OFFSET_2 = "offset-lg-2"
    LG_OFFSET_3 = "offset-lg-3"
    LG_OFFSET_4 = "offset-lg-4"
    LG_OFFSET_5 = "offset-lg-5"
    LG_OFFSET_6 = "offset-lg-6"
    LG_OFFSET_7 = "offset-lg-7"
    LG_OFFSET_8 = "offset-lg-8"
    LG_OFFSET_9 = "offset-lg-9"
    LG_OFFSET_10 = "offset-lg-10"
    LG_OFFSET_11 = "offset-lg-11"

    # Responsive offsets - XL
    XL_OFFSET_1 = "offset-xl-1"
    XL_OFFSET_2 = "offset-xl-2"
    XL_OFFSET_3 = "offset-xl-3"
    XL_OFFSET_4 = "offset-xl-4"
    XL_OFFSET_5 = "offset-xl-5"
    XL_OFFSET_6 = "offset-xl-6"
    XL_OFFSET_7 = "offset-xl-7"
    XL_OFFSET_8 = "offset-xl-8"
    XL_OFFSET_9 = "offset-xl-9"
    XL_OFFSET_10 = "offset-xl-10"
    XL_OFFSET_11 = "offset-xl-11"

    # Responsive offsets - XXL
    XXL_OFFSET_1 = "offset-xxl-1"
    XXL_OFFSET_2 = "offset-xxl-2"
    XXL_OFFSET_3 = "offset-xxl-3"
    XXL_OFFSET_4 = "offset-xxl-4"
    XXL_OFFSET_5 = "offset-xxl-5"
    XXL_OFFSET_6 = "offset-xxl-6"
    XXL_OFFSET_7 = "offset-xxl-7"
    XXL_OFFSET_8 = "offset-xxl-8"
    XXL_OFFSET_9 = "offset-xxl-9"
    XXL_OFFSET_10 = "offset-xxl-10"
    XXL_OFFSET_11 = "offset-xxl-11"


class Font(Enum):
    """
    Bootstrap Inline Text Elements classes.
    These are used for inline text formatting.
    """

    BOLD = "fw-bold"  # Strong emphasis (bold)
    NORMAL_FW = "fw-normal"  # Emphasis (italic)
    NORMAL_FST = "fst-normal"  # Emphasis (italic)
    ITALIC = "fst-italic"  # Italic text
    SMALL = "small"  # Smaller text
    SUBSCRIPT = "sub"  # Subscript text
    SUPERSCRIPT = "sup"  # Superscript text
    MARK = "mark"


class Background(Enum):
    """Bootstrap Background colors."""

    PRIMARY = "bg-primary"
    SECONDARY = "bg-secondary"
    SUCCESS = "bg-success"
    DANGER = "bg-danger"
    WARNING = "bg-warning"
    INFO = "bg-info"
    LIGHT = "bg-light"
    DARK = "bg-dark"
    WHITE = "bg-white"
    TRANSPARENT = "bg-transparent"
    BODY = "bg-body"


class Spacing(Enum):
    """Bootstrap Spacing utilities (margin and padding)."""

    PX1 = "px-1"  # Padding on X-axis
    PX2 = "px-2"  # Padding on X-axis
    PX3 = "px-3"  # Padding on X-axis
    PX4 = "px-4"  # Padding on X-axis
    PX5 = "px-5"  # Padding on X-axis

    PY1 = "py-1"  # Padding on Y-axis
    PY2 = "py-2"  # Padding on Y-axis
    PY3 = "py-3"  # Padding on Y-axis
    PY4 = "py-4"  # Padding on Y-axis
    PY5 = "py-5"  # Padding on Y-axis

    PT1 = "pt-1"  # Padding Top
    PT2 = "pt-2"  # Padding Top
    PT3 = "pt-3"  # Padding Top
    PT4 = "pt-4"  # Padding Top
    PT5 = "pt-5"  # Padding Top

    PB1 = "pb-1"  # Padding Bottom
    PB2 = "pb-2"  # Padding Bottom
    PB3 = "pb-3"  # Padding Bottom
    PB4 = "pb-4"  # Padding Bottom
    PB5 = "pb-5"  # Padding Bottom

    PS1 = "ps-1"  # Padding Start (left in LTR)
    PS2 = "ps-2"  # Padding Start (left in LTR)
    PS3 = "ps-3"  # Padding Start (left in LTR)
    PS4 = "ps-4"  # Padding Start (left in LTR)
    PS5 = "ps-5"  # Padding Start (left in LTR)

    PE1 = "pe-1"  # Padding End (right in LTR)
    PE2 = "pe-2"  # Padding End (right in LTR)
    PE3 = "pe-3"  # Padding End (right in LTR)
    PE4 = "pe-4"  # Padding End (right in LTR)
    PE5 = "pe-5"  # Padding End (right in LTR)

    P1 = "p-1"  # Padding all sides
    P2 = "p-2"  # Padding all sides
    P3 = "p-3"  # Padding all sides
    P4 = "p-4"  # Padding all sides
    P5 = "p-5"  # Padding all sides

    MX1 = "mx-1"  # Margin on X-axis
    MX2 = "mx-2"  # Margin on X-axis
    MX3 = "mx-3"  # Margin on X-axis
    MX4 = "mx-4"  # Margin on X-axis
    MX5 = "mx-5"  # Margin on X-axis

    MY1 = "my-1"  # Margin on Y-axis
    MY2 = "my-2"  # Margin on Y-axis
    MY3 = "my-3"  # Margin on Y-axis
    MY4 = "my-4"  # Margin on Y-axis
    MY5 = "my-5"  # Margin on Y-axis

    MT1 = "mt-1"  # Margin Top
    MT2 = "mt-2"  # Margin Top
    MT3 = "mt-3"  # Margin Top
    MT4 = "mt-4"  # Margin Top
    MT5 = "mt-5"  # Margin Top

    MB1 = "mb-1"  # Margin Bottom
    MB2 = "mb-2"  # Margin Bottom
    MB3 = "mb-3"  # Margin Bottom
    MB4 = "mb-4"  # Margin Bottom
    MB5 = "mb-5"  # Margin Bottom

    MS1 = "ms-1"  # Margin Start (left in LTR)
    MS2 = "ms-2"  # Margin Start (left in LTR)
    MS3 = "ms-3"  # Margin Start (left in LTR)
    MS4 = "ms-4"  # Margin Start (left in LTR)
    MS5 = "ms-5"  # Margin Start (left in LTR)

    ME1 = "me-1"  # Margin End (right in LTR)
    ME2 = "me-2"  # Margin End (right in LTR)
    ME3 = "me-3"  # Margin End (right in LTR)
    ME4 = "me-4"  # Margin End (right in LTR)
    ME5 = "me-5"  # Margin End (right in LTR)

    M1 = "m-1"  # Margin all sides
    M2 = "m-2"  # Margin all sides
    M3 = "m-3"  # Margin all sides
    M4 = "m-4"  # Margin all sides
    M5 = "m-5"  # Margin all sides

    GAP1 = "gap-1"
    GAP2 = "gap-2"
    GAP3 = "gap-3"
    GAP4 = "gap-4"
    GAP5 = "gap-5"

    AUTO_MX = "mx-auto"  # Center horizontally


class Display(Enum):
    """Bootstrap Display utilities."""

    NONE = "d-none"
    INLINE = "d-inline"
    INLINE_BLOCK = "d-inline-block"
    BLOCK = "d-block"
    GRID = "d-grid"
    FLEX = "d-flex"
    TABLE = "d-table"
    # Responsive display
    SM_BLOCK = f"d-{Breakpoint.SM.value}-block"
    MD_BLOCK = f"d-{Breakpoint.MD.value}-block"
    LG_BLOCK = f"d-{Breakpoint.LG.value}-block"
    XL_BLOCK = f"d-{Breakpoint.XL.value}-block"
    XXL_BLOCK = f"d-{Breakpoint.XXL.value}-block"

    SM_FLEX = f"d-{Breakpoint.SM.value}-flex"
    MD_FLEX = f"d-{Breakpoint.MD.value}-flex"
    LG_FLEX = f"d-{Breakpoint.LG.value}-flex"
    XL_FLEX = f"d-{Breakpoint.XL.value}-flex"
    XXL_FLEX = f"d-{Breakpoint.XXL.value}-flex"

    SM_NONE = f"d-{Breakpoint.SM.value}-none"
    MD_NONE = f"d-{Breakpoint.MD.value}-none"
    LG_NONE = f"d-{Breakpoint.LG.value}-none"
    XL_NONE = f"d-{Breakpoint.XL.value}-none"
    XXL_NONE = f"d-{Breakpoint.XXL.value}-none"
    # ... and so on for other breakpoints and display types


class Color(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"
    LIGHT = "light"
    DARK = "dark"
    WHITE = "white"
    WHITE_50 = "white-50"
    BLACK_50 = "-50"
    MUTED = "muted"
    BODY = "body"
    TRANSPARENT = "transparent"


class JustifyContent(Enum):
    START = "justify-content-start"
    END = "justify-content-end"
    CENTER = "justify-content-center"
    BETWEEN = "justify-content-between"
    AROUND = "justify-content-around"
    EVENLY = "justify-content-evenly"


class AlignItems(Enum):
    START = "align-items-start"
    END = "align-items-end"
    CENTER = "align-items-center"
    BASELINE = "align-items-baseline"
    STRETCH = "align-items-stretch"


class AlignSelf(Enum):
    AUTO = "align-self-auto"
    START = "align-self-start"
    END = "align-self-end"
    CENTER = "align-self-center"
    BASELINE = "align-self-baseline"
    STRETCH = "align-self-stretch"


class AlignContent(Enum):
    START = "align-content-start"
    END = "align-content-end"
    CENTER = "align-content-center"
    BETWEEN = "align-content-between"
    AROUND = "align-content-around"
    STRETCH = "align-content-stretch"


class Rounded(Enum):
    BASE = "rounded"  # Applies border-radius for rounded corners
    TOP = "rounded-top"  # Top corners rounded
    BOTTOM = "rounded-bottom"  # Bottom corners rounded
    START = "rounded-start"  # Left/start side rounded
    END = "rounded-end"  # Right/end side rounded
    CIRCLE = "rounded-circle"  # Fully rounded (circle)
    PILL = "rounded-pill"  # Rounded like a pill


class Float(Enum):
    FLOAT_START = "float-start"  # Float image to the left
    FLOAT_END = "float-end"  # Float image to the right
    FLOAT_NONE = "float-none"


class Overflow(Enum):
    OVERFLOW_AUTO = "overflow-auto"
    OVERFLOW_HIDDEN = "overflow-hidden"
    OVERFLOW_VISIBLE = "overflow-visible"
    OVERFLOW_SCROLL = "overflow-scroll"


class Position(Enum):
    POSITION_STATIC = "position-static"
    POSITION_RELATIVE = "position-relative"
    POSITION_ABSOLUTE = "position-absolute"
    POSITION_FIXED = "position-fixed"
    POSITION_STICKY = "position-sticky"


class Top(Enum):
    TOP_0 = "top-0"
    TOP_50 = "top-50"
    TOP_AUTO = "top-auto"


class Bottom(Enum):
    BOTTOM_0 = "bottom-0"
    BOTTOM_50 = "bottom-50"
    BOTTOM_AUTO = "bottom-auto"


class Start(Enum):
    START_0 = "start-0"
    START_50 = "start-50"
    START_AUTO = "start-auto"


class End(Enum):
    END_0 = "end-0"
    END_50 = "end-50"
    END_AUTO = "end-auto"


class Visibility(Enum):
    VISUALLY_HIDDEN = "visually-hidden"
    VISUALLY_HIDDEN_FOCUSABLE = "visually-hidden-focusable"
    VISIBLE_SM = "visible-sm"
    VISIBLE_MD = "visible-md"
    VISIBLE_LG = "visible-lg"
    VISIBLE_XL = "visible-xl"
    VISIBLE_XXL = "visible-xxl"


class Shadow(Enum):
    SHADOW_NONE = "shadow-none"
    SHADOW_SM = "shadow-sm"
    SHADOW = "shadow"
    SHADOW_LG = "shadow-lg"


class UserSelect(Enum):
    USER_SELECT_AUTO = "user-select-auto"
    USER_SELECT_NONE = "user-select-none"


class Effect(Enum):
    CLEARFIX = "clearfix"
    SHOW = "show"  # Tooltip visible state
    FADE = "fade"  # Fade effect for toast
    HIDE = "hide"  # Hidden state of toast


class Icons(Enum):
    BASE = ".icon"
    ICON_VARIANT = ".icon-{variant}"
    ICON_SIZE = ".icon-{size}"
    ICON_COLORr = ".icon-{color}"
    ICON_POSITION = ".icon-{position}"
    ICON_ANIMATION = ".icon-{animation}"


class State(Enum):
    ACTIVE = "active"  # Active state
    DISABLED = "disabled"


class Width(Enum):
    W25 = "w-25"
    W50 = "w-50"
    W75 = "w-75"
    W100 = "w-100"
    WAUTO = "w-auto"


class Height(Enum):
    H25 = "h-25"
    H50 = "h-50"
    H75 = "h-75"
    H100 = "h-100"
    HAUTO = "h-auto"


class SpacingFunc:
    """Bootstrap Spacing utilities (margin and padding)."""

    @staticmethod
    def PX(self, value: int):
        return f"px-{value}"  # Padding on X-axis

    @staticmethod
    def PY(self, value: int):
        return f"py-{value}"  # Padding on Y-axis

    @staticmethod
    def PT(self, value: int):
        return f"pt-{value}"  # Padding Top

    @staticmethod
    def PB(self, value: int):
        return f"pb-{value}"  # Padding Bottom

    @staticmethod
    def PS(self, value: int):
        return f"ps-{value}"  # Padding Start (self,left in LTR)

    @staticmethod
    def PE(self, value: int):
        return f"pe-{value}"  # Padding End (self,right in LTR)

    @staticmethod
    def P(self, value: int):
        return f"p-{value}"  # Padding all sides

    @staticmethod
    def MX(self, value: int):
        return f"mx-{value}"  # Margin on X-axis

    @staticmethod
    def MY(self, value: int):
        return f"my-{value}"  # Margin on Y-axis

    @staticmethod
    def MT(self, value: int):
        return f"mt-{value}"  # Margin Top

    @staticmethod
    def MB(self, value: int):
        return f"mb-{value}"  # Margin Bottom

    @staticmethod
    def MS(self, value: int):
        return f"ms-{value}"  # Margin Start (self,left in LTR)

    @staticmethod
    def ME(self, value: int):
        return f"me-{value}"  # Margin End (self,right in LTR)

    @staticmethod
    def M(self, value: int):
        return f"m-{value}"  # Margin all sides

    @staticmethod
    def AUTO_MX(
        self,
    ):
        return "mx-auto"  # Center horizontally


class GridFunc:
    """Bootstrap Grid System classes."""

    @staticmethod
    def COL(self, value: int):
        return f"col-{value}"

    @staticmethod
    def COL_AUTO(
        self,
    ):
        return "col-auto"

    @staticmethod
    def COL_SM(self, value: int):
        return f"col-sm-{value}"

    @staticmethod
    def COL_MD(self, value: int):
        return f"col-md-{value}"

    @staticmethod
    def COL_LG(self, value: int):
        return f"col-lg-{value}"

    @staticmethod
    def ROW(
        self,
    ):
        return "row"

    @staticmethod
    def CONTAINER(
        self,
    ):
        return "container"

    @staticmethod
    def CONTAINER_FLUID(
        self,
    ):
        return "container-fluid"


class Utilities:
    BREAKPOINT = Breakpoint
    TOOLTIP = Tooltip
    FLEX = Flex
    ORDER = Order
    ZINDEX = ZIndex
    OFFSET = Offset
    FONT = Font
    BACKGROUND = Background
    SPACING = Spacing
    DISPLAY = Display
    COLOR = Color
    JUSTIFYCONTENT = JustifyContent
    ALIGNITEMS = AlignItems
    ALIENSELF = AlignSelf
    ALIENTCONTENT = AlignContent
    ROUNDED = Rounded
    FLOAT = Float
    OVERFLOW = Overflow
    POSITION = Position
    TOP = Top
    BOTTOM = Bottom
    START = Start
    END = End
    VISIBILITY = Visibility
    SHADOW = Shadow
    USERSELECT = UserSelect
    EFFECT = Effect
    STATE = State
    WIDTH = Width
    HEIGHT = Height

    @property
    def values_as_list(self):
        vals = []
        vals.extend([x.value for x in self.BREAKPOINT])
        vals.extend([x.value for x in self.TOOLTIP])
        vals.extend([x.value for x in self.FLEX])
        vals.extend([x.value for x in self.ORDER])
        vals.extend([x.value for x in self.ZINDEX])
        vals.extend([x.value for x in self.OFFSET])
        vals.extend([x.value for x in self.FONT])
        vals.extend([x.value for x in self.BACKGROUND])
        vals.extend([x.value for x in self.SPACING])
        vals.extend([x.value for x in self.DISPLAY])
        vals.extend([x.value for x in self.COLOR])
        vals.extend([x.value for x in self.JUSTIFYCONTENT])
        vals.extend([x.value for x in self.ALIGNITEMS])
        vals.extend([x.value for x in self.ALIENSELF])
        vals.extend([x.value for x in self.ALIENTCONTENT])
        vals.extend([x.value for x in self.ROUNDED])
        vals.extend([x.value for x in self.FLOAT])
        vals.extend([x.value for x in self.OVERFLOW])
        vals.extend([x.value for x in self.POSITION])
        vals.extend([x.value for x in self.TOP])
        vals.extend([x.value for x in self.BOTTOM])
        vals.extend([x.value for x in self.START])
        vals.extend([x.value for x in self.END])
        vals.extend([x.value for x in self.VISIBILITY])
        vals.extend([x.value for x in self.SHADOW])
        vals.extend([x.value for x in self.USERSELECT])
        vals.extend([x.value for x in self.EFFECT])
        vals.extend([x.value for x in self.STATE])
        vals.extend([x.value for x in self.WIDTH])
        vals.extend([x.value for x in self.HEIGHT])
        return vals
