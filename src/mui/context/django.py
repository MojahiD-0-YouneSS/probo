from typing import Dict, Any, Optional
import re
from mui.context.context_logic import TemplateProcessor

class DjangoComponentTools(TemplateProcessor):
    """
    Helper methods to generate Django Template Language (DTL) syntax blocks.
    Inherited by DjangoComponent to provide a fluent API for template logic.
    """
    def __init__(self):
        super().__init__()
    def If(self,condition: str, content: str, else_content: str = None,**elif_blocks) -> str:
        """Generates {% if condition %}...{% endif %}"""
        return self.if_true(condition, content, style='django', else_statement=else_content, **elif_blocks)

    def For(self,item: str, iterable: str, content: str, empty_content=None,) -> str:
        """Generates {% for item in iterable %}...{% endfor %}"""
        
        return self.for_loop(f"{item} in {iterable}", content, style='django',empty_content=empty_content)

    def Var(self, variable_name: str) -> str:
        """Generates {{ variable_name }}"""
        return self.set_variable(variable_name)
    @staticmethod
    def With(assignments: str, content: str) -> str:
        """Generates {% with x=1 y=2 %}...{% endwith %}"""
        return f"{{% with {assignments} %}}\n{content}\n{{% endwith %}}"

    @staticmethod
    def Comment(content: str) -> str:
        """Generates {# comment #}"""
        return f"{{# {content} #}}"

    @staticmethod
    def Include(template_name: str, with_args: str = None) -> str:
        """Generates {% include 'name' %}"""
        args = f" with {with_args}" if with_args else ""
        return f"{{% include '{template_name}'{args} %}}"

    @staticmethod
    def Csrf() -> str:
        """Generates {% csrf_token %}"""
        return "{% csrf_token %}"

    @staticmethod
    def Load(library: str) -> str:
        """Generates {% load library %}"""
        return f"{{% load {library} %}}"


class DjangoComponent:
    """
    A declarative builder for Django Templates.
    Allows defining 'extends', 'blocks', raw template strings, and variables in Python.
    
    This class is framework-agnostic at import time. Actual rendering
    requires Django to be installed and configured in the execution environment.
    """
    def __init__(self, template_string: str = "", context: Dict[str, Any] = None, extends: str = None, **kwargs):
        self.raw_template = template_string
        self.context = context or {}
        self.extends_from = extends
        self.blocks: Dict[str, str] = {}
        # Store variables passed as kwargs for substitution
        self.variables = kwargs 
        super().__init__()
        
    def extends(self, template_name: str):
        """Sets the parent template (e.g. 'base.html')."""
        self.extends_from = template_name
        return self

    def add_block(self, name: str, content: str):
        """Adds a {% block name %}...{% endblock %} section."""
        self.blocks[name] = content
        return self

    def set_variables(self, **kwargs):
        """
        Sets context variables for the template.
        These are merged into the context at render time.
        """
        self.variables.update(kwargs)
        return self

    def _build_vars(self, source: str) -> str:
        """
        Compiles MUI Variable syntax into Django Template syntax.
        <$mui-var name='variable_name'/>  -->  {{ variable_name }}
        """
        # Regex matches <$mui-var name='...'/> or name="..."
        pattern = r"<\$mui-var\s+name=['\"](.*?)['\"]\s*/>"
        
        # Replace matches with Django variable syntax {{ ... }}
        compiled_source = re.sub(pattern, r"{{\1}}", source)
        
        return compiled_source

    def build_source(self) -> str:
        """Constructs the raw Django Template string."""
        parts = []
        
        # 1. Extends
        if self.extends_from:
            parts.append(f"{{% extends '{self.extends_from}' %}}")

        # 2. Blocks (If extending) or Raw Content (If not)
        if self.blocks:
            for name, content in self.blocks.items():
                parts.append(f"{{% block {name} %}}{content}{{% endblock %}}")
        
        # Append raw template content if not just blocks
        if self.raw_template:
            parts.append(self.raw_template)

        raw_source = "\n".join(parts)

        # 3. Apply Variable Substitution (MUI -> Django syntax)
        return self._build_vars(raw_source)

    def render(self, ) -> str:
        """
        Renders the constructed template using Django.
        Safe to call only if Django is installed and configured.
        """
        source = self.build_source()
        return source
