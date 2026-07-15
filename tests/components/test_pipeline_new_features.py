import pytest
from probo import DIV, SPAN, P, BUTTON
from probo.utility import DataPipeLineSource

# --- Group 1: New Variable Expressions (10 Tests) ---

def test_expr_1_simple_set():
    d = DIV({'name'})
    d.load_data({'name': 'John'})
    assert 'John' in d.render()

def test_expr_2_callable_in_set():
    d = DIV({'status', lambda **kwargs: "Active" if kwargs.get('status') else "Inactive"})
    d.load_data({'status': True})
    assert 'Active' in d.render()

def test_expr_3_callable_multi_vars():
    d = DIV({'a', 'b', lambda **kwargs: str(kwargs.get('a', 0) + kwargs.get('b', 0))})
    d.load_data({'a': 5, 'b': 10})
    assert '15' in d.render()

def test_expr_4_callable_with_missing_vars():
    d = DIV({'a', 'b', lambda **kwargs: str(kwargs.get('a', 0) + (kwargs.get('b', 0) or 0))})
    d.load_data({'a': 5}) # missing b
    assert '5' in d.render()

def test_expr_5_callable_returning_element():
    d = DIV({'is_admin', lambda **kwargs: SPAN("Admin") if kwargs.get('is_admin') else SPAN("User")})
    d.load_data({'is_admin': True})
    assert '<span>Admin</span>' in d.render()

def test_expr_6_multiple_callables():
    d = DIV(
        {'v1', lambda **k: f"V1:{k.get('v1')}"},
        {'v2', lambda **k: f"V2:{k.get('v2')}"}
    )
    d.load_data({'v1': 1, 'v2': 2})
    assert 'V1:1 V2:2' in d.render()

def test_expr_7_callable_in_attribute():
    d = DIV(Class={'status', lambda **kwargs: "btn-on" if kwargs.get('status') else "btn-off"})
    d.load_data({'status': False})
    assert 'class="btn-off"' in d.render()

def test_expr_8_dynamic_attr_update():
    d = DIV()
    d.attr_manager.set_attr('id', {'dynamic_id', lambda **k: k.get('dynamic_id')})
    d.load_data({'dynamic_id': 'my-id'})
    assert 'id="my-id"' in d.render()

def test_expr_9_callable_with_no_vars_in_set():
    d = DIV({lambda **kwargs: "Hello"})
    d.load_data({})
    assert 'Hello' in d.render()

def test_expr_10_callable_returning_empty_string():
    d = DIV({'hide', lambda **kwargs: "" if kwargs.get('hide') else "Visible"})
    d.load_data({'hide': True})
    assert 'Visible' not in d.render()


# --- Group 2: Variable Access (Dot Notation & Deep Access) (10 Tests) ---

class MockUser:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def test_access_1_dot_notation_dict():
    d = DIV({'user.name'})
    d.load_data({'user': {'name': 'Alice'}})
    assert 'Alice' in d.render()

def test_access_2_dot_notation_object():
    d = DIV({'user.name'})
    d.load_data({'user': MockUser('Bob', 'admin')})
    assert 'Bob' in d.render()

def test_access_3_deep_dict_access():
    d = DIV({'config.theme.color'})
    d.load_data({'config': {'theme': {'color': 'blue'}}})
    assert 'blue' in d.render()

def test_access_4_deep_mixed_access():
    d = DIV({'app.user.role'})
    d.load_data({'app': {'user': MockUser('Charlie', 'editor')}})
    assert 'editor' in d.render()

def test_access_5_dot_notation_missing_base():
    d = DIV({'missing.name'})
    d.load_data({})
    assert d.render() == '<div></div>' 

def test_access_6_dot_notation_missing_attr():
    d = DIV({'user.age'})
    d.load_data({'user': MockUser('Dave', 'user')})
    assert d.render() == '<div></div>'

def test_access_7_deep_access_missing_mid_path():
    d = DIV({'a.b.c.d'})
    d.load_data({'a': {}})
    assert d.render() == '<div></div>'

def test_access_8_dot_notation_in_attr():
    d = DIV(id={'user.id'})
    d.load_data({'user': {'id': 'u123'}})
    assert 'id="u123"' in d.render()

def test_access_9_dot_notation_parent_resolution():
    parent = DIV()
    parent.load_data({'global_store': {'theme': 'dark'}})
    child = DIV({'global_store.theme'})
    parent.add(child)
    assert 'dark' in parent.render()

def test_access_10_dot_notation_sibling_conflict():
    d = DIV({'user.name'})
    d.load_data({'user': {'name': 'Eve'}})
    assert 'Eve' in d.render()


# --- Group 3: Multi Source Data (DataPipeLineSource & | notation) (10 Tests) ---

def test_multi_1_basic_pipe():
    d = DIV({'status|Auth'})
    d.load_data(DataPipeLineSource(Auth={'status': 'Logged In'}))
    assert 'Logged In' in d.render()

def test_multi_2_named_source_add():
    src = DataPipeLineSource()
    src.add({'theme': 'light'}, name='Config')
    d = DIV({'theme|Config'})
    d.load_data(src)
    assert 'light' in d.render()

