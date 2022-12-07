from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # You must write an algorithm that runs in O(n) time and without using the division operation
        n = len(nums)
        r = [1] * n
        preI, postI = 1, 1

        for i in range(n):
            r[i] *= preI
            r[-i-1] *= postI
            preI *= nums[i]
            postI *= nums[-i-1]
        return r

t = [1, 2, 3, 4]
t = [-1,1,0,-3,3]
test = Solution()
print(test.productExceptSelf(t))

