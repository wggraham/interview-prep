class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        if not A:
            return

        n, m = len(A), len(A[0])
        adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def inBounds(y, x):
            return 0 <= y < n and 0 <= x < m

        def isRegion(y, x):
            nonlocal A
            return A[y][x] == 'O'

        def capture(i, j):
            nonlocal A, n, m, adjacent, explored
            A[i][j] = 'X'
            c = False
            for ii, jj in adjacent:
                y, x = ii + i, jj + j
                if inBounds(y, x) and isRegion(y, x) and not explored[y][x]:
                    capture(y, x)

        def explore(i, j):
            nonlocal A, n, m, explored, adjacent
            explored[i][j] = True

            for ii, jj in adjacent:
                y, x = ii + i, jj + j
                if inBounds(y, x) and isRegion(y, x) and not explored[i][j]:
                    explore(y, x)

        explored = [[False] * m for _ in A]

        # explore edges because 'O's on edges cannot be part of an enclosed region
        for j in range(m):
            if isRegion(0, j):
                explore(0, j)
            if isRegion(n - 1, j):
                explore(n - 1, j)

        for i in range(n):
            if isRegion(i, 0):
                explore(i, 0)
            if isRegion(i, m - 1):
                explore(i, m - 1)

        # total = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if not isRegion(i, j):
                    continue
                capture(i, j)
                # total += 1
        return A

A = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

test = Solution()
x = test.solve(A)
print(10)