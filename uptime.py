import time
import math
from datetime import datetime
import client_example

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

c = client_example.Communicator()

while True:
    try:
        now = datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds_since_midnight = int((now - midnight).total_seconds())

        if is_prime(seconds_since_midnight):
            c.send_msg("8,ON")
            print(seconds_since_midnight)
        else:
            c.send_msg("8,OFF")
    except:
        c.send_msg("8,ERROR")
    time.sleep(1)
