from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        total = 0

        def getArea(h):
            i, area = 1, 0
            while i < len(h):
                if h[0] <= h[i]:
                    break
                area += h[0] - h[i]
                i += 1

            h, area = (h[::-1], 0) if i == len(h) and h[0] > h[-1] else (h[i:], area)
            return area, h

        while height:
            area, height = getArea(height)
            total += area

        return total

    def trap2(self, height: List[int]) -> int:
        if not height: return 0

        i, j, area = 0, 0, 0
        while i < len(height):
            if height[j] <= height[i]:
                j = i
            area += height[j] - height[i]
            i += 1

        if j != len(height) - 1:
            i -= 1
            k = i
            while i > j:
                if height[k] <= height[i]:
                    k = i
                area -= height[j] - height[i]
                area += height[k] - height[i]
                i -= 1
        return area

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]
height = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
test = Solution()
print(test.trap(height))
print(test.trap2(height))
