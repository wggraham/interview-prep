from bisect import bisect

from sortedcontainers import SortedList


class MyCalendar:
    def __init__(self):
        self.intervals = [(0, 0)]

    def _is_overlap(self, start, end):
        for s, e in self.intervals:
            if start < e and s < end:
                return True
        return False

    def _merge(self):
        i = 1
        while i < len(self.intervals):
            s, e = self.intervals[i]
            ps, pe = self.intervals[i - 1]
            if pe == s:
                self.intervals.pop(i)
                self.intervals[i - 1] = (ps, max(pe, e))
            else:
                i += 1

    def _insert(self, start, end):
        i, should_merge = 0, False
        for i, ival in enumerate(self.intervals):
            s, e = ival
            if start == e or end == s:
                should_merge = True
            if end <= s:
                break

        self.intervals.insert(i, (start, end))
        if should_merge:
            self._merge()

    def book(self, start: int, end: int) -> bool:
        if self._is_overlap(start, end):
            return False

        self._insert(start, end)
        return True


class MyCalendar2:
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True


class MyCalendar3:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        i = self.calendar.bisect_right((start, end))
        if (i > 0 and self.calendar[i - 1][1] > start) or \
                (i < len(self.calendar) and self.calendar[i][0] < end):
            return False
        self.calendar.add((start, end))
        return True


class MyCalendar4:
    def __init__(self):
        self.min, self.max = [], []

    def book(self, start: int, end: int) -> bool:
        i, j = 0, len(self.min)

        while i < j:
            mid = (i + j) // 2
            if self.min[mid] <= start:
                i = mid + 1
            else:
                j = mid

        if self.check_intersect(start, end, i):
            return False

        self.min.insert(i, start)
        self.max.insert(i, end)

        return True

    def check_intersect(self, s, e, i):
        return (self.max[i - 1] > s if i >= 1 else False) or \
               (self.min[i] < e if i < len(self.min) else False)


class MyCalendar5:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        i = bisect(self.bookings, (start, end))

        if (i != 0 and start < self.bookings[i - 1][1]) or \
                (i != len(self.bookings) and end > self.bookings[i][0]):
            return False

        self.bookings.insert(i, (start, end))

        return True

# intervals = [[47, 50], [33, 41], [39, 45], [33, 42], [25, 32], [26, 35], [19, 25], [3, 8], [8, 13], [18, 27]]
intervals = [[97, 100], [33, 51], [89, 100], [83, 100], [75, 92], [76, 95], [19, 30], [53, 63], [8, 23], [18, 37],
             [87, 100], [83, 100], [54, 67], [35, 48], [58, 75], [70, 89], [13, 32], [44, 63], [51, 62], [2, 15]]
obj = MyCalendar()
for ival in intervals:
    s, e = ival
    print(obj.book(s, e))
