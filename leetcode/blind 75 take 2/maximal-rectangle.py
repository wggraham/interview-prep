from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def histogramArea(hist):
            s, area, hist = [-1], 0, hist + [0]

            for i in range(len(hist)):
                while hist[i] < hist[s[-1]]:  # why not pop equal values ?
                    height = hist[s.pop()]
                    width = i - s[-1] - 1
                    area = max(area, height * width)
                s.append(i)
            return area

        n, m = len(matrix), len(matrix[0])
        matrix = [[int(matrix[i][j]) for j in range(m)] for i in range(n)]

        maxArea = histogramArea(matrix[0])
        for i in range(1, n):
            for j in range(m):
                matrix[i][j] = matrix[i - 1][j] + 1 if matrix[i][j] else 0
            maxArea = max(maxArea, histogramArea(matrix[i]))

        return maxArea

    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        def histogramArea(hist):
            s, area, hist = [-1], 0, hist + [0]

            for i in range(len(hist)):
                while hist[i] < hist[s[-1]]:
                    height = hist[s.pop()]
                    width = i - s[-1] - 1
                    area = max(area, height * width)
                s.append(i)
            return area

        n, m, maxArea = len(matrix), len(matrix[0]), 0
        hist = [0] * m

        for i in range(n):
            for j in range(m):
                hist[j] = hist[j] + 1 if matrix[i][j] == '1' else 0
            maxArea = max(maxArea, histogramArea(hist))

        return maxArea


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
test = Solution()
print(test.maximalRectangle(matrix))
print(test.maximalRectangle2(matrix))

