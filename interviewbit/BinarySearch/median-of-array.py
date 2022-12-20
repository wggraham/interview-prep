from bisect import bisect_left
from sys import maxsize
import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, A, B):
        A, B = (B, A) if not A else (A, B)
        if not B:
            return A[len(A) // 2] * 1.0 if len(A) % 2 else (A[len(A) // 2 - 1] + A[len(A) // 2]) / 2.0
        l1, l2, r1, r2, n, m, m1, m2 = 0, 0, 0, 0, len(A), len(B), len(A) // 2, len(B) // 2
        step = min(n, m) // 2

        while step:
            l1 = -maxsize if m1 == 0 else A[m1 - 1]
            l2 = -maxsize if m2 == 0 else B[m2 - 1]
            r1 = maxsize if m1 >= n else A[m1]
            r2 = maxsize if m2 >= m else B[m2]
            if l1 > r2:
                m1 -= step
                m2 += step
            elif l2 > r1:
                m1 += step
                m2 -= step
            else:
                break
            step //= 2
            # step = math.floor(step / 2)
        return max(l1, l2) if (n + m) % 2 else (max(l1, l2) + min(r1, r2)) / 2

    def findMedianSortedArrays23(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums2, nums1) if len(nums2) > len(nums1) else (nums1, nums2)
        n, m = len(a), len(b)
        after = (n + m - 1) // 2
        mid = bisect_left(range(m), True, key=lambda i: after - i - 1 < 0 or b[i] >= a[after - i - 1])
        next_few = sorted(a[after - mid:after - mid + 2] + b[mid: mid + 2])
        return (next_few[0] + next_few[1 - (n + m) % 2]) / 2.0

    def findMedianSortedArrays33(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums2, nums1) if len(nums2) > len(nums1) else (nums1, nums2)
        n, m = len(a), len(b)
        after = (n + m - 1) // 2
        l, r = 0, m

        while l < r:
            mid = (l + r) // 2
            if after - mid - 1 < 0 or b[mid] >= a[after - mid - 1]:
                r = mid
            else:
                l = mid + 1

        median_values = sorted(a[after - l: after - l + 2] + b[l:l + 2])[:2]
        return median_values[0] * 1.0 if (n + m) % 2 else sum(median_values) / 2.0

    def findMedianSortedArrays22(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums1, nums2) if len(nums1) >= len(nums2) else (nums2, nums1)
        n, m, l1, l2, r1, r2 = len(a), len(b), 0, 0, 0, 0

        if not m:
            return a[n // 2] if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2
        stepSize = m // 2
        i, j = n // 2, m // 2
        while stepSize >= 1:
            l1 = -maxsize if i == 0 else a[i - 1]
            l2 = -maxsize if j == 0 else b[j - 1]
            r1 = maxsize if i >= n else a[i]
            r2 = maxsize if j >= m else b[j]

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

    def findMedianSortedArrays2(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            n, m = m, n
            A, B = B, A
        if m == 0:
            if n == 0:
                return 0
            if n % 2:
                return B[n / 2]
            else:
                return (B[n / 2] + B[n / 2 - 1]) / 2.0
        low = 0
        high = m
        while low <= high:
            i = (low + high) / 2
            j = (m + n + 1) / 2 - i
            if (j == 0 or i == m or B[j - 1] <= A[i]) and (i == 0 or j == n or A[i - 1] <= B[j]):
                if (m + n) % 2:
                    if i == 0:
                        return B[j - 1]
                    elif j == 0:
                        return A[i - 1]
                    return max(A[i - 1], B[j - 1])
                else:
                    if i == 0:
                        return (B[j - 1] + min(A[i], B[j])) / 2.0
                    if j == 0:
                        return (A[i - 1] + min(A[i], B[j])) / 2.0
                    if i == m:
                        return (max(A[i - 1], B[j - 1]) + B[j]) / 2.0
                    if j == n:
                        return (max(A[i - 1], B[j - 1]) + A[i]) / 2.0
                    return (max(A[i - 1], B[j - 1]) + min(A[i], B[j])) / 2.0
            elif j == 0 or i == m or B[j - 1] > A[i]:
                low = i + 1
            elif i == 0 or j == n or A[i - 1] > B[j]:
                high = i - 1
        return -1

    def findMedianSortedArrays3(self, A, B):
        nums1 = A
        nums2 = B

        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = n1
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            if cut1 == 0:
                left1 = -1000000
            else:
                left1 = nums1[cut1 - 1]

            if cut2 == 0:
                left2 = -1000000
            else:
                left2 = nums2[cut2 - 1]

            if cut1 == n1:
                right1 = 1000000
            else:
                right1 = nums1[cut1]

            if cut2 == n2:
                right2 = 1000000
            else:
                right2 = nums2[cut2]

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2 == 0:
                    return float(max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1

    def findMedianSortedArrays4(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, hl = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = hl - i
            if i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_left = B[j - 1]
                elif j == 0:
                    max_left = A[i - 1]
                else:
                    max_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_left
                else:
                    if i == m:
                        min_right = B[j]
                    elif j == n:
                        min_right = A[i]
                    else:
                        min_right = min(A[i], B[j])
                    return (max_left + min_right) / 2.0


test = Solution()
A = [1, 4, 5]
B = [2, 3, 6]
A = []
B = [20]
B = [0, 23]
A = [-40, -25, 5, 10, 14, 28, 29, 48]
B = [-48, -31, -15, -6, 1, 8]
print(test.findMedianSortedArrays(A, B))
print(test.findMedianSortedArrays22(A, B))
print(test.findMedianSortedArrays23(A, B))
# print(test.findMedianSortedArrays34(A, B))
print(test.findMedianSortedArrays33(A, B))
