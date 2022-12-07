class Solution:
    def climbStairs(self, A):
        if A < 2: return A
        a = [1, 2, 1]

        for _ in range(A - 2):
            a = [1, a[0] + a[1], a[1] + a[2]]
        return a[-1] - 1 if A % 2 else a[-1] - 1


n = 4
test = Solution()
print(test.climbStairs(n))
