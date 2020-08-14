## Python Decorator

装饰器使您可以在函数或类中注入或修改代码.


### 1. 统计运行时间

``` python
def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"func : {func.__name__} time : {end - start}s")
        return res
    return wrapper
```

### 2. 带参数统计运行时间

``` python
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
```

### 3. 统计函数运行次数

``` python
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
```

### 4. 限制函数运行次数

``` python
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
```

### 5. 缓存函数运行结果

``` python
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
```

### 5. 为类增加额外属性

``` python
def log_getattribute(cls):
    def new_getattribute(self, name):
        print('getting:', name)
    return orig_getattribute(self, name)
    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass
```