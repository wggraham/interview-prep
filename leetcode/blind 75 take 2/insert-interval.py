from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        if newInterval[0] <= intervals[0][0] and newInterval[1] >= intervals[-1][-1]: return [newInterval]
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        if newInterval[0] > intervals[-1][-1]: return intervals + [newInterval]

        j, k = 0, len(intervals) - 1
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0] and newInterval[1] < intervals[i + 1][0]:
                return intervals[:i + 1] + [newInterval] + intervals[i + 1:]

            if intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                j = i
            if intervals[i-1][0] < newInterval[1] < intervals[i][0]:
                k = i - 1

        x = min(newInterval[0], intervals[j][0])
        y = max(newInterval[1], intervals[k][1])
        return intervals[:j] + [[x, y]] + intervals[k + 1:]

    def insertWorking(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i, output = 0, []

        # Append first non-overlapping intervals
        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        # Merge overlapping intervals (if no overlapping then just append newInterval)
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        output.append(newInterval)

        # Append remaining non-overlapping intervals
        while i < n:
            output.append(intervals[i])
            i += 1

        return output

    def insertWorking2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        i, n = 0, len(intervals)

        # Append first non-overlapping intervals
        while i < n and intervals[i][1] < newInterval[0]: i += 1

        if i < n:
            newInterval[0] = min(intervals[i][0], newInterval[0])
        # Merge overlapping intervals (if no overlapping then just append newInterval)
        j = i
        while j < n and intervals[j][0] <= newInterval[1]: j += 1

        if newInterval[1] >= intervals[j-1][0]:
            newInterval[1] = max(intervals[j-1][1], newInterval[1])
        return intervals[:i] + [newInterval] + intervals[j:]

    def insertWorking3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0

        # Append first non-overlapping intervals
        while i < n and intervals[i][1] < newInterval[0]: i += 1

        # Merge overlapping intervals (if no overlapping then just append newInterval)
        j = i
        while j < n and intervals[j][0] <= newInterval[1]:
            newInterval[0] = min(intervals[j][0], newInterval[0])
            newInterval[1] = max(intervals[j][1], newInterval[1])
            j += 1

        return intervals[:i] + [newInterval] + intervals[j:]

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
# intervals = [[0, 2], [3, 3], [6, 11]]
# newInterval = [9, 15]
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
intervals = [[2,4],[5,7],[8,10],[11,13]]
newInterval = [3,6]
intervals = [[1,5]]
newInterval = [6,8]
intervals = [[1,5]]
newInterval = [0,0]
test = Solution()
print(test.insertWorking(intervals, newInterval))
print(test.insertWorking2(intervals, newInterval))
print(test.insertWorking3(intervals, newInterval))
