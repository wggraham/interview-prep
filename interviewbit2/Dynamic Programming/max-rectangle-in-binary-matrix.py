class Solution:
    def histogram_area(self, hist):
        area, s = 0, []
        hist = [0] + hist + [0]
        for i, h in enumerate(hist):
            while s and hist[s[-1]] > h:
                area = max(area, hist[s.pop()] * (i - s[-1]-1))
            s.append(i)

        return area

    def maximalRectangle(self, A):
        hist = A[0]
        area = self.histogram_area(A[0])

        for i in range(1, len(A)):
            for j in range(len(A[0])):
                hist[j] = hist[j] + 1 if A[i][j] == 1 else 0
            area = max(area, self.histogram_area(hist))

        return area

    def maximalRectangle2(self, A):
        def histArea(hist):
            hist, area, s = [-1] + hist + [-1], 0, []
            for i, val in enumerate(hist):
                while s and val < hist[s[-1]]:
                    height = hist[s.pop()]
                    width = i - s[-1] - 1
                    area = max(area, height * width)
                s.append(i)
            return area

        max_area = histArea(A[0])
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                A[i][j] += A[i - 1][j] if A[i][j] else 0
            max_area = max(max_area, histArea(A[i]))

        return max_area


A = [
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 0]
]
A = [
  [0, 0, 1, 0, 0, 0, 1, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 0, 0, 1, 1, 0, 1],
  [0, 1, 0, 0, 0, 0, 1, 1, 1],
  [1, 0, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 1, 1, 0, 1, 1, 1, 1],
  [1, 1, 1, 0, 1, 0, 1, 0, 1]
]
test = Solution()
print(test.maximalRectangle(A))
print(test.maximalRectangle2(A))
