class Solution:
    def solve(self, A):
        count = 0
        for p in A:
            count += 1 if p == '(' else -1
            if count < 0:
                return 0
        return 1 if count == 0 else 0