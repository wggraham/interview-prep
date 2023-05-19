from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        for i in range(1, n + 2):
            if i not in nums:
                return i

    def firstMissingPositive2(self, nums: List[int]) -> int:
        max_val = 0
        for i, v in enumerate(nums):
            if type(v) == bool: continue
            tmp = v - 1
            while 0 <= tmp < len(nums) and type(tmp) != bool and type(nums[tmp]) != bool:
                max_val = max(max_val, tmp + 1)
                nums[tmp], tmp = True, nums[tmp] - 1

        for i, v in enumerate(nums):
            if type(v) != bool:
                return i + 1
        return max_val + 1


nums = [1, 2, 0]
# nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
test = Solution()
print(test.firstMissingPositive(nums))
nums = [1, 2, 0]
nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
# nums = [1]
print(test.firstMissingPositive2(nums))
