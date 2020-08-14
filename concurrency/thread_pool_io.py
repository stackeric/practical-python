import asyncio
import concurrent
import time


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


if __name__ == "__main__":
    asyncio.run(main())
