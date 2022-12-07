import time

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        n, m = len(A), len(B)
        if m > n: return 0

        dp = {}

        def explore(i, j):
            nonlocal dp, n, m
            if (i, j) in dp: return dp[(i, j)]
            if j >= m: return 1
            if i >= n: return 0

            dp[(i, j)] = explore(i + 1, j)
            if A[i] == B[j]:
                dp[(i, j)] += explore(i + 1, j + 1)
            return dp[(i, j)]

        return explore(0, 0)

    def numDistinct2(self, A, B):
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


A = "rrrraabbbbiiiiiiiitt"
B = "rabbit"

test = Solution()
t0 = time.time()
print(test.numDistinct2(A, B))
t1 = time.time()
print(test.numDistinct(A, B))
t2 = time.time()

print("iterative: ", t1 - t0)
print("recursive: ", t2 - t1)
