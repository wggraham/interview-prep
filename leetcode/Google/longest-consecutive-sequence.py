from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, n_min, n_max = set(nums), min(nums), max(nums)

        longest, count = 0, 0
        for i in range(n_min, n_max+2):
            if i in nums:
                count += 1
                continue

            longest = max(longest, count)
            count = 0

        return longest

    def longestConsecutive2(self, nums: List[int]) -> int:
        nums, longest = set(nums), 0
        for v in nums:
            if v - 1 in nums:   # prevents re-scanning ranges of numbers already seen
                continue

            count, num = 1, v
            while num + 1 in nums:
                num += 1
                count += 1

            longest = max(longest, count)

        return longest


nums = [0,3,7,2,5,8,4,6,0,1]
test = Solution()
print(test.longestConsecutive(nums))
print(test.longestConsecutive2(nums))
