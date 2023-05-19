from functools import lru_cache


class Solution:
    def isInterleave(self, A, B, C):
        @lru_cache(None)
        def is_interleave(i, j):
            if i == n:
                return j == m or B[j:] == C[i + j:]
            if j == m:
                return A[i:] == C[i + j:]
            found = is_interleave(i + 1, j) if A[i] == C[i + j] else False
            return is_interleave(i, j + 1) if not found and B[j] == C[i + j] else found

        n, m = len(A), len(B)
        if n + m != len(C): return 0
        return 1 if is_interleave(0, 0) else 0


A = "aabcc"
B = "dbbca"
C = "aadbbcbcac"
A = "aabcc"
B = "dbbca"
C = "aadbbbaccc"
test = Solution()
print(test.isInterleave(A, B, C))
