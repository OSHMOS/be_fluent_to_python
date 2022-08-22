import math


def check_prime(number):
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number / i).is_integer():
            return False
    return True


print(f"check_prime(10000000) | {check_prime(10000000)}")
