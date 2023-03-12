from collections import defaultdict


class Solution:
    def solve(self, A):
        counts = defaultdict(int)
        longest = 0
        count = 0
        for i, v in enumerate(A):
            count += 1 if v else -1
            if count == 1:
                longest = i + 1
            elif count - 1 in counts:
                longest = max(longest, i - counts[count - 1])

            if count not in counts:
                counts[count] = i

        return longest


A = [0, 1, 1, 0, 0, 1]
# A = [1, 0, 0, 1, 0]
test = Solution()
print(test.solve(A))
