class Solution:
    def prevSmaller(self, A):
        s, g = [], [-1] * len(A)
        for i in range(len(A)):
            while s and A[s[-1]] >= A[i]:
                s.pop()
            if s:
                g[i] = A[s[-1]]
            s.append(i)

        return g
