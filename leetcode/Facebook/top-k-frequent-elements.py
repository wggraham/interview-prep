from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [v for v, c in Counter(nums).most_common(k)]



nums = [1, 1, 1, 2, 2, 3]
k = 2
test = Solution()
print(test.topKFrequent(nums, k))