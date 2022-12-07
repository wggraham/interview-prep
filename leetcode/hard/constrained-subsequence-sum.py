from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        pSum = [x for x in nums]
        for i in range(1, len(nums)):
            pSum[i] = max(max([x for x in pSum[max(0, i - k):i]]) + nums[i], nums[i])

        return max(pSum)

# for large k use maxHeap with (value, index) tuples

nums = [-1,-2,-3]
k = 1
test = Solution()
print(test.constrainedSubsetSum(nums, k))
