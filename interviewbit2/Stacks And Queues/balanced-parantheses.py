class Solution:
    def solve(self, A):
        count = 0
        for c in A:
            count += 1 if c == '(' else -1
            if count < 0:
                return 0
        return int(count == 0)