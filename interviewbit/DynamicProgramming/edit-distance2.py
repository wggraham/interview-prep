class Solution:
    def minDistance(self, A, B):
        a = " " + A
        b = " " + B
        dp = [[0]*len(b) for _ in range(len(a))]
        for i in range(len(a)):
            dp[i][0] = i

        for i in range(len(b)):
            dp[0][i] = i

        for i in range(1, len(a)):
            for j in range(1, len(b)):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                dp[i][j] += 1 if a[i] != b[j] else 0
        return dp[-1][-1]


A = "aaa"
B = "aa"
test = Solution()
print(test.minDistance(A, B))

