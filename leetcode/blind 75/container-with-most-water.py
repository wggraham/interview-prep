from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0

        while i < j:
            h = min(height[i], height[j])
            w = j - i
            area = max(area, h * w)

            if height[i] == h:
                i += 1
            else:
                j -= 1
        return area