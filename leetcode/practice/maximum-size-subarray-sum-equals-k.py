from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans, total, sums = 0, 0, {0: -1}
        for i, v in enumerate(nums):
            total += v
            if total not in sums:
                sums[total] = i
            if total - k in sums:
                ans = max(ans, i - sums[total - k])

        return ans


nums = [1, -1, 5, -2, 3]
k = 3
nums = [-2,-1,2,1]
k = 1
test = Solution()
print(test.maxSubArrayLen(nums, k))
