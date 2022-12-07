class Solution:
    def climbNaive(self, n: int) -> int:
        if n == 0: return 1
        if n < 0: return 0
        return self.climbNaive(n - 1) + self.climbNaive(n - 2)

    def climbMemoized(self, n: int) -> int:     # top down
        memo = [0] * (n + 1)

        def climb(n):
            if n < 0: return 0
            if n == 0: return 1
            if memo[n]: return memo[n]
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]
        return climb(n)

    def climbTabularized(self, n: int) -> int:     # bottom up
        dp = [0, 1, 2] + [0] * (n - 1)
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbTabularizedConstantSpace(self, n: int) -> int:     # bottom up
        nxt, cur, prev = 2, 1, 0
        for i in range(1, n+1):
            nxt = cur + prev
            prev = cur
            cur = nxt
        return cur


test = Solution()
print(test.climbNaive(10))
print(test.climbMemoized(10))
print(test.climbTabularized(10))
print(test.climbTabularizedConstantSpace(10))
