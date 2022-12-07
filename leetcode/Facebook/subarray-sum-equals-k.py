from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts, total, res = Counter(), 0, 0

        for val in nums:
            total += val

            res += counts[total - k]
            counts[total] += 1

        return res

    # sliding window doesn't handle negative values without sorting first
    def subarraySum2(self, nums: List[int], k: int) -> int:
        ans, total, n, i, j = 0, 0, len(nums), 0, 0
        if n == 1:
            return 1 if nums[0] == k else 0

        while i < n:
            while i < n and total < k:
                total += nums[i]
                i += 1
            while j < i and total > k:
                total -= nums[j]
                j += 1

            if total == k:
                ans += 1
                total -= nums[j]
                j += 1
        return ans


nums = [1,1,1]
k = 2
nums = [1,2,3]
k = 3
nums = [-1,-1,1]
k = 0
nums = [1,2,1,2,1]
k = 3

test = Solution()
print(test.subarraySum(nums, k))
print(test.subarraySum2(nums, k))
