
from typing import Dict, Any
import re
from probo.context.context_logic import TemplateProcessor


class DjangoComponentTools(TemplateProcessor):
    """
    Helper methods to generate Django Template Language (DTL) syntax blocks.
    Inherited by DjangoComponent to provide a fluent API for template logic.
    """
    __slots__ = ()
    def __init__(self):
        super().__init__()

    def If(
        self, condition: str, content: str, else_content: str = None, **elif_blocks
    ) -> str:
        """
        Generates a standard Django IF block: {% if condition %}...{% endif %}

        Args:
            condition (str): The boolean expression to evaluate (e.g., "user.is_authenticated").
            content (str): The template content to render if the condition is true.
            else_content (str, optional): The content for the {% else %} block.
            **elif_blocks: Key-value pairs where keys are conditions and values are content for {% elif %} blocks.

        Returns:
            str: The fully formatted Django template string.
        """
        return self.if_true(
            condition,
            content,
            style="django",
            else_statement=else_content,
            **elif_blocks,
        )

    def For(
        self,
        item: str,
        iterable: str,
        content: str,
        empty_content=None,
    ) -> str:
        """
        Generates a Django FOR loop: {% for item in iterable %}...{% endfor %}

        Args:
            item (str): The variable name for the current item in the loop.
            iterable (str): The collection or iterable to loop over.
            content (str): The template content to repeat for each item.
            empty_content (str, optional): Content to render in the {% empty %} block if the iterable is empty.

        Returns:
            str: The fully formatted Django template string.
        """
        return self.for_loop(
            f"{item} in {iterable}",
            content,
            style="django",
            empty_content=empty_content,
        )

    def Var(self, variable_name: str) -> str:
        """
        Generates a Django variable tag: {{ variable_name }}

        Args:
            variable_name (str): The name of the variable to output.

        Returns:
            str: The formatted variable string.
        """
        return self.set_variable(variable_name)

    @staticmethod
    def With(assignments: str, content: str) -> str:
        """
        Generates a Django WITH block: {% with x=1 y=2 %}...{% endwith %}

        Args:
            assignments (str): The variable assignments (e.g., "total=business.employees.count").
            content (str): The content where these variables are available.

        Returns:
            str: The formatted with-block string.
        """
        return f"{{% with {assignments} %}}\n{content}\n{{% endwith %}}"

    @staticmethod
    def Comment(content: str) -> str:
        """
        Generates a Django comment block: {# comment #}

        Args:
            content (str): The text content of the comment.

        Returns:
            str: The formatted comment string.
        """
        return f"{{# {content} #}}"

    @staticmethod
    def Include(template_name: str, with_args: str = None) -> str:
        """
        Generates a Django INCLUDE tag: {% include 'name' %}

        Args:
            template_name (str): The path/name of the template to include.
            with_args (str, optional): Additional context variables to pass (e.g., "arg=value").

        Returns:
            str: The formatted include tag.
        """
        args = f" with {with_args}" if with_args else ""
        return f"{{% include '{template_name}'{args} %}}"

    @staticmethod
    def Csrf() -> str:
        """
        Generates the Django CSRF token tag: {% csrf_token %}

        Returns:
            str: The csrf token tag.
        """
        return "{% csrf_token %}"

    @staticmethod
    def Load(library: str) -> str:
        """
        Generates a Django LOAD tag: {% load library %}

        Args:
            library (str): The name of the template library to load (e.g., "static").

        Returns:
            str: The formatted load tag.
        """
        return f"{{% load {library} %}}"

class DjangoComponent:
    """
    A declarative builder for Django Templates.
    Allows defining 'extends', 'blocks', raw template strings, and variables in Python.

    This class is framework-agnostic at import time. Actual rendering
    requires Django to be installed and configured in the execution environment.
    """
    __slots__ = (
        'raw_template',
        'context',
        'extends_from',
        'blocks',
        'variables',
    )

    def __init__(
        self,
        template_string: str = "",
        context: Dict[str, Any] = None,
        extends: str = None,
        **kwargs,
    ):
        """
        Initializes the DjangoComponent builder.

        Args:
            template_string (str, optional): The base raw template content.
            context (Dict[str, Any], optional): Initial context dictionary.
            extends (str, optional): The parent template to extend.
            **kwargs: Additional variables to be added to the context.
        """
        self.raw_template = template_string
        self.context = context or {}
        self.extends_from = extends
        self.blocks: Dict[str, str] = {}
        # Store variables passed as kwargs for substitution
        self.variables = kwargs
        super().__init__()

    def extends(self, template_name: str):
        """
        Sets the parent template (e.g. 'base.html').

        Args:
            template_name (str): The name/path of the parent template.

        Returns:
            DjangoComponent: Self, for method chaining.
        """
        self.extends_from = template_name
        return self

    def add_block(self, name: str, content: str):
        """
        Adds a named block to the template: {% block name %}...{% endblock %}

        Args:
            name (str): The name of the block.
            content (str): The content to insert into the block.

        Returns:
            DjangoComponent: Self, for method chaining.
        """
        self.blocks[name] = content
        return self

    def set_variables(self, **kwargs):
        """
        Sets context variables for the template.
        These are merged into the context at render time.

        Args:
            **kwargs: Key-value pairs representing template variables.

        Returns:
            DjangoComponent: Self, for method chaining.
        """
        self.variables.update(kwargs)
        return self

    def _build_vars(self, source: str) -> str:
        """
        Compiles internal variable syntax into valid Django Template syntax.
        Converts <$probo-var name='variable_name'/>  -->  {{ variable_name }}

        Args:
            source (str): The template string containing internal variable placeholders.

        Returns:
            str: The template string with valid Django variable tags.
        """
        # Regex matches <$probo-var name='...'/> or name="..."
        pattern = r"<\$probo-var\s+name=['\"](.*?)['\"]\s*/>"

        # Replace matches with Django variable syntax {{ ... }}
        compiled_source = re.sub(pattern, r"{{\1}}", source)

        return compiled_source

    def build_source(self) -> str:
        """
        Constructs the final raw Django Template string by assembling extensions, blocks, and content.

        It combines:
        1. The {% extends %} tag (if present).
        2. All defined blocks.
        3. Any raw template content.
        4. Variable syntax translation.

        Returns:
            str: The complete, renderable Django template source string.
        """
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

        # 3. Apply Variable Substitution (probo -> Django syntax)
        return self._build_vars(raw_source)

    def render(
        self,
    ) -> str:
        """
        Renders the constructed template using Django.

        This method compiles the source and returns it as a string.
        Note: This currently returns the *source* string, but in a real Django environment,
        this would likely interact with `django.template.Template` and `Context`.

        Returns:
            str: The final template source string (ready for Django engine processing).
        """
        source = self.build_source()
        return source
