# context_logic/processor.py
import re
from typing import Any, Optional, Callable, Dict
from dataclasses import dataclass, field
from collections.abc import Iterable


class TemplateProcessor:
    """
    A class to process only 'mui' style template blocks but with support
    for generating Django-style template tags. Static methods are included.
    """

    SUPPORTED_STYLES = ["django", "mui"]

    def __init__(self, data_context: dict = None):
        """
        Initializes the processor with a global data context.

        Args:
            data_context (dict, optional): A dictionary of global variables available
                                           to all templates rendered by this instance.
        """
        self._global_data_context = data_context if data_context is not None else {}

    def _evaluate_expression(self, expression: str, current_context: dict) -> Any:
        """
        Safely evaluates a string expression within a given context.

        Args:
            expression (str): The python-like expression to evaluate (e.g., "user.is_active").
            current_context (dict): The local context variables available for this evaluation.

        Returns:
            Any: The result of the evaluation, or None if an error occurs.
        """
        full_context = {**self._global_data_context, **current_context}
        try:
            return eval(expression, {}, full_context)
        except Exception as e:
            print(f"Error evaluating expression '{expression}': {e}")
            return None

    def _apply_filter(self, value: Any, filter_name: str) -> Any:
        """
        Applies a named transformation filter to a value.

        Supported filters: 'upper', 'lower', 'title', 'length'.

        Args:
            value (Any): The value to transform.
            filter_name (str): The name of the filter to apply.

        Returns:
            Any: The transformed value, or the original value if the filter is unknown.
        """
        filters = {
            "upper": lambda v: str(v).upper(),
            "lower": lambda v: str(v).lower(),
            "title": lambda v: str(v).title(),
            "length": lambda v: len(v) if hasattr(v, "__len__") else len(str(v)),
        }
        return filters.get(filter_name, lambda v: v)(value)

    def _process_template_block(self, text: str, current_context: dict) -> str:
        """
        recursively processes template logic within the text.

        It handles loops, conditional blocks, and variable substitutions
        in that specific order to ensure nested structures are rendered correctly.

        Args:
            text (str): The raw template string containing custom tags.
            current_context (dict): The data context for rendering.

        Returns:
            str: The fully rendered text string.
        """
        text = self._process_for_loops(text, current_context)
        text = self._process_if_blocks(text, current_context)
        text = self._process_variables(text, current_context)
        return text

    def _process_if_blocks(self, text: str, context: dict) -> str:
        """
        Parses and evaluates custom <$if>...<$elif>...<$else>...<$/if> tags.

        It supports evaluating conditions dynamically against the provided context.

        Args:
            text (str): The text containing IF blocks.
            context (dict): The data context used to evaluate the conditions.

        Returns:
            str: The text with the correct block content retained and tags removed.
        """
        # Matches <$if condition> ... <$else> ... </$if>
        if_pattern = re.compile(
            r"<\$if (.+?)>(.*?)"
            r"(?:(?:<\$elif (.+?)>(.*?))*)"
            r"(?:<\$else>(.*?))?"
            r"</\$if>",
            re.DOTALL,
        )

        def repl(match):
            condition = match.group(1).strip()
            if_block = match.group(2)
            elif_condition = match.group(3)
            elif_block = match.group(4)
            else_block = match.group(5)

            try:
                if self._evaluate_expression(condition, context):
                    return self._process_template_block(if_block, context)
                elif elif_condition and self._evaluate_expression(
                    elif_condition, context
                ):
                    return self._process_template_block(elif_block, context)
                elif else_block:
                    return self._process_template_block(else_block, context)
            except Exception as e:
                print(f"Error in IF evaluation: {e}")
            return ""

        return if_pattern.sub(repl, text)

    def _process_for_loops(self, text: str, context: dict) -> str:
        """
        Parses and evaluates custom <$for item in iterable>...<$/for> tags.

        Iterates over the provided collection and repeats the block content
        for each item.

        Args:
            text (str): The text containing FOR loops.
            context (dict): The data context containing the iterable variables.

        Returns:
            str: The text with the loop fully expanded.
        """
        for_pattern = re.compile(r"<\$for (.+?) in (.+?)>(.*?)</\$for>", re.DOTALL)

        def repl(match):
            loop_var = match.group(1).strip()
            iterable = self._evaluate_expression(match.group(2).strip(), context)
            loop_content = match.group(3)

            if not iterable:
                return ""
            result = []
            for item in iterable:
                local_context = {**context, loop_var: item}
                result.append(self._process_template_block(loop_content, local_context))
            return "".join(result)

        return for_pattern.sub(repl, text)

    def _process_variables(self, text: str, context: dict) -> str:
        """
        Replaces {{ variable|filter }} syntax with actual values from the context.

        Args:
            text (str): The text containing variable placeholders.
            context (dict): The data context to look up values.

        Returns:
            str: The text with variables replaced by their string representations.
        """
        # Matches variables like {{ var|filter }}
        var_pattern = re.compile(r"\{\{ (.+?) \}\}")

        def repl(match):
            expr = match.group(1)
            if "|" in expr:
                var_name, filter_name = expr.split("|", 1)
                value = self._evaluate_expression(var_name.strip(), context)
                return str(self._apply_filter(value, filter_name.strip()))
            return str(self._evaluate_expression(expr.strip(), context) or "")

        return var_pattern.sub(repl, text)

    def render_template(self, template_string: str, context: dict = None) -> str:
        """
        The main entry point for rendering a template string.

        Merges the instance's global context with the provided local context
        and processes all template blocks (loops, ifs, vars).

        Args:
            template_string (str): The raw template string to render.
            context (dict, optional): Additional local context for this specific render.

        Returns:
            str: The fully rendered string.
        """
        effective_context = {**self._global_data_context, **(context or {})}
        return self._process_template_block(template_string, effective_context)

    # ---------- STATIC METHODS FOR BLOCK CREATION ----------

    @staticmethod
    def if_true(
        expression, if_block, style="mui", else_statement=None, **elif_statements
    ):
        """
        Generates a conditional block string in the specified style (MUI or Django).

        Args:
            expression (str): The condition to evaluate (e.g., "user.is_admin").
            if_block (str): Content to render if true.
            style (str): The syntax style to generate ("mui" or "django").
            else_statement (str, optional): Content for the else block.
            **elif_statements: Key-value pairs where key is condition and value is content for elif blocks.

        Returns:
            str: The formatted conditional block string.
        """
        if style == "mui":
            return (
                f"<$if {expression}>{if_block}"
                + "".join(
                    [
                        f"<$elif {cond}>{block}"
                        for cond, block in elif_statements.items()
                    ]
                )
                + (f"<$else>{else_statement}" if else_statement else "")
                + "</$if>"
            )
        elif style == "django":
            return (
                f"{{% if {expression} %}}{if_block}"
                + "".join(
                    [
                        f"{{% elif {cond} %}}{block}"
                        for cond, block in elif_statements.items()
                    ]
                )
                + (f"{{% else %}}{else_statement}" if else_statement else "")
                + "{% endif %}"
            )
        else:
            return ""

    @staticmethod
    def for_loop(expression, for_block, style="mui", empty_content=None):
        """
        Generates a for-loop block string in the specified style.

        Args:
            expression (str): The loop expression (e.g., "item in items").
            for_block (str): The content to repeat inside the loop.
            style (str): The syntax style to generate ("mui" or "django").
            empty_content (str, optional): Content to display if the iterable is empty (Django style only).

        Returns:
            str: The formatted loop block string.
        """
        empty = f"{{% empty %}} {empty_content}" if empty_content else ""
        if style == "mui":
            return f"<$for {expression}>{for_block}</$for>"
        elif style == "django":
            return f"{{% for {expression} %}}{for_block}{empty}{{% endfor %}}"
        else:
            return ""

    @staticmethod
    def set_variable(
        expression,
    ):
        """
        Generates a variable output string.

        Args:
            expression (str): The variable expression to output (e.g., "user.name").

        Returns:
            str: The formatted variable string (e.g., "{{ user.name }}").
        """
        return f" {{{{ {expression} }}}}"

