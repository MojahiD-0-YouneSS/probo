import functools
import inspect
from typing import Callable, List, Dict


class LazyClassWrapper:
    """
    Defers OOP Class instantiation until the exact moment of rendering/streaming.
    """

    __slots__ = ("cls", "injected_el", "content", "kwargs", "extra_attrs")

    def __init__(self, cls, injected_el, *content, **kwargs):
        self.cls = cls
        self.injected_el = injected_el
        self.content = content
        self.kwargs = kwargs
        self.extra_attrs = {}
    
    def include_extra_attrs(self,**attrs):
        self.extra_attrs.update(attrs)
        return self
    def render(self, *args, **kw):
        # 1. Instantiate the class ONLY when rendering begins
        instance = self.cls(*self.content, **self.kwargs)
        # 2. Inject EL into the render method if required
        if self.injected_el:
            return instance.render(self.injected_el)
        return instance.render()

    def stream(self, *args, batch_size=50, **kw):
        # 1. Instantiate the class ONLY when streaming begins
        instance = self.cls(*self.content, **self.kwargs)
        batch_size = self.extra_attrs.get('batch',batch_size)
        # 2. Inject EL into the stream method if required
        if self.injected_el:
            yield from instance.stream(self.injected_el, batch_size=batch_size)
        else:
            yield from instance.stream(batch_size=batch_size)

