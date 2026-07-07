from typing import Protocol, Any, Optional, List, Callable, Dict, Generator, Self, Deque, TypeVar
T_SSDOM = TypeVar('T_SSDOM', bound='GenericSSDOM')
T_HTMLCollection = TypeVar('T_HTMLCollection', bound='GenericHTMLCollection')
T_AttrManager = TypeVar('T_AttrManager', bound='GenericAttrManager')
T_StyleManager = TypeVar('T_StyleManager', bound='GenericStyleManager')
T_PowerNode = TypeVar('T_PowerNode', bound='GenericPowerNode')
T_ProxyElement = TypeVar('T_ProxyElement', bound='GenericProxyElement')

class GenericHTMLCollection(Protocol):
    nodes:List[Any]
    def for_each(self, callback: Callable) -> T_HTMLCollection:
        pass
    def maping(self, callback: Callable) -> list[Any]:
        pass
    def filter(self, predicate: Callable) -> T_HTMLCollection:
        pass
    def add_class(self, *classes: str) -> T_HTMLCollection:
        pass

class GenericAttrManager(Protocol):
    """"""
    attrs:Dict[str,Any]

    def add_class(self, cls_str: str,*classes:tuple[str]) -> T_AttrManager:
        pass

    def remove_class(self, cls_str: str) -> T_AttrManager:
        pass

    def contains_class(self, cls_str: str) -> bool:
        pass

    def toggle_class(self, class_name: str, condition: bool = None) -> T_AttrManager:
        pass

    def set_attr(self, key: str, value: Union[str, bool]) -> T_AttrManager:
        pass
    
    def set_bulk_attr(self, **attrs:dict[str,Any]) -> T_AttrManager:
        pass

    def get_attr(self, key: str, default=None) -> str:
        pass

    def remove_attr(self, key: str) -> T_AttrManager:
        pass

    def set_data(self, key: str, value: str) -> T_AttrManager:
        pass
    
    def set_id(self, unique_id: str) -> T_AttrManager:
        pass
    
    def get_id(self,) -> str|None:
        pass

    def merge_attrs(self, **kwargs:dict[str,str]) -> T_AttrManager:
        pass

    def get(self, key: str, default=None) -> Any:
        pass

    def items(self):
        pass

    def keys(self):
        pass

    def update(self, **kwargs) -> T_AttrManager:
        pass

    def toggle_attr(self, key: str, condition: bool = None) -> T_AttrManager:
        pass

    def set_attr_if(self, condition: bool, key: str, value: Any) -> T_AttrManager:
        pass

    def render_attrs(self) -> str:
        pass
    
    def set_style(self, property: str, value: str) -> T_AttrManager:
        pass

class GenericStyleManager(Protocol):
    """"""

    def add(self, name: str, value: str) -> T_StyleManager:
        pass
    def remove(self, name: str) -> T_StyleManager:
        pass
    @property
    def render(self) -> str:
        pass

