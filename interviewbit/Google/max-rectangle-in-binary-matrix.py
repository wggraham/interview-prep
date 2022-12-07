class Solution:
    def __histogram_area__(self, hist):
        s = []
        hist = [-1] + hist + [-1]
        area = 0
        for i, val in enumerate(hist):
            while s and val < hist[s[-1]]:
                j = s.pop()
                height = hist[j]
                width = i - s[-1] - 1
                area = max(area, height * width)
            s.append(i)
        return area

    def maximalRectangle(self, A):
        n = len(A[0])
        hist = [0] * n
        area = 0
        for row in A:
            for i in range(n):
                if not row[i]:
                    hist[i] = -1
                hist[i] += 1
            area = max(area, self.__histogram_area__(hist))
        return area


test = Solution()
hist = [
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 0],
]

print(test.maximalRectangle(hist))
