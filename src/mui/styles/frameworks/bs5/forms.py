from enum import Enum
from mui.styles.frameworks.bs5.utilities import Breakpoint, Color

class FormEnum(Enum):

    LABEL='form-label'
    
    CONTROL='form-control'
    CONTROL_SM=f'form-control-{Breakpoint.SM.value}'
    CONTROL_MD=f'form-control-{Breakpoint.MD.value}'
    CONTROL_LG=f'form-control-{Breakpoint.LG.value}'
    CONTROL_XL=f'form-control-{Breakpoint.XL.value}'
    CONTROL_XXL=f'form-control-{Breakpoint.XXL.value}'

    PLAIN_TEXT=f'form-control-plaintext'

    TEXTAREA='form-textarea'
    
    SELECT='form-select'
    SELECT_SM=f'form-select-{Breakpoint.SM.value}'
    SELECT_MD=f'form-select-{Breakpoint.MD.value}'
    SELECT_LG=f'form-select-{Breakpoint.LG.value}'
    SELECT_XL=f'form-select-{Breakpoint.XL.value}'
    SELECT_XXL=f'form-select-{Breakpoint.XXL.value}'
    
    CHECKBOX='form-check'
    CHECKBOX_LABEL='form-check-label'
    CHECKBOX_INPUT='form-check-input'
    CHECKBOX_INLINE='form-check-inline'
    
    SWITCH = 'form-switch'
    
    RANGE = 'form-range'
    
    GROUP= 'input-group'
    GROUP_TEXT='input-group-text'
    GROUP_SM=f'input-group-{Breakpoint.SM.value}'
    GROUP_MD=f'input-group-{Breakpoint.MD.value}'
    GROUP_LG=f'input-group-{Breakpoint.LG.value}'
    GROUP_XL=f'input-group-{Breakpoint.XL.value}'
    GROUP_XXL=f'input-group-{Breakpoint.XXL.value}'
    
    VALID= 'is-valid,'
    INVALID='is-invalid'
    VALID_FEEDBACK='valid-feedback'
    INVALID_FEEDBACK='invalid-feedback'
    NEEDS_VALIDATION = 'needs-validation'
    WAS_VALIDATED = 'was-validated'
    VALID_TOOLTIP = 'valid-tooltip'
    INVALID_TOOLTIP = 'invalid-tooltip'
    
    FLOATING='form-floating'
    COLOR = 'form-control-color'

    FORM_TEXT = "form-text"
    FORM_GROUP = "form-group"

    INPUT_GROUP_PREPEND = "input-group-prepend"
    INPUT_GROUP_APPEND = "input-group-append"

class Form:
    FORM = FormEnum
    @property
    def values_as_list(self):
        vals = []
        vals.extend([x.value for x in self.FORM])
        return vals