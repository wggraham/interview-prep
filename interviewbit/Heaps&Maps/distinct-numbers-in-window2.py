from collections import Counter


class Solution:
    def dNums(self, a, b):
        if b > len(a):
            return []

        c = Counter(a[:b])
        res = [len(c)]
        for i, v in enumerate(a[b:]):
            c[a[i]] -= 1
            if not c[a[i]]:
                del c[a[i]]
            c[v] += 1
            res.append(len(c))
        return res


A = [1, 2, 1, 3, 4, 3]
B = 3
test = Solution()
print(test.dNums(A, B))
