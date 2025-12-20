from enum import Enum

#from tempo.styles.frameworks.bs5.bs5 

class DataBSAttribute(Enum):
   DATA_BS = [
    "data-bs-toggle",
    "data-bs-dismiss",
    "data-bs-parent",
    "data-bs-container",
    "data-bs-placement",
    "data-bs-backdrop",
    "data-bs-keyboard",
    "data-bs-focus",
    "data-bs-show",
    "data-bs-offset",
    "data-bs-reference",
    "data-bs-display",
    "data-bs-auto-close",
    "data-bs-scroll",
    "data-bs-title",
    "data-bs-content",
    "data-bs-html",
    "data-bs-delay",
    "data-bs-trigger",
    "data-bs-custom-class"
    "data-bs-boundary",
    "data-bs-slide",
    "data-bs-ride",
    "data-bs-interval",
    "data-bs-pause",
    "data-bs-wrap",
    "data-bs-touch",
    "data-bs-slide-to",
    "data-bs-autohide",
    "data-bs-target",
   ]

class AriaAttribute(Enum):
   ARIA_ATTRIBUTE = [
        'aria-activedescendant', 'aria-atomic', 'aria-autocomplete', 'aria-busy',
        'aria-checked', 'aria-colcount', 'aria-colindex', 'aria-colspan',
        'aria-controls', 'aria-current', 'aria-describedby', 'aria-details',
        'aria-disabled', 'aria-dropeffect', 'aria-errormessage', 'aria-expanded',
        'aria-flowto', 'aria-grabbed', 'aria-haspopup', 'aria-hidden',
        'aria-invalid', 'aria-keyshortcuts', 'aria-label', 'aria-labelledby',
        'aria-level', 'aria-live', 'aria-modal', 'aria-multiline',
        'aria-multiselectable', 'aria-orientation', 'aria-owns', 'aria-placeholder',
        'aria-posinset', 'aria-pressed', 'aria-readonly', 'aria-relevant',
        'aria-required', 'aria-roledescription', 'aria-rowcount', 'aria-rowindex',
        'aria-rowspan', 'aria-selected', 'aria-setsize', 'aria-sort',
        'aria-valuemax', 'aria-valuemin', 'aria-valuenow', 'aria-valuetext',
    ]

class VoidTags(Enum):
   VOID_TAGS = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr']

class GlobalAttribute(Enum):
   GLOBAL_ATTRIBUTE = [
        'accesskey', 'class', 'contenteditable', 'data-*', 'dir', 'draggable',
        'enterkeyhint', 'hidden', 'id', 'inert', 'inputmode', 'lang',
        'popover', 'spellcheck', 'style', 'tabindex', 'title', 'translate','referrerpolicy', "crossorigin", "integrity","role",
    ]

class EventAttribute(Enum):
   EVENT_ATTRIBUTE = [
        'onabort', 'onafterprint', 'onbeforeprint', 'onbeforeunload', 'onblur',
        'onchange', 'onclick', 'oncontextmenu', 'oncopy', 'oncut', 'ondblclick',
        'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover',
        'ondragstart', 'ondrop', 'onerror', 'onfocus', 'oninput', 'oninvalid',
        'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onmousedown',
        'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover',
        'onmouseup', 'onmousewheel', 'onoffline', 'ononline', 'onpaste',
        'onreset', 'onscroll', 'onsearch', 'onselect', 'onsubmit', 'onunload',
        'onwheel'
    ]

class AllVisibleAttribute(Enum):
   VISIBLE_ATTRIBUTE = [
        'id', 'class', 'style', 'title', 'hidden',
        'alt', 'src', 'href', 'value', 'placeholder',
        'type', 'name', 'width', 'height', 'maxlength', 'minlength',
        'rows', 'cols', 'size', 'selected', 'checked', 'disabled', 'readonly',
        'label', 'for', 'wrap'
    ]

class NotSupportedInHtml5(Enum):
    NOT_SUPPORTED_IN_HTML5 = [
        'align', 'alink', 'bgcolor', 'border', 'color', 'link', 'marginheight',
        'marginwidth', 'text', 'vlink'
    ]

