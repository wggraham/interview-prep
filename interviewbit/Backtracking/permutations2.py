class Solution:
    def permute(self, A):

        def perm(a, p):
            if not a:
                return [p]

            perms = []
            for i, v in enumerate(a):
                if i and a[i - 1] == v:
                    continue
                perms.extend(perm(a[:i] + a[i + 1:], p + [v]))
            return perms

        return perm(A, [])


a = [1, 2, 3]
test = Solution()
print(test.permute(a))
