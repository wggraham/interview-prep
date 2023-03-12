class Solution:
    def diffPossible(self, A, B):
        vals = set()
        for val in A:
            if val - B in vals or val + B in vals:
                return 1
            vals.add(val)

        return 0


A = [1, 5, 3]
B = 2
A = [2, 4, 3]
B = 3

test = Solution()
print(test.diffPossible(A, B))
