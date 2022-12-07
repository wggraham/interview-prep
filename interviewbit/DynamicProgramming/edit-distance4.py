class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        if not A or not B: return 0
        A = ' ' + A
        B = ' ' + B

        dp = [[0] * len(B) for _ in A]
        dp[0] = [x for x in range(len(B))]
        for i in range(len(A)):
            dp[i][0] = i

        for i, a in enumerate(A[1:]):
            for j, b in enumerate(B[1:]):
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j] + 1, dp[i][j + 1] + 1) \
                    if a == b else min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
        return dp[-1][-1]


a = "abad"
b = "abac"
a = "Anshuman"
b = "Antihuman"
a = "aa"
b = "aaa"
test = Solution()
print(test.minDistance(a, b))
