from heapq import *


class Solution:
    def slidingMaximum(self, a, k):
        if not a or len(a) < k:
            return []

        h = [(-v, i) for i, v in enumerate(a[:k - 1])]
        heapify(h)

        res = []
        for i in range(k-1, len(a)):
            heappush(h, (-a[i], i))
            while h[0][1] <= (i - k):
                heappop(h)
            res.append(-h[0][0])
        return res


A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
A = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
B = 2
test = Solution()
print(test.slidingMaximum(A, B))
