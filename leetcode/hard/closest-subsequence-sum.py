from bisect import bisect_left
from sys import maxsize
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def get_all_sums(a):
            sums = {0}
            for v in a:
                sums = sums.union({x + v for x in sums})
            return sums

        s1 = get_all_sums(nums[1::2])
        s2 = sorted(get_all_sums(nums[::2]))

        ans = maxsize
        for s in s1:
            remain = goal - s
            i = bisect_left(s2, remain)
            if i < len(s2):
                ans = min(ans, abs(remain - s2[i]))
            if i > 0:
                ans = min(ans, abs(remain - s2[i - 1]))
        return ans

    def minAbsDifference2(self, nums: List[int], goal: int) -> int:
        def gen_sums(i, pSum):
            if i < 0:
                return {pSum}
            return gen_sums(i - 1, pSum).union(gen_sums(i - 1, pSum + s[i]))

        s = nums[:len(nums) // 2]
        s1, s = gen_sums(len(s) - 1, 0), nums[len(nums) // 2:]
        s2, ans = sorted(gen_sums(len(s) - 1, 0)), maxsize

        for s in s1:
            remain = goal - s
            i = bisect_left(s2, remain)
            if i < len(s2):
                ans = min(ans, abs(remain - s2[i]))
            if i > 0:
                ans = min(ans, abs(remain - s2[i - 1]))
        return ans

    def minAbsDifference3(self, nums: List[int], goal: int) -> int:
        def get_all_sums(a):
            sums = {0}
            for v in a:
                sums |= {x + v for x in sums}
            return sums

        s1 = get_all_sums(nums[1::2])
        s2 = sorted(get_all_sums(nums[::2]))

        ans = maxsize
        for s in s1:
            remain = goal - s
            i = bisect_left(s2, remain)
            if i < len(s2):
                ans = min(ans, abs(remain - s2[i]))
            if i > 0:
                ans = min(ans, abs(remain - s2[i - 1]))
        return ans

    def minAbsDifference4(self, nums: List[int], goal: int) -> int:
        def get_all_sums(a):
            sums = {0}
            for v in a:
                sums |= {x + v for x in sums}
            return sums

        s1 = get_all_sums(nums[1::2])
        s2 = sorted(get_all_sums(nums[::2]))

        ans = maxsize
        for s in s1:
            remain = goal - s
            i = bisect_left(s2, remain)
            i += i <= 0
            i -= i == len(s2)
            ans = min(ans, abs(remain - s2[i]), abs(remain - s2[i - 1]))
        return ans

    def minAbsDifference5(self, nums: List[int], goal: int) -> int:
        def get_all_sums(a):
            sums = {0}
            for v in a:
                sums |= {x + v for x in sums}
            return sums

        s1 = get_all_sums(nums[1::2])
        s2 = sorted(get_all_sums(nums[::2]))

        ans = 10 ** 10
        for s in s1:
            remain = goal - s
            i = bisect_left(s2, remain)
            ans = min([abs(remain - s2[x]) for x in (i - 1, i) if 0 <= x < len(s2)] + [ans])
        return ans


nums = [5, -7, 3, 5]
goal = 6
test = Solution()
print(test.minAbsDifference(nums, goal))
print(test.minAbsDifference2(nums, goal))
print(test.minAbsDifference3(nums, goal))
print(test.minAbsDifference4(nums, goal))
print(test.minAbsDifference5(nums, goal))
