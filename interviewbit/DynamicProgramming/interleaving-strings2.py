class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        n, m, o = len(A), len(B), len(C)
        found = {}

        def explore(i, j, k):
            if (i,j) in found: return found[i,j]
            if k == o:
                found[(i, j)] = 1
                return found[(i, j)]

            match = 0
            if i < n and A[i] == C[k]:
                match = explore(i + 1, j, k + 1)
                if match: return 1
            if j < m and B[j] == C[k]:
                match |= explore(i, j + 1, k + 1)

            return match

        return explore(0, 0, 0)


A = "aabcc"
B = "dbbca"
C = "aadbbcbcac"
test = Solution()
print(test.isInterleave(A, B, C))
