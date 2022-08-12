import asyncio


async def function_that_returns_a_future_object():
    print("function_that_returns_a_future_object")


async def some_python_coroutine():
    print("some_python_coroutine")


async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )


asyncio.run(main())
