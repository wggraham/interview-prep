from bisect import bisect


class Solution:
    def searchMatrix(self, mat, val):
        l, r = 0, len(mat) - 1
        while l <= r:
            m = (l + r) // 2
            if mat[m][0] <= val <= mat[m][-1]:
                x = bisect(mat[m], val)
                return 1 if x > 0 and val == mat[m][x - 1] else 0
            elif val < mat[m][0]:
                r = m - 1
            else:
                l = m + 1

        return 0


A = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50],
]
B = 3
test = Solution()
print(test.searchMatrix(A, B))
