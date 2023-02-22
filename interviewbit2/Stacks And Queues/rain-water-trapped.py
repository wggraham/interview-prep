class Solution:
    def trap(self, A):
        area, j = 0, 0
        for i, h in enumerate(A):
            if h < A[j]:
                area += A[j] - h
            else:
                j = i

        prev, pp = A[j], A[-1]
        for h in reversed(A[j:]):
            area -= prev - h
            if h < pp:
                area += pp - h
            else:
                pp = h

        return area


A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
test = Solution()
print(test.trap(A))
