from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()

        for i, v in enumerate(nums):
            if v in d:
                return [d[v], i]
            d[target - v] = i


t = [3,2,4]
test = Solution()
print(test.twoSum(t, 6))