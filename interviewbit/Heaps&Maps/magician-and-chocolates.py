from heapq import heapify, heapreplace, heappush, heappop
import time

class Solution:
    def nchoc(self, x, bags):
        h = []
        for i, c in enumerate(bags):
            if i < x:
                heappush(h, c)
            elif c > h[0]:
                heapreplace(h, c)

        h = [-v for v in h]
        heapify(h)

        total = 0
        for i in range(x):
            t = -h[0]
            total += t

            heapreplace(h, -(t // 2))
        return total % 1000000007

    def nchoc2(self, x, bags):
        total = 0
        h = [-v for v in bags]
        heapify(h)
        for _ in range(x):
            total += -heapreplace(h, -(-h[0] >> 1))

        return total % 1000000007

    def nchoc3(self, A, B):
        h = [-b for b in B]
        heapify(h)
        s = 0
        for _ in range(A):
            chocs = -heappop(h)
            s = (s + chocs) % 1000000007
            heappush(h, -(chocs // 2))
        return s




A = 3
B = [6, 5]
A =20
B = [2, 4, 6, 8, 10, 7, -10, -3, -2, 2, 4, 6, 8, 10, 7, -10, -3, -2, 2, 4, 6, 8, 10, 7, -10, -3, -2]
# A = 10
# B = [2147483647, 2000000014, 2147483647]
test = Solution()
t0 = time.time()
test.nchoc(A, B)
t1 = time.time()
test.nchoc2(A, B)
t2 = time.time()
test.nchoc3(A, B)
t3= time.time()

print(t1-t0)
print(t2-t1)
print(t3-t2)
