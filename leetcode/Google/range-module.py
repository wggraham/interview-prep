from bisect import bisect_left, bisect_right


class RangeModule:

    def __init__(self):
        self.intervals = []

    def _getRange(self, left, right):
        return bisect_left(self.intervals, left), bisect_right(self.intervals, right)

    def addRange(self, left: int, right: int) -> None:
        start, end = self._getRange(left, right)

        interval = [left] if not start % 2 else []
        interval += [right] if not end % 2 else []

        self.intervals[start:end] = interval

    def queryRange(self, left: int, right: int) -> bool:
        end, start = self._getRange(right, left)
        return start == end and bool(start % 2)

    def removeRange(self, left: int, right: int) -> None:
        start, end = self._getRange(left, right)

        interval = [left] if start % 2 else []
        interval += [right] if end % 2 else []

        self.intervals[start:end] = interval


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10,20)
obj.removeRange(14, 16)
print(obj.queryRange(10, 14))
print(obj.queryRange(13, 15))
print(obj.queryRange(16, 17))
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)