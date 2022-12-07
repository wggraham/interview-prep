from collections import defaultdict


class Solution:
    def isInterleave(self, A, B, C):
        n, m, o = len(A), len(B), len(C)
        if n + m != o: return 0
        explored = defaultdict(bool)

        def tryAll(i, j, k):
            nonlocal A, B, C, explored
            if (i, j, k) in explored: return explored[(i, j, k)]
            if i < 0: return B[:j + 1] == C[:k + 1]
            if j < 0: return A[:i + 1] == C[:k + 1]

            explored[(i, j, k)] |= tryAll(i - 1, j, k - 1) if i >= 0 and A[i] == C[k] else False
            explored[(i, j, k)] |= tryAll(i, j - 1, k - 1) if j >= 0 and B[j] == C[k] else False
            return explored[(i, j, k)]

        return 1 if tryAll(n - 1, m - 1, o - 1) else 0

    def isInterleave2(self, A, B, C):
        # doesn't work
        yog = sorted(A+B)
        C = sorted(C)
        if yog==C:
            return 1
        return 0


A = "aabcc"
B = "zbbca"
C = "aaabbcbczc"

# A = "sblIWKBF9yT3sAw4"
# B = "OxRZnGzMeMJ7ZCwidxBSTDyaNj1D"
# C = "OsxblRZnGIWKzBF9yTMyaNj1D"
test = Solution()
print(test.isInterleave(A, B, C))
print(test.isInterleave2(A, B, C))
