from math import ceil, log2


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        cycles = minutesToTest // minutesToDie + 1

        return ceil(log2(buckets) / log2(cycles))


test = Solution()
print(test.poorPigs(4, 15, 15))
