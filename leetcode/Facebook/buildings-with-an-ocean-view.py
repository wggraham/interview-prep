from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res, n, highest = [], len(heights), 0
        for i, height in enumerate(reversed(heights)):
            res += [n - i - 1] if height > highest else []
            highest = max(highest, height)
        return res[::-1]


heights = [4, 2, 3, 1]
test = Solution()
print(test.findBuildings(heights))