def loop(data, renderer):
    """
    Iterates over data and generates elements using a renderer function.

    Args:
        data: An int (for simple duplication), a dict, or an iterable (list/queryset).
        renderer: A function/lambda that takes the item(s) and returns an Element,
                  OR a static Element to simply duplicate.

    Returns:
        A list of rendered elements.
    """
    results = []
    iterator = []
    if not renderer:
        renderer = lambda u: u
    # --- 1. NORMALIZE INPUT TO ITERATOR ---
    if isinstance(data, int):
        # Case: Integer -> Repeat N times
        # We use range so the renderer gets the index (0, 1, 2...)
        iterator = range(data)
    elif isinstance(data, dict):
        # Case: Dictionary -> Iterate over (key, value) pairs
        iterator = data.items()
    elif isinstance(data, Iterable) and not isinstance(data, (str, bytes)):
        # Case: List, QuerySet, Tuple, etc.
        iterator = data
    else:
        # Fallback: Treat as single item list
        iterator = [data]
    # --- 2. EXECUTE LOOP ---
    for item in iterator:
        if callable(renderer):
            # Dynamic: Pass data to the function (The "Placeholder" concept)
            if isinstance(data, dict):
                # For dicts, unpack key and value: renderer(key, value)
                key, value = item
                results.append(renderer(key, value))
            else:
                # For lists/ints, pass the single item: renderer(item)
                results.append(renderer(item))
    return results