class AttributeValue(Enum):
   """Class to validate HTML attributes and their values."""
   
   ATTRIBUTE_VALUE = {
      'accept': ['file_extension', 'audio/*', 'video/*', 'image/*', 'media_type'], 
      'accept-charset': ['UTF-8 ', 'ISO-8859-1', 'ASCII', 'ANSI'],
      'accesskey': 'any', 
      'action': 'any', 
      'alt': 'any', 
      'async': 'async', 
      'autocomplete': {'form':['on', 'off'],'input':['on', 'off', 'address-line1', 'address-line2', 'address-line3', 'address-level1', 'address-level2', 'address-level3', 'address-level4', 'street-address', 'country', 'country-name', 'postal-code', 'name', 'additional-name', 'family-name', 'give-name', 'honoric-prefix', 'honoric-suffix', 'nickname', 'organization-title', 'username', 'new-password', 'current-password', 'bday', 'bday-day', 'bday-month', 'bday-year', 'sex', 'one-time-code', 'organization', 'cc-name', 'cc-given-name', 'cc-additional-name', 'cc-family-name', 'cc-number', 'cc-exp', 'cc-exp-month', 'cc-exp-year', 'cc-csc', 'cc-type', 'transaction-currency', 'transaction-amount', 'language', 'url', 'email', 'photo', 'tel', 'tel-country-code', 'tel-national', 'tel-area-code', 'tel-local', 'tel-local-prefix', 'tel-local-suffix', 'tel-extension', 'impp']}, 
      'autofocus': 'autofocus', 
      'autoplay': 'autoplay', 
      'charset': ['UTF-8', 'ISO-8859-1', 'ASCII', 'ANSI'], 
      'checked': 'checked', 
      'cite': 'any', 
      'class': 'any', 
      'cols': 'any', 
      'colspan': 'any', 
      'content': "any", 
      'contenteditable': ["true", "false"], 
      'controls': 'controls', 
      'coords': 'any', 
      'data': 'any', 
      'data-*': 'any', 
      'datetime': 'any', 
      'default': 'default', 
      'defer': 'defer', 
      'dir': ['ltr', 'rtl', 'auto'], 
      'dirname': '*.dir', 
      'disabled': 'disabled', 
      'download': {'a':'download', 'area':'any'}, 
      'draggable': ['true', 'false', 'auto'], 
      'enctype': ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain'], 
      'enterkeyhint': ['done', 'enter', 'go', 'next', 'previous', 'search', 'send'], 
      'for': 'any', 
      'form': 'any', 
      'formaction': 'any', 
      'headers': 'any', 
      'height': 'any',#number 
      'hidden': 'hidden', 
      'high': 'any',#number 
      'href': 'any', 
      'hreflang': ['ab', 'aa', 'af', 'ak', 'sq', 'am', 'ar', 'an', 'hy', 'as', 'av', 'ae', 'ay', 'az', 'bm', 'ba', 'eu', 'be', 'bn', 'bh', 'bi', 'bs', 'br', 'bg', 'my', 'ca', 'ch', 'ce', 'ny', 'zh', 'zh-Hans', 'zh-Hant', 'cv', 'kw', 'co', 'cr', 'hr', 'cs', 'da', 'dv', 'nl', 'dz', 'en', 'eo', 'et', 'ee', 'fo', 'fj', 'fi', 'fr', 'ff', 'gl', 'gd', 'gv', 'ka', 'de', 'el', 'kl', 'gn', 'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho', 'hu', 'is', 'io', 'ig', 'id', 'in', 'ia', 'ie', 'iu', 'ik', 'ga', 'it', 'ja', 'jv', 'kl', 'kn', 'kr', 'ks', 'kk', 'km', 'ki', 'rw', 'rn', 'ky', 'kv', 'kg', 'ko', 'ku', 'kj', 'lo', 'la', 'lv', 'li', 'ln', 'lt', 'lu', 'lg', 'lb', 'gv', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mh', 'mo', 'mn', 'na', 'nv', 'ng', 'nd', 'ne', 'no', 'nb', 'nn', 'ii', 'oc', 'oj', 'cu', 'or', 'om', 'os', 'pi', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'rm', 'ro', 'ru', 'se', 'sm', 'sg', 'sa', 'sr', 'sh', 'st', 'tn', 'sn', 'ii', 'sd', 'si', 'ss', 'sk', 'sl', 'so', 'nr', 'es', 'su', 'sw', 'ss', 'sv', 'tl', 'ty', 'tg', 'ta', 'tt', 'te', 'th', 'bo', 'ti', 'to', 'ts', 'tr', 'tk', 'tw', 'ug', 'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'cy', 'wo', 'fy', 'xh', 'yi', 'ji', 'yo', 'za', 'zu'], 
      'http-equiv': ['content-security-policy', 'x-ua-compatible','content-type', 'default-style', 'refresh'], 
      'id': 'any', 
      'integrity': 'any', 
      'inert': 'inert', 
      'inputmode': ['decimal', 'email', 'none', 'numeric', 'search', 'tel', 'text', 'url'], 
      'ismap': 'ismap', 
      'kind': ['captions', 'chapters', 'descriptions', 'metadata', 'subtitles'], 
      'label': 'any', 
      'lang': ['ab', 'aa', 'af', 'ak', 'sq', 'am', 'ar', 'an', 'hy', 'as', 'av', 'ae', 'ay', 'az', 'bm', 'ba', 'eu', 'be', 'bn', 'bh', 'bi', 'bs', 'br', 'bg', 'my', 'ca', 'ch', 'ce', 'ny', 'zh', 'zh-Hans', 'zh-Hant', 'cv', 'kw', 'co', 'cr', 'hr', 'cs', 'da', 'dv', 'nl', 'dz', 'en', 'eo', 'et', 'ee', 'fo', 'fj', 'fi', 'fr', 'ff', 'gl', 'gd', 'gv', 'ka', 'de', 'el', 'kl', 'gn', 'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho', 'hu', 'is', 'io', 'ig', 'id', 'in', 'ia', 'ie', 'iu', 'ik', 'ga', 'it', 'ja', 'jv', 'kl', 'kn', 'kr', 'ks', 'kk', 'km', 'ki', 'rw', 'rn', 'ky', 'kv', 'kg', 'ko', 'ku', 'kj', 'lo', 'la', 'lv', 'li', 'ln', 'lt', 'lu', 'lg', 'lb', 'gv', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mh', 'mo', 'mn', 'na', 'nv', 'ng', 'nd', 'ne', 'no', 'nb', 'nn', 'ii', 'oc', 'oj', 'cu', 'or', 'om', 'os', 'pi', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'rm', 'ro', 'ru', 'se', 'sm', 'sg', 'sa', 'sr', 'sh', 'st', 'tn', 'sn', 'ii', 'sd', 'si', 'ss', 'sk', 'sl', 'so', 'nr', 'es', 'su', 'sw', 'ss', 'sv', 'tl', 'ty', 'tg', 'ta', 'tt', 'te', 'th', 'bo', 'ti', 'to', 'ts', 'tr', 'tk', 'tw', 'ug', 'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'cy', 'wo', 'fy', 'xh', 'yi', 'ji', 'yo', 'za', 'zu'], 
      'list': 'any', 
      'loop': 'loop', 
      'low': 'any',#number 
      'max': 'any',#date 
      'maxlength': 'any',#number 
      'media': {'operator':['and', 'not', ','], 'devices':['all', 'aural', 'braille', 'handheld', 'projection', 'print', 'screen', 'tty', 'tv'], 'values':['width', 'height', 'device-width', 'device-height', 'orientation', 'aspect-ratio', 'device-aspect-ratio', 'color', 'color-index', 'monochrome', 'resolution', 'scan', 'grid']}, 
      'method': ['get', 'post'], 
      'min': 'any', 
      'multiple': 'multiple', 
      'muted': 'muted', 
      'name': 'any', 
      'novalidate': 'novalidate', 
      'open': 'open', 
      'optimum': 'any',#float number 
      'pattern': 'any', 
      'crossorigin': 'any', 
      'placeholder': 'any', 
      'popover': 'popover', 
      'popovertarget': 'any', 
      'popovertargetaction': ['hide', 'show', 'toggle'], 
      'poster': 'any', 
      'preload': ['auto', 'metadata', 'none'], 
      'readonly': 'readonly', 
      'rel': {'a':['alternate', 'author', 'bookmark', 'external', 'help', 'license', 'next', 'nofollow', 'noopener', 'noreferrer', 'prev', 'search', 'tag'], 'area':['alternate', 'author', 'bookmark', 'help', 'license', 'next', 'nofollow', 'noreferrer', 'prefetch', 'prev', 'search', 'tag'], 'link':['alternate', 'author', 'dns-prefetch', 'help', 'icon', 'license', 'next', 'pingback', 'preconnect', 'prefetch', 'preload', 'prerender', 'prev', 'search', 'stylesheet'], 'form':['external', 'help', 'license', 'next', 'nofollow', 'noopener', 'noreferrer', 'opener', 'prev', 'search']}, 
      'required': 'required', 
      'reversed': 'reversed', 
      'referrerpolicy': 'any',
      'role':['alert','alertdialog','application','article', 'banner', 'button', 'cell', 'checkbox', 'columnheader', 'combobox', 'command', 'comment', 'complementary', 'composite', 'contentinfo', 'definition', 'dialog', 'directory', 'Deprecated', 'document','feed','figure','form','generic','grid','gridcell','group','heading','img','input','landmark','link','list','listbox','listitem','log','main','mark','marquee','math','menu','menubar','menuitem','menuitemcheckbox','menuitemradio','meter','navigation','none','note','option','presentation','progressbar','radio','radiogroup','range','region','roletype','row','rowgroup','rowheader','scrollbar','search','searchbox','section','sectionhead','select','separator','slider','spinbutton','status','Structural','structure','suggestion','switch','tab','table','tablist','tabpanel','term','textbox','timer','toolbar','tooltip','tree','treegrid','treeitem','widget','window',],
      'rows': 'any',#number 
      'rowspan': 'any',#number 
      'rel': 'any',#number 
      'sandbox': 'sandbox', 
      'scope': ['col', 'row', 'colgroup', 'rowgroup'], 
      'selected': 'selected', 
      'shape': ['default', 'rect', 'circle', 'poly'], 
      'size': 'any',#number 
      'sizes': 'any', #numberxnumber
      'span': 'any',#number
      'spellcheck': ['true', 'false'], 
      'src': 'any',#url 
      'srcdoc': 'any', #HTML_code
      'srclang': ['ab', 'aa', 'af', 'ak', 'sq', 'am', 'ar', 'an', 'hy', 'as', 'av', 'ae', 'ay', 'az', 'bm', 'ba', 'eu', 'be', 'bn', 'bh', 'bi', 'bs', 'br', 'bg', 'my', 'ca', 'ch', 'ce', 'ny', 'zh', 'zh-Hans', 'zh-Hant', 'cv', 'kw', 'co', 'cr', 'hr', 'cs', 'da', 'dv', 'nl', 'dz', 'en', 'eo', 'et', 'ee', 'fo', 'fj', 'fi', 'fr', 'ff', 'gl', 'gd', 'gv', 'ka', 'de', 'el', 'kl', 'gn', 'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho', 'hu', 'is', 'io', 'ig', 'id', 'in', 'ia', 'ie', 'iu', 'ik', 'ga', 'it', 'ja', 'jv', 'kl', 'kn', 'kr', 'ks', 'kk', 'km', 'ki', 'rw', 'rn', 'ky', 'kv', 'kg', 'ko', 'ku', 'kj', 'lo', 'la', 'lv', 'li', 'ln', 'lt', 'lu', 'lg', 'lb', 'gv', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mh', 'mo', 'mn', 'na', 'nv', 'ng', 'nd', 'ne', 'no', 'nb', 'nn', 'ii', 'oc', 'oj', 'cu', 'or', 'om', 'os', 'pi', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'rm', 'ro', 'ru', 'se', 'sm', 'sg', 'sa', 'sr', 'sh', 'st', 'tn', 'sn', 'ii', 'sd', 'si', 'ss', 'sk', 'sl', 'so', 'nr', 'es', 'su', 'sw', 'ss', 'sv', 'tl', 'ty', 'tg', 'ta', 'tt', 'te', 'th', 'bo', 'ti', 'to', 'ts', 'tr', 'tk', 'tw', 'ug', 'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'cy', 'wo', 'fy', 'xh', 'yi', 'ji', 'yo', 'za', 'zu'], 
      'srcset': 'any',#url 
      'start': 'any',#number 
      'step': 'any',#number 
      'style': 'any',#css 
      'tabindex': 'any',#number 
      'target': ['_blank', '_self', '_parent', '_top', 'framename'], #[0]=any tag, [1]= <base>tag
      'title': 'any', 
      'translate': ['yes', 'no'], 
      'type': ['button', 'checkbox', 'color', 'date', 'datetime-local', 'email', 'file', 'hidden', 'image', 'month', 'number', 'password', 'radio', 'range', 'reset', 'search', 'submit', 'tel', 'text', 'time', 'url', 'week'], #[0]=<input>, [1]=<bottun>, [2]=any
      'usemap': ['#any'], #starts with '#'
      'value': 'any', 
      'width': 'any',#number 
      'wrap': ['soft', 'hard']
   }
      
   BOOTSTRAP_DATA_BS_ATTRIBUTE = {
    # === General (used across multiple components) ===
    "data-bs-toggle": [
        "modal", "dropdown", "collapse", "offcanvas", "tooltip", "popover", "tab", "button"
    ],
    "data-bs-dismiss": ["modal", "alert", "offcanvas", "toast"],
    "data-bs-container": ["body", "element selector"],
    "data-bs-placement": [
        "top", "bottom", "left", "right", "auto", 
        "top-start", "top-end", "bottom-start", "bottom-end", 
        "left-start", "left-end", "right-start", "right-end"
    ],

    # === Modals ===
    "data-bs-backdrop": ["true", "false", "static"],
    "data-bs-keyboard": ["true", "false"],
    "data-bs-focus": ["true", "false"],
    "data-bs-show": ["true", "false"],

    # === Collapse / Accordion ===
    "data-bs-target": "any",
    "data-bs-parent": "any",

    # === Dropdowns ===
    "data-bs-offset": "any",
    "data-bs-reference": ["toggle", "parent", "body"],
    "data-bs-display": ["dynamic", "static"],
    "data-bs-auto-close": ["true", "false", "inside", "outside"],

    # === Offcanvas ===
    "data-bs-scroll": ["true", "false"],

    # === Tooltips & Popovers ===
    "data-bs-title": "any",
    "data-bs-content": "any",
    "data-bs-html": ["true", "false"],
    "data-bs-delay": "any",
    "data-bs-trigger": ["hover", "focus", "click", "manual"],
    "data-bs-custom-class": "any",
    "data-bs-boundary": ["clippingParents", "viewport", "window"],

    # === Carousel ===
    "data-bs-slide": ["next", "prev"],
    "data-bs-ride": ["carousel"],
    "data-bs-interval": ["any","false"],
    "data-bs-pause": ["hover", "false"],
    "data-bs-wrap": ["true", "false"],
    "data-bs-touch": ["true", "false"],
    "data-bs-slide-to": "any",

    # === Toasts ===
    "data-bs-autohide": ["true", "false"],
   }

   ARIA_ATTRIBUTES = {
    # === Global States and Properties ===
    "aria-activedescendant": "any",
    "aria-atomic": ["true", "false"],
    "aria-autocomplete": ["none", "inline", "list", "both"],
    "aria-busy": ["true", "false"],
    "aria-checked": ["true", "false", "mixed", "undefined"],
    "aria-colcount": "any",
    "aria-colindex": "any",
    "aria-colspan": "any",
    "aria-controls": "any",
    "aria-current": ["page", "step", "location", "date", "time", "true", "false"],
    "aria-describedby": "any",
    "aria-details": "any",
    "aria-disabled": ["true", "false"],
    "aria-errormessage": "any",
    "aria-expanded": ["true", "false", "undefined"],
    "aria-flowto": "any",
    "aria-haspopup": ["true", "false", "menu", "listbox", "tree", "grid", "dialog"],
    "aria-hidden": ["true", "false"],
    "aria-invalid": ["grammar", "false", "spelling", "true"],
    "aria-keyshortcuts": "any",
    "aria-label": "any",
    "aria-labelledby": "any",
    "aria-live": ["off", "polite", "assertive"],
    "aria-modal": ["true", "false"],
    "aria-multiline": ["true", "false"],
    "aria-multiselectable": ["true", "false"],
    "aria-orientation": ["horizontal", "vertical"],
    "aria-owns": "any",
    "aria-placeholder": "any",
    "aria-posinset": "any",
    "aria-pressed": ["true", "false", "mixed"],
    "aria-readonly": ["true", "false"],
    "aria-relevant": [
        "additions", "removals", "text", "all"
    ],
    "aria-required": ["true", "false"],
    "aria-roledescription": "any",
    "aria-rowcount": "any",
    "aria-rowindex": "any",
    "aria-rowspan": "any",
    "aria-selected": ["true", "false"],
    "aria-setsize": "any",
    "aria-sort": ["none", "ascending", "descending", "other"],
    "aria-valuemax": "any",
    "aria-valuemin": "any",
    "aria-valuenow": "any",
    "aria-valuetext": "any",

    # === Live Region Attributes ===
    "aria-live": ["off", "polite", "assertive"],
    "aria-atomic": ["true", "false"],
    "aria-relevant": ["additions", "removals", "text", "all"],
    "aria-busy": ["true", "false"],

    # === Drag and Drop ===
    "aria-dropeffect": [
        "none", "copy", "execute", "link", "move", "popup"
    ],
    "aria-grabbed": ["true", "false"],

    # === Relationship Attributes ===
    "aria-controls": "any",
    "aria-describedby": "any",
    "aria-labelledby": "any",
    "aria-owns": "any",
    "aria-flowto": "any",

    # === Widget-specific Attributes ===
    "aria-autocomplete": ["none", "inline", "list", "both"],
    "aria-checked": ["true", "false", "mixed"],
    "aria-expanded": ["true", "false", "undefined"],
    "aria-level": "integer (hierarchy level)",
    "aria-modal": ["true", "false"],
    "aria-multiselectable": ["true", "false"],
    "aria-orientation": ["horizontal", "vertical"],
    "aria-pressed": ["true", "false", "mixed"],
    "aria-selected": ["true", "false"],
    "aria-sort": ["none", "ascending", "descending", "other"],
    "aria-valuemax": "any",
    "aria-valuemin": "any",
    "aria-valuenow": "any",
    "aria-valuetext": "any",

    # === Application / Structural Roles ===
    "role": [
        "alert", "alertdialog", "application", "article", "banner", "button", "cell", "checkbox",
        "columnheader", "combobox", "complementary", "contentinfo", "definition", "dialog", "directory",
        "document", "feed", "figure", "form", "grid", "gridcell", "group", "heading", "img", "link",
        "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem",
        "menuitemcheckbox", "menuitemradio", "navigation", "none", "note", "option", "presentation",
        "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar",
        "search", "searchbox", "separator", "slider", "spinbutton", "status", "switch", "tab", "table",
        "tablist", "tabpanel", "term", "textbox", "timer", "toolbar", "tooltip", "tree", "treegrid",
        "treeitem"
    ]
   }

