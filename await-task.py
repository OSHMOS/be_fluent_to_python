import asyncio


async def nested(a):
    print(a)
    return 42


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested(3))

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task  # return을 바로 출력해주는 것은 아니다.
    # print(await task)

asyncio.run(main())
