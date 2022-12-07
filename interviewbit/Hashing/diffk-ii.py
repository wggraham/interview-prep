class Solution:
    def diffPossible(self, nums, k):
        vals = set()
        for i, v in enumerate(nums):
            if v - k in vals or v + k in vals:
                return 1
            vals.add(v)
        return 0

A = [1, 5, 3]
k = 7
A = [ 77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37, 39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77, 12, 93, 0 ]
B = 53
test = Solution()
print(test.diffPossible(A, B))
