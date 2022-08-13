import aiohttp  # '비동기'
import asyncio
import time


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def scrap():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(scrap())
    end = time.time()
    print(end - start)
