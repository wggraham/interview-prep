from typing import List
from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total, res, counts = 0, 0, Counter([0])

        for v in nums:
            total = (total + v) % k
            res += counts[total]
            counts[total] += 1

        return res


nums = [4, 5, 0, -2, -3, -5]
k = 5
test = Solution()
print(test.subarraysDivByK(nums, k))
