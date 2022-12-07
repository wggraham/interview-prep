# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
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


a = [Interval(4, 100), Interval(48, 94), Interval(16, 21), Interval(58, 71), Interval(36, 53), Interval(49, 68), Interval(18, 42), Interval(37, 90), Interval(68, 75), Interval(6, 57), Interval(25, 78), Interval(58, 79), Interval(18, 29), Interval(69, 94), Interval(5, 31), Interval(10, 87), Interval(21, 35), Interval(1, 32), Interval(7, 24), Interval(17, 85), Interval(30, 95), Interval(5, 63), Interval(1, 17), Interval(67, 100), Interval(53, 55), Interval(30, 63), Interval(7, 76), Interval(33, 51), Interval(62, 68), Interval(78, 83), Interval(12, 24), Interval(31, 73), Interval(64, 74), Interval(33, 40), Interval(51, 63), Interval(17, 31), Interval(14, 29), Interval(9, 15), Interval(39, 70), Interval(13, 67), Interval(27, 100), Interval(10, 71), Interval(18, 47), Interval(48, 79), Interval(70, 73), Interval(44, 59), Interval(68, 78), Interval(24, 67), Interval(32, 70), Interval(29, 94), Interval(45, 90), Interval(10, 76), Interval(12, 28), Interval(31, 78), Interval(9, 44), Interval(29, 83), Interval(21, 35), Interval(46, 93), Interval(66, 83), Interval(21, 72), Interval(29, 37), Interval(6, 11), Interval(56, 87), Interval(10, 26), Interval(11, 12), Interval(15, 88), Interval(3, 13), Interval(56, 70), Interval(40, 73), Interval(25, 62), Interval(63, 73), Interval(47, 74), Interval(8, 36)]

test = Solution()
print(test.merge(a))