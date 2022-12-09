from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums2: return nums1
        i, n, m = 0, len(nums1), len(nums2)
        while nums1[i] != 0 and nums1[i] <= nums2[0]: i += 1

        temp, j = nums2[0], 0
        for i in range(i, n-1):
            if j < m - 1 and nums2[j] < nums1[i]:
                if nums1[i + 1] <
                j += 1

            temp, nums2[j] = max(nums2[j], temp), min(nums2[j], temp)

        nums1[-1] = temp
        return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
# nums1 = [0]
# nums2 = [1]
test = Solution()
print(test.merge(nums1, 3, nums2, 3))


