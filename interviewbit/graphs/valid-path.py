class Solution:
    def solve(self, x, y, n, r, a, b):

        def inRange(i, j):
            nonlocal r
            return (i ** 2 + j ** 2) <= r ** 2

        def getAffectedOffsets():
            nonlocal r
            rngs = []
            for i in range(-r - 1, r + 1):
                for j in range(-r - 1, r + 1):
                    if inRange(i, j):
                        rngs.append((i, j))
            return rngs

        def inBounds(i, j):
            return 0 <= i <= y and 0 <= j <= x

        grid = [[0] * (x + 1) for _ in range(y + 1)]

        rngs = getAffectedOffsets()
        for i, j in zip(b, a):
            for rr, cc in rngs:
                ii, jj = i + rr, j + cc
                if inBounds(ii, jj):
                    grid[ii][jj] = 2

        if grid[0][0] == 2 or grid[y][x] == 2:
            return "NO"

        s = [(0, 0)]
        adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, -1)]
        while s:
            i, j = s.pop()
            if i == y and j == x:
                return "YES"

            for r, c in adj:
                ii, jj = i + r, j + c
                if inBounds(ii, jj) and grid[ii][jj] < 1:
                    grid[ii][jj] = 1
                    s.append((ii, jj))

        return "NO"


x = 2
y = 3
N = 1
R = 1
A = [2]
B = [3]
test = Solution()
print(test.solve(x, y, N, R, A, B))
