from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights, s, area = heights + [0], [-1], 0

        for i, h in enumerate(heights):
            while len(s) > 1 and h <= heights[s[-1]]:
                height = heights[s.pop()]
                width = i - s[-1] - 1
                area = max(area, height * width)
            s.append(i)

        return area


heights = [5,4,1,2]
heights = [2,1,2]
test = Solution()
print(test.largestRectangleArea(heights))
