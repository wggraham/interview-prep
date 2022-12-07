from typing import List
from sys import maxsize
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        seen = {(0, 0, k)}
        adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def inBounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def isBlock(i, j):
            return grid[i][j]

        q = deque([(0, 0, k, 0)])
        while q:
            i, j, k, steps = q.popleft()
            if i == n - 1 and j == m - 1:
                return steps
            for y, x in adj:
                ii, jj = i + y, j + x
                if not inBounds(ii, jj):
                    continue
                if not k and isBlock(ii, jj):
                    continue
                if (ii, jj, k - grid[ii][jj]) in seen:
                    continue
                seen.add((ii, jj, k - grid[ii][jj]))
                q.append((ii, jj, k - grid[ii][jj], steps + 1))

        return -1

    # doesn't work for single row
    def shortestPathDFS(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0 if k >= grid[0][0] else -1
        n, m = len(grid), len(grid[0])
        dp = [[{}] * m for _ in range(n)]
        adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dp[0][0] = {i: 0 for i in range(k+1)}
        visited = set()

        def inBounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def explore(i, j, k):
            if k < 0 or (i, j) in visited:
                return maxsize

            if k in dp[i][j]:
                return dp[i][j][k]

            visited.add((i, j))
            res = [explore(i + y, j + x, k - grid[i + y][j + x]) for y, x in adj if inBounds(i + y, j + x)]
            visited.remove((i, j))
            dp[i][j][k] = min(res) + 1 if res and min(res) != maxsize else maxsize
            return dp[i][j][k]

        ans = explore(n - 1, m - 1, k+1)
        return ans if ans != maxsize else -1


# doesn't get min because once a section is explored with a given k, it will not be re-explored for a smaller k value

grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
# grid = [[0, 1, 1], [1, 1, 1], [1, 0, 0]]
grid = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]
grid =[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
grid =[[0]]
grid = [[0,0,0]]

k = 1
test = Solution()
print(test.shortestPath(grid, k))
print(test.shortestPathDFS(grid, k))
