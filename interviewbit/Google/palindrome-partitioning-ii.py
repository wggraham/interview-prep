from sys import maxsize


class Solution:
    def minCut(self, A):
        if not A: return 0
        minCuts = [len(A)] * (len(A) + 1)
        minCuts[0] = -1
        n = len(minCuts)

        def isPal(s):
            return s == s[::-1]

        for i in range(1, n):
            for j in range(i):
                if not isPal(A[j:i]):
                    continue
                minCuts[i] = min(minCuts[i], minCuts[j] + 1)
        return minCuts[-1]

    def minCut2(self, A):   #too slow

        minCuts = {}
        n = len(A)

        def isPal(s):
            return s == s[::-1]

        def explore(i, j):
            nonlocal minCuts, n
            if (i, j) in minCuts: return minCuts[(i, j)]
            if isPal(A[i:j + 1]):
                minCuts[(i, j)] = 0
            else:
                m = maxsize
                for k in range(i, j):
                    m = min(m, explore(i, k) + explore(k + 1, j) + 1)
                minCuts[(i, j)] = m
            return minCuts[(i, j)]

        return explore(0, n - 1)



test = Solution()
A = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
print(test.minCut(A))
print(test.minCut2(A))