class GenericPowerNode(Protocol):
    target_predicate :Callable[[Any],bool]
    run_in_background:bool
    hook_phase:str|None
    node_children:List[Any]
    parent:Self|None
    _void_node:bool
    _data_pipeline: Any 
    _data_policies: Dict[str, NodeDataPolicy]
    _custom_retriever: Optional[Callable[[Any, str, Any], Any]]
    _has_pipeline_vars: bool 
    resolved: bool 
    _has_unresolved_pipeline_vars: bool 
    strict_data: bool 
    _proxy_registry: List[T_ProxyElement]
    _power_node_registry: List[T_PowerNode]
    run_in_background: bool
    hook_phase: str|None 
    _before_render_list: List[T_ProxyElement|T_PowerNode]

    def fetch_target(self) -> T_SSDOM:
        pass
    def exe(self) -> None:
        pass
    def execute(self, target:T_SSDOM, *args, **kwargs):
        pass
    def can_run(self) -> bool:
        pass

    # ElementNodeMixin API
    @property
    def children_nodes(self) -> list[T_SSDOM]:
        pass
    @property
    def first_child(self) -> Optional[T_SSDOM]:
        pass
    @property
    def last_child(self) -> Optional[T_SSDOM]:
        pass
    @property
    def next_sibling(self) -> Optional[T_SSDOM]:
        pass
    @property
    def previous_sibling(self) -> Optional[T_SSDOM]:
        pass
    @property
    def ancestors(self) -> Generator[T_SSDOM, None, None]:
        pass

    def reset_node_children(self) -> T_PowerNode:
        pass

    def enforce_custom_attrs(self,global_tree=False,kwargs=None) -> T_PowerNode:
        pass

    def add(self, child: Optional[T_SSDOM], index: Optional[int] = None) -> T_PowerNode:
        pass

    def remove(self, child: Optional[T_SSDOM], func:Callable=None) ->T_PowerNode:
        pass

    def pop(self, child: Optional[T_SSDOM], func: Callable = None) -> Any:
        pass

    def append(self, *nodes: Optional[T_SSDOM]) -> T_PowerNode:
        pass

    def prepend(self, *nodes: Optional[T_SSDOM]) -> T_PowerNode:
        pass

    def insert_before(self, new_node: Optional[T_SSDOM], reference_node: Optional[T_SSDOM]) -> T_PowerNode:
        pass

    def replace_with(self, new_node: Optional[T_SSDOM]) -> T_SSDOM:
        pass

    def clear_children(self) -> T_PowerNode:
        pass

    def clone_node(self, deep: bool = True) -> Optional[T_SSDOM]:
        pass
    @property
    def text(self) -> str:
        pass
    @property
    def inner_text(self) -> List[str]:
        pass
    @property
    def text_content(self) -> str:
        pass

    def create_element(self, *content:Any,tag: str|None=None,is_light: bool = False, **kwargs) -> T_SSDOM:
        pass

    def get_child_count(self) -> int:
        pass

    def get_children(self) -> GenericHTMLCollection:
        pass

    def get_tree_depth(self,) -> int:
        pass

    def get_max_depth(self) -> int:
        pass

    def find(self, predicate: Callable[[Any], bool],stream_mode=False) -> Optional[T_SSDOM]:
        pass

    def find_all(self, predicate: Callable[[Any], bool]) -> GenericHTMLCollection[Optional[T_SSDOM]]:
        pass

    def select(self, selector: str) -> Optional[T_SSDOM]:
        pass

    def _match_selector(self, n: Any, selector: str) -> bool:
        pass

    def css_selector(self, selector: str) -> Optional[T_SSDOM]:
        pass

    def css_selector_all(self, selector: str) -> GenericHTMLCollection:
        pass

    def deep_remove(self,child:Any, func:Callable=None)-> Optional[T_SSDOM]:
        pass

    def deep_pop(self,child:Any,  func:Callable=None)-> Optional[T_SSDOM]:
        pass

    def deep_replace(self, old_child: Any, new_child: Any) -> T_PowerNode:
        pass

    def modify(self, target: Callable, content: Any = None, **kwargs) -> T_PowerNode:
        pass

    def stream_node(self, target_lambda: Callable[[Any], bool], chunk_size: int = 50) -> Generator[str, None, None]:
        pass

    def walk(self, include_text:bool=False)->Generator[T_SSDOM,None,None]:
        pass

    # DataPipeLineMixin api

    def extract_pipeline_args(self, kwargs: dict) -> None:
        pass
    @property
    def get_data_pipeline(self) -> Any:
        pass
    @property
    def has_pipeline_vars(self) -> bool:
        pass
    @property
    def has_unresolved_pipeline_vars(self) -> bool:
        pass

    def load_data(self, store: Any, custom_retriever: Optional[Callable] = None) -> None:
        pass

    def provide_data(self, key: str, value: Any, policy: str|None =None ) -> None:
        pass

    def _retrieve_local_data(self, key: str, default: Any = None) -> Any:
        pass

    def get_data(self, key: str, default: Any = None, _depth: int = 0) -> Any:
        pass

    def _detect_pipeline_vars(self, *content) -> None:
        pass

    def resolve_pipeline_variables(self, content=None,swap_vars:bool=False) -> bool:
        pass

    # MutationPipelineMixin api

    def add_proxy(self, proxy) -> None:
      pass
    def add_power_node(self, power_node) -> None:
        pass
    def resolve_execution(self, node) -> None:
        pass
    def get_power_node(self,name:str|None=None,all_nodes:bool=False) ->  list[T_PowerNode]|T_PowerNode|None:
        pass

    def get_proxy_node(self,name:str|None=None,all_nodes:bool=False) ->  list[T_ProxyElement]|T_ProxyElement|None:
        pass

    def extract_mutation_args(self, kwargs: dict) -> None:
        pass

    def detect_effect_nodes(self, content) -> None:
        pass

    def execute_full_traverse_pass(self) -> T_PowerNode:
        pass
                  
    def run_mutation(self, name: str | None = None, all_nodes: bool = False) -> T_PowerNode:
        pass
    def before_render_exe(self) -> T_PowerNode:
        pass