ATTR_CLUSTER = set(GlobalAttribute.GLOBAL_ATTRIBUTE.value + EventAttribute.EVENT_ATTRIBUTE.value + AllVisibleAttribute.VISIBLE_ATTRIBUTE.value + AriaAttribute.ARIA_ATTRIBUTE.value + DataBSAttribute.DATA_BS.value)

class ElementAttribute(Enum):        
   ELEMENT_ATTRIBUTE = {

   'accept':	['<input>'],

   'accept-charset':	['<form>'],

   'action':	['<form>'],

   'alt':	['<area>', '<img>', '<input>'],

   'Async':	['<script>'],

   'autocomplete':	['<form>', '<input>'],

   'autofocus':	['<button>', '<input>', '<select>', '<textarea>'],

   'autoplay':	['<audio>', '<video>'],

   'charset':	['<meta>', '<script>'],

   'checked':	['<input>'],

   'cite':	['<blockquote>', '<del>', '<ins>', '<q>'],

   'cols':	['<textarea>'],

   'colspan':	['<td>', '<th>'],

   'content':	['<meta>'],

   'controls':	['<audio>', '<video>'],

   'coords':	['<area>'],

   'data':	['<object>'],

   'datetime':	['<del>', '<ins>', '<time>'],

   'default':	['<track>'],

   'defer':	['<script>'],

   'dirname':	['<input>', '<textarea>'],

   'disabled':	['<button>', '<fieldset>', '<input>', '<optgroup>', '<option>', '<select>', '<textarea>'],

   'download':	['<a>', '<area>'],

   'enctype':	['<form>'],

   'For':	['<label>', '<output>'],

   'form':	['<button>', '<fieldset>', '<input>', '<label>', '<meter>', '<object>', '<output>', '<select>', '<textarea>'],

   'formaction':	['<button>', '<input>'],

   'headers':	['<td>', '<th>'],

   'height':	['<canvas>', '<embed>', '<iframe>', '<img>', '<input>', '<object>', '<video>'],

   'high':	['<meter>'],

   'href':	['<a>', '<area>', '<base>', '<link>'],

   'hreflang':	['<a>', '<area>', '<link>'],

   'http-equiv':	['<meta>'],

   'ismap':	['<img>'],

   'kind':	['<track>'],

   'label':	['<track>', '<option>', '<optgroup>'],

   'list':	['<input>'],

   'loop':	['<audio>', '<video>'],

   'low':	['<meter>'],

   'max':	['<input>', '<meter>', '<progress>'],

   'maxlength':	['<input>', '<textarea>'],

   'media':	['<a>', '<area>', '<link>', '<source>', '<style>'],

   'method':	['<form>'],

   'min':	['<input>', '<meter>'],

   'multiple':	['<input>', '<select>'],

   'muted':	['<video>', '<audio>'],

   'name':	['<button>', '<fieldset>', '<form>', '<iframe>', '<input>', '<map>', '<meta>', '<object>', '<output>', '<param>', '<select>', '<textarea>'],

   'novalidate':	['<form>'],

   'onabort':	['<audio>', '<embed>', '<img>', '<object>', '<video>'],

   'onafterprint':	['<body>'],

   'onbeforeprint':	['<body>'],

   'onbeforeunload':	['<body>'],

   'oncanplay':	['<audio>', '<embed>', '<object>', '<video>'],

   'oncanplaythrough':	['<audio>', '<video>'],

   'oncuechange':	['<track>'],

   'ondurationchange':	['<audio>', '<video>'],

   'onemptied':	['<audio>', '<video>'],

   'onended':	['<audio>', '<video>'],

   'onerror':	['<audio>', '<body>', '<embed>', '<img>', '<object>', '<script>', '<style>', '<video>'],

   'onhashchange':	['<body>'],

   'onload':	['<body>', '<iframe>', '<img>', '<input>', '<link>', '<script>', '<style>'],

   'onloadeddata':	['<audio>', '<video>'],

   'onloadedmetadata':	['<audio>', '<video>'],

   'onloadstart':	['<audio>', '<video>'],

   'onoffline':	['<body>'],

   'ononline':	['<body>'],

   'onpagehide':	['<body>'],

   'onpageshow':	['<body>'],

   'onpause':	['<audio>', '<video>'],

   'onplay':	['<audio>', '<video>'],

   'onplaying':	['<audio>', '<video>'],

   'onpopstate':	['<body>'],

   'onprogress':	['<audio>', '<video>'],

   'onratechange':	['<audio>', '<video>'],

   'onreset':	['<form>'],

   'onresize':	['<body>'],

   'onsearch':	['<input>'],

   'onseeked':	['<audio>', '<video>'],

   'onseeking':	['<audio>', '<video>'],

   'onstalled':	['<audio>', '<video>'],

   'onstorage':	['<body>'],

   'onsubmit':	['<form>'],

   'onsuspend':	['<audio>', '<video>'],

   'ontimeupdate':	['<audio>', '<video>'],

   'ontoggle':	['<details>'],

   'onunload':	['<body>'],

   'onvolumechange':	['<audio>', '<video>'],

   'onwaiting':	['<audio>', '<video>'],

   'open':	['<details>'],

   'optimum':	['<meter>'],

   'pattern':	['<input>'],

   'placeholder':	['<input>', '<textarea>'],

   'popovertarget':	['<button>', '<input>'],

   'popovertargetaction':	['<button>', '<input>'],

   'poster':	['<video>'],

   'preload':	['<audio>', '<video>'],

   'readonly':	['<input>', '<textarea>'],

   'rel':	['<a>', '<area>', '<form>', '<link>'],

   'required':	['<input>', '<select>', '<textarea>'],

   'reversed':	['<ol>'],

   'rows':	['<textarea>'],

   'rowspan':	['<td>', '<th>'],

   'sandbox':	['<iframe>'],

   'scope':	['<th>'],

   'selected':	['<option>'],

   'shape':	['<area>'],

   'size':	['<input>', '<select>'],

   'sizes':	['<img>', '<link>', '<source>'],

   'span':	['<col>', '<colgroup>'],

   'src':	['<audio>', '<embed>', '<iframe>', '<img>', '<input>', '<script>', '<source>', '<track>', '<video>'],

   'srcdoc':	['<iframe>'],

   'srclang':	['<track>'],

   'srcset':	['<img>', '<source>'],

   'start':	['<ol>'],

   'step':	['<input>'],

   'target':	['<a>', '<area>', '<base>', '<form>'],

   'type':	['<a>', '<button>', '<embed>', '<input>', '<link>', '<menu>', '<object>', '<script>', '<source>', '<style>'],

   'usemap':	['<img>', '<object>'],

   'value':	['<button>', '<input>', '<li>', '<option>', '<meter>', '<progress>', '<param>'],

   'width':	['<canvas>', '<embed>', '<iframe>', '<img>', '<input>', '<object>', '<video>'],

   'wrap':	['<textarea>'],
   
   }

