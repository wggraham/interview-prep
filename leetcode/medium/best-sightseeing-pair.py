from sys import maxsize
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i = 0
        score = -maxsize

        for j in range(1, len(values)):
            score = max(score, values[i] + values[j] + i - j)
            i = j if values[j] - 1 >= values[i] + i - j else i
        return score


v = [7,8,8,10]
test = Solution()
print(test.maxScoreSightseeingPair(v))
