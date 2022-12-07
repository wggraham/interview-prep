from sys import maxsize
import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums1, nums2) if len(nums1) >= len(nums2) else (nums2, nums1)
        n, m = len(a), len(b)
        if m == 0:
            return a[n // 2] if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2
        stepSize = m // 2
        i, j = n // 2, m // 2
        i -= 1 if not (n + m) % 2 else 0
        while stepSize > 1:
            if a[i] == b[j]:
                break
            if a[i] > b[j]:
                i -= stepSize
                j += stepSize
            elif a[i] < b[j]:
                i += stepSize
                j -= stepSize
            stepSize = math.floor(stepSize / 2)

        if (n + m) % 2:
            return min(a[i], b[j])

        res = (a[i] + b[j]) / 2
        if i > 0:
            res = min(res, (a[i - 1] + b[j + 1]) / 2)
        if j > 0:
            res = min(res, (a[i + 1] + b[j - 1]) / 2)
        return res

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        def setlr():
            return -maxsize if i == 0 else a[i - 1], \
                   -maxsize if j == 0 else b[j - 1], \
                   maxsize if i >= n else a[i], \
                   maxsize if j >= m else b[j]

        a, b = (nums1, nums2) if len(nums1) >= len(nums2) else (nums2, nums1)
        n, m = len(a), len(b)
        if not m:
            return a[n // 2] if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2
        stepSize = m // 2
        i, j = n // 2, m // 2
        l1, l2, r1, r2 = setlr()
        while stepSize >= 1:
            l1, l2, r1, r2 = setlr()

            if l1 > r2:
                i -= stepSize
                j += stepSize
            elif l2 > r1:
                i += stepSize
                j -= stepSize
            else:
                break

            stepSize = math.floor(stepSize / 2)
        return max(l1, l2) if (n + m) % 2 else (max(l1, l2) + min(r1, r2)) / 2


nums1 = [1, 3]
nums2 = [2]
# nums1 = [1,3]
# nums2 = [2,7]
test = Solution()
print(test.findMedianSortedArrays(nums1, nums2))
print(test.findMedianSortedArrays2(nums1, nums2))
