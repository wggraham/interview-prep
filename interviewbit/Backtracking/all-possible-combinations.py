class Solution:
    def specialStrings(self, A):
        def gen_combos(combo):
            if len(combo) == n:
                res.append(''.join(combo))
                return
            for c in A[len(combo)]:
                gen_combos(combo + [c])

        res, n = [], len(A)
        gen_combos([])
        return res


A = ['ab', 'cd']
test = Solution()
print(test.specialStrings(A))
