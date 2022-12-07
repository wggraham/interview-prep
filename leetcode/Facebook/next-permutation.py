from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = n = len(nums)
        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]: break

        for j in reversed(range(i+1, n)):
            if nums[j] > nums[i]: break

        if nums[i] >= nums[j]:
            nums[:] = nums[::-1]
            return

        nums[j], nums[i] = nums[i], nums[j]
        nums[i+1:] = sorted(nums[i+1:])

    def nextPermutation2(self, nums: List[int]) -> None:
        i, j = len(nums) - 2, len(nums) - 1
        if i < 0: return
        while i and nums[i] >= nums[i+1]: i -= 1
        while j and nums[j] <= nums[i]: j -= 1

        if nums[i] >= nums[j]:
            nums[:] = nums[::-1]
            return

        nums[j], nums[i] = nums[i], nums[j]
        nums[i+1:] = nums[i+1:][::-1]




nums = [2, 3, 1]
nums = [4, 2, 0, 2, 3, 2, 0]
nums = [1, 3, 2]
nums = [1,2]
nums = [3,2,1]
nums2 = [3,2,1]
test = Solution()
test.nextPermutation(nums)
test.nextPermutation2(nums2)
print(nums)
print(nums2)
