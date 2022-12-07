import time
from typing import List
from collections import defaultdict


class Solution:
    def canPartitionBruteForce(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        total //= 2

        def tryAll(a, p):
            res = False
            if p == total:
                return True
            for i in range(len(a)):
                res |= tryAll(a[:i] + a[i + 1:], p + a[i])
            return res

        return tryAll(nums, 0)

    def canPartitionTopDown(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        total //= 2
        dp = defaultdict(bool)

        def tryAll(a, p):
            n = len(a)
            if p < 0:
                return False
            if p == 0:
                return True
            if (n, p) in dp:
                return dp[(n, p)]
            for i in range(n):
                dp[(n, p)] |= tryAll(a[:i] + a[i + 1:], p - a[i])
            return dp[(n, p)]

        return tryAll(nums, total)

    def canPartitionTopDownImproved(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        total //= 2
        dp = defaultdict(bool)

        def tryAll(i, p):
            if p < 0 or i < 0:
                return False
            if p == 0:
                return True
            if (i, p) in dp:
                return dp[(i, p)]

            dp[(i, p)] |= tryAll(i - 1, p - nums[i]) or tryAll(i - 1, p)
            return dp[(i, p)]

        return tryAll(len(nums) - 1, total)

    def canPartitionBottomUp(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        total //= 2
        pSums = {total}

        for i, v in enumerate(nums):
            t = set()
            for x in pSums:
                val = x - v
                if val < 0:
                    continue
                if val == 0:
                    return True
                if val not in pSums:
                    t.add(val)
            pSums.update(t)

        return False


nums = [1, 5, 11, 5]
# nums = [1,2,3,5]
nums = [4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12, 12, 12, 12, 12, 12, 16, 16, 16, 16, 16, 16, 16, 16,
        20, 20, 20, 20, 20, 20, 20, 20, 24, 24, 24, 24, 24, 24, 24, 24, 28, 28, 28, 28, 28, 28, 28, 28, 32, 32, 32, 32,
        32, 32, 32, 32, 36, 36, 36, 36, 36, 36, 36, 36, 40, 40, 40, 40, 40, 40, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44,
        48, 48, 48, 48, 48, 48, 48, 48, 52, 52, 52, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56, 56, 56, 56, 60, 60, 60, 60,
        60, 60, 60, 60, 64, 64, 64, 64, 64, 64, 64, 64, 68, 68, 68, 68, 68, 68, 68, 68, 72, 72, 72, 72, 72, 72, 72, 72,
        76, 76, 76, 76, 76, 76, 76, 76, 80, 80, 80, 80, 80, 80, 80, 80, 84, 84, 84, 84, 84, 84, 84, 84, 88, 88, 88, 88,
        88, 88, 88, 88, 92, 92, 92, 92, 92, 92, 92, 92, 96, 96, 96, 96, 96, 96, 96, 96, 97, 99]
test = Solution()
# t0 = time.time()
# print(test.canPartitionBruteForce(nums))
t1 = time.time()
print(test.canPartitionTopDownImproved(nums))
t2 = time.time()
# print(test.canPartitionBottomUp(nums))
t3 = time.time()
print(test.canPartitionBottomUp(nums))
t4 = time.time()
# print("Brute Force: ", t1 - t0)
print("Top Down DP: ", t2 - t1)
# print("Bottom Up New: ", t3 - t2)
print("Bottom Up Old: ", t4 - t3)

