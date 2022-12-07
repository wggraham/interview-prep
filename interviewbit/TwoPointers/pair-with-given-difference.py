class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        m = set()
        for val in A:
            if val in m:
                return 1
            m.add(val - B)
            m.add(val + B)
        return 0