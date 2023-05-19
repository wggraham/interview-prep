class Solution:
    def numDistinct2(self, s: str, t: str) -> int:
        def count(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            return count(i + 1, j) + count(i + 1, j + 1) if s[i] == t[j] else count(i + 1, j)

        return count(0, 0)

    def numDistinct(self, s: str, t: str) -> int:
        dp = [[1] * (len(s) + 1)] + [[0] * (len(s) + 1) for _ in range(len(t))]
        for i in range(len(s)):
            for j in reversed(range(min(i + 1, len(t)))):
                dp[j + 1][i + 1] = dp[j+1][i] + dp[j][i] if s[i] == t[j] else dp[j+1][i]

        return dp[-1][-1]


s = "rabbbit"
t = "rabbit"
s = "babgbag"
t = "bag"
test = Solution()
print(test.numDistinct(s, t))
# print(test.numDistinct2(s, t))
