from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()#key=lambda time: (time[1], time[0]))

        j, res, count = 0, 0, 0
        for i in range(len(intervals)):
            while intervals[j][1] <= intervals[i][0]:
                count -= 1
                j += 1
            count += 1
            res = max(res, count)
        return res


    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        ends = [e for _, e in intervals]
        starts = [s for s, _ in intervals]
        ends.sort()
        starts.sort()

        j, res, count = 0, 0, 0
        for time in ends:
            while j < len(starts) and starts[j] < time:
                count += 1
                j += 1
            res = max(res, count)
            count -= 1
        return res


intervals = [[0, 30], [5, 10], [15, 20]]
# intervals =[[7,10],[2,4]]
#intervals = [[5, 8], [6, 8]]
#intervals = [[6,17],[8,9],[11,12],[6,9]]
test = Solution()
print(test.minMeetingRooms(intervals))
print(test.minMeetingRooms2(intervals))
