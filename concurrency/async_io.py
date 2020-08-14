import asyncio


async def block_io():
    await asyncio.sleep(1)
    print("Done")


async def main():
    n = 4
    tasks = []
    for i in range(n):
        tasks.append(block_io())
    await asyncio.gather(*tasks)


asyncio.run(main())
