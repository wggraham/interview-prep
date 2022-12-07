class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        n, m = len(A), len(B)
        if m > n: return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = [1] * (n + 1)

        for i, b in enumerate(B):
            for j, a in enumerate(A):
                dp[i + 1][j + 1] = dp[i + 1][j]

                if a == b:
                    dp[i + 1][j + 1] += dp[i][j]
        return dp[-1][-1]


A = "rabbbit"
B = "rabbit"
A = "abc"
B = "abc"
test = Solution()
print(test.numDistinct(A,B))
