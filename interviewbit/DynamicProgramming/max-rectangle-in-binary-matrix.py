class Solution:
    def maximalRectangle(self, A):

        def histArea(hist):
            s = []
            area = 0
            hist = [-1] + hist + [-1]
            for i, val in enumerate(hist):
                while s and val < hist[s[-1]]:
                    j = s.pop()
                    height = hist[j]
                    width = i - s[-1] - 1
                    area = max(area, height * width)
                s.append(i)
            return area


        maxArea = 0
        n, m = len(A), len(A[0])

        for i in range(n):
            for j in range(m):
                if not i:
                    break
                if A[i][j]:
                    A[i][j] = A[i - 1][j] + 1
            maxArea = max(maxArea, histArea(A[i]))

        return maxArea


A = [
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 0],
]
test = Solution()
print(test.maximalRectangle(A))
