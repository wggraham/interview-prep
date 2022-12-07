class Solution:
    def minDistance(self, A, B):
        if len(A) < len(B):
            A, B = B, A

        A = ' ' + A
        B = ' ' + B
        n, m = len(A), len(B)

        ed = [[0] * m for _ in A]
        for i in range(n):
            if i < m:
                ed[0][i] = i
            ed[i][0] = i

        for i in range(1, n):
            for j in range(1, m):
                ed[i][j] = min(ed[i-1][j-1], ed[i-1][j], ed[i][j-1])
                if A[i] != B[j]:
                    ed[i][j] += 1
        return ed[-1][-1] if ed[-1][-1] else n-m

test = Solution()
a = "abac"
b = "aac"
print(test.minDistance(a, b))
