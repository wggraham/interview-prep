class Solution:
    def combine(self, n, k):
        def gen_subs(i, sub, k):
            if not k:
                res.append(sub)
                return
            for i in range(i, n + 2 - k):
                gen_subs(i + 1, sub + [i], k - 1)

        res = []
        gen_subs(1, [], k)
        return res


n = 4
k = 2
test = Solution()
print(test.combine(n, k))
