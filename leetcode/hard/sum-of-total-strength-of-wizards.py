from copy import copy
from heapq import heappop, heappush
from itertools import accumulate
from sys import maxsize
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        def get_totals(i, j, min_vals):
            nonlocal res
            h2 = copy(min_vals)
            for k in range(j, i):
                while min_vals and min_vals[0][1] <= k:
                    heappop(min_vals)
                res += (sum_to[i] - sum_to[k]) * min_vals[0][0] % (10 ** 9 + 7)

            if i < n - 1:
                heappush(h2, (strength[i + 1], i + 1))
                get_totals(i + 1, j, h2)

        res, n, sum_to = 0, len(strength) + 1, [0]
        for v in strength:
            sum_to.append(sum_to[-1] + v)

        strength = [0] + strength
        get_totals(0, 0, [(0, 0)])

        return res

    def totalStrength2(self, strength: List[int]) -> int:
        sum_to = list(accumulate(accumulate(strength), initial=0))
        s = [-1]
        res = 0
        strength += [0]
        for i, v in enumerate(strength):
            while s and strength[s[-1]] > v:
                j = s.pop()
                left = s[-1]
                left_sum = sum_to[j] - sum_to[max(left, 0)]
                right_sum = sum_to[i] - sum_to[j]
                left_len, right_len = j - left, i - j
                res += strength[j] * (right_sum * left_len - left_sum * right_len) % (10 ** 9 + 7)
            s.append(i)

        return res

    def totalStrength3(self, strength: List[int]) -> int:
        sum_to = list(accumulate(strength, initial=0))
        strength += [0]
        res = 0
        s = [-1]
        for i, v in enumerate(strength):
            while s and strength[s[-1]] > v:
                j = s.pop()
                min_val = strength[j]
                total1 = sum_to[j]
                for k in range(max(s[-1], 0), j):
                    total1 += k * sum_to[k]
                total2 = sum_to[i-1]
                for k in range(j+1, i):
                    total2 += k * sum_to[k]
                res += min_val * (total2 * (j - s[-1]) - total1 * (i - j))
            s.append(i)

        return res


strength = [1, 3, 1, 2]
strength = [5, 4, 6]
test = Solution()
print(test.totalStrength(strength))
# print(test.totalStrength2(strength))
print(test.totalStrength3(strength))
