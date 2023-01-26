from heapq import heapreplace, heappush, heappop
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counts, most_used_room, most_used_count = [0] * n, 0, 0
        earliest_available, room_available = [], [i for i in range(n)]

        for start, end in sorted(meetings):
            while earliest_available and earliest_available[0][0] <= start:
                heappush(room_available, heappop(earliest_available)[1])

            room = room_available[0] if room_available else earliest_available[0][1]

            if room_available:
                heappush(earliest_available, (end, heappop(room_available)))
            else:
                # heapreplace(earliest_available, (max(end - start + earliest_available[0][0], end), room))
                heapreplace(earliest_available, (end - start + earliest_available[0][0], room))

            counts[room] += 1
            if counts[room] > most_used_count or \
                    (counts[room] == most_used_count and room < most_used_room):
                most_used_count, most_used_room = counts[room], room

        return most_used_room

    def mostBooked2(self, n: int, meetings: List[List[int]]) -> int:
        earliest_available, room_available, counts = [], [i for i in range(n)], [0] * n

        for start, end in sorted(meetings):
            while earliest_available and earliest_available[0][0] <= start:
                heappush(room_available, heappop(earliest_available)[1])

            room = room_available[0] if room_available else earliest_available[0][1]
            counts[room] += 1

            if room_available:
                heappush(earliest_available, (end, heappop(room_available)))
            else:
                heapreplace(earliest_available, (end - start + earliest_available[0][0], room))

        return counts.index(max(counts))


n = 2
meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
n = 4
meetings = [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]
n = 4
meetings = [[19, 20], [14, 15], [13, 14], [11, 20]]
n = 4
meetings = [[48, 49], [22, 30], [13, 31], [31, 46], [37, 46], [32, 36], [25, 36], [49, 50], [24, 34], [6, 41]]
n = 97
meetings = [[432, 463], [50, 258], [168, 486], [379, 463], [315, 323], [176, 408], [8, 280], [146, 486], [345, 435],
            [318, 329], [118, 287], [473, 481], [486, 489], [449, 453], [79, 364], [468, 494], [326, 455], [11, 217],
            [24, 438], [215, 241], [463, 486], [169, 237], [324, 394], [120, 377], [1, 442], [479, 490], [241, 292],
            [182, 203], [179, 266], [21, 170], [55, 264], [183, 349], [349, 479], [116, 242], [393, 450], [236, 298],
            [257, 460], [443, 451]]
test = Solution()
print(test.mostBooked(n, meetings))