class GenericSSDOM(Protocol):
    """
    A structural Protocol that mimics a Probo SSDOM Element (like DIV, H1, etc.).
    Use this for type hinting SSDOM nodes to avoid circular import issues while 
    retaining full IDE autocompletion for the SSDOM API.
    """
    # Core element attributes
    tag: str
    element_tag: str
    content: Deque[Any]
    attributes: Dict[str, Any]
    custom_attrs: bool
    _override_style:bool
    _render_conditions:Dict[str,Any]
    rendering:bool
    node_children:List[Any]
    parent:Self|None
    _void_node:bool
    _el_instance:None
    use_list:bool
    use_deque:bool
    element_data:Dict[str,Any]
    _share_element:bool
    _data_pipeline: Any 
    _data_policies: Dict[str, NodeDataPolicy]
    _custom_retriever: Optional[Callable[[Any, str, Any], Any]]
    _has_pipeline_vars: bool 
    resolved: bool 
    _has_unresolved_pipeline_vars: bool 
    strict_data: bool 
    _proxy_registry: List[T_ProxyElement]
    _power_node_registry: List[T_PowerNode]
    run_in_background: bool
    hook_phase: str|None 
    _before_render_list: List[T_ProxyElement|T_PowerNode]
    
    # BaseHTMLElement API
    @property
    def attr_manager(self) -> GenericAttrManager: 
        pass

    @property
    def style_manager(self) -> GenericStyleManager: 
        pass

    def inner_html(self, *content: Any) -> T_SSDOM: 
        pass
    def include_custom_attrs(self) -> T_SSDOM: 
        pass
    def add_render_constraints(self, **constraints: str) -> T_SSDOM: 
        pass
    # ElementNodeMixin API
    @property
    def children_nodes(self) -> list[T_SSDOM]:
        pass
    @property
    def first_child(self) -> Optional[T_SSDOM]:
        pass
    @property
    def last_child(self) -> Optional[T_SSDOM]:
        pass
    @property
    def next_sibling(self) -> Optional[T_SSDOM]:
        pass
    @property
    def previous_sibling(self) -> Optional[T_SSDOM]:
        pass
    @property
    def ancestors(self) -> Generator[T_SSDOM, None, None]:
        pass

    def reset_node_children(self) -> T_SSDOM:
        pass

    def enforce_custom_attrs(self,global_tree=False,kwargs=None) -> T_SSDOM:
        pass

    def add(self, child: Optional[T_SSDOM], index: Optional[int] = None) -> T_SSDOM:
        pass

    def remove(self, child: Optional[T_SSDOM], func:Callable=None) ->T_SSDOM:
        pass

    def pop(self, child: Optional[T_SSDOM], func: Callable = None) -> Any:
        pass

    def append(self, *nodes: Optional[T_SSDOM]) -> T_SSDOM:
        pass

    def prepend(self, *nodes: Optional[T_SSDOM]) -> T_SSDOM:
        pass

    def insert_before(self, new_node: Optional[T_SSDOM], reference_node: Optional[T_SSDOM]) -> T_SSDOM:
        pass

    def replace_with(self, new_node: Optional[T_SSDOM]) -> T_SSDOM:
        pass

    def clear_children(self) -> T_SSDOM:
        pass

    def clone_node(self, deep: bool = True) -> Optional[T_SSDOM]:
        pass
    @property
    def text(self) -> str:
        pass
    @property
    def inner_text(self) -> List[str]:
        pass
    @property
    def text_content(self) -> str:
        pass

    def create_element(self, *content:Any,tag: str|None=None,is_light: bool = False, **kwargs) -> T_SSDOM:
        pass

    def get_child_count(self) -> int:
        pass

    def get_children(self) -> GenericHTMLCollection:
        pass

    def get_tree_depth(self,) -> int:
        pass

    def get_max_depth(self) -> int:
        pass

    def find(self, predicate: Callable[[Any], bool],stream_mode=False) -> Optional[T_SSDOM]:
        pass

    def find_all(self, predicate: Callable[[Any], bool]) -> GenericHTMLCollection[Optional[T_SSDOM]]:
        pass

    def select(self, selector: str) -> Optional[T_SSDOM]:
        pass

    def _match_selector(self, n: Any, selector: str) -> bool:
        pass

    def css_selector(self, selector: str) -> Optional[T_SSDOM]:
        pass

    def css_selector_all(self, selector: str) -> GenericHTMLCollection:
        pass

    def deep_remove(self,child:Any, func:Callable=None)-> Optional[T_SSDOM]:
        pass

    def deep_pop(self,child:Any,  func:Callable=None)-> Optional[T_SSDOM]:
        pass

    def deep_replace(self, old_child: Any, new_child: Any) -> T_SSDOM:
        pass

    def modify(self, target: Callable, content: Any = None, **kwargs) -> T_SSDOM:
        pass

    def stream_node(self, target_lambda: Callable[[Any], bool], chunk_size: int = 50) -> Generator[str, None, None]:
        pass

    def walk(self, include_text:bool=False)->Generator[T_SSDOM,None,None]:
        pass
    # ElementMutatorMixin api
    
    @property
    def EL(self):
        pass
    
    def toggle_share_element(self, share=True) -> T_SSDOM:
        pass
    
    def delegate_render_conditions(self, use_list: bool = False, use_deque: bool = False) -> T_SSDOM:
        pass

    def el_is_attached(self) -> bool:
        pass

    def bind_element(self, parent_element) -> None:
        pass

    def unbind(self) -> None:
        pass
    # DataPipeLineMixin api

    def extract_pipeline_args(self, kwargs: dict) -> None:
        pass
    @property
    def get_data_pipeline(self) -> Any:
        pass
    @property
    def has_pipeline_vars(self) -> bool:
        pass
    @property
    def has_unresolved_pipeline_vars(self) -> bool:
        pass

    def load_data(self, store: Any, custom_retriever: Optional[Callable] = None) -> None:
        pass

    def provide_data(self, key: str, value: Any, policy: str|None =None ) -> None:
        pass

    def get_data(self, key: str, default: Any = None, _depth: int = 0) -> Any:
        pass

    def resolve_pipeline_variables(self, content=None,swap_vars:bool=False) -> bool:
        pass

    # MutationPipelineMixin api

    def add_proxy(self, proxy) -> None:
      pass
    def add_power_node(self, power_node) -> None:
        pass
    def resolve_execution(self, node) -> None:
        pass
    def get_power_node(self,name:str|None=None,all_nodes:bool=False) ->  list[GenericPowerNode]|GenericPowerNode|None:
        pass

    def get_proxy_node(self,name:str|None=None,all_nodes:bool=False) ->  list[T_ProxyElement]|T_ProxyElement|None:
        pass

    def extract_mutation_args(self, kwargs: dict) -> None:
        pass

    def detect_effect_nodes(self, content) -> None:
        pass

    def execute_full_traverse_pass(self) -> T_SSDOM:
        pass
                  
    def run_mutation(self, name: str | None = None, all_nodes: bool = False) -> T_SSDOM:
        pass
    def before_render_exe(self) -> T_SSDOM:
        pass

class GenericProxyElement(GenericSSDOM):
    run_in_background:bool
    hook_phase:str|None
    wrap_result:bool
    _proxy_tag:str
    _logic_obj:Any
    render_callable:Callable
    stream_callable:Callable

    def exe(self) -> None:
        pass

    def load_logic(self,logic_obj) -> None:
        pass

    def load_render_logic(self,render_logic:Callable) -> None:
        pass

    def load_stream_logic(self,render_logic:Callable) -> None:
        pass

    def render(self,obj_as_arg=True) -> ProboSourceString:
        pass
    def stream(self,obj_as_arg=True,batch=50) -> Generator[ProboSourceString,None,None]:
        pass