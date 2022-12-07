from typing import List


class Solution:
    def adjacent(self, nums: List[List[int]]) -> int:
        n = len(nums[0])
        if n < 3:
            return max(max(nums[0]), max(nums[1]))
        dp = [max(nums[0][i], nums[1][i]) for i in range(2)] + [0] * (n - 2)
        for i in range(2, n):
            dp[i] = max(0, nums[0][i], nums[1][i]) + max(dp[i - 2], dp[i - 3])

        return max(dp[-2:])


nums = [[1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]]
nums = [
    [74, 37, 82, 1],
    [66, 38, 16, 1]]
nums = [
  [28],
  [10]
]

nums = [
  [16, 5, 54, 55, 36, 82, 61, 77, 66, 61],
  [31, 30, 36, 70, 9, 37, 1, 11, 68, 14]
]
test = Solution()
print(test.adjacent(nums))
