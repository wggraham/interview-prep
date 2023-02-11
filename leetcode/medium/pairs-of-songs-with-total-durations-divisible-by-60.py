from collections import Counter
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = Counter()
        ans = 0
        for t in time:
            rem = t % 60
            v = 60 - rem if rem else 0
            if v in counts:
                ans += counts[v]
            counts[rem] += 1

        return ans


time = [30, 20, 150, 100, 40]
# time = [60, 60, 60]
test = Solution()
print(test.numPairsDivisibleBy60(time))
