import aiohttp
import asyncio
import os
import time
import threading


async def fetcher(session, url):
    print(f'{os.getpid()} process | {threading.get_ident()} url : {url}')
    async with session.get(url) as response:
        return await response.text()


async def scrap():
    urls = ["https://apple.com", "https://google.com"] * 50

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(scrap())
    end = time.time()
    print(end - start)  # 2초
