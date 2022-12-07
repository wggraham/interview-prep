from typing import List
from collections import Counter
from itertools import chain


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [x for x, _ in counts.most_common(k)]

    def topKFrequent2(self, nums, k):
        bucket = [[] for _ in nums]
        for num, freq in Counter(nums).items():
            bucket[freq-1].append(num)
        flat_list = list(chain(*bucket))
        return flat_list[-k:]


nums = [1, 1, 1, 2, 2, 3]
k = 2

test = Solution()
print(test.topKFrequent(nums, k))
print(test.topKFrequent2(nums, k))
