import operator


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def __merge(self, intervals):
        r = []
        if len(intervals) == 0:
            return r

        for i in intervals:
            i.start, i.end = (i.end, i.start) if i.end < i.start else (i.start, i.end)

        intervals.sort(key=lambda i: (i.start, i.end))

        mn, mx = intervals[0].start, intervals[0].end
        for i in intervals[1:]:
            if i.start > mx:
                r.append(Interval(mn, mx))
                mn = i.start
            mx = max(mx, i.end)
        r.append(Interval(mn, mx))
        return r

    def insert(self, intervals, new_interval):
        intervals.append(new_interval)
        for i in intervals:
            i.start, i.end = (i.end, i.start) if i.end < i.start else (i.start, i.end)

        intervals.sort(key=lambda i: (i.start, i.end))

        return self.__merge(intervals)
