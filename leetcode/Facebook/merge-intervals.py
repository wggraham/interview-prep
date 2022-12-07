from sys import maxsize
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        vals = [[v, not i % 2] for val in intervals for i, v in enumerate(val, 1)]
        vals.sort()
        res = []
        start = vals[0][0]
        end = None
        for val, isEnd in vals:
            if isEnd:
                end = max(end, val) if end is not None else val
            elif end is not None and val > end:
                res.append([start,end])
                start = val

        return res + [[start, end]]

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [[-maxsize, -maxsize]]
        for start, end in intervals:
            if merged[-1][-1] < start:
                merged.append([start, end])
            merged[-1][1] = max(merged[-1][1], end)
        return merged[1:]



intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1,4],[0,0]]
# intervals = [[1,4],[0,2],[3,5]]
test = Solution()
print(test.merge(intervals))
print(test.merge2(intervals))
