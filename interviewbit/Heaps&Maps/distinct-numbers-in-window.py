from collections import Counter


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if B <= 0 or len(A) < B: return 0

        counts = Counter()
        total = 0
        for val in A[:B]:
            if val in counts:
                total -= 1
            total += 1
            counts[val] += 1

        totals = []
        for i in range(B, len(A)):
            totals.append(total)
            counts[A[i-B]] -= 1
            if counts[A[i-B]] == 0:
                total -= 1
            counts[A[i]] += 1
            if counts[A[i]] == 1:
                total += 1
        totals.append(total)
        return totals


A = [1, 1, 2, 2]
B = 1
test = Solution()
print(test.dNums(A, B))
