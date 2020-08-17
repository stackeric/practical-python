## Python Concurrency

GIL is ok for IO bound program.


### 1. 基础block任务

``` python
def block_task():
    time.sleep(1)
    print("Done")

```

### 2. asyncio运行

``` python
async def block_io():
    await asyncio.sleep(1)
    print("Done")


async def main():
    n = 4
    tasks = []
    for i in range(n):
        tasks.append(block_io())
    await asyncio.gather(*tasks)

```

### 3. 多进程

``` python
def block_task(q):
    time.sleep(1)
    q.put("Done")


def main():
    n = 4
    tasks = []
    q = Queue()
    result = []
    for i in range(n):
        p = Process(target=block_task, args=(q,))
        tasks.append(p)

    for i in tasks:
        i.start()

    for i in tasks:
        res = q.get()
        result.append(res)

    for i in tasks:
        i.join()

    for r in result:
        print(r)
```

### 4. 多线程

``` python
lock = Lock()


def block_task(q):
    time.sleep(1)
    global lock
    lock.acquire()
    q.append("Done")
    lock.release()


def main():
    n = 4
    tasks = []
    result = []
    for i in range(n):
        p = Thread(target=block_task, args=(result,))
        tasks.append(p)

    for i in tasks:
        i.start()

    for i in tasks:
        i.join()

    for r in result:
        print(r)
```

### 5. 异步线程池

``` python
def block_task():
    time.sleep(1)
    return "Done"


async def main():
    n = 4
    tasks = []
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as pool:
        for i in range(n):
            tasks.append(loop.run_in_executor(pool, block_task))

        results = [await f for f in asyncio.as_completed(tasks)]

        for i in results:
            print(i)
```

### 6. 异步进程池

``` python
def block_task():
    time.sleep(1)
    return "Done"


async def main():
    n = 4
    tasks = []
    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor(max_workers=n) as pool:
        for i in range(n):
            tasks.append(loop.run_in_executor(pool, block_task))

        results = [await f for f in asyncio.as_completed(tasks)]

        for i in results:
            print(i)
```