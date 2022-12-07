from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hist = heights + [-1]
        area, s = 0, []

        for i in range(len(hist)):
            while s and hist[i] < hist[s[-1]]:
                height = hist[s.pop()]
                width = i - s[-1] - 1 if s else i
                area = max(area, height * width)
            s.append(i)

        return area

    def largestRectangleArea2(self, heights: List[int]) -> int:
        heights.append(-1)
        area, s = 0, []

        for i in range(len(heights)):
            while s and heights[i] < heights[s[-1]]:
                height = heights[s.pop()]
                width = i - s[-1] - 1 if s else i
                area = max(area, height * width)
            s.append(i)

        heights.pop()
        return area

    def getLargestSubMatrix(self, mat):
        n, m = len(mat), len(mat[0])
        largest = self.largestRectangleArea2(mat[0])
        for i in range(1, n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                mat[i][j] += mat[i-1][j]
            largest = max(largest, self.largestRectangleArea2(mat[i]))
        return largest


heights = [2,1,2]
#heights = [2,1,5,6,2,3]
#heights = [2,4]
#heights = [1,2,2]
#heights = [4,2,0,3,2,5]

m = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]
m = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
test = Solution()
print(test.largestRectangleArea2(heights))
print(test.getLargestSubMatrix(m))