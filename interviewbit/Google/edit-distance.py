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

    def minDistance2(self, A, B):
        if not A or not B: return 0
        a = ' ' + A
        b = ' ' + B

        dp = [[0] * len(b) for _ in a]
        dp[0] = [x for x in range(len(b))]
        for i in range(len(a)):
            dp[i][0] = i

        for i, x in enumerate(a[1:]):
            for j, y in enumerate(b[1:]):
                dp[i + 1][j + 1] = dp[i][j] if x == y else \
                    min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
        return dp[-1][-1]

    def minDistance3(self, A, B):
        if not A or not B: return 0

        dp = [0] * (len(B) + 1)
        for i, a in enumerate(A):
            dp_next = [i] + [0] * len(B)
            for j, b in enumerate(B):
                if a == b:
                    dp_next[j + 1] = dp[j]
                    continue
                dp_next[j + 1] = min(dp[j + 1], dp[j], dp_next[j]) + 1
            dp = dp_next
        return dp[-1]

    def minDistance4(self, A, B):
        m = len(A)
        n = len(B)
        dp = [[None] * (n + 1) for i in range(m + 1)]

        def rec(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if dp[i][j]:
                return dp[i][j]
            if A[i - 1] == B[j - 1]:
                dp[i][j] = rec(i - 1, j - 1)
                return dp[i][j]
            else:
                ins = rec(i, j - 1) + 1
                dell = rec(i - 1, j) + 1
                sub = rec(i - 1, j - 1) + 1
                dp[i][j] = min(ins, dell, sub)
                return dp[i][j]

        return rec(len(A), len(B))


o = "Anshumancampant"
m = "tntihumantestan"
test = Solution()
print(test.minDistance(o, m))
print(test.minDistance2(o, m))
print(test.minDistance3(o, m))
print(test.minDistance4(o, m))
