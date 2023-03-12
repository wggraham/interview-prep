from collections import defaultdict
from time import time


class Solution:
    def numDistinct(self, A, B):
        n, m = len(A), len(B)
        c_map = defaultdict(list)
        for i, c in enumerate(B):
            c_map[c].append(i)
        ways = [0 for _ in range(m)]

        for i, c in enumerate(A):
            if c not in c_map: continue

            for j in c_map[c]:
                if j == 0:
                    ways[0] += 1
                elif j > 0 and ways[j - 1] > 0:
                    ways[j] = ways[j - 1] * ways[j] if ways[j] else ways[j - 1]

        return ways[-1]

    def numDistinct2(self, A, B):
        n, m = len(A), len(B)
        if m > n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] if A[j - 1] == B[i - 1] else dp[i][j - 1]

        return dp[m][n]

    def numDistinct3(self, A, B):
        def rec(p1, p2):
            if p2 > p1:
                return 0
            elif p2 == -1:
                return 1
            if (p1, p2) not in d:
                if A[p1] == B[p2]:
                    d[(p1, p2)] = rec(p1 - 1, p2 - 1) + rec(p1 - 1, p2)
                else:
                    d[(p1, p2)] = rec(p1 - 1, p2)
            return d[(p1, p2)]

        d = {}
        return rec(len(A) - 1, len(B) - 1)

    def numDistinct4(self, A, B):
        n, m = len(A), len(B)
        dp = [1] + [0] * m

        for i in range(1, n + 1):
            for j in reversed(range(1, m + 1)):
                if A[i - 1] == B[j - 1]:
                    dp[j] = dp[j - 1] + dp[j]

        return dp[-1]

    def numDistinct5(self, A, B):
        dp, n, m = [1] + [0] * len(B), len(A), len(B)
        for c in A:
            for j in reversed(range(1, m + 1)):
                if c != B[j - 1]: continue
                dp[j] += dp[j - 1]

        return dp[-1]

    def numDistinct6(self, seq, word):
        chrs = defaultdict(list)
        for i in reversed(range(len(word))):
            chrs[word[i]].append(i)

        seq = [c for c in seq if c in chrs]
        i, j = 0, len(seq) - 1
        while i < j + 1 and seq[i] != word[0]: i += 1
        while j > i and seq[j] != word[-1]: j -= 1
        seq = seq[i:j + 1]

        dp = [1] + [0] * len(word)
        for c in seq:
            for j in chrs[c]:
                dp[j + 1] += dp[j]

        return dp[-1]


A = "rabbbit"
B = "rabbit"
# A = "abc"
# B = "abc"
A = "aaaababbababbaabbacdaababzaaabbbaaabbb"
B = "bbabacdbza"
test = Solution()
t0 = time()
for _ in range(10):
    test.numDistinct6(A, B)
t1 = time()
for _ in range(10):
    test.numDistinct5(A, B)
t2 = time()

print(t1 - t0)
print(t2 - t1)
# print(((t1 - t0) - (t2 - t1)) / (t1 - t0) * 100)
print(((t2 - t1) - (t1 - t0)) / (t2 - t1) * 100)