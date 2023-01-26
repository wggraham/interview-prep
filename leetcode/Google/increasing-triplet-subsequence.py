from sys import maxsize
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest, next_smallest = maxsize, maxsize

        for val in nums:
            if val > next_smallest:
                return True
            next_smallest = val if smallest < val < next_smallest else next_smallest
            smallest = min(val, smallest)

        return False


nums = [1, 2, 3, 4, 5]
nums = [20, 100, 10, 12, 5, 13]
nums[1:5] = [5, 10]
test = Solution()
print(test.increasingTriplet(nums))
