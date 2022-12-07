from typing import List
from itertools import accumulate


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = list(accumulate(cardPoints[:k]))
        right = list(accumulate(cardPoints[-k:][::-1]))

        res = max(left.pop(), right.pop())
        right = right[::-1]
        for i in range(k-1):
            res = max(res, left[i] + right[i])
        return res


cardPoints = [1,2,3,4,5,6,1]
k = 3
test = Solution()
print(test.maxScore(cardPoints, k))
