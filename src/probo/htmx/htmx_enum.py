from enum import Enum
from typing import List


class HxAttr(Enum):
    """HTMX attributes"""

    BOOST = "hx-boost"
    GET = "hx-get"
    POST = "hx-post"
    PUT = "hx-put"
    PATCH = "hx-patch"
    DELETE = "hx-delete"
    TARGET = "hx-target"
    SWAP = "hx-swap"
    SWAP_OOB = "hx-swap-oob"
    TRIGGER = "hx-trigger"
    VALS = "hx-vals"
    PARAMS = "hx-params"
    CONFIRM = "hx-confirm"
    PUSH_URL = "hx-push-url"
    SELECT = "hx-select"
    SELECT_OOB = "hx-select-oob"
    SYNC = "hx-sync"
    VARS = "hx-vars"
    EXT = "hx-ext"
    HEADERS = "hx-headers"
    HISTORY = "hx-history"
    HISTORY_ELT = "hx-history-elt"
    INCLUDE = "hx-include"
    INDICATOR = "hx-indicator"
    PRESERVE = "hx-preserve"
    PROMPT = "hx-prompt"
    REPLACE_URL = "hx-replace-url"
    REQUEST = "hx-request"
    SSE = "hx-sse"
    VALIDATE = "hx-validate"
    WS = "hx-ws"

    @classmethod
    def all_attrs(cls) -> List[str]:
        return [attr.value for attr in cls]


class HxBoolValue(Enum):
    TRUE = "true"
    FALSE = "false"


class HxSwap(Enum):
    INNER_HTML = "innerHTML"
    OUTER_HTML = "outerHTML"
    BEFORE_BEGIN = "beforebegin"
    AFTER_BEGIN = "afterbegin"
    BEFORE_END = "beforeend"
    AFTER_END = "afterend"
    DELETE = "delete"
    NONE = "none"


class HxTrigger(Enum):
    CLICK = "click %s"
    DBLCLICK = "dblclick %s"
    MOUSEENTER = "mouseenter %s"
    MOUSELEAVE = "mouseleave %s"
    LOAD = "load %s"
    INPUT = "input %s"
    CHANGE = "change %s"
    SUBMIT = "submit %s"
    FOCUS = "focus %s"
    BLUR = "blur %s"
    SEARCH = "search %s"
    KEYUP = "keyup %s"
    EVERY = "every %s"
    REVEALED = "revealed %s"
    INTERSECT = "intersect %s"
    INTERSECT_ROOT = "root %s"
    INTERSECT_THRESHOLD = "threshold %f"
    ONCE = "once %s"
    DELAY = "delay:%s"
    THROTTLE = "throttle:%s"
    FROM = "from:%s"
    CHANGED = "changed %s"


class HxParams(Enum):
    ALL = "all"
    NONE = "none"
    STAR = "*"


class HxSyncStrategy(Enum):
    DROP = "drop"
    ABORT = "abort"
    REPLACE = "replace"
    QUEUE = "queue"
