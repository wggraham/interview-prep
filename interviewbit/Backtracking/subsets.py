class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, A):
        if not A or not len(A):
            return [[]]
        self.gensubs(sorted(A), [])
        return self.res

    def gensubs(self, s, sub):
        self.res.append(sub)

        for i, val in enumerate(s):
            self.gensubs(s[i + 1:], sub + [val])


test = Solution()
a = [1,1, 2, 3]
print(test.subsets(a))
