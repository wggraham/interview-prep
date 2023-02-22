class Solution:
    def uniquePathsWithObstacles(self, A):
        n, m = len(A), len(A[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            if A[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(m):
            if A[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                if A[i][j]: continue
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


A = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]
A = [[0]]
A = [
  [0, 0]
]
test = Solution()
print(test.uniquePathsWithObstacles(A))
