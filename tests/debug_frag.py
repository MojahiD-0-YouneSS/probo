from collections import deque
from probo.components.tag_classes.block_tags import DIV
from probo.components.fragment import Frag

f1 = Frag("hello", "world")
print("f1 render:", repr(f1.render()))

f2 = Frag("hello", "world")
f2.delegate_render_conditions(use_list=True)
print("f2 render:", repr(f2.render()))

f3 = Frag("hello", "world")
f3.delegate_render_conditions(use_list=True, use_deque=True)
print("f3 render:", repr(f3.render()))

d1 = DIV(Frag("hello", "world"))
print("d1 render:", repr(d1.render()))

d2 = DIV(Frag("hello", "world"))
d2.delegate_render_conditions(use_list=True)
print("d2 render:", repr(d2.render()))

f_stream = Frag("hello", "world")
print("f stream:", repr(list(f_stream.stream())))

f_stream2 = Frag("hello", "world")
f_stream2.delegate_render_conditions(use_list=True)
print("f stream2:", repr(list(f_stream2.stream())))
