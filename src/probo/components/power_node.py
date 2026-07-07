from probo.components.node import ElementNodeMixin,MutationPipelineMixin,DataPipeLineMixin, GenericSSDOM
from typing import Callable

class PowerNode( DataPipeLineMixin, MutationPipelineMixin,ElementNodeMixin):
    __slots__ = ('target_predicate', 'run_in_background', 'hook_phase')
    
    def __init__(self, target_predicate:Callable, **kwargs):
        DataPipeLineMixin.__init__(self)
        MutationPipelineMixin.__init__(self)
        ElementNodeMixin.__init__(self)

        self.target_predicate = target_predicate
        self.run_in_background = kwargs.pop("run_in_background", True)
        self.hook_phase = kwargs.pop("hook", None)
        self.extract_pipeline_args(kwargs)
        self.extract_mutation_args(kwargs)
        
    def fetch_target(self) -> GenericSSDOM:
        from probo.exceptions.components_error import TargetNotFound

        if hasattr(self, "parent") and self.parent:
            # We search from the parent up to root
            root = self.parent
            # while hasattr(root, "parent") and root.parent:
            #     root = root.parent
            target = root.find(self.target_predicate)
            if not target:
                raise TargetNotFound("Target node could not be found.")
            return target
        raise TargetNotFound("PowerNode has no parent to search from.")
        
    def exe(self) -> None:
        target = self.fetch_target()
        self.execute(target)

    def execute(self, target:GenericSSDOM, *args, **kwargs):
        """Override for heavy logic, API calls, and calculations."""
        raise NotImplementedError("PowerNodes must implement an execute() method.")

    def can_run(self) -> bool:
        from probo.exceptions.components_error import TargetNotFound
        try:
            self.fetch_target()
            return True
        except TargetNotFound as e:
            raise e
