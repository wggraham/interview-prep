class Solution:
    def subsets(self, A):
        if not A: return []

        res = [[]]
        A.sort()

        def getSubs(a, p):
            for i, v in enumerate(a):
                res.append(p + [v])
                getSubs(a[i + 1:], p + [v])

        getSubs(A, [])
        return res

s = [1,2,3]
test = Solution()
print(test.subsets(s))


