# class Solution:
#     def canCompleteCircuit(self, A, B):
#         n = len(A)
#         total = 0
#         loc, nVal = -1, 0
#         for i in range(n):
#             total += A[i] - B[i]
#             if total < 0:
#                 if loc == -1:
#                     loc, nVal = i, total
#                 else:
#                     nVal += total
#                     loc = i
#                 total = 0
#         return loc + 1 if total >= -nVal else -1
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        loc, nVal = -1, 0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                if loc == -1:
                    loc, nVal = i, total
                else:
                    nVal += total
                    loc = i
                total = 0
        return loc + 1 if total >= -nVal else -1


A = [959, 329, 987, 951, 942, 410, 282, 376, 581, 507, 546, 299, 564, 114, 474, 163, 953, 481, 337, 395, 679, 21, 335,
     846, 878, 961, 663, 413, 610, 937, 32, 831, 239, 899, 659, 718, 738, 7, 209]
B = [862, 783, 134, 441, 177, 416, 329, 43, 997, 920, 289, 117, 573, 672, 574, 797, 512, 887, 571, 657, 420, 686, 411,
     817, 185, 326, 891, 122, 496, 905, 910, 810, 226, 462, 759, 637, 517, 237, 884]
test = Solution()
print(test.canCompleteCircuit(A, B))
