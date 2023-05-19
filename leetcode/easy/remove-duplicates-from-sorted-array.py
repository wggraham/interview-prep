from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]: continue
            nums[i+1] = nums[j]
            i += 1

        return i + 1


nums = [1,1,2]
test = Solution()
print(test.removeDuplicates(nums))
