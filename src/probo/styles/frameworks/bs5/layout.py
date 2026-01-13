from enum import Enum
from dataclasses import dataclass
from probo.styles.frameworks.bs5.utilities import Breakpoint, Color


class Container(Enum):
    BASE = "container"
    SM = f"container-{Breakpoint.SM.value}"
    MD = f"container-{Breakpoint.MD.value}"
    LG = f"container-{Breakpoint.LG.value}"
    XL = f"container-{Breakpoint.XL.value}"
    XXL = f"container-{Breakpoint.XXL.value}"
    FLUID = "container-fluid"

    def __call__(self):
        return self.value

    @classmethod
    def get(
        cls,
        name=None,
    ):
        if not name:
            return cls.BASE
        try:
            return cls[name]
        except KeyError:
            return None


class Row(Enum):
    """Bootstrap Row utilities. Represents the row class for the Bootstrap grid system."""

    BASE = "row"
    SM = f"row-{Breakpoint.SM.value}"
    MD = f"row-{Breakpoint.MD.value}"
    LG = f"row-{Breakpoint.LG.value}"
    XL = f"row-{Breakpoint.XL.value}"
    XXL = f"row-{Breakpoint.XXL.value}"
    SM_COL_1 = f"row-cols-{Breakpoint.SM.value}-1"
    MD_COL_1 = f"row-cols-{Breakpoint.MD.value}-1"
    LG_COL_1 = f"row-cols-{Breakpoint.LG.value}-1"
    XL_COL_1 = f"row-cols-{Breakpoint.XL.value}-1"
    XXL_COL_1 = f"row-cols-{Breakpoint.XXL.value}-1"

    def __call__(self):
        return self.value

    @classmethod
    def get(
        cls,
        name=None,
    ):
        if not name:
            return cls.BASE
        try:
            return cls[name]
        except KeyError:
            return None


