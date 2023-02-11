from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans, next_greater, s, indices, n = [], [], [], {}, len(nums2)
        for i in reversed(range(n)):
            val = nums2[i]
            while s and s[-1] <= val:
                s.pop()

            next_greater += [s[-1]] if s else [-1]
            s.append(val)
            indices[val] = i

        for v in nums1:
            ans += [next_greater[n - 1 - indices[v]]]

        return ans


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
test = Solution()
print(test.nextGreaterElement(nums1, nums2))
