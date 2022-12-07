from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inBound(y, x):
            return 0 <= y < n and 0 <= x < m

        def explore(y, x):
            if not inBound(y, x) or grid[y][x] != '1':
                return

            grid[y][x] = '2'
            for yy, xx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                explore(y + yy, x + xx)

        n, m, islandCount = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '1':
                    continue

                explore(i, j)
                islandCount += 1

        return islandCount


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
test = Solution()
print(test.numIslands(grid))
