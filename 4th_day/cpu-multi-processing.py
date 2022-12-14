import time
import os
import threading
from concurrent.futures import ProcessPoolExecutor

# nums = [50, 63, 32]
# nums = [30] * 100
nums = [50] * 100


def cpu_bound_func(num):
    print(f'{os.getpid()} process | {threading.get_ident()} thread, {num}')
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    executor = ProcessPoolExecutor(max_workers=10)
    result = list(executor.map(cpu_bound_func, nums))
    print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 64.70, 16.56, 400.86
