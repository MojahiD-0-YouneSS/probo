# probo/core/tree.py
import uuid
from typing import Generator, List, Optional, Callable, Any, Self,Dict,Set
from probo.utility import ProboSourceString, StreamManager, HTMLCollection
from enum import Enum
from probo.type_hints import GenericSSDOM, GenericPowerNode,GenericProxyElement, GenericHTMLCollection


class ElementNodeMixin:
    """Adds hierarchical tree capabilities and traversal methods to a class.

    This mixin manages parent-child relationships and provides recursive search 
    utilities. It includes built-in protection for "void" (self-closing) nodes, 
    preventing child attachment where it's semantically invalid in HTML.

    Attributes:
        children (List[Any]): A list of child nodes attached to this element.
        parent (Optional[Any]): A reference to the parent node in the tree.
        __void_node (bool): Internal flag indicating if the node is a void tag.
    """
    __slots__ = ()

    def __init__(self,*args,**kwargs):
        self.node_children:list[GenericSSDOM] = []
        self.parent:GenericSSDOM|None = None
        self._void_node:bool = False
        self.custom_attrs:bool = kwargs.pop('custom_attrs', False)
        super().__init__(*args,**kwargs)

    def __init_subclass__(cls, **kwargs:dict[str,Any]):
        """Metaprogramming hook to configure tag-specific node behavior.

        Automatically assigns a unique Probo-ID and sets the default tag name 
        based on the class name. It also attaches a normalization method 
        to the subclass for processing initial content.
 
        Args:
            **kwargs: Configuration options, including optional 'id' prefix.
        """
        super().__init_subclass__(**kwargs)
        cls._id = f"{(kwargs.get('id', None) or 'probo')}-{uuid.uuid4().hex[:8]}"
        cls.tag=cls.__name__.upper()
        is_light = cls.__name__ == cls.__name__.capitalize() and cls.__name__[0]=="L"
        if is_light:
            cls.light_tag = f"L-{cls.__name__.lower()[1:]}"

        def __normalize_node_children(self,content=None,is_void=False):
            if is_void:
                self._void_node = True
                return None
            for item in content:
                if isinstance(item, ElementNodeMixin):
                    # O(1) assignment bypassing the self.add() O(N) deque scan trap
                    item.parent = self
                    self.node_children.append(item)
        cls._set_node_children = __normalize_node_children

    @property
    def children_nodes(self) -> list[GenericSSDOM]:
        return self.node_children

    @property
    def first_child(self) -> Optional[GenericSSDOM]:
        return self.node_children[0] if self.node_children else None

    @property
    def last_child(self) -> Optional[GenericSSDOM]:
        return self.node_children[-1] if self.node_children else None

    @property
    def next_sibling(self) -> Optional[GenericSSDOM]:
        if not self.parent:
            return None
        siblings = self.parent.node_children
        idx = siblings.index(self)
        return siblings[idx + 1] if idx + 1 < len(siblings) else None

    @property
    def previous_sibling(self) -> Optional[GenericSSDOM]:
        if not self.parent:
            return None
        siblings = self.parent.node_children
        idx = siblings.index(self)
        return siblings[idx - 1] if idx > 0 else None

    @property
    def ancestors(self) -> Generator[GenericSSDOM, None, None]:
        """Yields all ancestors up to the root."""
        current = self.parent
        while current:
            yield current
            current = current.parent

    def reset_node_children(self) -> Self:
        self.node_children.clear()
        return self

    def enforce_custom_attrs(self,global_tree=False,kwargs=None) -> Self:
        if not kwargs:
            kwargs={}

        def _process(n,k):
                if hasattr(n,'include_custom_attrs'):
                    flag = n.include_custom_attrs()
                    if not flag is True:
                        k.update(
            {
                'probo_custom_attrs':True,
            })

        if global_tree:

            for n in self.walk():
                _process(n,kwargs)
        else:
            for n in self.node_children:
                _process(n,kwargs)
        return self

    def add(self, child: Optional[GenericSSDOM], index: Optional[int] = None) -> Self:
        """Adds a child node and establishes the parent linkage."""
        if self._void_node == True:
            return self
        if child is None or child is self:
            return self

        if hasattr(child, 'parent'):
            child.parent = self

        if index is None:
            self.node_children.append(child)
        else:
            self.node_children.insert(index, child)
            
        if hasattr(self, "content") and child not in self.content:
            if isinstance(self.content, tuple):
                self.content = list(self.content)
                self.content.append(child)
                self.content = tuple(self.content)
            else:
                self.content.append(child)
                
            if isinstance(child, set):
                self._has_pipeline_vars = True
                self.resolved = False
                self._has_unresolved_pipeline_vars = True
                
        return self

    def remove(self, child: Optional[GenericSSDOM], func:Callable=None) ->Self:
        """Removes a child node and clears its parent reference.

        Args:
            child: The node instance to remove.

        Returns:
            The current instance for method chaining.
        """
        if callable(func):
            child = func(child)

        if child in self.node_children:
            self.node_children.remove(child)
            if hasattr(child, 'parent'):
                child.parent = None
            if hasattr(self,'content'):
                self.content.remove(child)
        return self

    def pop(self, child: Optional[GenericSSDOM], func: Callable = None) -> Any:
        """Pops a child node and clears its parent reference.

        Args:
            child: The node instance to remove.

        Returns:
            The popped node.
        """
        if callable(func):
            child = func(child)
        self.remove(child)
        return child

    def append(self, *nodes: Optional[GenericSSDOM]) -> Self:
        """Appends one or more nodes to the end of the children list."""
        for node in nodes:
            self.add(node)
        return self

    def prepend(self, *nodes: Optional[GenericSSDOM]) -> Self:
        """Prepends one or more nodes to the start of the children list."""
        for node in reversed(nodes):
            self.add(node, index=0)
        return self

    def insert_before(self, new_node: Optional[GenericSSDOM], reference_node: Optional[GenericSSDOM]) -> Self:
        """Inserts a new node directly before a specific sibling."""
        if reference_node in self.node_children:
            idx = self.node_children.index(reference_node)
            self.add(new_node, index=idx)
        return self

    def replace_with(self, new_node: Optional[GenericSSDOM]) -> GenericSSDOM:
        """Replaces this node entirely with a new node in the parent tree."""
        if self.parent:
            parent_ref = self.parent
            idx = parent_ref.node_children.index(self)
            parent_ref.remove(self)
            parent_ref.add(new_node, index=idx)
        return new_node

    def clear_children(self) -> Self:
        """Removes all children from the node."""
        for child in list(self.node_children):
            self.remove(child)
        return self

    def clone_node(self, deep: bool = True) -> Optional[GenericSSDOM]:
        """Creates a copy of the node. If deep=True, clones all children recursively."""
        import copy
        clone = copy.copy(self)
        clone.parent = None
        clone.node_children = []
        if hasattr(clone, "content"):
            clone.content = type(self.content)() # empty list/deque
            
        if deep:
            for child in self.content:
                if hasattr(child, 'clone_node'):
                    clone.add(child.clone_node(deep=True))
                else:
                    clone.add(copy.deepcopy(child))
        return clone

    @property
    def text(self) -> str:
        """Returns the text inside the element directly."""
        content = getattr(self, "content", [])
        return "".join(str(child) for child in content if not isinstance(child, ElementNodeMixin))

    @property
    def inner_text(self) -> List[str]:
        """Returns text that is inner including children as a list."""
        text_parts = []
        content = getattr(self, "content", [])
        for child in content:
            if isinstance(child, str):
                text_parts.append(child)
            elif hasattr(child, 'inner_text'):
                text_parts.extend(child.inner_text)
            elif hasattr(child, 'text_content'):
                text_parts.append(child.text_content)
            else:
                text_parts.append(str(child))

        return text_parts

    @property
    def text_content(self) -> str:
        """Recursively extracts pure text content, stripping all tags."""
        text_parts = []
        for child in self.node_children:
            if isinstance(child, str):
                text_parts.append(child)
            elif hasattr(child, 'inner_text'):
                text_parts.extend(child.inner_text)
            else:
                text_parts.append(str(child))

        return " ".join(text_parts)

    def create_element(self, *content:Any,tag: str|None=None,is_light: bool = False, **kwargs) -> GenericSSDOM:
        """Uses Heavy/light nodes to create children and appends them to this node."""
        if tag is None:
            tag = 'div'
        if is_light:
            from probo.templates import LightNodeProxy
            child = LightNodeProxy(tag,*content, **kwargs)
        else:
            from probo.templates import  HeavyNodeProxy
            child = HeavyNodeProxy(tag,*content, **kwargs)
            
        self.add(child)
        return child

    def get_child_count(self) -> int:
        """Returns the number of direct children."""
        return len(self.node_children)

    def get_children(self) -> GenericHTMLCollection:
        """Returns the direct children wrapped in an HTMLCollection."""
        from probo.utility import HTMLCollection
        return HTMLCollection(self.node_children)

    def get_tree_depth(self,) -> int:
        """Calculates how deep the node is within the tree.

        Returns:
            The number of steps from this node to the root.
        """
        depth = 0
        p = self.parent
        while p:
            depth += 1
            p = p.parent
        return depth

    def get_max_depth(self) -> int:
        """Calculates the maximum depth (height) of the tree from this node downwards.

        Returns:
            The maximum number of edges from this node down to the deepest leaf.
            Returns 0 if the node has no children.
        """
        children = getattr(self, "node_children", [])
        
        # Handle DOCTYPE which might not have node_children, but uses html_doc or doc_html
        if not children:
            doc = getattr(self, "html_doc", None) 
            if doc:
                children = [doc]

        if not children:
            return 0
            
        max_child_depth = 0
        for child in children:
            if hasattr(child, 'get_max_depth'):
                child_depth = child.get_max_depth()
                if child_depth > max_child_depth:
                    max_child_depth = child_depth
                    
        return max_child_depth + 1

    def find(self, predicate: Callable[[Any], bool],stream_mode=False) -> Optional[GenericSSDOM]:
        """Searches the tree for the first node that matches a condition.

        Uses a recursive Depth-First Search (DFS) algorithm.

        Args:
            predicate: A function that takes a node and returns True if matched.

        Returns:
            The first matching node found, or None if no match exists.

        Examples:
            >>> # Find an element with a specific ID
            >>> target = root.find(lambda node: getattr(node, "_id", "").startswith("btn"))
        """
        if predicate(self):
            return self

        for child in self.node_children:
            if hasattr(child, 'find'):
                result = child.find(predicate)
                if result:
                    if stream_mode:
                        result.toggle_share_element(share=False)
                    return result
        return None

    def find_all(self, predicate: Callable[[Any], bool]) -> GenericHTMLCollection:
        """Searches the tree for all nodes that match a condition.

        Args:
            predicate: A function that takes a node and returns True if matched.

        Returns:
            A list containing all matching nodes found in the subtree.
        """
        results = []
        if predicate(self):
            results.append(self)

        for child in self.node_children:
            if hasattr(child, 'find_all'):
                results.extend(child.find_all(predicate))
        return HTMLCollection(results)

    def select(self, selector: str) -> Optional[GenericSSDOM]:
        """Retrieves a node using CSS-style selectors.

        Supports class (.name), ID (#name), and Tag (NAME) lookups.

        Args:
            selector: The CSS selector string.

        Returns:
            The first matching node found.
        """
        return self.css_selector(selector)

    def _match_selector(self, n: Any, selector: str) -> bool:
        attrs = getattr(n, "attrs", None)
        if attrs is None:
            attrs = getattr(n, "attributes", {})
        if not attrs and not hasattr(n, "tag"):
            return False

        if selector.startswith("."):
            cls_attr = attrs.get("class", attrs.get("Class", ""))
            classes = cls_attr if isinstance(cls_attr, list) else str(cls_attr).split()
            return selector[1:] in classes
        if selector.startswith("#"):
            return attrs.get("id") == selector[1:] or attrs.get("Id") == selector[1:]
        return getattr(n, "tag", "").lower() == selector.lower()

    def css_selector(self, selector: str) -> Optional[GenericSSDOM]:
        """Retrieves the first node matching a CSS-style selector.

        Supports class (`.name`), ID (`#name`), and Tag (`NAME`) lookups.
        Robustly handles both string and list class attribute types.

        Args:
            selector: The CSS selector string to search for.

        Returns:
            The first matching node found in the subtree, or None.
        """
        return self.find(lambda n: self._match_selector(n, selector))

    def css_selector_all(self, selector: str) -> GenericHTMLCollection:
        """Retrieves all nodes matching a CSS-style selector.

        Supports class (`.name`), ID (`#name`), and Tag (`NAME`) lookups.

        Args:
            selector: The CSS selector string to search for.

        Returns:
            An HTMLCollection containing all matching nodes found.
        """
        from probo.utility import HTMLCollection
        return self.find_all(lambda n: self._match_selector(n, selector))

    def deep_remove(self,child:Any, func:Callable=None)-> Optional[GenericSSDOM]:
        """Locates the parent of a specific node and removes the child from it.

        This utility uses the tree's search engine to find the immediate parent 
        of the target child. Once found, it invokes the standard `remove` 
        logic on that parent, effectively performing a 'targeted strike' 
        deletion anywhere in the document tree.

        Args:
            child (Any): The node instance or data to be removed from the tree.

        Returns:
            Optional[Self]: Returns the root (self) for method chaining, 
                or None if the operation completes.
        """
        if callable(func):
            child = func(child)
        target:Self = self.find(lambda n:child in n.node_children)
        if target:
            target.remove(child)
        return None

    def deep_pop(self,child:Any,  func:Callable=None)-> Optional[GenericSSDOM]:
        """Locates the parent, removes the child, and returns the removed node.

        Similar to `deep_remove`, but follows the 'pop' convention of returning 
        the extracted node. This is ideal for 'Safe Transfers' where you want 
        to move a component (like a product card) from one page tree to another.

        Args:
            child (Any): The node instance or data to be extracted.

        Returns:
            Optional[Any]: The removed child node if found, otherwise None.
        """
        if callable(func):
            child = func(child)
        target:Self = self.find(lambda n:child in n.node_children)
        if target:
            target.pop(child)
        return child

    def deep_replace(self, old_child: Any, new_child: Any) -> Self:
        """Finds the parent of old_child and replaces it with new_child.
        
        Perfect for dynamic updates where you don't want to change the 
        index order, just the content (e.g., swapping a placeholder for 
        real recipe data).
        """
        target = self.find(lambda n: old_child in n.content)
        if target:
            content_list = list(target.content)
            idx = content_list.index(old_child)
            content_list[idx] = new_child
            target.content = tuple(content_list)
        return self

    def modify(self, target: Callable, content: Any = None, **kwargs) -> Self:
        """
        Feature 11: Fluently targets a child by ID and applies mutations.
        Usage: tree.modify("btn-submit", content="Loading...", class_="btn-disabled")
        """
        target = self.find(target())

        if target:
            # 2. Modify Content if provided
            if content is not None:
                if isinstance(target.content, list):
                    target.inner_html(content)
                     
                else:
                    target.content.append(content)

            if hasattr(target, "attributes"):
                target.attributes.update(kwargs)
        return self

    def stream_node(self, target_lambda: Callable[[Any], bool], chunk_size: int = 50) -> Generator[str, None, None]:
        """
        Feature 2: HTMX Targeting.
        Finds a specific node by ID and yields its stream only.
        """
        target = self.find(target_lambda)
        if target and hasattr(target, 'stream'):
            target.toggle_share_element(share=False)  # Detach from parent Element to prevent shared state issues
            yield from target.stream(chunk_size=chunk_size)
        else:
            # Silently yield nothing if not found, or a comment
            yield f"<!-- Node not found -->"

    def walk(self, include_text:bool=False)->Generator[GenericSSDOM,None,None]:
        """
        Generates a depth-first traversal of the SSDOM tree.
        
        Args:
            include_text (bool): If True, yields raw text/string children 
                                 alongside actual Node instances.
                                 
        Yields:
            Node | str: The current node, followed by all its descendants.
        """
        # 1. Yield the current node first (pre-order traversal)
        yield self

        # 2. Safely iterate through children
        for child in self.node_children if not include_text else self.content:
            if hasattr(child, "walk") and callable(child.walk):
                # Recursively walk child nodes
                yield from child.walk(include_text=include_text)
            elif include_text:
                # Yield raw strings/data if requested
                yield child

