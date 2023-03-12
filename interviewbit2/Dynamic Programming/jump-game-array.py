class Solution:
    def canJump(self, A):
        reach = 0
        for i, v in enumerate(A):
            if reach < i: return 0
            reach = max(reach, i + v)

        return 1


A = [2, 3, 1, 1, 4]
A = [3, 2, 1, 0, 4]
test = Solution()
print(test.canJump(A))
