from collections import Counter


class Solution:
    def permute(self, A):
        def gen_perms(counts, perm):
            if not counts:
                return [perm]
            vals = set(counts.keys())
            res = []
            for val in vals:
                counts[val] -= 1
                if counts[val] == 0:
                    del counts[val]
                res += gen_perms(counts, perm + [val])
                counts[val] += 1
            return res

        return gen_perms(Counter(A), [])

    def permute1(self, A):
        def gen_perms(counts):
            if len(counts) == 1:
                v = counts.most_common(1)
                if v[0][1] == 1:
                    return [[v[0][0]]]

            vals = list(counts.keys())
            res = []
            for val in vals:
                counts[val] -= 1
                if counts[val] == 0:
                    del counts[val]
                res += [p + [val] for p in gen_perms(counts)]
                counts[val] += 1

            return res

        return gen_perms(Counter(A))

    def permute2(self, A):
        if len(A) == 1:
            return [A]
        res = []
        for i, v in enumerate(A):
            res += [[v] + p for p in self.permute2(A[:i] + A[i + 1:])]
        return res

    def permute3(self, A):
        if len(A) == 1:
            return [A]
        res = []
        for i in range(len(A)):
            nxt = self.permute(A[:i] + A[i + 1:])
            for j in nxt:
                res.append([A[i]] + j)
        return res

    def permute4(self, A):
        def gen_perms(rem):
            if len(rem) == 1:
                return [rem]
            res = []
            for i, v in enumerate(rem):
                res += [p + [v] for p in gen_perms(rem[:i] + rem[i + 1:])]
            return res

        return gen_perms(A)


A = [1, 1,3,3, 3]
test = Solution()
print(test.permute(A))
# print(test.permute2(A))
# print(test.permute3(A))
print(test.permute1(A))
