import time


def block_task():
    time.sleep(1)
    print("Done")


n = 4

for i in range(n):
    block_task()
