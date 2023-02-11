from bisect import bisect_left
from sys import maxsize


class Solution:
    def lis(self, A):
        seq_lens = [-maxsize]

        for i, v in enumerate(A):
            j = 0
            for j in reversed(range(len(seq_lens))):
                if v > seq_lens[j]:
                    break

            if j == len(seq_lens) - 1:
                seq_lens += [v] if v > seq_lens[-1] else []
            else:
                seq_lens[j + 1] = v

        return len(seq_lens) - 1

    def lis2(self, A):
        seq_lens = [-maxsize]

        for i, v in enumerate(A):
            if v >= seq_lens[-1]:
                seq_lens += [v] if v > seq_lens[-1] else []
                continue

            for j in reversed(range(len(seq_lens)-1)):
                if v > seq_lens[j]:
                    seq_lens[j + 1] = v
                    break

        return len(seq_lens) - 1

    def lis3(self, A):
        seq_lens = []

        for i, v in enumerate(A):
            j = bisect_left(seq_lens, v)
            seq_lens = seq_lens + [v] if j == len(seq_lens) else seq_lens[:j] + [min(seq_lens[-1], v)] + seq_lens[j+1:]

        return len(seq_lens)


A = [1, 2, 1, 5]
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# A = [56, 49, 44, 6, 31, 44, 79, 26, 77, 92, 44, 90, 90, 33, 69, 15, 99, 52, 46, 63, 61, 86, 11, 76, 45, 45, 35, 91, 60,
#      69, 63, 3, 91, 8, 77, 29, 6, 90, 80, 3, 77, 41, 25, 12, 85, 76, 63, 26, 31, 48, 2, 52, 56, 100, 31, 48, 4, 36, 88,
#      94]
A = [1]
test = Solution()
print(test.lis(A))
print(test.lis2(A))
print(test.lis3(A))
