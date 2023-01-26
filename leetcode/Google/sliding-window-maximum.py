from typing import List
from heapq import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, max_heap = [], [(-v, i) for i, v in enumerate(nums[:k-1])]
        heapify(max_heap)

        for i, val in enumerate(nums[k-1:], k-1):
            while max_heap and max_heap[0][1] <= i - k:
                heappop(max_heap)

            if max_heap and val >= -max_heap[0][0]:
                max_heap = []

            heappush(max_heap, (-val, i))
            res.append(-max_heap[0][0])

        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# nums = [1, -1]
# k = 1

test = Solution()
print(test.maxSlidingWindow(nums, k))
