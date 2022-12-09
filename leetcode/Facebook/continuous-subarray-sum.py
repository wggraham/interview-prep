from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen, total = {0:-1}, 0
        for i, v in enumerate(nums):
            total = (total + v) % k
            if total in seen:
                if i - seen[total] > 1:
                    return True
                continue
            seen[total] = i
        return False


nums = [23,2,4,6,6]
k = 7
test = Solution()
print(test.checkSubarraySum(nums, k))
