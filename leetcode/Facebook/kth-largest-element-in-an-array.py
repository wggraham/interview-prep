import time
from typing import List
from heapq import heapreplace, heapify, heappushpop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for val in nums[k:]:
            heapreplace(heap, max(val, heap[0]))
        return heap[0]

    def findKthLargestpush(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for val in nums[k:]:
            heappushpop(heap, val)
        return heap[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for val in nums[k:]:
            if val <= heap[0]: continue
            heapreplace(heap, val)
        return heap[0]

nums = [3,2,1,5,6,4]
k = 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
nums = [2,1]
k = 2
nums = [5,2,4,1,3,6,0]
k = 4

test = Solution()
t0 = time.time()
print(test.findKthLargest(nums, k))
t1 = time.time()
print(test.findKthLargestpush(nums, k))
t2 = time.time()
print(test.findKthLargest2(nums, k))
t3 = time.time()
print(t1-t0)
print(t2-t1)
print(t3-t2)