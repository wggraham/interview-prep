from collections import defaultdict


class Solution:
    def lszero(self, A):
        sumTo = []
        total = 0
        sums = defaultdict(int)
        sums[0] = -1
        longest = 0
        indices = (None, None)
        for i, v in enumerate(A):
            total += v
            sumTo.append(total)
            if total not in sums:
                sums[total] = i
            else:
                if longest < i - sums[total]:
                    longest = i - sums[total]
                    indices = (sums[total]+1, i)

        return A[indices[0]:indices[1]+1] if indices[0] is not None else []


a = [1, 2, -2, 4, -4]
# a = [1, 2, -3, 3]
a = [ -19, 8, 2, -8, 19, 5, -2, -23 ]
test = Solution()
print(test.lszero(a))
