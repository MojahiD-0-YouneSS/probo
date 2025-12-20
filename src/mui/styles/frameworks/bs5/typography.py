from enum import Enum
from mui.styles.frameworks.bs5.utilities import Breakpoint, Color

class Heading(Enum):
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    
    DISPLAY_1 = "display-1"
    DISPLAY_2 = "display-2"
    DISPLAY_3 = "display-3"
    DISPLAY_4 = "display-4"
    DISPLAY_5 = "display-5"
    DISPLAY_6 = "display-6"

class Text(Enum):
    """Bootstrap Text colors and alignment."""
    PRIMARY = "text-primary"
    SECONDARY = "text-secondary"
    SUCCESS = "text-success"
    DANGER = "text-danger"
    WARNING = "text-warning"
    INFO = "text-info"
    LIGHT = "text-light"
    DARK = "text-dark"
    WHITE = "text-white"
    MUTED = "text-muted"
    
    BG_PRIMARY = "text-bg-primary"
    BG_SECONDARY = "text-bg-secondary"
    BG_SUCCESS = "text-bg-success"
    BG_DANGER = "text-bg-danger"
    BG_WARNING = "text-bg-warning"
    BG_INFO = "text-bg-info"
    BG_LIGHT = "text-bg-light"
    BG_DARK = "text-bg-dark"
    BG_WHITE = "text-bg-white"
    BG_MUTED = "text-bg-muted"
    
    START = "text-start"
    CENTER = "text-center"
    END = "text-end"
    UNDERLINE = "text-decoration-underline"
    DELETED = "text-decoration-line-through"
    JUSTIFY = "text-justify"  # Justify text
    WRAP = "text-wrap"  # Wrap text
    NO_WRAP = "text-nowrap"  #
    NONE='text-decoration-none'
    LOWER='text-lowercase'
    UPPER='text-uppercase'
    BODY='text-body'
    BLACK_50='text-black-50'
    WHITE_50='text-white-50'
    LEFT = "text-left"
    RIGHT = "text-right"
    CAPITALIZE = "text-capitalize"
    TRUNCATE = "text-truncate"
    BREAK = 'text-break'

class Lead(Enum):
    """Bootstrap Lead class for larger paragraph text."""
    LEAD = "lead"

class Abbreviation(Enum):
    """
    Bootstrap Abbreviations classes.
    These are used for defining abbreviations and acronyms.
    """
    
    ABBREVIATION = "abbreviation"
    INITIALISM = "initialism"

class Blockquote(Enum):
    """
    Bootstrap Blockquote class.
    Used for quoting sections of text.
    """
    BLOCKQUOTE = "blockquote"
    NAMING_A_SOURCE = "blockquote-footer"

class Image(Enum):
    """
    Bootstrap Images classes.
    These are used for styling images.
    """
    RESPONSIVE = "img-fluid"  # Responsive image
    THUMBNAIL = "img-thumbnail"  # Thumbnail image
    ROUND = "rounded"  # Rounded corners
    CIRCLE = "rounded-circle"  # Circle shape
    FIGURE_IMG = 'figure-img'
    FIGURE = "figure"
    CAPTION = 'figure-caption'
    PICTURE= "picture"

class Typography:
    """
    Bootstrap Typography classes.
    These are used for text styling and formatting.
    """
    HEADING = Heading
    TEXT = Text
    LEAD=Lead
    ABBREVIATION = Abbreviation
    BLOCK_QUOTE=Blockquote
    IMAGE = Image
    @property
    def values_as_list(self):
        vals = []
        vals.extend([x.value for x in self.HEADING])
        vals.extend([x.value for x in self.TEXT])
        vals.extend([x.value for x in self.LEAD])
        vals.extend([x.value for x in self.ABBREVIATION])
        vals.extend([x.value for x in self.BLOCK_QUOTE])
        vals.extend([x.value for x in self.IMAGE])
        return vals