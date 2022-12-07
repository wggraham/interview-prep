from typing import List

class Solution:
    def __init__(self, matrix = None):
        self.lpath = {}
        self.explored = set()
        self.matrix = matrix

    def inBounds(self, i, j):
        return not (i < 0 or j < 0 or i > len(self.matrix) - 1 or j > len(self.matrix[0]) - 1)

    def explore(self, i, j):

        m = 1
        if self.inBounds(i-1, j) and self.matrix[i-1][j] > self.matrix[i][j]:
            if (i-1, j) not in self.explored:
                self.explore(i-1, j)
            m = max(m, self.lpath[(i-1,j)] + 1)
        if self.inBounds(i+1, j) and self.matrix[i+1][j] > self.matrix[i][j]:
            if (i+1, j) not in self.explored:
                self.explore(i+1, j)
            m = max(m, self.lpath[(i+1,j)] + 1)
        if self.inBounds(i, j-1) and self.matrix[i][j-1] > self.matrix[i][j]:
            if (i, j-1) not in self.explored:
                self.explore(i, j-1)
            m = max(m, self.lpath[(i,j-1)] + 1)
        if self.inBounds(i, j+1) and self.matrix[i][j+1] > self.matrix[i][j]:
            if (i, j+1) not in self.explored:
                self.explore(i, j+1)
            m = max(m, self.lpath[(i,j+1)] + 1)
        self.lpath[(i,j)] = m


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.__init__(matrix)
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in self.explored:
                    self.explore(i, j)
                m = max(m, self.lpath[(i,j)])
        return m


matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
test = Solution()
print(test.longestIncreasingPath(matrix))
