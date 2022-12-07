from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, val in enumerate(nums):
            t = target - val
            if t in d:
                return [d[t], i]
            d[val] = i


nums = [3,3]
target = 6
test = Solution()
print(test.twoSum(nums, target))
