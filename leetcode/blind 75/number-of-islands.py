from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[False] * m for _ in grid]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def inBounds(y, x):
            nonlocal n, m
            return 0 <= x < m and 0 <= y < n

        def isIsland(y, x):
            nonlocal grid
            return grid[y][x] == "1"

        def explore(i, j):
            nonlocal grid, dp, directions
            s = [(i, j)]
            while s:
                y, x = s.pop()
                dp[y][x] = True
                for ii, jj in directions:
                    r, c = y + ii, x + jj
                    if not inBounds(r, c) or not isIsland(r, c) or dp[r][c]:
                        continue
                    s.append((r, c))

        count = 0
        for i in range(n):
            for j in range(m):
                if dp[i][j] or not isIsland(i, j):
                    continue
                explore(i, j)
                count += 1
        return count


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
test = Solution()
print(test.numIslands(grid))
