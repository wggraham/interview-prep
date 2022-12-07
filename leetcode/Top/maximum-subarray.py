from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = total = nums[0]

        for v in nums[1:]:
            total += v
            maxSum = max(maxSum, total)
            total = 0 if total < 0 else total

        return maxSum

    def maxSubArray2(self, nums: List[int]) -> int:
        maxSum = total = nums[0]
        for v in nums[1:]:
            total = max(v, total + v)
            maxSum = max(maxSum, total)

        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [5, 4, -1, 7, 8]
nums = [1]
nums = [-4, -5, -3, -2, -3]
nums = [-163, -20]
test = Solution()
print(test.maxSubArray(nums))
print(test.maxSubArray2(nums))
