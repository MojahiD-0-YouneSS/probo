from dataclasses import dataclass,field
from typing import (
    Any,
    Optional,
    Iterable,
    List,
    Dict,
    Union,
)

class StatePropsValidator:
    """
    Processes the rules defined in a StateProps object
    against a component's final props dictionary.
    """

    def __init__(self, rules: 'StateProps', props: dict) -> None:
        self.rules=rules
        self.props=props
        
    def is_valid(self,) -> bool:
        """
        Checks if the component's props satisfy ALL defined rules.
        Returns True if all constraints pass, False otherwise.
        
        'props' is the dictionary containing all component data,
        including 'user', 'session', etc.
        """
        result = list()
        if not self.rules.display_it:
            return False
        # We run each check. If any single check fails, we stop
        # and return False immediately.
        
        if not self._check_equals(self.rules.prop_equals, self.props):
            result.append(False)
        else:
            result.append(True)
            
        if not self._check_is_in(self.rules.prop_is_in, self.props):
            result.append(False)
        else:
            result.append(True)
            
        if not self._check_truthy(self.rules.prop_is_truthy, self.props):
            result.append(False)
        else:
            result.append(True)
            
        if not self._check_has_attributes(self.rules.prop_has_attributes, self.props):
            result.append(False)
        else:
            result.append(True)
            
        if not self._check_permissions(self.rules.has_permissions, self.props):
            result.append(False)
        else:
            result.append(True)
        
        if not self._check_s_props(self.rules.s_props, self.props):
            result.append(False)
        else:
            result.append(True)
        if self.rules.required and not all(result):
            
            return False
        else:
        # If all checks passed
            return all(result)

    # --- Private Logic Methods ---

    def _check_equals(self, rules_dict: Optional[Dict[str, Any]], props: dict) -> bool:
        """Logic for: prop_equals"""
        if rules_dict:
            for key, required_value in rules_dict.items():
                if key not in props:
                    return False  # The required prop doesn't even exist
                if props[key] != required_value:
                   return False  # The value does not match
        return True  # All checks passed

    def _check_is_in(self, rules_dict: Optional[Dict[str, List[Any]]], props: dict) -> bool:
        """Logic for: prop_is_in"""
        if rules_dict:
            for key, allowed_values in rules_dict.items():
                if not isinstance(allowed_values, (list, set, tuple)):
                    # Rule is misconfigured, fail safely
                    return False 
                if key not in props:
                    return False  # The required prop doesn't exist
                if props[key] not in allowed_values:
                    return False  # The value is not in the allowed list
        return True  # All checks passed

    def _check_truthy(self, rules_list: Optional[List[str]], props: dict) -> bool:
        """Logic for: prop_is_truthy"""
        if rules_list:
            for key in rules_list:
                if key not in props:
                    return False  # The required prop doesn't exist
                if not props[key]:
                    # Fails if prop is None, False, 0, "", [], {}, etc.
                    return False
        return True  # All checks passed

    def _check_has_attributes(self, rules_dict: Optional[Dict[str, List[str]]], props: dict) -> bool:
        """Logic for: prop_has_attributes"""
        if rules_dict:
            for key, required_attrs in rules_dict.items():
                if key not in props:
                    return False  # The required prop (object) doesn't exist
                
                obj_to_check = props[key]
                
                for attr_name in required_attrs:
                    if not hasattr(obj_to_check, attr_name):
                        return False  # The object is missing a required attribute
        return True  # All checks passed

    def _check_permissions(self, permission_list: Optional[list[str]], props: dict) -> bool:
        """Logic for: has_permission"""
        if not permission_list:
            return True  # No permission rule was defined, so it passes

        # To check permissions, we MUST have a 'user' object in props
        if 'user' not in props:
            return False  # Cannot check permissions without a user
            
        user = props['user']

        # Check if the user object is a valid Django user (or mock)
        if not hasattr(user, 'has_perm'):
            return False  # Not a valid user object

        # The final check against Django's permission system
        if not all(user.has_perm(perm) for perm in permission_list):
            return False
            
        return True  # User has the permission
    
    def _check_s_props(self,s_props:dict,props:dict) -> bool:
        
        if not s_props:
            return True

        #return self.props.items() <= props.items()
        def __exists_in_dict(x):
            status = list()
            for value in props.values():
                # Check key
                if x == value:
                    status.append( True)
                # Check nested dict
                else:
                    # Check nested key or nested value
                    status.append( False)
            return any(status)

        def valid_props(props):
            if not all([x in props for x in s_props]):
                return False
            else:
                return all([__exists_in_dict(x) for x in s_props.values()])
            
        return valid_props(props=props)


@dataclass
class StateProps:
    """
    A dataclass that holds a set of declarative rules (constraints)
    to validate against a component's incoming props.
    
    If all rules pass, the element is rendered.
    """
    
    # Rule: Checks if props[key] == required_value
    # Example: {'status': 'published', 'is_active': True}
    prop_equals: Optional[Dict[str, Any]] = field(default_factory=dict)

    # Rule: Checks if props[key] is IN allowed_values
    # Example: {'user_role': ['admin', 'editor']}
    prop_is_in: Optional[Dict[str, List[Any]]] = field(default_factory=dict)

    # Rule: Checks if props[key] is "truthy" (not None, False, 0, "", [])
    # Example: ['user', 'items_list']
    prop_is_truthy: Optional[List[str]] = field(default_factory=list)

    # Rule: Checks if props[key] (an object) has the listed attributes
    # Example: {'user': ['is_staff', 'email']}
    prop_has_attributes: Optional[Dict[str, List[str]]] = field(default_factory=dict)

    # Rule: Checks if props['user'] has a specific Django permission
    # Example: "app_label.can_edit_post"
    has_permissions: Optional[list[str]] = field(default_factory=list)

    s_props :dict = field(default_factory=dict)

    element_state_id:str=field(default_factory=str)

    required:bool=field(default_factory=bool)
    
    display_it:bool=field(default=True)

    
    def get_prop(self,prom):
        return self.s_props.get(prom,None)
    def render_as_dict(self,) -> dict[str,Any]:
        return {
            'prop_equals':self.prop_equals,
            'prop_is_in':self.prop_is_in,
            'prop_is_truthy':self.prop_is_truthy,
            'prop_has_attributes':self.prop_has_attributes,
            'has_permissions':self.has_permissions,
            's_props':self.s_props,
            'element_state_id':self.element_state_id,
            'required':self.required,
            'display_it':self.display_it,
        }
    def validator(self, props:dict)-> StatePropsValidator:
        return StatePropsValidator(rules=self,props=props)