from sys import maxsize
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        flatSchedule = [(time.start, time.end) for s in schedule for time in s]
        flatSchedule.sort(key=lambda x: (x[0], -x[1]))

        startTime, endTime, res = flatSchedule[0][0], flatSchedule[0][1], []
        for time in flatSchedule:
            if time[0] <= endTime:
                endTime = max(endTime, time[1])
                continue

            res += [Interval(endTime, time[0])] if endTime - time[0] else []
            startTime, endTime = time[0], time[1]

        return res

def toIntervals(schedules):
    res = []
    for schedule in schedules:
        t = []
        for s, e in schedule:
            t.append(Interval(s,e))
        res.append(t)
    return res

tt = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
tt = [[[45,56],[89,96]],[[5,21],[57,74]]]
tt = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
test = Solution()
v = test.employeeFreeTime(toIntervals(tt))
print(10)
