import bisect
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        for i,v in enumerate(nums):
            if target - v in vals:
                return [vals[target - v], i]
            vals[v] = i

    def twoSumNoSpace(self, nums: List[int], target: int) -> List[int]:
        # to get the correct initial indices you would need additional space
        def bin_search(i, val):
            nonlocal nums
            s, e = i + 1, len(nums) - 1

            while s <= e:
                m = (s+e) // 2
                if nums[m] == val:
                    return m
                if nums[m] < val:
                    s = m + 1
                elif nums[m] > val:
                    e = m - 1
            return 0

        nums.sort()
        for i, v in enumerate(nums):
            j = bin_search(i, target - v)
            if j:
                return [i, j]


nums = [3, 2, 4]
target = 6
test = Solution()
print(test.twoSum(nums, target))
print(test.twoSumNoSpace(nums, target))
