from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, n = 0, len(nums)
        while i < n and nums[i] != 0:
            i += 1
        j = i + 1
        while j < n and nums[j] == 0:
            j += 1
        if j >= n: return
        count = sum(1 for v in nums if v == 0)
        for j in range(j, n):
            if nums[j] == 0:
                continue
            nums[i] = nums[j]
            i += 1
        if not count: return
        nums[-count:] = [0] * count

    def moveZeroes2(self, nums: List[int]) -> None:
        j = 0
        for v in nums:
            if v == 0: continue
            nums[j] = v
            j += 1
        nums[j:] = [0] * (len(nums) - j)


nums = [0, 1, 0, 3, 12]
# nums = [1,0]
# nums = [0,0,1]
# nums = [1]
# nums = [0,0,0,0,0,0,1,1,1]
test = Solution()
test.moveZeroes2(nums)
print(nums)
