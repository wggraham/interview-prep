from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            m = (s + e) // 2

            if nums[m] == target:
                return m

            if (nums[s] <= target < nums[m]) or \
                    (nums[s] > nums[m] and (target < nums[m] or target >= nums[s])):
                e = m - 1
            else:
                s = m + 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

test = Solution()
print(test.search(nums, target))
