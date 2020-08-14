import time
from functools import wraps


def countthis(func):
    n = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal n
        n += 1
        res = func(*args, **kwargs)
        print(f"func : {func.__name__} run time : {n}")
        return res
    return wrapper


@countthis
def run():
    print("I am running")


for i in range(10):
    run()