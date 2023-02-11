from heapq import heapify, heapreplace
from random import randint
from time import time


def getMinimumOperations(executionTime, x, y):
    ans, total = 0, 0
    time = sorted(executionTime, reverse=True)

    delta = x - y
    h = [-t for t in time[:time[0]//y]]
    heapify(h)
    while -h[0] > total:
        total += y
        ans += 1
        heapreplace(h, -(-h[0] - delta))

    return ans

def getMinimumOperations2(executionTime, x, y):
    ops, time, delta, mx = 0, 0, x - y, max(executionTime)

    h = executionTime[:mx // y]
    heapify(h)
    for v in executionTime[mx // y:]:
        if v <= h[0]:
            continue
        heapreplace(h, v)

    h = [-v for v in h]
    heapify(h)
    while -h[0] > time:
        time += y
        ops += 1
        heapreplace(h, -(-h[0] - delta))

    return ops


# return the minimum number of operations that must be performed for all jobs to run to completion
tt = [3, 4, 1, 7, 6]
a = [randint(1,10) for _ in range(10000000)]
x = 8
y = 7
t0 = time()
for _ in range(1):
    print(getMinimumOperations(a, x, y))
t1 = time()
for _ in range(1):
    print(getMinimumOperations2(a, x, y))
t2 = time()
print(t1 - t0)
print(t2 - t1)