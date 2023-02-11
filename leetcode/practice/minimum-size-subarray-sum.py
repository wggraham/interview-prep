from sys import maxsize
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, j, total = maxsize, 0, 0

        for i, v in enumerate(nums):
            total += v
            if total < target: continue
            while total >= target:
                total -= nums[j]
                j += 1
            ans = min(ans, i - j + 2)

        return ans


target = 7
nums = [2, 3, 1, 2, 4, 3]
target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
# target = 4
# nums = [1, 4, 4]
# target = 11
# nums = [1, 2, 3, 4, 5]
test = Solution()
print(test.minSubArrayLen(target, nums))
