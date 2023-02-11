class Solution:
    def solve(self, A):
        def inBounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def get_adjacent(i, j, val):
            return {(y, x) for y, x in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
                    if inBounds(y, x) and dp[y][x] < val and A[i][j] <= A[y][x]}

        n, m = len(A), len(A[0])
        cells = {(i, 0) for i in range(n)}.union({(0, i) for i in range(m)})
        dp = [[0] * m for _ in range(n)]

        while cells:
            r, c = cells.pop()
            dp[r][c] = 1
            cells.update(get_adjacent(r, c, 1))

        cells = {(i, m - 1) for i in range(n)}.union({(n - 1, i) for i in range(m)})
        res = 0
        while cells:
            r, c = cells.pop()
            dp[r][c] += 2
            if dp[r][c] == 3:
                res += 1
            cells.update(get_adjacent(r, c, 2))

        return res


A = [
       [1, 2, 2, 3, 5],
       [3, 2, 3, 4, 4],
       [2, 4, 5, 3, 1],
       [6, 7, 1, 4, 5],
       [5, 1, 1, 2, 4]
     ]
test = Solution()
print(test.solve(A))
