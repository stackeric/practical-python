import time
from threading import Thread, Lock

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


if __name__ == "__main__":
    main()
