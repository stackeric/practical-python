import time
from functools import wraps


def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"func : {func.__name__} time : {end - start}s")
        return res
    return wrapper


@timethis
def count_down():
    time.sleep(1)

