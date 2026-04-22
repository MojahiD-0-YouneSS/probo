# probo/core/tree.py
import uuid
from typing import Generator, List, Optional, Callable, Any, Self
from probo.utility import ProboSourceString, StreamManager

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

    def __init__(self):
        self.node_children = []
        self.parent = None
        self.__void_node = False
        if hasattr(self,'element_tag'):
            self.element_tag = self.__class__.__name__.lower()
    def __init_subclass__(cls, **kwargs:dict[str,Any]):
        """Metaprogramming hook to configure tag-specific node behavior.

        Automatically assigns a unique Probo-ID and sets the default tag name 
        based on the class name. It also attaches a normalization method 
        to the subclass for processing initial content.
 
        Args:
            **kwargs: Configuration options, including optional 'id' prefix.
        """
        cls._id = f"{(kwargs.get('id', None) or 'probo')}-{uuid.uuid4().hex[:8]}"
        cls.tag=cls.__name__.upper()
        is_light = cls.__name__ == cls.__name__.capitalize() and cls.__name__[0]=="L"
        if is_light:
            cls.light_tag = f"L-{cls.__name__.lower()[1:]}"

        def __normalize_node_children(self,content=None,is_void=False):
            if is_void:
                self.__void_node = True
                return None
            for item in content:
                if isinstance(item, ElementNodeMixin):
                    self.add(item)
        cls._set_node_children = __normalize_node_children

    @property
    def children_nodes(self):
        return self.node_children

    def add(self, child: Any, index: Optional[int] = None) -> Self:
        """Adds a child node and establishes the parent linkage.

        If the current node is a 'void' node, the addition is ignored to 
        maintain HTML semantic validity.

        Args:
            child: The node instance to add.
            index: Optional position to insert the child.

        Returns:
            The current instance for method chaining.
        """
        if self.__void_node == True:
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
            self.content.append(child)
        return self

    def remove(self, child: Any) ->Self:
        """Removes a child node and clears its parent reference.

        Args:
            child: The node instance to remove.

        Returns:
            The current instance for method chaining.
        """
        if child in self.node_children:
            self.node_children.remove(child)
            if hasattr(child, 'parent'):
                child.parent = None
            if hasattr(self,'content'):
                self.content.remove(child)
        return self

    def pop(self, child: Any) -> Any:
        """Pops a child node and clears its parent reference.

        Args:
            child: The node instance to remove.

        Returns:
            The current instance for method chaining.
        """
        self.remove(child)
        return child

    def get_tree_depth(self) -> int:
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

    def find(self, predicate: Callable[[Any], bool],stream_mode=False) -> Optional[Any]:
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

    def find_all(self, predicate: Callable[[Any], bool]) -> List[Any]:
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
        return results

    def select(self, selector: str) -> Optional[Any]:
        """Retrieves a node using CSS-style selectors.

        Supports class (.name), ID (#name), and Tag (NAME) lookups.

        Args:
            selector: The CSS selector string.

        Returns:
            The first matching node found.
        """
        if selector.startswith("."):
            # Search by class in attrs
            return self.find(lambda n: selector[1:] in n.attrs.get("class", []))
        if selector.startswith("#"):
            # Search by ID
            return self.find(lambda n: n.attrs.get("id") == selector[1:])
        # Search by tag
        return self.find(lambda n: n.tag == selector)

    def deep_remove(self,child:Any)-> Optional[Self]:
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
        target:Self = self.find(lambda n:child in n.children)
        if target:
            target.remove(child)
        return None

    def deep_pop(self,child:Any)-> Optional[Self]:
        """Locates the parent, removes the child, and returns the removed node.

        Similar to `deep_remove`, but follows the 'pop' convention of returning 
        the extracted node. This is ideal for 'Safe Transfers' where you want 
        to move a component (like a product card) from one page tree to another.

        Args:
            child (Any): The node instance or data to be extracted.

        Returns:
            Optional[Any]: The removed child node if found, otherwise None.
        """
        target:Self = self.find(lambda n:child in n.children)
        if target:
            target.pop(child)
        return child

    def deep_replace(self, old_child: Any, new_child: Any) -> Optional[Self]:
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

    def modify(
        self, target: Callable, content: Any = None, **kwargs
    ) -> "ElementNodeMixin":
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

    def stream_node(
        self, target_lambda: Callable[[Any], bool], chunk_size: int = 50
    ) -> Generator[str, None, None]:
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

    def walk(self, include_text:bool=False)->Generator[Self,None,None]:
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

    def __init__(self, use_list: bool = False, use_deque: bool = False, **data):
        self._el_instance = None
        self.use_list = use_list
        self.use_deque = use_deque
        self.element_data = data

        self._share_element = True  # Flag to control whether to share the Element instance with children
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
    def toggle_share_element(self, share=True):
        """Utility to enable or disable sharing the Element instance with children.

        When `share` is set to False, this node will not attempt to use the 
        parent's Element instance and will instead create its own when accessed. 
        This is useful for nodes that need to manage their own state independently 
        of the parent branch, such as when streaming content or performing dynamic updates.
        """
        self._share_element = share
        return self
    def delegate_render_conditions(self, use_list: bool = False, use_deque: bool = False):
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
        "_ElementNodeMixin__void_node",
    )

    def __init__(self):
        self._parent: Optional["ComponentNode"] = None
        self._node_depth: int = 0
        self._children_count: int = 0

        ElementNodeMixin.__init__(self)

    @property
    def get_parent(self) -> Optional["ComponentNode"]:
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

    def _set_parent(self, parent_node: "ComponentNode"):
        """Internal method to link the node to the tree."""
        if parent_node and parent_node != self:
            self._parent = parent_node
            self._node_depth = parent_node.depth + 1
            # Propagate the new child count to the parent
            parent_node._increment_children()

    def _increment_children(self):
        """Internal counter update."""
        self._children_count += 1

    def get_root(self) -> "ComponentNode":
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


from probo.components.base import BaseHTMLElement

class ProxyElement(BaseHTMLElement, ElementNodeMixin, ElementMutatorMixin):
    __slots__ = (
        "_proxy_tag",
        "wrap_result", "_logic_obj",
        "render_callable",
        "stream_callable",
    )
    def __init__(
        self, *content: tuple[Optional[str]], tag='div',wrap_result: bool = False, **attrs
    ):
        super().__init__(*content,**attrs)
        ElementNodeMixin.__init__(self)
        ElementMutatorMixin.__init__(self,tag)
        self.wrap_result = wrap_result
        self._proxy_tag = tag
        self._logic_obj=None
        self.render_callable:Callable=None
        self.stream_callable:Callable=None
        self._set_node_children(content)

    def load_logic(self,logic_obj):
        self._logic_obj=logic_obj
    def load_render_logic(self,render_logic:Callable):
        self.render_callable=render_logic
    def load_stream_logic(self,render_logic:Callable):
        self.stream_callable=render_logic
    def render(self,obj_as_arg=True):
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

    def stream(self,obj_as_arg=True,batch=50):
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
            elemnt_info = EL.element
            stream_manager = StreamManager(
                elemnt_info[0],
                EL.reset_generator_content().stream(batch) if len(elemnt_info) == 1 else EL.set_generator_content(stream_content).stream(batch),
                None if len(elemnt_info) == 1 else elemnt_info[-1],
                batch
            )
            return stream_manager
