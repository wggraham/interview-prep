from heapq import *


class Solution:
    def solve(self, A, B, C):
        a = sorted(A, reverse=True)
        b = sorted(B, reverse=True)
        n = len(a)
        res = []
        s = {(0, 0)}
        h = [(-(a[0] + b[0]), 0, 0)]

        def inBounds(i, j):
            return i < n and j < n

        while len(res) < C:
            v, i, j = heappop(h)
            res.append(-v)
            if inBounds(i + 1, j) and (i + 1, j) not in s:
                s.add((i + 1, j))
                heappush(h, (-(a[i + 1] + b[j]), i + 1, j))
            if inBounds(i, j + 1) and (i, j + 1) not in s:
                s.add((i, j + 1))
                heappush(h, (-(a[i] + b[j + 1]), i, j + 1))

        return res


A = [3, 2]
B = [1, 4]
C = 2
A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
C = 4
A = [59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83]
B = [59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83]
C = 10
test = Solution()
print(test.solve(A, B, C))
