from _testcapi import INT_MAX, INT_MIN


class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)[::-1]
        neg = y[-1] == '-'
        y = -1 * int(y[:-1]) if neg else int(y)
        return 0 if INT_MIN > y or y > INT_MAX else y
