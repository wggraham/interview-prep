class Solution:
    def solve(self, A):
        if not A: return 0
        n = len(A)
        dp = [[0]*n for _ in A]
        for i in range(n):
            dp[i][i] = 1

        longest = 0
        for i in reversed(range(n-1)):
            for j in range(i+1, n):
                if A[i] == A[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                longest = max(longest, dp[i][j])
        return longest



A = "bebeeed"
test = Solution()
print(test.solve(A))
