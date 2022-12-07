from typing import List
from copy import copy


class Solution:
    def rob(self, nums: List[int]) -> int:
        maxTo = copy(nums)
        for i, v in enumerate(nums[2:]):
            maxTo[i + 2] = max(maxTo[max(0, i - 1):i + 1]) + v
        return max(maxTo[-3:])

    def robCircular(self, nums: List[int]) -> int:
        prev = cur = 0

        for v in nums[2:-2]:
            temp = prev
            prev = cur
            cur = max(cur, temp + v)

        p = c = 0
        for i in range(-2, 2):
            v = nums[i]
            temp = p
            p = c
            c = max(c, temp + v)
        return cur + c

s = [1, 2, 3, 1]
s = [2, 7, 9, 3, 1]
s = [2,3,2]
s = [1,2,3,1]
test = Solution()
print(test.rob(s))
print(test.robCircular(s))

