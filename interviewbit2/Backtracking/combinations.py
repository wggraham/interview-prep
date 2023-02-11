class Solution:
    def combine(self, n, k):
        def gen_combos(i, combo):
            if len(combo) == k:
                res.append(combo)
                return
            for j in range(i, n):
                gen_combos(j + 1, combo + [vals[j]])

        res = []
        res, vals = [], [i for i in range(1, n + 1)]
        gen_combos(0, [])
        return res


n, k = 4, 2
test = Solution()
print(test.combine(n, k))
