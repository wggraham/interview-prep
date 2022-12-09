from typing import List


class Solution:
    # this trash solution only works if no duplicate numbers are adjacent
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 3: return nums.index(max(nums))
        l, r, m = 0, len(nums) - 1, 0
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
                continue
            l = m + 1
        return m if nums[m] > nums[m + 1] else m + 1


nums = [1, 2, 3, 1]
nums = [1, 2, 1, 3, 5, 6, 4]
test = Solution()
print(test.findPeakElement(nums))
