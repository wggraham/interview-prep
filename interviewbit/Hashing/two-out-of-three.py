from collections import Counter


class Solution:
    # this version handles duplicates (this is the better version)
    def solve(self, A, B, C):
        def inTwo(val):
            return True if sum(1 for x in (a, b, c) if val in x) > 1 else 0

        a, b, c = Counter(A), Counter(B), Counter(C)
        nums = sorted(list(set(A + B + C)))
        res = []
        for val in nums:
            if not inTwo(val): continue
            count = min(x[val] for x in (a, b, c) if val in x)
            res += [val] * count

        return res

    def solve2(self, A, B, C):
        def inTwo(val):
            return True if sum(1 for x in (a, b, c) if val in x) > 1 else False

        a, b, c, nums = Counter(A), Counter(B), Counter(C), sorted(list(set(A + B + C)))
        return [v for v in nums if inTwo(v)]


A = [1, 1, 2]
B = [2, 3]
C = [3]
A = [1, 2]
B = [1, 3]
C = [2, 3]
A = [56, 56, 34, 34, 72, 71]
B = [56, 56, 34, 34, 72, 71]
C = [56, 56, 34, 34, 72, 71]
test = Solution()
print(test.solve(A, B, C))
print(test.solve2(A, B, C))