class ProboFunctionalExecuter:
    """
    Probo Functional DSL: The Ultimate Developer Experience

    Building deep, complex HTML trees using functional programming often leads to "Parenthesis Hell" (deeply nested function calls that are hard to read and format).

    Probo solves this with the ProboFunctionalExecuter and its custom Domain Specific Language (DSL). By leveraging operator overloading (+ and /) and lazy evaluation, you can build massive, complex DOM trees with zero indentation and perfect readability.

    1. The Core Components

    To use the DSL, you need two things: the Executer and the Tuplizer (_).

    from probo.executer import ProboFunctionalExecuter, tuplizer as _
    from probo import div, h1, p, a
    from probo.components.light_tags import l_div



    ProboFunctionalExecuter: The engine that manages the AST (Abstract Syntax Tree) paths and lazily evaluates the nodes.

    _ (The Tuplizer): A tiny helper function that cleanly bundles your tags, content, and kwargs into a format the Executer can read, saving you from writing ugly dictionaries.

    2. Initializing the Tree

    Everything starts with a Root node.

    # Initialize with a root tag (div) and optional attributes
    exe = ProboFunctionalExecuter(div, id="app-root", Class="container")


    At this point, the AST looks like this: {"root": <div id="app-root" class="container">}

    3. The + Operator (Add to Path)

    Use the + operator to quickly add anonymous leaf nodes.

    If you don't specify a path, it defaults to adding directly to the "root".

    # Add to root: exe + _(tag, *content, **kwargs)
    exe += _(h1, "Admin Dashboard", Class="text-xl")
    exe += _(p, "Welcome back, user.")

    # Add to a specific path: exe + _("path", tag, *content, **kwargs)
    # (We will create the "sidebar" path in the next step)


    4. The / Operator (Smart Nesting & Routing)

    The / operator is the workhorse of the Probo DSL. It features Smart Routing depending on the arguments you pass it:

    A. Branching (Nesting)

    If you pass a string as the second argument, the Executer creates a named branch that you can target later.

    Syntax: exe / _("parent_path", "new_branch_name", tag, **kwargs)

    # Create a branch named "sidebar" under "root"
    exe /= _("root", "sidebar", div, Class="sidebar-dark")

    # Create a branch named "nav" under "root.sidebar"
    exe /= _("root.sidebar", "nav", div, role="navigation")


    B. Leaf Addition

    If you pass a Callable Tag as the second argument, the Executer treats it as an anonymous leaf addition (just like + but for a specific path).

    Syntax: exe / _("target_path", tag, *content, **kwargs)

    # Add links directly to the "root.sidebar.nav" path
    exe /= _("root.sidebar.nav", a, "Home", href="/home")
    exe /= _("root.sidebar.nav", a, "Settings", href="/settings")


    5. Chaining It All Together

    Because the operators return the Executer instance (self), you can chain operations flawlessly. This is where the DX truly shines:

    shared_el = Element()
    exe = ProboFunctionalExecuter(div, id="main-layout").include_dependency(EL=shared_el)

    (
        exe
        + _(h1, "System Overview", Class="title")
        / _("root", "grid", div, Class="grid-layout")
        / _("root.grid", "col1", div, Class="col-span-1")
        / _("root.grid", "col2", div, Class="col-span-2")
        / _("root.grid.col1", p, "Stats go here")
        / _("root.grid.col2", l_div, "Light Node Graph Component")
    )


    6. Execution & Smart Dependency Injection

    Nothing is actually rendered or stored in memory during the building phase. The Executer simply maps out lazy functools.partial callbacks.

    When you are ready, call .execute():

    html_string = exe.execute()

    # Render eagerly to a string

    # OR Stream it in O(1) memory with args stream and batch set up
    for chunk in final_tree:
        response.write(chunk)


    🧠 The Dependency Injection Magic

    Notice in the chained example above, we used l_div (a Light tag that requires a shared EL pipeline to render).

    You do not need to pass EL manually. The ProboFunctionalExecuter uses Python's inspect module to check the signature of every tag it executes. If it detects a tag or class render method asking for EL, it automatically injects the shared_el you provided via .include_dependency().
    """

    _signature_cache = {}

    @classmethod
    def _get_tag_func_meta(cls, tag_func):
        """
        Caches the inspection of tag functions and classes.
        inspect.signature is very slow and the AST builds execute this thousands of times.
        This memoizes whether a target is a class and whether it requires the 'EL' pipeline.
        """
        if tag_func in cls._signature_cache:
            return cls._signature_cache[tag_func]
        
        is_class = inspect.isclass(tag_func)
        requires_el = False
        
        if is_class:
            for method_name in ("render", "stream"):
                if hasattr(tag_func, method_name):
                    try:
                        sig = inspect.signature(getattr(tag_func, method_name))
                        if "EL" in sig.parameters:
                            requires_el = True
                            break
                    except (ValueError, TypeError):
                        pass
        else:
            try:
                sig = inspect.signature(tag_func)
                params = list(sig.parameters.values())
                if params and params[0].name == "EL":
                    requires_el = True
            except (ValueError, TypeError):
                pass
                
        cls._signature_cache[tag_func] = (is_class, requires_el)
        return is_class, requires_el

    def __init__(self, root_tag,*content, stream=False,batch:int=50,use_EL:bool=False, **root_attrs):
        self.use_EL=use_EL
        self._nodes = {
            "root": {
                "tag": root_tag,
                "content": list(content) if type(content) is tuple else [content],
                "attrs": root_attrs,
                "children": [],
            }
        }
        self.default_flags = {"stream": stream,"batch":batch,}
        self.dependencies = {}
        self._callable_cache = {}
        if use_EL:
            from probo.components.elements import Element
            self.dependencies['EL']=Element()
    
    def include_dependency(self, **deps):
        """Injects shared state (like EL=Element()) into the context."""
        self.dependencies.update(deps)
        return self


    def find(
        self,
        tag=None,
        attrs: dict = None,
        content: str = None,
        predicate: Callable = None,
    ) -> List[Dict]:
        """
        Traverses the AST to find branches or anonymous leaves matching specific criteria.
        Because it returns the actual dictionary references, you can modify the returned nodes
        to mutate the AST before execution!
        """
        results = []

        def match_node(node_def: dict) -> bool:
            # 1. Custom Predicate Check
            if predicate and not predicate(node_def):
                return False

            # 2. Tag Check (Supports direct function comparison or string name)
            if tag is not None:
                node_tag = node_def.get("tag")
                tag_name = getattr(node_tag, "__name__", str(node_tag))
                if node_tag != tag and tag_name != tag:
                    return False

            # 3. Attributes Check (Must contain all specified key/value pairs)
            if attrs:
                node_attrs = node_def.get("attrs", {})
                for k, v in attrs.items():
                    if node_attrs.get(k) != v:
                        return False

            # 4. Content Check (Substring match within any content item)
            if content is not None:
                node_content = node_def.get("content", [])
                if not any(content in str(c) for c in node_content):
                    return False

            return True

        # Search all named paths and their anonymous children
        for path, node_def in self._nodes.items():
            # Check the named branch itself
            if match_node(node_def):
                results.append({"path": path, "type": "branch", "node": node_def})

            # Check all anonymous leaf children inside this branch
            for child in node_def.get("children", []):
                if child.get("type") == "anonymous" and match_node(child):
                    results.append({"path": path, "type": "anonymous", "node": child})

        return results

    def nest(
        self, parent_path: str, new_path_name: str, tag_func, *content, **user_attrs
    ):
        if parent_path not in self._nodes:
            raise ValueError(f"Path '{parent_path}' not found")

        full_path = f"{parent_path}.{new_path_name}"
        self._nodes[full_path] = {
            "tag": tag_func,
            "content": list(content),
            "attrs": user_attrs,
            "children": [],
        }
        self._nodes[parent_path]["children"].append(
            {"type": "path", "value": full_path}
        )
        return self

    def add_to(self, target_path: str, tag_func, *content, **user_attrs):
        if target_path not in self._nodes:
            raise ValueError(f"Path '{target_path}' not found")

        self._nodes[target_path]["children"].append(
            {
                "type": "anonymous",
                "tag": tag_func,
                "content": list(content),
                "attrs": user_attrs,
            }
        )
        return self

    def _prepare_node_callable(self, tag_func, user_attrs):
        if not callable(tag_func):
            return lambda *args: str(tag_func)

        cache_key = None
        if not user_attrs:
            cache_key = tag_func
        else:
            try:
                cache_key = (tag_func, frozenset(user_attrs.items()))
            except TypeError:
                pass # user_attrs has unhashable types, skip cache

        if cache_key is not None and cache_key in self._callable_cache:
            return self._callable_cache[cache_key]

        is_class, requires_el = self._get_tag_func_meta(tag_func)

        # ==========================================
        # OOP CLASS HANDLING (LAZY INITIALIZATION)
        # ==========================================
        if is_class:
            final_kwargs = {**self.default_flags, **user_attrs}
            el_val = final_kwargs.pop("EL", self.dependencies.get("EL")) if requires_el and "EL" in self.dependencies else None

            # Return a lambda that creates the Lazy Wrapper instead of instantiating the Class!
            callable_obj = lambda *content: LazyClassWrapper(tag_func, el_val, *content, **user_attrs).include_extra_attrs(**final_kwargs)
            if cache_key is not None:
                self._callable_cache[cache_key] = callable_obj
            return callable_obj

        # ==========================================
        # STANDARD FUNCTIONAL HANDLING
        # ==========================================
        if requires_el and "EL" in self.dependencies:
            final_kwargs = {**self.default_flags, **user_attrs}
            el_val = final_kwargs.pop("EL", self.dependencies["EL"])
            callable_obj = functools.partial(tag_func, el_val, **final_kwargs)
        elif user_attrs:
            callable_obj = functools.partial(tag_func, **{**self.default_flags, **user_attrs})
        else:
            callable_obj = functools.partial(tag_func, **self.default_flags)

        if cache_key is not None:
            self._callable_cache[cache_key] = callable_obj
        return callable_obj

    def execute(self):
        """Recursively builds and returns the final SSDOM tree."""

        def build_node(node_def):
            resolved_children = list(node_def["content"])
            for child in node_def["children"]:
                if child["type"] == "path":
                    resolved_children.append(build_node(self._nodes[child["value"]]))
                elif child["type"] == "anonymous":
                    node_callable = self._prepare_node_callable(
                        child["tag"], child["attrs"]
                    )
                    resolved_children.append(node_callable(*child["content"]))

            node_callable = self._prepare_node_callable(
                node_def["tag"], node_def["attrs"]
            )
            return node_callable(*resolved_children)

        return build_node(self._nodes["root"])

    def _apply_add(self, other):
        if hasattr(other, "args"):
            args, attrs = other.args, other.kwargs
        else:
            attrs = other[-1] if isinstance(other[-1], dict) else {}
            args = other[:-1] if isinstance(other[-1], dict) else other

        if isinstance(args[0], str):
            target_path = args[0]
            tag_func = args[1]
            content = args[2:]
        else:
            target_path = "root"
            tag_func = args[0]
            content = args[1:]

        return self.add_to(target_path, tag_func, *content, **attrs)

    def _apply_div(self, other):
        if hasattr(other, "args"):
            args, attrs = other.args, other.kwargs
        else:
            attrs = other[-1] if isinstance(other[-1], dict) else {}
            args = other[:-1] if isinstance(other[-1], dict) else other

        # SMART ROUTING: Branch vs Leaf
        if len(args) >= 3 and isinstance(args[1], str):
            parent_path = args[0]
            new_path_name = args[1]
            tag_func = args[2]
            content = args[3:]
            return self.nest(parent_path, new_path_name, tag_func, *content, **attrs)
        else:
            target_path = args[0]
            tag_func = args[1]
            content = args[2:]
            return self.add_to(target_path, tag_func, *content, **attrs)

    def _process_chain(self, other):
        if hasattr(other, "_chain"):
            for child in other._chain:
                self._apply_div(child)
                self._process_chain(child)

    def __add__(self, other):
        """
        Syntactic sugar for adding anonymous leaves (add_to).
        Usage (Root): exe + _(div, "content")
        Usage (Path): exe + _("root.sidebar", a, "Link")
        """
        if not isinstance(other, tuple) or len(other) < 1:
            raise TypeError("Must provide a tuple. Did you forget the _() tuplizer?")

        self._apply_add(other)
        self._process_chain(other)
        return self

    def __truediv__(self, other):
        """
        Smart syntactic sugar for nesting AND adding.
        Usage (Nest):   exe / _("root", "sidebar", div, Class="bg-dark")
        Usage (Add To): exe / _("root.sidebar", a, "Link", href="/")
        """
        if not isinstance(other, tuple) or len(other) < 2:
            raise TypeError(
                "Must provide a tuple with at least ('parent_path', 'new_name', tag_func)."
            )

        self._apply_div(other)
        self._process_chain(other)
        return self

class TupleExe(tuple):
    """
    Custom tuple to handle operator chaining precedence gracefully.
    Allows `exe + _() / _()` to evaluate without TypeError by capturing
    the chained operations and feeding them to the Executer sequentially.
    """

    def __new__(cls, *args, **kwargs):
        tup_content = args + (kwargs,) if kwargs else args
        obj = super().__new__(cls, tup_content)
        obj.args = args
        obj.kwargs = kwargs
        obj._chain = []
        return obj

    def __truediv__(self, other):
        self._chain.append(other)
        return self

def tuplizer(*args, **kwargs):
    """
    Tuplizer alias for clean DSL syntax.
    Bundles positional and keyword arguments into a tuple.
    """
    return TupleExe(*args, **kwargs,)
