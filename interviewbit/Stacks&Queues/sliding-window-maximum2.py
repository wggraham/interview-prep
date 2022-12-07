from heapq import heapify, heappop, heappush
from collections import deque
from sys import maxsize


class Solution:
    def slidingMaximum(self, nums, size):
        res, ms = [], [(-v, i) for i, v in enumerate(nums[:size - 1])]
        heapify(ms)

        for i, v in enumerate(nums[size - 1:], size - 1):
            while ms and ms[0][1] <= i - size:
                heappop(ms)
            heappush(ms, (-v, i))
            res.append(-ms[0][0])

        return res

    def slidingMaximum2(self, nums, size):
        q, res = deque([x for x in reversed(range(size)) if nums[x] > max(nums[x+1:size] + [-maxsize])][::-1]), []

        for i, v in enumerate(nums[size - 1:], size - 1):
            while q and nums[q[-1]] <= v:
                q.pop()

            q.append(i)
            if q[0] <= i - size:
                q.popleft()

            res.append(nums[q[0]])

        return res


A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# A = [3, 2, 1]
B = 2
A = [648, 614, 490, 138, 657, 544, 745, 582, 738, 229, 775, 665, 876, 448, 4, 81, 807, 578, 712, 951, 867, 328, 308,
     440, 542, 178, 637, 446, 882, 760, 354, 523, 935, 277, 158, 698, 536, 165, 892, 327, 574, 516, 36, 705, 900, 482,
     558, 937, 207, 368]
B = 9
A = [1]
B = 1
test = Solution()
print(test.slidingMaximum(A, B))
print(test.slidingMaximum2(A, B))