class ElementMutatorMixin:
    """
    Mixin to share a single Element builder across an SSDOM branch to save memory,
    while allowing detached nodes to independently manage their own state.
    """

    def __init__(self,*args,**kwargs):
        self._el_instance:None = None
        self.use_list:bool = kwargs.pop('use_list',False)
        self.use_deque:bool = kwargs.pop('use_deque',False)
        self.element_data:dict[str,Any] = kwargs.pop('data',{})

        self._share_element:bool = True  # Flag to control whether to share the Element instance with children
        super().__init__(*args,**kwargs)

    @property
    def EL(self):
        """
        LAZY PROPAGATION:
        1. If I already have an Element, return it.
        2. If I have a parent, climb up and grab the parent's Element!
        3. If I have no parent, I am the Root. I will spawn the Element.
        """
        if self._el_instance is not None  and self._share_element:
            return self._el_instance

        # 🚀 Climb the tree! If we have a parent, steal their EL builder.
        if hasattr(self, "parent") and self.parent is not None and self._share_element:
            if hasattr(self.parent, 'EL'):
                # This recursively climbs all the way to the Root node!
                self._el_instance = self.parent.EL 

                # Inherit the high-performance flags from the root
                self.use_list = getattr(self.parent, 'use_list', self.use_list)
                self.use_deque = getattr(self.parent, 'use_deque', self.use_deque)

                return self._el_instance
        # We have no parent. We must be the Root Node! Spawn the singleton.
        from probo.components.elements import Element
        self._el_instance = Element(
            is_list=self.use_list, 
        )
        if self.use_deque:
            self._el_instance.use_deque()
        self.toggle_share_element(share=True)  
        return self._el_instance
    
    def toggle_share_element(self, share=True) -> Self:
        """Utility to enable or disable sharing the Element instance with children.

        When `share` is set to False, this node will not attempt to use the 
        parent's Element instance and will instead create its own when accessed. 
        This is useful for nodes that need to manage their own state independently 
        of the parent branch, such as when streaming content or performing dynamic updates.
        """
        self._share_element = share
        return self
    
    def delegate_render_conditions(self, use_list: bool = False, use_deque: bool = False) -> Self:
        """
        Broadcasting method: Sets the engine flags for this node and 
        recursively pushes them down to every child in the tree.
        """
        # 1. Update this node's flags
        # self.toggle_share_element(share=True)
        if hasattr(self, 'use_list'):
            self.use_list = use_list
        if hasattr(self, 'use_deque'):
            self.use_deque = use_deque

        if hasattr(self, '_el_instance'):
            self._el_instance = None 
        for child in getattr(self, 'node_children', []):
            if hasattr(child, 'delegate_render_conditions'):
                child.delegate_render_conditions(use_list=use_list, use_deque=use_deque)

        return self # Allow chaining: el.delegate(...).render()

    def el_is_attached(self) -> bool:
        """Utility to check if the node is currently bound to a parent Element."""
        return self._el_instance is not None

    def bind_element(self, parent_element) -> None:
        """
        Rule 3: Injects the parent's Element builder into this child.
        This prevents the child from creating a new object in memory.
        """
        self._el_instance = parent_element

        # Inherit the parent's high-performance flags automatically
        self.use_list = parent_element.is_list
        self.use_deque = getattr(parent_element, "_use_deque", False)

    def unbind(self) -> None:
        """
        Safely detaches the node from the branch. The next time .EL is called,
        it will generate its own independent builder, keeping its data intact.
        """
        self._el_instance = None

