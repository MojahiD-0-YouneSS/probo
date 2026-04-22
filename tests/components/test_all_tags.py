import pytest
import inspect
from probo.components.elements import Element

# Functional Heavy
import probo.components.tag_functions.block_tags as heavy_tags_func
import probo.components.tag_functions.self_closing as heavy_tags2_func
import probo.components.tag_functions.svg_tags as heavy_tags3_func

# Functional Light
import probo.components.light_tags.func.block_tags as light_tags_func
import probo.components.light_tags.func.svg_tags as light_tags3_func
import probo.components.light_tags.func.self_closing as light_tags2_func

# OOP Light
import probo.components.light_tags.oop.block_tags as light_tags
import probo.components.light_tags.oop.self_closing as light_tags2
import probo.components.light_tags.oop.svg_tags as light_tags3

# OOP Heavy
import probo.components.tag_classes.block_tags as heavy_tags
import probo.components.tag_classes.self_closing as heavy_tags2
import probo.components.tag_classes.svg_tags as heavy_tags3


def test_heavy_tags_bulk_coverage():
    """Renders every heavy-weight tag function to ensure basic stability."""
    modules = [heavy_tags_func, heavy_tags2_func, heavy_tags3_func]

    for mod in modules:
        functions = [
            obj for name, obj in inspect.getmembers(mod)
            if inspect.isfunction(obj) and not name.startswith("_")
        ]
        for tag_func in functions:
            res = (
                tag_func("test content", id="test-id", Class="test-class")
                if "content" in inspect.signature(tag_func).parameters
                else tag_func(id="test-id", Class="test-class")
            )
            rendered = "".join(res)
            assert "test-id" in rendered


def test_light_tags_bulk_coverage():
    """Renders every light-weight tag function."""
    modules = [light_tags_func, light_tags2_func, light_tags3_func]
    EL = Element(is_list=True)

    for mod in modules:
        functions = [
            obj for name, obj in inspect.getmembers(mod)
            if inspect.isfunction(obj) and not name.startswith("_")
        ]
        for tag_func in functions:
            res = (
                tag_func(EL, "test", id="test-id")
                if "content" in inspect.signature(tag_func).parameters
                else tag_func(EL, id="test-id", Class="test-class")
            )
            rendered = "".join(res)
            assert 'id="test-id"' in rendered


def test_oop_light_tags_bulk_coverage():
    """Renders every light-weight OOP class."""
    modules = [light_tags, light_tags2, light_tags3]
    EL = Element(is_list=True)
    for mod in modules:
        classes = [
            obj for name, obj in inspect.getmembers(mod)
            # FIX: Use isclass, and verify it belongs to this exact module!
            if inspect.isclass(obj) and obj.__module__ == mod.__name__ and not name.startswith("_")
        ]
        for tag_cls in classes:
            res = (
                tag_cls("test", Id="test-id").render(EL)
                if "content" in inspect.signature(tag_cls).parameters
                else tag_cls(Id="test-id", Class="test-class").render(EL)
            )
            rendered = "".join(res)
            assert 'id="test-id"' in rendered


def test_oop_heavy_tags_bulk_coverage():
    """Renders every heavy-weight OOP class."""
    modules = [heavy_tags, heavy_tags2, heavy_tags3]
    for mod in modules:
        classes = [
            obj for name, obj in inspect.getmembers(mod)
            # FIX: Use isclass here too!
            if inspect.isclass(obj) and obj.__module__ == mod.__name__ and not name.startswith("_")
        ]
        for tag_cls in classes:
            res = (
                tag_cls("test", Id="test-id").render()
                if "content" in inspect.signature(tag_cls).parameters
                else tag_cls(id="test-id", Class="test-class").render()
            )
            rendered = "".join(res)
            assert 'id="test-id"' in rendered


def test_heavy_tags_bulk_stream_coverage():
    """Streams every heavy-weight tag function."""
    modules = [heavy_tags_func, heavy_tags2_func, heavy_tags3_func]

    for mod in modules:
        functions = [
            obj for name, obj in inspect.getmembers(mod)
            if inspect.isfunction(obj) and not name.startswith("_")
        ]
        for tag_func in functions:
            res = (
                tag_func("test content", stream=True, id="test-id", Class="test-class")
                if "content" in inspect.signature(tag_func).parameters
                else tag_func(stream=True, id="test-id", Class="test-class")
            )
            rendered = "".join(res)
            assert "test-id" in rendered


def test_light_tags_bulk_stream_coverage():
    """Streams every light-weight tag function."""
    modules = [light_tags_func, light_tags2_func, light_tags3_func]
    EL = Element(is_list=True)

    for mod in modules:
        functions = [
            obj for name, obj in inspect.getmembers(mod)
            if inspect.isfunction(obj) and not name.startswith("_")
        ]
        for tag_func in functions:
            res = (
                tag_func(EL, "test", stream=True, id="test-id")
                if "content" in inspect.signature(tag_func).parameters
                else tag_func(EL, stream=True, id="test-id", Class="test-class")
            )
            rendered = "".join(res)
            assert 'id="test-id"' in rendered


def test_oop_light_tags_bulk_stream_coverage():
    """Streams every light-weight OOP class."""
    modules = [light_tags, light_tags2, light_tags3]
    EL = Element(is_list=True)
    for mod in modules:
        classes = [
            obj for name, obj in inspect.getmembers(mod)
            if inspect.isclass(obj) and obj.__module__ == mod.__name__ and not name.startswith("_")
        ]
        for tag_cls in classes:
            # FIX: Call .stream() instead of .render() to get stream coverage
            res = (
                tag_cls("test", id="test-id").stream(EL)
                if "content" in inspect.signature(tag_cls).parameters
                else tag_cls(id="test-id", Class="test-class").stream(EL)
            )
            rendered = "".join(res)
            assert 'id="test-id"' in rendered


def test_oop_heavy_tags_bulk_stream_coverage():
    """Streams every heavy-weight OOP class."""
    modules = [heavy_tags, heavy_tags2, heavy_tags3]
    for mod in modules:
        classes = [
            obj for name, obj in inspect.getmembers(mod)
            if inspect.isclass(obj) and obj.__module__ == mod.__name__ and not name.startswith("_")
        ]
        for tag_cls in classes:
            # FIX: Call .stream() instead of .render()
            res = (
                tag_cls("test", id="test-id").stream()
                if "content" in inspect.signature(tag_cls).parameters
                else tag_cls(id="test-id", Class="test-class").stream()
            )
            rendered = "".join(res)
            assert 'id="test-id"' in rendered