class TemplateComponentMap:
    """Template Components Map is the cordinator that serves the right component to spesific view"""

    def __init__(self, r_props: dict[str, Any] = None, **url_name_comp):
        self.url_name_comp = url_name_comp
        self.r_props = r_props or {}

    def get_component(self, url_name) -> str | tuple:
        """
        Retrieves a component associated with a URL name and injects request properties.

        Args:
            url_name (str): The key/name representing the URL route.

        Returns:
            str | tuple: The rendered component (usually a string or HTML tuple).

        Raises:
            ValueError: If the url_name does not exist in the map.
        """
        comp = self.url_name_comp.get(url_name, None)
        if comp:
            comp.props["request-props"] = self.r_props.get("request-props", {})
            comp.props["state-prop"] = self.r_props.get("state-prop", {})
            return comp.render()

        else:
            raise ValueError("no such url maping")

    def set_component(self, url_name=None, component_name=None, **url_name_comp):
        """
        Registers new components or updates existing mappings.

        Args:
            url_name (str, optional): The specific URL key to update.
            component_name (object, optional): The component object to associate.
            **url_name_comp: Additional mappings passed as keyword arguments.

        Returns:
            TemplateComponentMap: Self, allowing for method chaining.
        """
        self.url_name_comp.update(url_name_comp)
        if url_name and component_name:
            self.url_name_comp[url_name] = component_name
        return self

@dataclass
class StaticData:
    """
    data class to define and get statiic data for rendering components
    """

    static_data: dict[str, Any]

    def get(self, Value):
        """
        Retrieves a value from the static data dictionary.

        Args:
            Value (str): The key to look up.

        Returns:
            Any: The value associated with the key, or None if not found.
        """
        return self.static_data.get(Value, None)

@dataclass
class DynamicData:
    """
    data class to define and get dynamic data (from user or db) with custom manipulation plug in function for rendering components
    """

    data_obj: Optional[object] = None
    processor: Optional[Callable[[Any], Dict]] = None
    dynamic_data: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """
        This runs AUTOMATICALLY immediately after __init__.
        It processes the data_obj and populates dynamic_data instantly.
        """
        if self.processor and callable(self.processor) and self.data_obj:
            self.dynamic_data = self.processor(self.data_obj)
        elif isinstance(self.data_obj, dict):
            self.dynamic_data = self.data_obj

    def get(self, Value):
        """
        Retrieves a value from the processed dynamic data.

        Args:
            Value (str): The key to look up.

        Returns:
            Any: The value associated with the key, or None if not found.
        """
        return self.dynamic_data.get(Value, None)

    # Optional: Keep this if you want a "Safe Accessor" that ensures a Dict return type
    @property
    def data(self) -> Dict:
        """
        Safely accesses the full dynamic data dictionary.

        Returns:
            Dict: The dynamic data dictionary, ensuring a dict type is returned even if empty.
        """
        return self.dynamic_data or {}
