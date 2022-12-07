from typing import List
from bisect import bisect_left, bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect_left(nums, target)
        j = bisect(nums, target, lo=i)
        return [i, j-1] if i < len(nums) and nums[i] == target else [-1, -1]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        i, j = bisect_left(nums, target), bisect(nums, target)
        return [i, j-1] if i < len(nums) and nums[i] == target else [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
test = Solution()
print(test.searchRange(nums, target))