class Tag(Enum):
   DOCTYPE = ('!DOCTYPE html', {"void": True})
   A = ('a', {"void": False})
   ABBR = ('abbr', {"void": False})
   ADDRESS = ('address', {"void": False})
   AREA = ('area', {"void": True})
   ARTICLE = ('article', {"void": False})
   ASIDE = ('aside', {"void": False})
   AUDIO = ('audio', {"void": False})
   B = ('b', {"void": False})
   BASE = ('base', {"void": True})
   BDI = ('bdi', {"void": False})
   BDO = ('bdo', {"void": False})
   BLOCKQUOTE = ('blockquote', {"void": False})
   BODY = ('body', {"void": False})
   BR = ('br', {"void": True})
   BUTTON = ('button', {"void": False})
   CANVAS = ('canvas', {"void": False})
   CAPTION = ('caption', {"void": False})
   CITE = ('cite', {"void": False})
   CODE = ('code', {"void": False})
   COL = ('col', {"void": True})
   COLGROUP = ('colgroup', {"void": False})
   DATA = ('data', {"void": False})
   DATALIST = ('datalist', {"void": False})
   DD = ('dd', {"void": False})
   DEL = ('del', {"void": False})
   DETAILS = ('details', {"void": False})
   DFN = ('dfn', {"void": False})
   DIALOG = ('dialog', {"void": False})
   DIV = ('div', {"void": False})
   DL = ('dl', {"void": False})
   DT = ('dt', {"void": False})
   EM = ('em', {"void": False})
   EMBED = ('embed', {"void": True})
   FIELDSET = ('fieldset', {"void": False})
   FIGCAPTION = ('figcaption', {"void": False})
   FIGURE = ('figure', {"void": False})
   FOOTER = ('footer', {"void": False})
   FORM = ('form', {"void": False})
   H1 = ('h1', {"void": False})
   H2 = ('h2', {"void": False})
   H3 = ('h3', {"void": False})
   H4 = ('h4', {"void": False})
   H5 = ('h5', {"void": False})
   H6 = ('h6', {"void": False})
   HEAD = ('head', {"void": False})
   HEADER = ('header', {"void": False})
   HGROUP = ('hgroup', {"void": False})
   HR = ('hr', {"void": True})
   HTML = ('html', {"void": False})
   I = ('i', {"void": False})
   IFRAME = ('iframe', {"void": False})
   IMG = ('img', {"void": True})
   INPUT = ('input', {"void": True})
   INS = ('ins', {"void": False})
   KBD = ('kbd', {"void": False})
   LABEL = ('label', {"void": False})
   LEGEND = ('legend', {"void": False})
   LI = ('li', {"void": False})
   LINK = ('link', {"void": True})
   MAIN = ('main', {"void": False})
   MATH = ('math', {"void": False})
   MAP = ('map', {"void": False})
   MARK = ('mark', {"void": False})
   MENU = ('menu', {"void": False})
   META = ('meta', {"void": True})
   METER = ('meter', {"void": False})
   NAV = ('nav', {"void": False})
   NOSCRIPT = ('noscript', {"void": False})
   OBJECT = ('object', {"void": False})
   OL = ('ol', {"void": False})
   OPTGROUP = ('optgroup', {"void": False})
   OPTION = ('option', {"void": False})
   OUTPUT = ('output', {"void": False})
   P = ('p', {"void": False})
   PARAM = ('param', {"void": True})
   PORTAL = ('portal', {"void": False})
   PICTURE = ('picture', {"void": False})
   PRE = ('pre', {"void": False})
   PROGRESS = ('progress', {"void": False})
   Q = ('q', {"void": False})
   RP = ('rp', {"void": False})
   RT = ('rt', {"void": False})
   RUBY = ('ruby', {"void": False})
   S = ('s', {"void": False})
   SAMP = ('samp', {"void": False})
   SCRIPT = ('script', {"void": False})
   SEARCH = ('search', {"void": False})
   SECTION = ('section', {"void": False})
   SELECT = ('select', {"void": False})
   SLOT = ('slot', {"void": False})
   SMALL = ('small', {"void": False})
   SOURCE = ('source', {"void": True})
   SPAN = ('span', {"void": False})
   STRONG = ('strong', {"void": False})
   STYLE = ('style', {"void": False})
   SUB = ('sub', {"void": False})
   SUMMARY = ('summary', {"void": False})
   SUP = ('sup', {"void": False})
   SVG = ('svg', {"void": False})
   TABLE = ('table', {"void": False})
   TBODY = ('tbody', {"void": False})
   TD = ('td', {"void": False})
   TEMPLATE = ('template', {"void": False})
   TEXTAREA = ('textarea', {"void": False})
   TFOOT = ('tfoot', {"void": False})
   TH = ('th', {"void": False})
   THEAD = ('thead', {"void": False})
   TIME = ('time', {"void": False})
   TITLE = ('title', {"void": False})
   TR = ('tr', {"void": False})
   TRACK = ('track', {"void": True})
   U = ('u', {"void": False})
   UL = ('ul', {"void": False})
   VAR = ('var', {"void": False})
   VIDEO = ('video', {"void": False})
   WBR = ('wbr', {"void": True})
   # --- SVG Specific Elements ---
   # --- Basic Shapes & Paths (Void) ---
   PATH = ('path', {"void": True})      # Essential for Icons
   CIRCLE = ('circle', {"void": True})
   RECT = ('rect', {"void": True})
   LINE = ('line', {"void": True})
   POLYLINE = ('polyline', {"void": True})
   POLYGON = ('polygon', {"void": True})
   # --- Advanced SVG Elements ---
   ELLIPSE = ('ellipse', {"void": True})
   IMAGE = ('image', {"void": True})  # SVG specific image tag
   SYMBOL = ('symbol', {"void": False})
   MARKER = ('marker', {"void": False})
   PATTERN = ('pattern', {"void": False})
   MASK = ('mask', {"void": False})
   CLIP_PATH = ('clipPath', {"void": False})
   
   # --- Gradients ---
   LINEAR_GRADIENT = ('linearGradient', {"void": False})
   RADIAL_GRADIENT = ('radialGradient', {"void": False})
   
   # --- Filters (The "fe" prefix tags) ---
   FILTER = ('filter', {"void": False})
   FE_BLEND = ('feBlend', {"void": True})
   FE_COLOR_MATRIX = ('feColorMatrix', {"void": True})
   FE_COMPONENT_TRANSFER = ('feComponentTransfer', {"void": False})
   FE_COMPOSITE = ('feComposite', {"void": True})
   FE_CONVOLVE_MATRIX = ('feConvolveMatrix', {"void": True})
   FE_DIFFUSE_LIGHTING = ('feDiffuseLighting', {"void": False})
   FE_DISPLACEMENT_MAP = ('feDisplacementMap', {"void": True})
   FE_DROP_SHADOW = ('feDropShadow', {"void": True})
   FE_FLOOD = ('feFlood', {"void": True})
   FE_FUNC_A = ('feFuncA', {"void": True})
   FE_FUNC_B = ('feFuncB', {"void": True})
   FE_FUNC_G = ('feFuncG', {"void": True})
   FE_FUNC_R = ('feFuncR', {"void": True})
   FE_GAUSSIAN_BLUR = ('feGaussianBlur', {"void": True})
   FE_IMAGE = ('feImage', {"void": True})
   FE_MERGE = ('feMerge', {"void": False})
   FE_MERGE_NODE = ('feMergeNode', {"void": True})
   FE_MORPHOLOGY = ('feMorphology', {"void": True})
   FE_OFFSET = ('feOffset', {"void": True})
   FE_POINT_LIGHT = ('fePointLight', {"void": True})
   FE_SPECULAR_LIGHTING = ('feSpecularLighting', {"void": False})
   FE_SPOT_LIGHT = ('feSpotLight', {"void": True})
   FE_TILE = ('feTile', {"void": True})
   FE_TURBULENCE = ('feTurbulence', {"void": True})
   
   # --- Animation & Interactivity ---
   ANIMATE = ('animate', {"void": True})
   ANIMATE_MOTION = ('animateMotion', {"void": False})
   ANIMATE_TRANSFORM = ('animateTransform', {"void": True})
   SET = ('set', {"void": True})
   VIEW = ('view', {"void": True})
   FOREIGN_OBJECT = ('foreignObject', {"void": False}) # Embed HTML inside SVG
   # --- Containers & Text (Non-Void) ---
   G = ('g', {"void": False})           # Grouping
   DEFS = ('defs', {"void": False})     # Definitions
   TEXT = ('text', {"void": False})
   TSPAN = ('tspan', {"void": False})
   USE = ('use', {"void": True})        # Re-using shapes
   STOP = ('stop', {"void": True})      # For gradients
   @property
   def tag_name(self):
      return self.value[0]

   @property
   def is_void(self):
      return self.value[1]["void"]

   def render(self):
      if self.is_void:
         return f"<{self.tag_name} />"
      else:
         return f"<{self.tag_name}></{self.tag_name}>"
   @classmethod
   def get(cls, name, default=None):
      try:
         return cls[name.upper()]
      except KeyError:
         return default

