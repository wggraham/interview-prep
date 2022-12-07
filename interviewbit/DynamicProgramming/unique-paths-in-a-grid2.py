class Solution:
    def uniquePathsWithObstacles(self, A):
        if not A or not A[0] or A[0][0]:
            return 0
        n, m = len(A), len(A[0])
        dp = [[0] * m for _ in A]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    continue
                if i:
                    dp[i][j] += dp[i - 1][j]
                if j:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]


t = [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]
test = Solution()
print(test.uniquePathsWithObstacles(t))