def test_multi_3_fallback_unnamed():
    src = DataPipeLineSource({'val': 42})
    d = DIV({'val'})
    d.load_data(src)
    assert '42' in d.render()

def test_multi_4_pipe_missing_source():
    src = DataPipeLineSource(Auth={'status': 'OK'})
    d = DIV({'status|Missing'})
    d.load_data(src)
    assert 'OK' not in d.render()

def test_multi_5_class_name_as_source():
    class AuthStore:
        status = "Active"
    d = DIV({'status|AuthStore'})
    d.load_data(DataPipeLineSource(AuthStore()))
    assert 'Active' in d.render()

def test_multi_6_pipe_in_attr():
    d = DIV(Class={'mode|Settings'})
    d.load_data(DataPipeLineSource(Settings={'mode': 'dark-mode'}))
    assert 'class="dark-mode"' in d.render()

def test_multi_7_multiple_sources_same_key():
    src = DataPipeLineSource()
    src.add({'id': 1}, name='S1')
    src.add({'id': 2}, name='S2')
    d1 = DIV({'id|S1'})
    d2 = DIV({'id|S2'})
    d1.load_data(src)
    d2.load_data(src)
    assert '1' in d1.render()
    assert '2' in d2.render()

def test_multi_8_search_order():
    src = DataPipeLineSource({'key': 'unnamed'}, S1={'key': 'named'})
    d = DIV({'key'})
    d.load_data(src)
    assert 'named' in d.render() 

def test_multi_9_parent_multi_source():
    parent = DIV()
    src = DataPipeLineSource(Global={'lang': 'en'})
    parent.load_data(src)
    child = DIV({'lang|Global'})
    parent.add(child)
    assert 'en' in parent.render()

def test_multi_10_dot_notation_as_source_alias():
    d = DIV({'Auth.status'})
    d.load_data(DataPipeLineSource(Auth={'status': 'Ready'}))
    assert 'Ready' in d.render()


# --- Group 4: Mixing all three (5 Tests) ---

def test_mix_1_callable_with_multi_source():
    src = DataPipeLineSource(Auth={'role': 'admin'}, Config={'debug': True})
    d = DIV({'role|Auth', 'debug|Config', lambda **k: "Admin-Debug" if k.get('role|Auth') == 'admin' and k.get('debug|Config') else "Other"})
    d.load_data(src)
    assert 'Admin-Debug' in d.render()

def test_mix_2_callable_with_deep_access_multi_source():
    src = DataPipeLineSource(App={'user': {'status': 'active'}})
    d = DIV({'App.user.status', lambda **k: "Online" if k.get('App.user.status') == 'active' else "Offline"})
    d.load_data(src)
    assert 'Online' in d.render()

def test_mix_3_attr_callable_deep_access():
    src = DataPipeLineSource({'site': {'theme': 'dark'}})
    d = DIV(Class={'site.theme', lambda **k: f"theme-{k.get('site.theme')}"})
    d.load_data(src)
    assert 'class="theme-dark"' in d.render()

def test_mix_4_complex_ui_component():
    src = DataPipeLineSource(Session={'user': MockUser('Frank', 'admin')})
    d = DIV(
        SPAN({'Session.user.name'}),
        BUTTON({'Session.user.role', lambda **k: "Delete" if k.get('Session.user.role') == 'admin' else ""})
    )
    d.load_data(src)
    res = d.render()
    assert 'Frank' in res
    assert 'Delete' in res

def test_mix_5_missing_deep_in_multi_source():
    src = DataPipeLineSource(Data={'a': {'b': {}}})
    d = DIV(
        {'Data.a.b.c', lambda **k: "Found" if k.get('Data.a.b.c') else "Fallback"}
    )
    d.load_data(src)
    assert 'Fallback' in d.render()


# --- Group 5: Variable Injection After Initialization (5 Tests) ---

def test_inject_1_add_after_init():
    d = DIV()
    d.add({'username'})
    d.load_data({'username': 'Sarah'})
    assert 'Sarah' in d.render()

def test_inject_2_set_attribute_after_init():
    d = DIV()
    d.attr_manager.set_attr('data-user', {'user_id'})
    d.load_data({'user_id': 99})
    assert 'data-user="99"' in d.render()

def test_inject_3_add_callable_after_init():
    d = DIV()
    d.add({'is_active', lambda **k: "Active" if k.get('is_active') else "Inactive"})
    d.load_data({'is_active': False})
    assert 'Inactive' in d.render()

def test_inject_4_set_class_after_init():
    d = DIV()
    d.attr_manager.set_attr('class', {'theme', lambda **k: f"bg-{k.get('theme')}"})
    d.load_data({'theme': 'dark'})
    assert 'class="bg-dark"' in d.render()

def test_inject_5_add_deep_access_after_init():
    d = DIV()
    d.add({'Auth.user.role'})
    src = DataPipeLineSource(Auth={'user': {'role': 'manager'}})
    d.load_data(src)
    assert 'manager' in d.render()

