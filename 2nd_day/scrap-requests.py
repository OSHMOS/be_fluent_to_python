import requests  # '동기'
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def scrap():
    urls = ["https://naver.com", "https://google.com",
            "https://instagram.com"] * 10

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    scrap()
    end = time.time()
    print(end - start)
