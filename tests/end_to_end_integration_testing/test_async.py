import asyncio
import pytest
from probo import DIV, SPAN, MAIN, SECTION, P

def test_async_simple_string():
    """Test 1: Awaiting a basic tag with an async string function."""
    async def fetch_string():
        await asyncio.sleep(0.01)
        return "Async Hello"

    async def run():
        html = await DIV(fetch_string())
        assert html == "<div>Async Hello</div>"

    asyncio.run(run())

def test_async_nested_tags():
    """Test 2: Awaiting a tag that contains an awaitable returning another tag."""
    async def fetch_tag():
        await asyncio.sleep(0.01)
        return SPAN("Nested", Class="highlight")

    async def run():
        html = await DIV("User: ", fetch_tag(), id="main-container")
        assert html == "<div id=\"main-container\">User: <span class=\"highlight\">Nested</span></div>"

    asyncio.run(run())

def test_async_multiple_awaitables():
    """Test 3: Passing multiple awaitable coroutines inside a single tag."""
    async def fetch_first():
        await asyncio.sleep(0.01)
        return "First"

    async def fetch_second():
        await asyncio.sleep(0.01)
        return SPAN("Second")

    async def run():
        # Using string concatenation internally in Probo adds spaces between text items.
        html = await SECTION(fetch_first(), "-", fetch_second())
        assert html == "<section>First -<span>Second</span></section>"

    asyncio.run(run())

def test_async_iterable_return():
    """Test 4: Awaiting a coroutine that returns a list of tags."""
    async def fetch_items():
        await asyncio.sleep(0.01)
        return [SPAN("Item 1"), SPAN("Item 2")]

    async def run():
        html = await DIV("List: ", fetch_items())
        assert html == "<div>List: <span>Item 1</span> <span>Item 2</span></div>"

    asyncio.run(run())

def test_async_deep_tree():
    """Test 5: Awaiting a deep tree of tags containing async data."""
    async def fetch_footer():
        await asyncio.sleep(0.01)
        return P("Copyright 2026")

    async def run():
        tree = MAIN(
            SECTION(
                DIV("Header")
            ),
            SECTION(
                fetch_footer()
            )
        )
        html = await tree
        assert html == "<main><section><div>Header</div></section><section><p>Copyright 2026</p></section></main>"

    asyncio.run(run())
