class Solution:
    def searchMatrix(self, A, B):

        l, r, m = 0, len(A) - 1, 0
        while l <= r:
            m = (l + r) // 2
            if A[m][0] <= B <= A[m][-1]:
                break
            if A[m][0] > B:
                r = m - 1
            else:
                l = m + 1

        l, r, i = 0, len(A[m]) - 1, m
        while l <= r:
            m = (l + r) // 2
            if A[i][m] == B:
                return 1
            if A[i][m] > B:
                r = m - 1
            else:
                l = m + 1
        return 0


A = [[1, 3, 5, 7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]
B = 3

# A = [[5, 17, 100, 111],
#      [119, 120, 127, 131]]
# B = 3
A = [[1]]
B = 1
test = Solution()
print(test.searchMatrix(A, B))

