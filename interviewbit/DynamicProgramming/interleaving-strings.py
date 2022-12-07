class Solution:
    def isInterleave(self, A, B, C):
        if len(A) + len(B) != len(C):
            return 0

        dp = {}
        def isInter(i, j, k):
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            if k == len(C):
                return 1
            inter = 0
            if i < len(A) and A[i] == C[k]:
                inter = isInter(i + 1, j, k + 1)
            if j < len(B) and B[j] == C[k]:
                inter |= isInter(i, j + 1, k + 1)
            dp[(i,j,k)] = inter
            return inter

        return isInter(0, 0, 0)


A = "aabcc"
B = "dbbca"
C = "aadbbbaccc"
test = Solution()
print(test.isInterleave(A, B, C))


