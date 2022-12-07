from sys import maxsize


class Solution:
    def rodCut(self, A, B):
        dp = {}

        def minCuts(rod, cuts):
            if rod in dp: return dp[rod]
            if not cuts: return 0

            dp[rod] = maxsize
            for i, val in enumerate(cuts):
                dp[rod] = min(dp[rod], minCuts((rod[0], val), cuts[:i]) +
                              minCuts((val, rod[1]), cuts[i + 1:]))
            dp[rod] += rod[1] - rod[0]
            return dp[rod]

        return minCuts((0, A), sorted(B))


A = 6
B = [1, 2, 5]
test = Solution()
print(test.rodCut(A, B))
