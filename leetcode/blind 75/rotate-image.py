from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0, n // 2):
            for j in range(i, n - 1-i):
                matrix[i][j], matrix[j][-1 - i], matrix[-1 - i][-1 - j], matrix[-1 - j][i] = \
                    matrix[-1 - j][i], matrix[i][j], matrix[j][-1 - i], matrix[-1 - i][-1 - j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix)
test = Solution()
test.rotate(matrix)
print(matrix)
