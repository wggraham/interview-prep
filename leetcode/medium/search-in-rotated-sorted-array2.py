from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            l, r = (l, m - 1) if nums[l] < nums[m] and nums[l] <= target < nums[m] or (
                        nums[l] > nums[m] and (target >= nums[l] or target < nums[m])) else (m + 1, r)

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
nums = [5,1,3]
target = 5
test = Solution()
print(test.search(nums, target))
