from bisect import bisect_left


class Solution:
    def prevSmaller(self, A):
        s, g = [], []

        for i, v in enumerate(A):
            while s and A[s[-1]] >= v:
                s.pop()
            j = bisect_left(s, v, key=lambda i: A[i] < v)
            g += [A[s[j - 1]]] if s and A[s[j - 1]] < v else [-1]
            s.append(i)
        return g

    def prevSmaller2(self, A):
        def bin_search():
            l, r, m = 0, len(s) - 1, 0
            while l < r:
                m = (l + r) // 2
                if A[s[m]] < v:
                    if m + 1 > len(s) or A[s[m + 1]] >= v:
                        return s[m]
                    l = m + 1
                else:
                    r = m - 1
            return s[m]

        s, g = [], []
        for i, v in enumerate(A):
            while s and A[s[-1]] >= v:
                s.pop()
            j = bin_search() if s else 0
            g += [A[j]] if s and A[j] < v else [-1]
            s.append(i)
        return g

    def prevSmaller3(self, A):
        s, g = [], [-1] * len(A)
        for i in reversed(range(len(A))):
            while s and A[i] < A[s[-1]]:
                g[s.pop()] = A[i]
            s.append(i)
        return g


A = [4, 5, 2, 10, 8]
A = [8, 23, 22, 16, 22, 7, 7, 27, 35, 27, 32, 20, 5, 1, 35, 28, 20, 6, 16, 26, 48, 34]
test = Solution()
print(test.prevSmaller(A))
print(test.prevSmaller3(A))
