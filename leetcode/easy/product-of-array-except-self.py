from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        bProd = 1
        res = [1] * len(nums)

        for i, val in enumerate(nums):
            res[i] = bProd
            bProd *= val

        aProd = 1
        for i, val in enumerate(reversed(nums)):
            res[-1 - i] *= aProd
            aProd *= val

        return res

a = [1,2,3,4]
test = Solution()
print(test.productExceptSelf(a))
