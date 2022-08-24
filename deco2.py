# Decorator
from time import time
from unittest import result


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f"It took {t2-t1}s")
        return result
    return wrapper


@performance
def long_time(x):
    for i in range(x):
        1*5


long_time(10000000)
