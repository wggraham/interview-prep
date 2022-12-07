from collections import defaultdict


class Solution:
    def isInterleave(self, A, B, C):
        if not A or not B or not C or len(A) + len(B) != len(C):
            return 0

        dp = defaultdict()

        def explore(i, j, k):
            if (i, j) in dp:
                return dp[(i, j)]
            if k < 0:
                return 1
            if i < 0 and j >= 0:
                return B[:j+1] == C[:k+1]
            if j < 0 and i >= 0:
                return A[:i+1] == C[:k+1]

            dp[(i, j)] = 0
            if A[i] == C[k]:
                dp[(i, j)] |= explore(i - 1, j, k - 1)
            if B[j] == C[k]:
                dp[(i, j)] |= explore(i, j - 1, k - 1)
            return dp[(i, j)]

        return explore(len(A) - 1, len(B) - 1, len(C) - 1)


test = Solution()
A = "aabcc"
B = "dbbca"
C = "aadbbbaccc"

print(test.isInterleave(A, B, C))
