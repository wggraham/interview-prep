from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dp = [[0] * m for _ in range(n)]

        def inBounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def explore(i, j):
            val = matrix[i][j]
            if not dp[i][j]:
                dp[i][j] = 1
                for y, x in adj:
                    if inBounds(i + y, j + x) and matrix[i + y][j + x] < val:
                        dp[i][j] = max(dp[i][j], explore(i + y, j + x) + 1)
            return dp[i][j]

        longest = 0
        for i in range(n):
            for j in range(m):
                if not dp[i][j]:
                    longest = max(longest,explore(i,j))
        return longest


matrix = [[9,9,4],[6,6,8],[2,1,1]]
test = Solution()
print(test.longestIncreasingPath(matrix))
