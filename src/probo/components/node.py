# probo/core/tree.py
import uuid
class ElementNodeMixin:
    """+
    Adds Tree capabilities to any class.
    """
    def __init__(self):
        self.children = []
        self.parent = None
    def __init_subclass__(cls, **kwargs):
        cls._id = f"{(kwargs.get("id",None) or 'probo')}-{uuid.uuid4().hex[:8]}"
    def add(self, child, index=None):
        """
        Adds a child node. Handles parent linkage automatically.
        """
        if child is None: return self
        
        # Link the child to this parent
        if hasattr(child, 'parent'):
            child.parent = self
            
        if index is None:
            self.children.append(child)
        else:
            self.children.insert(index, child)
        return self  # Return self for chaining! .add(x).add(y)

    def remove(self, child):
        if child in self.children:
            self.children.remove(child)
            if hasattr(child, 'parent'):
                child.parent = None
        return self

    def get_tree_depth(self):
        """Helper to know how deep this node is."""
        depth = 0
        p = self.parent
        while p:
            depth += 1
            p = p.parent
        return depth