# probo/core/tree.py
import uuid
from typing import List, Optional, Callable, Any, Self

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
        self.children = []
        self.parent = None
        self.__void_node = False

    def __init_subclass__(cls, **kwargs):
        """Metaprogramming hook to configure tag-specific node behavior.

        Automatically assigns a unique Probo-ID and sets the default tag name 
        based on the class name. It also attaches a normalization method 
        to the subclass for processing initial content.
 
        Args:
            **kwargs: Configuration options, including optional 'id' prefix.
        """
        cls._id = f"{(kwargs.get('id', None) or 'probo')}-{uuid.uuid4().hex[:8]}"
        cls.tag=cls.__name__.upper()
        
        def __normalize_node_children(self,content=[],is_void=False):
            if is_void:
                self.__void_node = True
                return None
            for item in content:
                if isinstance(item, ElementNodeMixin):
                    self.add(item)
        cls._set_node_children = __normalize_node_children
    
    def add(self, child: Any, index: Optional[int] = None) -> 'ElementNodeMixin':
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
            self.children.append(child)
        else:
            self.children.insert(index, child)
        if hasattr(self,'content'):
            self.content.append(child)
        return self

    def remove(self, child: Any) -> 'ElementNodeMixin':
        """Removes a child node and clears its parent reference.

        Args:
            child: The node instance to remove.

        Returns:
            The current instance for method chaining.
        """
        if child in self.children:
            self.children.remove(child)
            if hasattr(child, 'parent'):
                child.parent = None
            if hasattr(self,'content'):
                self.content.remove(child)
        return self

    def pop(self, child: Any) -> 'Any':
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

    def find(self, predicate: Callable[[Any], bool]) -> Optional[Any]:
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
        
        for child in self.children:
            if hasattr(child, 'find'):
                result = child.find(predicate)
                if result:
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
            
        for child in self.children:
            if hasattr(child, 'find_all'):
                results.extend(child.find_all(predicate))
        return results

    def select(self, selector: str):
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