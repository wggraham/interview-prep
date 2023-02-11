from functools import lru_cache
from time import time


class Solution:
    def generateParenthesis(self, n):
        # @lru_cache(None)
        def explore(part, left, right):
            if left < 0 or right < 0 or right < left:
                return []
            if not left and not right:
                return [part]

            return explore(part + '(', left - 1, right) + explore(part + ')', left, right - 1)

        return explore("", n, n)

    def generateParenthesis2(self, n):
        partials = {'()'}
        for i in range(1, n):
            new_set = set()
            for p in partials:
                for j in range(i+1):
                    new_set.add(p[:j] + '()' + p[j:])
            partials = new_set
        return partials

    def generateParenthesis3(self, n):
        partials = {'()'}
        for i in range(1, n):
            new_set = set()
            for j in range(i+1):
                for p in partials:
                    new_set.add(p[:j] + '()' + p[j:])
            partials = new_set

        return partials

    def generateParenthesis4(self, n):
        def genP(lcount, rcount, part):
            p = []
            if not lcount and not rcount:
                return [''.join(part)]
            if lcount:
                p += genP(lcount - 1, rcount, part + ['('])
            if rcount > lcount:
                p += genP(lcount, rcount - 1, part + [')'])
            return p

        return genP(n, n, [])



test = Solution()
t0 = time()
print(test.generateParenthesis(3))
t1 = time()
print(test.generateParenthesis2(3))
t2 = time()
print(test.generateParenthesis4(3))
t3 = time()
print(t1 - t0)
print(t2 - t1)
print(t3 - t2)