class ElementAttributeValidator:
   """Class to validate HTML attributes for elements.
   This class checks if the provided attributes are valid for a given HTML element."""
         
   def __init__(self, element_tag: str = "", **kwargs):
        self.element_tag = element_tag if element_tag else "" 
        self.raw_attrs = kwargs
        self.valid_attrs = {}
        self.error_attrs = []
        
        # Run validation on init
        self.is_valid = self.validate()

   def validate(self) -> bool:
      """
      Core Logic. Returns True if all attributes are processed successfully.
      Populates self.valid_attrs with the final, clean dictionary.
      """
      if not self.raw_attrs:
         return True

      all_valid = True
      el_attr_definitions = ElementAttribute.ELEMENT_ATTRIBUTE.value
      # Access the master dictionary
      definitions = AttributeValue.ATTRIBUTE_VALUE.value

      for raw_key, value in self.raw_attrs.items():
         # 1. NORMALIZE KEY (class_ -> class, aria_hidden -> aria-hidden)
         
         key = raw_key.lower().strip().replace('_', '-')
         
         # --- SKIP PART 1: BOOLEANS ---
         if isinstance(value, bool):
               if value is True:
                  self.valid_attrs[key] = True 
               # If False, we ignore it (it won't render)
               continue 

         # --- SKIP PART 2: WILDCARDS ---
         # Bootstrap (data-*), HTMX (hx-*), Aria (aria-*), Events (on*), XML/Vue/Angular
         if key.startswith(('data-', 'aria-', 'hx-', 'on', 'xml', 'ng-', 'v-')):
               self.valid_attrs[key] = value
               continue

         if key in el_attr_definitions and self.element_tag not in el_attr_definitions[key]  :
            return False
         # --- SKIP PART 3: THE CLUSTER (Fast Pass) ---
         in_cluster = key in ATTR_CLUSTER

         # --- CHECK: DEFINITIONS ---
         if key in definitions:
               rule = definitions[key]
               
               # Case A: 'any' -> Accept anything
               if rule == 'any':
                  self.valid_attrs[key] = value
                  continue
               
               # Case B: List of allowed values -> Check it
               if isinstance(rule, list):
                  # Convert to string to handle ints safely
                  if str(value) not in rule:
                     self.error_attrs.append(f"{key}='{value}' (Expected: {rule})")
                     all_valid = False
                     continue
                  else:
                     self.valid_attrs[key] = value
                     continue
               
               # Case C: Dictionary (Element-Specific Rules) -> Check it
               if isinstance(rule, dict):
                  tag_clean = self.element_tag.strip('<>')
                  
                  if tag_clean in rule:
                     allowed_vals = rule[tag_clean]
                     if str(value) not in allowed_vals:
                           self.error_attrs.append(f"{key}='{value}' on <{tag_clean}> (Expected: {allowed_vals})")
                           all_valid = False
                           continue
                  else:
                     # Tag not specified in rule, be loose
                     self.valid_attrs[key] = value
                     continue

         # --- FALLBACK ---
         if in_cluster:
               self.valid_attrs[key] = value
         else:
               # Unknown/Custom attribute -> Allow it
               self.valid_attrs[key] = value

      return all_valid
