class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if not A: return 1
        count = 0
        for p in A:
            if p == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return 0
        return 1 if not count else 0