class ComponentNode(ElementNodeMixin,):
    """
    A Mixin for ProboUI Components to enable node tree capabilities.
    Handles parent-child relationships, depth tracking, and child indexing.
    """

    __slots__ = (
        "_parent",
        "_node_depth",
        "_children_count",
        "parent",
        "node_children",
        "_void_node",
        'custom_attrs'
    )

    def __init__(self,**kwargs):
        self._parent: Optional[Self] = None
        self._node_depth: int = 0
        self._children_count: int = 0

        ElementNodeMixin.__init__(self)

    @property
    def get_parent(self) -> Optional[Self]:
        return self._parent

    @property
    def depth(self) -> int:
        return self._node_depth

    @property
    def children_count(self) -> int:
        """Returns the current number of registered child nodes."""
        return self._children_count

    @property
    def node_children_count(self) -> int:
        """Returns the current number of registered child nodes."""
        return len(self.node_children)

    def _set_parent(self, parent_node: Self):
        """Internal method to link the node to the tree."""
        if parent_node and parent_node != self:
            self._parent = parent_node
            self._node_depth = parent_node.depth + 1
            # Propagate the new child count to the parent
            parent_node._increment_children()

    def _increment_children(self):
        """Internal counter update."""
        self._children_count += 1

    def get_root(self) -> Self:
        """Traverses up the tree to find the top-level component."""
        curr = self
        while curr._parent:
            curr = curr._parent
        return curr

    def is_descendant_of(self, other: Self) -> bool:
        """Efficiently checks hierarchy using depth."""
        if self.depth <= other.depth:
            return False
        curr = self._parent
        while curr:
            if curr == other:
                return True
            if curr.depth <= other.depth:
                break
            curr = curr._parent
        return False

    def component_to_string(self) -> str:
        """Utility to convert the component and its subtree to a string representation."""
        return ProboSourceString(
            "".join(
                [
                    child.render() if hasattr(child, "render") else str(child)
                    for child in self.node_children
                ]
            )
        )

