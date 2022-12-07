from collections import defaultdict
import timeit


class Solution:
    def numDistinct(self, A, B):

        if len(A) < len(B):
            return 0

        bSet = set([c for c in B])
        m = defaultdict(list)
        for i, c in enumerate(A):
            if c in bSet:
                m[c].append(i)

        p = m[B[0]]
        for c in B[1:]:
            tmp = []
            for s in p:
                for i in m[c]:
                    if s < i:
                        tmp.append(i)

            p = tmp
        return len(p)

    def numDistinctTabulation(self, A, B):
        if len(A) < len(B):
            return 0

        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) + 1):
            dp[i][0] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

    def numDistinctTabulationOptimized(self, A, B):
        if len(A) < len(B):
            return 0

        dp = [1] + [0] * len(B)

        for i in range(1, len(A) + 1):
            tmp = [0] * (len(B) + 1)
            tmp[0] = dp[0]
            for j in range(1, len(B) + 1):
                tmp[j] = dp[j]
                if A[i - 1] == B[j - 1]:
                    tmp[j] += dp[j-1]
            dp = tmp
        return dp[-1]

    def numDistinctMemoize(self, A, B):
        if not len(B): return 1
        if not len(A): return 0
        return self.numDistinctMemoize(A[1:], B[1:]) + self.numDistinctMemoize(A[1:], B) if A[0] == B[0] else self.numDistinctMemoize(A[1:], B)


a = "aaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3ppaaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3ppaaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3ppaaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3ppaaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3pp"
b = "aaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3ppaaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3ppaaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3ppaaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3ppaaaaabbbccdfnrhgoiwhoitrhgfnewiprgnhiotqhgioreqgnpiewhpiqjpergptiwhjpijhpoqrejhpetjipjio2qj5ipjp3pp"
# a = "rabbbit"
# b = "rabbit"
a = "baabbaaabaaabaaaabbbbabaaabbbabbba"
b = "bab"
test = Solution()
start = timeit.default_timer()
t = test.numDistinctTabulation(a, b)
stop = timeit.default_timer()
print("Tabulation Time: ", stop - start)
print(t)

start = timeit.default_timer()
t = test.numDistinctTabulationOptimized(a, b)
stop = timeit.default_timer()
print("Tabulation optimized Time: ", stop - start)
print(t)
# start = timeit.default_timer()
# test.numDistinctMemoize(a, b)
# stop = timeit.default_timer()
# print("Memoization Time: ", stop - start)


