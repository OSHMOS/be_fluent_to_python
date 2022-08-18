import requests
import os
import time
import threading


def fetcher(session, url):
    print(f'{os.getpid()} process | {threading.get_ident()} url : {url}')
    with session.get(url) as response:
        return response.text


def scrap():
    urls = ["https://apple.com", "https://google.com"] * 50

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    scrap()
    end = time.time()
    print(end - start)  # 16초
