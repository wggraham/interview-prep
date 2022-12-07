from typing import List
from collections import deque


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = total = nums[0]
        q = deque([total])

        for val in nums:
            total += val
            q.append(val)
            while q and total < 0:
                maxSum = max(maxSum, total)
                total -= q.popleft()




        while q:
            maxSum = max(maxSum, total)
            total -= q.popleft()
        return maxSum


a = [-2, -1]
a = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
print(test.maxSubArray(a))
