class Solution:
    def permute(self, A):
        def genP(a, p):
            if not a: return [p]
            perms = []
            for i, val in enumerate(a):
                perms += genP(a[:i] + a[i+1:], p + [val])
            return perms

        return genP(A, [])


a = [1,2,3]
test = Solution()
print(test.permute(a))
