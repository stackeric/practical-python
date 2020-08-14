import time
from functools import wraps


def cache(func):
    memory = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # only if args is hashable else pickle it before
        nonlocal memory
        if args in memory:
            print(f"read result from memory")
            return memory[args]
        res = func(*args, **kwargs)
        memory[args] = res
        return res
    return wrapper


@cache
def add(x, y):
    return x+y


add(1, 1)
add(1, 2)
add(1, 1)
