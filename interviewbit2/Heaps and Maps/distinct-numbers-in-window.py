from collections import Counter


class Solution:
    def dNums(self, A, B):
        counts = Counter(A[:B])
        res = [len(counts)]
        for i, val in enumerate(A[B:], B):
            counts[val] += 1
            counts[A[i - B]] -= 1
            if counts[A[i - B]] == 0:
                del counts[A[i - B]]

            res.append(len(counts))

        return res


A = [1, 2, 1, 3, 4, 3]
B = 3
test = Solution()
print(test.dNums(A, B))
