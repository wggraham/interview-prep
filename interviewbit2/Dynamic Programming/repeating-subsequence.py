from collections import defaultdict


class Solution:
    def anytwo(self, A):
        d = defaultdict(tuple)
        for i in range(len(A)):
            for j in range(i):
                sub = A[j] + A[i]
                if sub in d and d[sub][0] != j and d[sub][1] != i:
                    return 1
                if sub not in d:
                    d[sub] = (j, i)
        return 0


A = "abab"
A = "abba"
A = "aabb"
test = Solution()
print(test.anytwo(A))
