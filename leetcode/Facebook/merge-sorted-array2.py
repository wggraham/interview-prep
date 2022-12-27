from typing import List
from heapq import heapify, heapreplace, heappop


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0: return
        if m == 0:
            nums1[:n+1] = nums2
            return
        i, j, k = m - 1, n - 1, m + n - 1
        h = [(-nums1[m - 1], True), (-nums2[n - 1], False)]
        heapify(h)
        while h:
            if h[0][1]:
                if i > 0:
                    i -= 1
                    nums1[k] = -heapreplace(h, (-nums1[i], True))[0]

                else:
                    nums1[k] = -heappop(h)[0]
            else:
                if j > 0:
                    j -= 1
                    nums1[k] = -heapreplace(h, (-nums2[j], False))[0]

                else:
                    nums1[k] = -heappop(h)[0]

            k -= 1

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        for k in range(n + m - 1, -1, -1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        for k in reversed(range(n + m)):
            if j < 0:
                break
            if i < 0:
                nums1[:j + 1] = nums2[:j + 1]
                break
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [4, 5, 6]
n = 3
nums1 = [0,0,0,0,0]
m = 0
nums2 = [1,2,3,4,5]
n = 5
test = Solution()
test.merge3(nums1, m, nums2, n)
print(nums1)
