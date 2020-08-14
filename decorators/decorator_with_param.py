import time
from functools import wraps


def timethis(format="day"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            res = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"func : {func.__name__} time : {end - start}s")
            print(f"func : {func.__name__} params : {format}")
            return res
        return wrapper

    return decorator


@timethis("year")
def count_down():
    time.sleep(1)


count_down()
