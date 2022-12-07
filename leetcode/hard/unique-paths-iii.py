from collections import defaultdict


class Solution:
    def uniquePathsIII(self, grid):
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        open = 0
        start = end = None
        dp = [[] for _ in grid]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                dp[i].append(defaultdict(int))
                if not val:
                    open |= 1 << (m * i + j)
                if val == 1:
                    start = (i, j)
                if val == 2:
                    end = (i, j)
                    open |= 1 << (m * i + j)

        # dp = [[{}] * m for _ in grid]
        dp[end[0]][end[1]][0] = 1
        dp[start[0]][start[1]][open] = 0
        def dfs(opn, i, j):
            if not opn:
                return

            for y, x in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                mask = 0
                if 0 <= y < n and 0 <= x < m:
                    mask = ~(1 << (m * y + x))
                    if opn & mask not in dp[y][x] and (y, x) != end:
                        dp[y][x][opn & mask] = 0
                        dfs(opn & mask, y, x)
                    if opn & ~mask:
                        dp[i][j][opn] += dp[y][x][opn & mask]

        dfs(open, start[0], start[1])
        return dp[start[0]][start[1]][open]


test = Solution()
a = [[0,1, 2]]#, [0, 2]]
print(test.uniquePathsIII(a))
