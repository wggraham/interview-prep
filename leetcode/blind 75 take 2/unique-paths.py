class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for _ in range(1, n):
            temp = [1] * m
            for j in range(1, m):
                temp[j] = temp[j-1] + dp[j]
            dp = temp

        return dp[-1]


m = 3
n = 7
m = 3
n = 2
test = Solution()
print(test.uniquePaths(m,n))