class Column(Enum):
    BASE = "col"

    col1 = "col-1"
    col2 = "col-2"
    col3 = "col-3"
    col4 = "col-4"
    col5 = "col-5"
    col6 = "col-6"
    col7 = "col-7"
    col8 = "col-8"
    col9 = "col-9"
    col10 = "col-10"
    col11 = "col-11"
    col12 = "col-12"

    SM = f"col-{Breakpoint.SM.value}"
    SM1 = f"col-{Breakpoint.SM.value}-1"
    SM2 = f"col-{Breakpoint.SM.value}-2"
    SM3 = f"col-{Breakpoint.SM.value}-3"
    SM4 = f"col-{Breakpoint.SM.value}-4"
    SM5 = f"col-{Breakpoint.SM.value}-5"
    SM6 = f"col-{Breakpoint.SM.value}-6"
    SM7 = f"col-{Breakpoint.SM.value}-7"
    SM8 = f"col-{Breakpoint.SM.value}-8"
    SM9 = f"col-{Breakpoint.SM.value}-9"
    SM10 = f"col-{Breakpoint.SM.value}-10"
    SM11 = f"col-{Breakpoint.SM.value}-11"
    SM12 = f"col-{Breakpoint.SM.value}-12"

    MD = f"col-{Breakpoint.MD.value}-1"
    MD1 = f"col-{Breakpoint.MD.value}-2"
    MD2 = f"col-{Breakpoint.MD.value}-3"
    MD3 = f"col-{Breakpoint.MD.value}-4"
    MD4 = f"col-{Breakpoint.MD.value}-5"
    MD5 = f"col-{Breakpoint.MD.value}-6"
    MD6 = f"col-{Breakpoint.MD.value}-7"
    MD7 = f"col-{Breakpoint.MD.value}-8"
    MD8 = f"col-{Breakpoint.MD.value}-9"
    MD9 = f"col-{Breakpoint.MD.value}-10"
    MD10 = f"col-{Breakpoint.MD.value}-11"
    MD11 = f"col-{Breakpoint.MD.value}-12"

    LG = f"col-{Breakpoint.LG.value}"
    LG1 = f"col-{Breakpoint.LG.value}-1"
    LG2 = f"col-{Breakpoint.LG.value}-2"
    LG3 = f"col-{Breakpoint.LG.value}-3"
    LG4 = f"col-{Breakpoint.LG.value}-4"
    LG5 = f"col-{Breakpoint.LG.value}-5"
    LG6 = f"col-{Breakpoint.LG.value}-6"
    LG7 = f"col-{Breakpoint.LG.value}-7"
    LG8 = f"col-{Breakpoint.LG.value}-8"
    LG9 = f"col-{Breakpoint.LG.value}-9"
    LG10 = f"col-{Breakpoint.LG.value}-10"
    LG11 = f"col-{Breakpoint.LG.value}-11"
    LG12 = f"col-{Breakpoint.LG.value}-12"

    XL = f"col-{Breakpoint.XL.value}"
    XL1 = f"col-{Breakpoint.XL.value}-1"
    XL2 = f"col-{Breakpoint.XL.value}-2"
    XL3 = f"col-{Breakpoint.XL.value}-3"
    XL4 = f"col-{Breakpoint.XL.value}-4"
    XL5 = f"col-{Breakpoint.XL.value}-5"
    XL6 = f"col-{Breakpoint.XL.value}-6"
    XL7 = f"col-{Breakpoint.XL.value}-7"
    XL8 = f"col-{Breakpoint.XL.value}-8"
    XL9 = f"col-{Breakpoint.XL.value}-9"
    XL10 = f"col-{Breakpoint.XL.value}-10"
    XL11 = f"col-{Breakpoint.XL.value}-11"
    XL12 = f"col-{Breakpoint.XL.value}-12"

    XXL = f"col-{Breakpoint.XXL.value}"
    XXL1 = f"col-{Breakpoint.XXL.value}-1"
    XXL2 = f"col-{Breakpoint.XXL.value}-2"
    XXL3 = f"col-{Breakpoint.XXL.value}-3"
    XXL4 = f"col-{Breakpoint.XXL.value}-4"
    XXL5 = f"col-{Breakpoint.XXL.value}-5"
    XXL6 = f"col-{Breakpoint.XXL.value}-6"
    XXL7 = f"col-{Breakpoint.XXL.value}-7"
    XXL8 = f"col-{Breakpoint.XXL.value}-8"
    XXL9 = f"col-{Breakpoint.XXL.value}-9"
    XXL10 = f"col-{Breakpoint.XXL.value}-10"
    XXL11 = f"col-{Breakpoint.XXL.value}-11"
    XXL12 = f"col-{Breakpoint.XXL.value}-12"

    AUTO = "col-auto"
    SM_AUTO = f"col-{Breakpoint.SM.value}-auto"
    MD_AUTO = f"col-{Breakpoint.MD.value}-auto"
    LG_AUTO = f"col-{Breakpoint.LG.value}-auto"
    XL_AUTO = f"col-{Breakpoint.XL.value}-auto"
    XXL_AUTO = f"col-{Breakpoint.XXL.value}-auto"

    FORM_LABEL = "col-form-label"
    FORM_LABEL_SM = f"col-form-label-{Breakpoint.SM.value}"
    FORM_LABEL_MD = f"col-form-label-{Breakpoint.MD.value}"
    FORM_LABEL_LG = f"col-form-label-{Breakpoint.LG.value}"
    FORM_LABEL_XL = f"col-form-label-{Breakpoint.XL.value}"
    FORM_LABEL_XXL = f"col-form-label-{Breakpoint.XXL.value}"

    def __call__(self):
        return self.value

    @classmethod
    def get(
        cls,
        name=None,
    ):
        if not name:
            return cls.BASE
        try:
            return cls[name]
        except KeyError:
            return None


