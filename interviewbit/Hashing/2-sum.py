class Solution:
    def twoSum(self, nums, target):
        vals = {}
        for i, v in enumerate(nums):
            if target - v in vals:
                return [vals[target - v] + 1, i + 1]
            if v not in vals:
                vals[v] = i
        return []


A = [2, 7, 11, 15]
B = 9
A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
B = -3

test = Solution()
print(test.twoSum(A, B))