class NodeDataPolicy(Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    PROTECTED = "protected"

class DataPipeLineMixin:
    """
    Mixin to handle data pipeline, sharing, and HTML variable swapping.
    """
    def __init__(self,*args,**kwargs):
        self._data_pipeline: Any =  None
        self._data_policies: Dict[str, NodeDataPolicy] = {}
        self._custom_retriever: Optional[Callable[[Any, str, Any], Any]] = None
        self.__policy:Dict[str,NodeDataPolicy] = {'pub':NodeDataPolicy.PUBLIC,'pri':NodeDataPolicy.PRIVATE,'pro':NodeDataPolicy.PROTECTED}
        # Optimization flag
        self._has_pipeline_vars: bool = False
        self.resolved: bool = False
        self._has_unresolved_pipeline_vars: bool = False
        self.strict_data: bool = False

        super().__init__(*args,**kwargs)

    def extract_pipeline_args(self, kwargs: dict) -> None:
        """
        Extracts pipeline-specific arguments from a kwargs dictionary, popping them out
        so they aren't accidentally applied as HTML attributes.
        """
        if "data_pipeline" in kwargs:
            self._data_pipeline = kwargs.pop("data_pipeline")
        if "custom_retriever" in kwargs:
            self._custom_retriever = kwargs.pop("custom_retriever")
        if "strict_data" in kwargs:
            self.strict_data = kwargs.pop("strict_data")

    @property
    def get_data_pipeline(self) -> Any:
        return self._data_pipeline
    @property
    def has_pipeline_vars(self) -> bool:
        return self._has_pipeline_vars
    @property
    def has_unresolved_pipeline_vars(self) -> bool:
        return self._has_unresolved_pipeline_vars

    def load_data(self, store: Any, custom_retriever: Optional[Callable] = None) -> None:
        self._data_pipeline = store
        if custom_retriever:
            self._custom_retriever = custom_retriever

    def provide_data(self, key: str, value: Any, policy: str|None =None ) -> None:
        if policy is None:
            policy = NodeDataPolicy.PUBLIC
        else:
            policy = self.__policy.get(policy,'pub')
        if isinstance(self._data_pipeline, dict):
            self._data_pipeline[key] = value
            self._data_policies[key] = policy

    def _retrieve_local_data(self, key: str, default: Any = None) -> Any:
        _no_val = object()
        if self._custom_retriever:
            val = self._custom_retriever(self._data_pipeline, key, _no_val)
            if val is not _no_val: return val

        if isinstance(key, str) and '.' in key:
            parts = key.split('.')
            if hasattr(self._data_pipeline, "get"):
                obj = self._data_pipeline.get(parts[0], _no_val)
            else:
                obj = getattr(self._data_pipeline, parts[0], _no_val)
                
            if obj is not _no_val:
                for part in parts[1:]:
                    if hasattr(obj, 'get') and isinstance(obj, dict):
                        obj = obj.get(part, _no_val)
                    else:
                        obj = getattr(obj, part, _no_val)
                    if obj is _no_val:
                        break
                if obj is not _no_val:
                    return obj

        if hasattr(self._data_pipeline, "get"):
            return self._data_pipeline.get(key, default)
        else:
            return getattr(self._data_pipeline, key, default)

    def get_data(self, key: str, default: Any = None, _depth: int = 0) -> Any:
        local_val = self._retrieve_local_data(key, default=None)
        
        if local_val is not None:
            if _depth > 0:
                policy = self._data_policies.get(key, NodeDataPolicy.PUBLIC)
                if policy == NodeDataPolicy.PRIVATE:
                    local_val = None
                elif policy == NodeDataPolicy.PROTECTED and _depth > 1:
                    local_val = None

            if local_val is not None:
                return local_val

        if hasattr(self, "parent") and self.parent and hasattr(self.parent, "get_data"):
            return self.parent.get_data(key, default, _depth + 1)
            
        return default

    def _detect_pipeline_vars(self, *content) -> None:
        """Called when content is added to flag the node."""
        for child in content:
            if isinstance(child, set) and len(child) == 1 and isinstance(list(child)[0], str):
                self._has_pipeline_vars = True
                break

    def resolve_pipeline_variables(self, content=None,swap_vars:bool=False) -> bool:
        """
        Swaps variables in content. 
        Returns False if strict_data is True and a variable is missing (meaning the node should not render).
        Otherwise returns True.
        """
        if content is None:
            content = getattr(self, "content", [])
        is_closed_tag = getattr(self,'_void_node',False)
        attrs = getattr(self, "attributes", {})
        if not getattr(self, "_has_unresolved_pipeline_vars", False) and self.resolved:
            return True
        content_is_tuple = isinstance(content, tuple)
        mutable_content = list(content) if content_is_tuple else content
        got_vars = False

        for k,v in attrs.items():
            if isinstance(v,set):
                v_list = list(v)
                if len(v_list) == 1 and isinstance(v_list[0], str):
                    var_name = v_list[0]
                    resolved_val = self.get_data(var_name, default=None)
                    self._has_pipeline_vars = True
                    got_vars = True

                    if resolved_val is None:
                        self._has_unresolved_pipeline_vars = True
                        if getattr(self, "strict_data", False):
                            return False  # Missing data in strict mode -> drop the HTML
                        if swap_vars:
                            attrs[k] = ""  # Standard mode -> blank variable
                    else:
                        attrs[k] = resolved_val
                else:
                    func = None 
                    for x in v_list:
                        if callable(x):
                            func = x
                            break
                    if func:
                        var_names = [x for x in v_list if isinstance(x, str)]
                        kwargs_to_pass = {} 
                        has_missing = False
                        for var_name in var_names:
                            val = self.get_data(var_name, default=None)
                            if val is None:
                                has_missing = True
                            kwargs_to_pass[var_name] = val
                        
                        self._has_pipeline_vars = True
                        got_vars = True
                        
                        if has_missing:
                            self._has_unresolved_pipeline_vars = True
                            if getattr(self, "strict_data", False):
                                return False
                            if swap_vars:
                                attrs[k] = func(**kwargs_to_pass)
                            else:
                                attrs[k] = v
                        else:
                                attrs[k] = func(**kwargs_to_pass)

                    else:
                        if getattr(self, "strict_data", False):
                            return False
                        elif swap_vars:
                            attrs[k] = ""
                        else:
                            attrs[k] = v

        if not is_closed_tag:
            for i, child in enumerate(mutable_content):
                if isinstance(child, set):
                    child_list = list(child)
                    
                    if len(child_list) == 1 and isinstance(child_list[0], str):
                        var_name = child_list[0]
                        resolved_val = self.get_data(var_name, default=None)
                        self._has_pipeline_vars = True
                        got_vars = True

                        if resolved_val is None:
                            self._has_unresolved_pipeline_vars = True
                            if getattr(self, "strict_data", False):
                                return False # Missing data in strict mode -> drop the HTML
                            if swap_vars:
                                mutable_content[i] = "" # Standard mode -> blank variable
                        else:
                            mutable_content[i] = resolved_val
                    else:
                        func = None
                        for x in child_list:
                            if callable(x):
                                func=x
                                break
                        if func:
                            var_names = [x for x in child_list if isinstance(x, str)]
                            kwargs_to_pass = {}
                            has_missing = False
                            for var_name in var_names:
                                val = self.get_data(var_name, default=None)
                                if val is None:
                                    has_missing = True
                                kwargs_to_pass[var_name] = val
                            
                            self._has_pipeline_vars = True
                            got_vars = True
                            
                            if has_missing:
                                self._has_unresolved_pipeline_vars = True
                                if getattr(self, "strict_data", False):
                                    return False
                                if swap_vars:
                                    mutable_content[i] = func(**kwargs_to_pass)
                                else:
                                    mutable_content[i]=child
                            else:
                                mutable_content[i] = func(**kwargs_to_pass)
                        else:
                            if getattr(self, "strict_data", False):
                                return False
                            elif swap_vars:
                                mutable_content[i] = ""
                            else:
                                mutable_content[i] = child

        self.resolved = True
        setattr(self, 'content', tuple(mutable_content) if content_is_tuple else mutable_content)
        
        # Synchronize node_children if we resolved variables into components

        if not got_vars:
            # Prevent double resolution
            self._has_unresolved_pipeline_vars = False

        return True

from probo.components.base import BaseHTMLElement

class MutationPipelineMixin:
    """
    Mixin to handle proxies and power nodes pipeline execution phases.
    """
    def __init__(self, *args, **kwargs):
        self._proxy_registry: List[GenericProxyElement] = []
        self._power_node_registry: List[GenericPowerNode] = []
        self.run_in_background: bool = False
        self.hook_phase: str|None = None
        self._before_render_list: List[GenericProxyElement | GenericPowerNode] = []
        
        # self.extract_mutation_args(kwargs)
        super().__init__(*args,**kwargs)
    
    def __init_subclass__(cls, **kwargs:dict[str,Any]):
        super().__init_subclass__(**kwargs)
        def on_mount(self):
            """Executed when the object is added."""
            pass

        def before_render(self):
            """Executed just before rendering the parent."""
            pass
        def can_run(self):
            """Override to check if targets/dependencies are ready before running."""
            return True

        def on_error(self):
            """Override to clear heavy memory objects post-render."""
            pass

        def fallback(self):
            """Override to clear heavy memory objects post-render."""
            pass

        parent_names = [base.__name__ for base in cls.__bases__]
        if cls.__name__ in ['PowerNode', 'ProxyElement'] or 'ProxyElement' in parent_names or 'PowerNode' in parent_names  :
            if not hasattr(cls, 'on_mount'):
                setattr(cls, 'on_mount', on_mount)
            if not hasattr(cls, 'before_render'):
                setattr(cls, 'before_render', before_render)
            if not hasattr(cls, 'can_run'):
                setattr(cls, 'can_run', can_run)
            if not hasattr(cls, 'on_error'):
                setattr(cls, 'on_error', on_error)
            if not hasattr(cls, 'fallback'):
                setattr(cls, 'fallback', fallback)

    def add_proxy(self, proxy) -> None:
        if proxy not in self._proxy_registry:
            self._proxy_registry.append(proxy)
            if hasattr(proxy, "parent"):
                proxy.parent = self
            self.resolve_execution(proxy)
            
    def add_power_node(self, power_node) -> None:
        if power_node not in self._power_node_registry:
            self._power_node_registry.append(power_node)
            if hasattr(power_node, "parent"):
                power_node.parent = self
            self.resolve_execution(power_node)

    def resolve_execution(self, node) -> None:
        hook = getattr(node, "hook_phase", None)
        if hook == "on_mount":
            if hasattr(node, "can_run") and node.can_run():
                if hasattr(node,'on_mount'):
                    node.on_mount()
                node.exe()
        elif hook == 'before_render' and hasattr(self,'rendering') and self.rendering:
            if hasattr(node,'can_run') and node.can_run():
                if hasattr(node, 'before_render'):
                    node.before_render()
                node.exe()
        else:
            if hook == 'before_render' and hasattr(self,'rendering') and not self.rendering:
                self._before_render_list.append(node)

    def get_power_node(self,name:str|None=None,all_nodes:bool=False) ->  list[GenericPowerNode]|GenericPowerNode|None:
        nodes = []
        if not name:
            for pnode in self._power_node_registry:
                if hasattr(pnode,'parent') and pnode.parent == self:
                    if all_nodes:
                        nodes.append(pnode)
                    else:
                        return pnode
        return nodes
    
    def get_proxy_node(self,name:str|None=None,all_nodes:bool=False) ->  list[GenericProxyElement]|GenericProxyElement|None:
        nodes = []
        if not name:
            for pnode in self._proxy_registry:
                if hasattr(pnode,'parent') and pnode.parent == self:
                    if all_nodes:
                        nodes.append(pnode)
                    else:
                        return pnode
        return nodes
    
    def extract_mutation_args(self, kwargs: dict) -> None:
        if "proxies" in kwargs:
            for proxy in kwargs.pop("proxies"):
                self.add_proxy(proxy)
        if "power_nodes" in kwargs:
            for pnode in kwargs.pop("power_nodes"):
                self.add_power_node(pnode)

    def detect_effect_nodes(self, content) -> None:
        """
        Extracts PowerNodes and Proxies from content and registers them.
        Returns a new tuple without the effect nodes, so they aren't rendered as HTML children.
        """
        from probo.components.power_node import PowerNode
        for i,item in enumerate(content):
            if issubclass(item.__class__, PowerNode):
                self.add_power_node(item)
                content[i]=''
            elif 'ProxyElement' in [base.__name__ for base in item.__class__.__bases__]:
                self.add_proxy(item)
                if item.run_in_background:
                    content[i] = ''
            else:
                continue

    def execute_full_traverse_pass(self) -> Self:
        # Run nodes marked for background execution
        for node in self._power_node_registry + self._proxy_registry:
            if getattr(node, "run_in_background", False):
                if hasattr(node, "exe"):
                    node.exe()
        return self
                        
    def run_mutation(self, name: str | None = None, all_nodes: bool = False) -> Self:
        if not name:
            for pnode in self._power_node_registry + self._proxy_registry:
                if hasattr(pnode, 'parent') and pnode.parent == self:
                    if hasattr(pnode, "exe"):
                        pnode.exe()
                    if not all_nodes:
                        break
        return self
    
    def before_render_exe(self) -> Self:
        for node in self._before_render_list:
           self.resolve_execution(node)
        return self

class ProxyElement( DataPipeLineMixin, ElementNodeMixin, ElementMutatorMixin,MutationPipelineMixin, BaseHTMLElement):
    __slots__ = (
        "_proxy_tag",
        "wrap_result", "_logic_obj",
        "render_callable",
        "stream_callable",
        "run_in_background",
        "hook_phase"
    )
    def __init__(
        self, *content: tuple[Optional[str]], tag='div',wrap_result: bool = False, **attrs
    ):
        super().__init__(*content,**attrs)
        
        self.extract_pipeline_args(self.attributes)
        self.extract_mutation_args(self.attributes)
        self.run_in_background:bool = self.attributes.pop("run_in_background", True)
        self.hook_phase:str|None = self.attributes.pop("hook", None)
        self.wrap_result:bool = wrap_result
        self._proxy_tag:str = tag
        self._logic_obj:Any=None
        self.render_callable:Callable=None
        self.stream_callable:Callable=None
        
        # Detect effect nodes (power nodes/proxies) from content
        self.detect_effect_nodes(content)
        self._set_node_children(content,)
        self.resolve_pipeline_variables()

    def exe(self) -> None:
        # Override this in custom proxies if they have side-effects
        pass

    def load_logic(self,logic_obj) -> None:
        self._logic_obj=logic_obj
    
    def load_render_logic(self,render_logic:Callable) -> None:
        self.render_callable=render_logic
    
    def load_stream_logic(self,render_logic:Callable) -> None:
        self.stream_callable=render_logic
    
    def render(self,obj_as_arg=True) -> ProboSourceString:
        from probo.components.elements import Element

        if self._logic_obj and self.render_callable and obj_as_arg:
            return ProboSourceString(self.render_callable(self._logic_obj)) if not self.wrap_result else Element(tag=self._proxy_tag,content= ProboSourceString(self.render_callable(self._logic_obj)),**self.attributes).element
        if not self._logic_obj and self.render_callable:
            return ProboSourceString(self.render_callable()) if not self.wrap_result else Element(tag=self._proxy_tag,content= ProboSourceString(self.render_callable()),**self.attributes).element
        if self._logic_obj and hasattr(self._logic_obj,'render'):
            return ProboSourceString(self._logic_obj.render()) if not self.wrap_result else Element(tag=self._proxy_tag,content= ProboSourceString(self._logic_obj.render()),**self.attributes).element
        if self._proxy_tag and self.wrap_result:
            content = "".join(self._get_rendered_content())
            return Element(tag=self._proxy_tag,content=ProboSourceString(content),**self.attributes).element
        return ProboSourceString()

    def stream(self,obj_as_arg=True,batch=50) -> Generator[ProboSourceString,None,None]:
        from probo.components.elements import Element
        EL = Element(is_list=True,tag=self._proxy_tag,**self.attributes)

        if self.wrap_result:
            yield EL.element[0]
        if self._logic_obj and self.stream_callable and obj_as_arg:
            yield from self.stream_callable(self._logic_obj)
            if self.wrap_result and len(EL.element)!=1:
                yield EL.element[-1]
            return
        if not self._logic_obj and self.stream_callable:
            yield from  self.stream_callable()
            if self.wrap_result and len(EL.element)!=1:
                yield EL.element[-1]
            return
        if self._logic_obj and hasattr(self._logic_obj,'stream'):
            yield from self._logic_obj.stream(batch)
            if self.wrap_result and len(EL.element)!=1:
                yield EL.element[-1]
            return
        else:
            stream_content = self._get_stream_content()

            method = getattr(EL,self._proxy_tag,None)
            if callable(method):
                method()
            element_info = EL.element
            stream_manager = StreamManager(
                element_info[0],
                EL.reset_generator_content().stream(batch) if len(element_info) == 1 else EL.set_generator_content(stream_content).stream(batch),
                None if len(element_info) == 1 else element_info[-1],
                batch
            )
            return stream_manager
