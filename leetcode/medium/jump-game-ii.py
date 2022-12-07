from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        l, r = 0, nums[0]
        hops = 1
        while r < len(nums) - 1:
            hops += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r + 1, nxt
        return hops


nums = [2, 3, 1, 1, 4]
test = Solution()
print(test.jump(nums))
