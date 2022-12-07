from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        i = 0
        while newInterval[0] > intervals[i][1]: i += 1
        j = i
        while j < len(intervals) and newInterval[1] >= intervals[j][0]: j += 1

        start = min(newInterval[0], intervals[i][0])
        end = max(newInterval[1], intervals[j-1][1])

        return sorted(intervals[:i] + [[start, end]] + intervals[j:])


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
intervals = [[1,3],[6,9]]
newInterval = [2,5]
test = Solution()
print(test.insert(intervals, newInterval))
