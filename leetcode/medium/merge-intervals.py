import operator
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)):
            intervals[i] = (intervals[i][1], intervals[i][0]) if intervals[i][1] < intervals[i][0] else (
            intervals[i][0], intervals[i][1])

        intervals.sort(key=operator.itemgetter(0, 1))
        i, n = 0, len(intervals)
        res = []

        while i < n:
            j = i + 1
            start, end = intervals[i][0], intervals[i][1]
            while j < n and end >= intervals[j][0]:
                end = max(end, intervals[j][1])
                j += 1
            res += [(start, end)]

            i = j

        return res


intervals = [[1,4],[0,2],[3,5]]
intervals = [[1,3],[2,6],[8,10],[15,18]]
test = Solution()
print(test.merge(intervals))
