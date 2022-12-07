from bisect import bisect_left
from sys import maxsize
from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, v in enumerate(nums):
            j = bisect_left(nums, -v, i + 1)
            if j == len(nums) or v != -nums[j]:
                continue
            res.add(tuple(sorted((v, -v))))
        return res

    def twoSumHash(self, nums: List[int]) -> List[List[int]]:
        sums, res = set(), set()
        for i, v in enumerate(nums):
            if -v in sums:
                res.add(tuple(sorted((v, -v))))
            sums.add(v)

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n, sums = set(), len(nums), defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if -nums[j] in sums:
                    res.add(tuple(sorted((sums[-nums[j]][0], sums[-nums[j]][1], nums[j]))))
                sums[nums[j] + nums[i]] = [min(nums[i], nums[j]), max(nums[i], nums[j])]

        return res

    def threeSumNoSort(self, nums: List[int]) -> List[List[int]]:
        res, n, sums, prev = set(), len(nums), defaultdict(list), -maxsize
        for i, v in enumerate(nums):
            if v == prev: continue
            prev = v
            for j, v2 in enumerate(nums[i + 1:]):
                comp = -(v + v2)
                if comp in sums:
                    res.add(tuple(sorted((sums[comp][0], sums[comp][1], comp))))
                sums[v + v2] = [min(v, v2), max(v, v2)]

        return res

    def threeSumNoSort2(self, nums: List[int]) -> List[List[int]]:
        res, n, prev = set(), len(nums), -maxsize
        vals = {v:i for i, v in enumerate(nums)}

        for i, v in enumerate(nums):
            if v == prev: continue
            prev = v
            for j, v2 in enumerate(nums[i + 1:], i + 1):
                comp = -(v + v2)
                if comp in vals and vals[comp] not in (i, j):
                    res.add(tuple(sorted((comp, v, v2))))

        return res

    def threeSumNoSort3(self, nums: List[int]) -> List[List[int]]:
        res, n, prev = set(), len(nums), -maxsize
        vals = {}

        for i, v in enumerate(nums):
            if v not in vals:
                vals[v] = i
            for j, v2 in enumerate(nums[i + 1:], i + 1):
                comp = -(v + v2)
                if comp in vals and vals[comp] not in (i, j):
                    res.add(tuple(sorted((comp, v, v2))))

        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, res = len(nums), set()
        for i in range(n):
            for j in range(i + 1, n):
                k = bisect_left(nums, -(nums[i] + nums[j]), j + 1)
                if 0 > k or k == n or nums[k] != -(nums[i] + nums[j]): continue
                res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return res


nums = [-1, 0, 1, 2, -1, -4]
# nums = [1, 2, -2, -1]
# nums = [0,0,0]
test = Solution()
# print(test.twoSum(nums))
# print(test.twoSumHash(nums))
# print(test.threeSum(nums))
print(test.threeSumNoSort(nums))
print(test.threeSumNoSort2(nums))
print(test.threeSumNoSort3(nums))
# print(test.threeSum2(nums))
