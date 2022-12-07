# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import math


def isBadVersion(v):
    return v == 2147483647


class Solution:
    def firstBadVersion(self, n: int) -> int:
        v = int(math.sqrt(n))
        i = 1
        found = False
        for i in range(v, n + 1, v):
            if isBadVersion(i):
                found = True
                break

        l, r = (i - v + 1, i + 1) if found else (i, n + 1)
        for j in range(l, r):
            if isBadVersion(j):
                return j


test = Solution()
print(test.firstBadVersion(2147483647))
