class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4: return n

        b2 = 3
        b1 = 2

        for i in range(3, n):
            t = b1 + b2
            b1 = b2
            b2 = t
        return t


test = Solution()
print(test.climbStairs(5))
