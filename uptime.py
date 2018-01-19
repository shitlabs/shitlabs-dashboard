import time
import math

def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0 or number < 2:
        return False

    i = 5
    w = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += w
        w = 6 - w

    return True

t0 = time.time()
while True:

    t = int(time.time() - t0)
    if is_prime(t):
        print(time.time() - t0, t)

    time.sleep(1)
