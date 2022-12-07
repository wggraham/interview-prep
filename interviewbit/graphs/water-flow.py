from collections import deque


class Solution:
    def solve(self, A):
        if not A:
            return 0

        total = 0
        n, m = len(A), len(A[0])
        dp = [[0] * m for _ in A]

        def inBounds(i, j):
            nonlocal n, m
            return 0 <= i < n and 0 <= j < m

        def canFlow(x, y):
            return x <= y

        def explore(q):
            nonlocal A, total, dp
            seen = set(q)
            while q:
                i, j = q.popleft()
                dp[i][j] += 1
                if dp[i][j] == 2:
                    total += 1
                for k, l in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    y, x = i + k, j + l
                    if inBounds(y, x) and \
                            canFlow(A[i][j], A[y][x]) and \
                            (y, x) not in seen:
                        seen.add((y, x))
                        q.append((y, x))

        q = deque([(0, i) for i in range(m)] + [(i, 0) for i in range(1, n)])
        explore(q)

        q = deque([(i, m - 1) for i in range(n)] + [(n - 1, i) for i in range(m-1)])
        explore(q)

        return total


A = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]

# A = [[2,2],[2,2]]

test = Solution()
print(test.solve(A))
