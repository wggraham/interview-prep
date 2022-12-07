class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        def palin(string):
            if string == string[::-1]:
                return 1
            else:
                return 0

        dp = [0 for i in range(len(A) + 1)]
        dp[-1] = -1
        for i in range(len(A) - 1, -1, -1):
            val = len(A) - 1 - i
            for j in range(i + 1, len(A) + 1):
                if (palin(A[i:j]) == 1):
                    val = min(val, 1 + dp[j])
            dp[i] = val
        return dp[0]

class Solution:
    def minCut(self, A):
        def isPal(s):
            return s == s[::-1]

        n = len(A)
        minCuts = [i for i in range(n+1)]
        minCuts[0] = -1

        for i in range(1, n + 1):
            for j in range(i):
                if isPal(A[j:i]):
                    minCuts[i] = min(minCuts[i], minCuts[j] + 1)
        return minCuts[-1]


test = Solution()
A = "aabbbbaaa"
print(test.minCut(A))

