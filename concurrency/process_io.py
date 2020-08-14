import time
from multiprocessing import Process, Queue


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


if __name__ == "__main__":
    main()