class Gutter(Enum):
    G0 = "g-0"
    G1 = "g-1"
    G2 = "g-2"
    G3 = "g-3"
    G4 = "g-4"
    G5 = "g-5"

    SM0 = "g-sm-0"
    SM1 = "g-sm-1"
    SM2 = "g-sm-2"
    SM3 = "g-sm-3"
    SM4 = "g-sm-4"
    SM5 = "g-sm-5"

    MD0 = "g-md-0"
    MD1 = "g-md-1"
    MD2 = "g-md-2"
    MD3 = "g-md-3"
    MD4 = "g-md-4"
    MD5 = "g-md-5"

    LG0 = "g-lg-0"
    LG1 = "g-lg-1"
    LG2 = "g-lg-2"
    LG3 = "g-lg-3"
    LG4 = "g-lg-4"
    LG5 = "g-lg-5"

    XL0 = "g-xl-0"
    XL1 = "g-xl-1"
    XL2 = "g-xl-2"
    XL3 = "g-xl-3"
    XL4 = "g-xl-4"
    XL5 = "g-xl-5"

    XXL0 = "g-xxl-0"
    XXL1 = "g-xxl-1"
    XXL2 = "g-xxl-2"
    XXL3 = "g-xxl-3"
    XXL4 = "g-xxl-4"
    XXL5 = "g-xxl-5"

    FLUID = "g-fluid"
    SM_FLUID = "g-sm-fluid"
    MD_FLUID = "g-md-fluid"
    LG_FLUID = "g-lg-fluid"
    XL_FLUID = "g-xl-fluid"
    XXL_FLUID = "g-xxl-fluid"

    Y0 = "gy-0"
    Y1 = "gy-1"
    Y2 = "gy-2"
    Y3 = "gy-3"
    Y4 = "gy-4"
    Y5 = "gy-5"
    X0 = "gx-0"
    X1 = "gx-1"
    X2 = "gx-2"
    X3 = "gx-3"
    X4 = "gx-4"
    X5 = "gx-5"

    def __call__(self):
        return self.value

    @classmethod
    def get(
        cls,
        name=None,
    ):
        if not name:
            return cls.G0
        try:
            return cls[name]
        except KeyError:
            return None


class Button(Enum):
    """Bootstrap Button classes."""

    BTN = "btn"  # Base class for buttons
    PRIMARY = f"btn-{Color.PRIMARY.value}"
    SECONDARY = f"btn-{Color.SECONDARY.value}"
    SUCCESS = f"btn-{Color.SUCCESS.value}"
    DANGER = f"btn-{Color.DANGER.value}"
    WARNING = f"btn-{Color.WARNING.value}"
    INFO = f"btn-{Color.INFO.value}"
    LIGHT = f"btn-{Color.LIGHT.value}"
    DARK = f"btn-{Color.DARK.value}"
    LINK = "btn-link"

    OUTLINE_PRIMARY = f"btn-outline-{Color.PRIMARY.value}"
    OUTLINE_SECONDARY = f"btn-outline-{Color.SECONDARY.value}"
    OUTLINE_SUCCESS = f"btn-outline-{Color.SUCCESS.value}"
    OUTLINE_DANGER = f"btn-outline-{Color.DANGER.value}"
    OUTLINE_WARNING = f"btn-outline-{Color.WARNING.value}"
    OUTLINE_INFO = f"btn-outline-{Color.INFO.value}"
    OUTLINE_LIGHT = f"btn-outline-{Color.LIGHT.value}"
    OUTLINE_DARK = f"btn-outline-{Color.DARK.value}"

    SM = f"btn-{Breakpoint.SM.value}"
    LG = f"btn-{Breakpoint.LG.value}"
    BLOCK = "d-grid"

    GROUP = "btn-group"
    GROUP_SM = f"btn-group-{Breakpoint.SM.value}"
    GROUP_MD = f"btn-group-{Breakpoint.MD.value}"
    GROUP_LG = f"btn-group-{Breakpoint.LG.value}"
    GROUP_XL = f"btn-group-{Breakpoint.XL.value}"
    GROUP_XXL = f"btn-group-{Breakpoint.XXL.value}"

    GROUP_VERTICAL = "btn-group-vertical"
    CLOSE = "btn-close"  # Close button

    def __call__(self):
        return self.value

    @classmethod
    def get(
        cls,
        name=None,
    ):
        if not name:
            return cls.BTN
        try:
            return cls[name.upper().replace('-','_')].value
        except KeyError:
            return None


@dataclass
class Layout:
    """ALL 6 OBJ ARE ENUMS"""

    CONTAINER = Container
    ROW = Row
    COLUMN = Column
    GUTTER = Gutter
    BUTTON = Button
    __BREAKPOINT = Breakpoint

    @property
    def values_as_list(self):
        vals = []
        vals.extend([x.value for x in self.COLUMN])
        vals.extend([x.value for x in self.CONTAINER])
        vals.extend([x.value for x in self.GUTTER])
        vals.extend([x.value for x in self.ROW])
        vals.extend([x.value for x in self.__BREAKPOINT])
        vals.extend([x.value for x in self.BUTTON])
        return vals
