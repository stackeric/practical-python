import time
from functools import wraps


def once_per_second(func):
    last_run = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal last_run
        now = time.perf_counter()
        if last_run != 0 and now - last_run <= 1:
            raise RuntimeError(f"Can't Run  {func.__name__} twice within 1s")
        res = func(*args, **kwargs)
        last_run = now
        return res
    return wrapper


@once_per_second
def run():
    print("I am running")
    time.sleep(0.5)


for i in range(2):
    run()
