from collections import deque


class Solution:
    def nearestHotel2(self, A, B):
        n = len(A)
        m = len(A[0])
        inf = 1 << 30
        dis = [[0 for _ in range(1005)] for _ in range(1005)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    dis[i + 1][j + 1] = inf
                else:
                    dis[i + 1][j + 1] = 0
                    q.append([i + 1, j + 1])

        while len(q) > 0:
            curr = q[0]
            q.popleft()
            x = curr[0]
            y = curr[1]
            if dis[x][y + 1] == inf:
                dis[x][y + 1] = dis[x][y] + 1
                q.append([x, y + 1])

            if dis[x][y - 1] == inf:
                dis[x][y - 1] = dis[x][y] + 1
                q.append([x, y - 1])

            if dis[x + 1][y] == inf:
                dis[x + 1][y] = dis[x][y] + 1
                q.append([x + 1, y])

            if dis[x - 1][y] == inf:
                dis[x - 1][y] = dis[x][y] + 1
                q.append([x - 1, y])

        ans = []
        for i in range(len(B)):
            ans.append(dis[B[i][0]][B[i][1]])

        return ans

    def nearestHotel(self, grid, coords):
        def inBound(y, x):
            return 0 <= y < n and 0 <= x < m

        def explore(i, j, dist):
            dist = 1 if grid[i][j] == 1 else dist
            grid[i][j] = dist
            seen.add((i, j))
            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                y, x = i + ii, j + jj
                if not inBound(y, x): continue
                if (y, x) in seen and dist + 1 >= grid[y][x]: continue

                explore(y, x, dist + 1)

        n, m = len(grid), len(grid[0])
        seen = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in seen:
                    explore(i, j, 1)

        return [grid[y - 1][x - 1] - 1 for y, x in coords]

    def nearestHotel3(self, grid, coords):
        def inBound(y, x):
            return 0 <= y < n and 0 <= x < m

        n, m = len(grid), len(grid[0])
        q = deque()
        seen = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j, 1))
                    seen.add((i,j))

        while q:
            i, j, dist = q.popleft()
            grid[i][j] = dist
            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                y, x = i + ii, j + jj
                if not inBound(y, x) or (y, x) in seen: continue
                seen.add((y,x))
                q.append((y,x,dist + 1))

        return [grid[y - 1][x - 1] - 1 for y, x in coords]


A = [[0, 0],
     [1, 0]]
B = [[1, 1],
     [2, 1],
     [1, 2]]

A = [[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
B = [[8, 29],
     [4, 29],
     [2, 2],
     [9, 19],
     [1, 11],
     [21, 25],
     [7, 24],
     [44, 2],
     [42, 15],
     [38, 10],
     [17, 15],
     [16, 16],
     [34, 2],
     [21, 21],
     [16, 25],
     [37, 29],
     [3, 13],
     [9, 7],
     [16, 29],
     [6, 8],
     [39, 13],
     [1, 7],
     [25, 4],
     [16, 12],
     [11, 3],
     [15, 14],
     [33, 1],
     [37, 26],
     [28, 6],
     [33, 2],
     [11, 2],
     [42, 19],
     [41, 12],
     [43, 3],
     [27, 29],
     [37, 19],
     [18, 21],
     [43, 16],
     [35, 3],
     [23, 5],
     [15, 14],
     [26, 1],
     [28, 6],
     [11, 28],
     [1, 11],
     [25, 28],
     [6, 19],
     [24, 17],
     [43, 3],
     [1, 9],
     [7, 10],
     [34, 5],
     [42, 19],
     [42, 10],
     [19, 19],
     [17, 13],
     [8, 29],
     [21, 8],
     [41, 14],
     [19, 3],
     [44, 10],
     [9, 26],
     [40, 13],
     [22, 24],
     [29, 24],
     [29, 5],
     [6, 28],
     [28, 15],
     [14, 8],
     [44, 18],
     [37, 23],
     [13, 5],
     [40, 14],
     [35, 13],
     [8, 7],
     [19, 24],
     [19, 18],
     [6, 15],
     [25, 22],
     [1, 20],
     [2, 11],
     [6, 28],
     [26, 10],
     [43, 3],
     [23, 7],
     [27, 6],
     [39, 23],
     [39, 26],
     [41, 1],
     [27, 5],
     [37, 10],
     [31, 3],
     [8, 4],
     [6, 3],
     [18, 8],
     [8, 1],
     [28, 17],
     [16, 17],
     [14, 3],
     [8, 2],
     [29, 6],
     [17, 18],
     [3, 10],
     [4, 16],
     [11, 5],
     [31, 11],
     [9, 9],
     [2, 12],
     [44, 20],
     [38, 8],
     [22, 28],
     [36, 8],
     [5, 3],
     [3, 29],
     [30, 12],
     [2, 13],
     [4, 4],
     [33, 28],
     [40, 11],
     [3, 12],
     [4, 4],
     [18, 8],
     [35, 20],
     [13, 25],
     [6, 15],
     [42, 17],
     [41, 8],
     [32, 8],
     [14, 4],
     [2, 11],
     [31, 27],
     [22, 9],
     [19, 3],
     [39, 5],
     [42, 16],
     [17, 7],
     [34, 29],
     [24, 5],
     [11, 27],
     [43, 13],
     [4, 23],
     [22, 25],
     [12, 18],
     [25, 20],
     [34, 27],
     [19, 21],
     [40, 16],
     [16, 14],
     [32, 16],
     [26, 15],
     [22, 7],
     [18, 2],
     [34, 14],
     [25, 5],
     [38, 9],
     [17, 17],
     [12, 13],
     [15, 4],
     [10, 4],
     [2, 3],
     [7, 3],
     [21, 15],
     [25, 21],
     [35, 25],
     [33, 10],
     [12, 20],
     [11, 23],
     [37, 13],
     [4, 25],
     [1, 24],
     [3, 23],
     [30, 14],
     [43, 9],
     [27, 28],
     [39, 14],
     [16, 4],
     [3, 29],
     [32, 17],
     [11, 3],
     [28, 14],
     [6, 1],
     [20, 6],
     [17, 6],
     [39, 2],
     [12, 4],
     [20, 26],
     [18, 11],
     [15, 3],
     [40, 2],
     [31, 12],
     [27, 25],
     [2, 10],
     [3, 22],
     [16, 9],
     [33, 4],
     [26, 14],
     [37, 16],
     [26, 1],
     [41, 10],
     [35, 29],
     [25, 4],
     [10, 19],
     [27, 10],
     [16, 14],
     [33, 8],
     [32, 18],
     [19, 16],
     [1, 15],
     [7, 22],
     [25, 22],
     [3, 28],
     [14, 21],
     [16, 1],
     [26, 28],
     [42, 16],
     [34, 25],
     [17, 23],
     [3, 13],
     [35, 22],
     [20, 25],
     [20, 17],
     [20, 12],
     [26, 6],
     [13, 15],
     [15, 5],
     [11, 23],
     [9, 29],
     [3, 12],
     [25, 2],
     [32, 20],
     [4, 12],
     [27, 21],
     [6, 11],
     [15, 16],
     [37, 19],
     [35, 1],
     [38, 17],
     [29, 8],
     [28, 8],
     [25, 7],
     [2, 10],
     [42, 15],
     [8, 17],
     [29, 17],
     [26, 21],
     [4, 12],
     [11, 5],
     [34, 12],
     [4, 19],
     [14, 16],
     [13, 2],
     [2, 24],
     [19, 23],
     [21, 4],
     [9, 8],
     [25, 10],
     [17, 7],
     [30, 6],
     [3, 13],
     [34, 5],
     [7, 2],
     [10, 15],
     [16, 26],
     [29, 25],
     [1, 19],
     [8, 29],
     [40, 12],
     [5, 14],
     [39, 27],
     [34, 25],
     [34, 22],
     [18, 1],
     [16, 28],
     [32, 27],
     [22, 22],
     [20, 1],
     [10, 5],
     [6, 22],
     [1, 3],
     [30, 22],
     [3, 8],
     [25, 5],
     [41, 25],
     [43, 14],
     [29, 28],
     [2, 14],
     [26, 12],
     [8, 14],
     [7, 14],
     [22, 22],
     [21, 26],
     [11, 20],
     [33, 22],
     [24, 21],
     [13, 2],
     [37, 1],
     [35, 17],
     [17, 10],
     [8, 12],
     [20, 28],
     [42, 5],
     [43, 12],
     [29, 14],
     [34, 16],
     [1, 20],
     [33, 11],
     [1, 1],
     [12, 19],
     [9, 24],
     [4, 17],
     [17, 12],
     [15, 8],
     [17, 28],
     [37, 16],
     [1, 28],
     [9, 6],
     [6, 21],
     [39, 24],
     [36, 19],
     [16, 19],
     [36, 8],
     [17, 26],
     [1, 5],
     [26, 19],
     [30, 21],
     [38, 6],
     [27, 26],
     [19, 27],
     [33, 17],
     [43, 4],
     [5, 7],
     [42, 26],
     [5, 8],
     [36, 1],
     [18, 7],
     [32, 28],
     [2, 19],
     [2, 5],
     [6, 25],
     [18, 27],
     [32, 9],
     [18, 8],
     [26, 16],
     [42, 18],
     [26, 2],
     [4, 20],
     [27, 22],
     [2, 8],
     [43, 17],
     [25, 15],
     [31, 25],
     [19, 29],
     [16, 11],
     [5, 7],
     [26, 19],
     [27, 16],
     [6, 10],
     [16, 21],
     [18, 26],
     [40, 27],
     [10, 21],
     [17, 4],
     [31, 19],
     [14, 22],
     [43, 1],
     [13, 20],
     [20, 9],
     [43, 8],
     [5, 18],
     [32, 1],
     [7, 6],
     [38, 6],
     [25, 20],
     [40, 28],
     [20, 28],
     [8, 5],
     [19, 14],
     [28, 22],
     [18, 9],
     [1, 6],
     [42, 1],
     [34, 2],
     [31, 17],
     [32, 15],
     [39, 26],
     [16, 4],
     [8, 22],
     [19, 3],
     [21, 27],
     [19, 17],
     [43, 16],
     [34, 17],
     [22, 19],
     [26, 11],
     [43, 15],
     [44, 22],
     [24, 5],
     [19, 11],
     [26, 22],
     [30, 23],
     [20, 15],
     [18, 24],
     [10, 6],
     [5, 22],
     [42, 6],
     [11, 5],
     [7, 1],
     [23, 28],
     [34, 18],
     [32, 27],
     [42, 25],
     [22, 25],
     [37, 19],
     [8, 15],
     [29, 22],
     [3, 20],
     [33, 9],
     [32, 19],
     [23, 15],
     [25, 21],
     [28, 20],
     [25, 11],
     [40, 21],
     [43, 12],
     [21, 25],
     [16, 10],
     [3, 22],
     [20, 12],
     [44, 16],
     [28, 24],
     [42, 9],
     [42, 15],
     [26, 26],
     [32, 28],
     [25, 18],
     [18, 10],
     [34, 15],
     [6, 17],
     [19, 7],
     [21, 9],
     [29, 2],
     [28, 26],
     [11, 26],
     [6, 28],
     [22, 25],
     [21, 14],
     [43, 27],
     [29, 26],
     [22, 29],
     [24, 10],
     [28, 3],
     [20, 1],
     [37, 1],
     [20, 5],
     [15, 24],
     [17, 19],
     [27, 22],
     [10, 16],
     [13, 25],
     [31, 20],
     [19, 25],
     [2, 11],
     [23, 23],
     [32, 24],
     [34, 2],
     [30, 3],
     [30, 24],
     [5, 29],
     [33, 4],
     [28, 19],
     [32, 10],
     [41, 2],
     [14, 27],
     [44, 10],
     [13, 26],
     [23, 21],
     [7, 27],
     [3, 1],
     [15, 25],
     [16, 15],
     [3, 6],
     [20, 11],
     [5, 13],
     [22, 26],
     [30, 21],
     [27, 2],
     [39, 8],
     [30, 17],
     [32, 18],
     [24, 9],
     [12, 28],
     [11, 5],
     [2, 2],
     [12, 21],
     [1, 16],
     [28, 28],
     [35, 29],
     [20, 9],
     [40, 25],
     [33, 2],
     [35, 12],
     [15, 6],
     [3, 13],
     [31, 16],
     [3, 6],
     [8, 29],
     [16, 7],
     [6, 8],
     [11, 7],
     [17, 14],
     [39, 15],
     [17, 16],
     [6, 9],
     [44, 24],
     [20, 13],
     [38, 27],
     [14, 3],
     [2, 14],
     [8, 27],
     [41, 24],
     [28, 26],
     [34, 5],
     [27, 16],
     [13, 17],
     [11, 3],
     [34, 18],
     [13, 29],
     [31, 28],
     [34, 25],
     [38, 9],
     [28, 26],
     [17, 1],
     [41, 5],
     [22, 19],
     [10, 8],
     [3, 26],
     [43, 17],
     [20, 25],
     [37, 16],
     [24, 21],
     [10, 29],
     [31, 22],
     [37, 20],
     [17, 1],
     [9, 7],
     [1, 7],
     [12, 4],
     [28, 1],
     [36, 19],
     [13, 20],
     [10, 14],
     [31, 11],
     [20, 19],
     [13, 11],
     [28, 18],
     [34, 26],
     [16, 26],
     [44, 18],
     [1, 26],
     [16, 28],
     [28, 5],
     [16, 8],
     [44, 18],
     [6, 23],
     [5, 26],
     [17, 15],
     [15, 12],
     [5, 15],
     [30, 10],
     [24, 7],
     [6, 3],
     [24, 13],
     [16, 8],
     [29, 18],
     [16, 2],
     [3, 9],
     [15, 21],
     [17, 27],
     [8, 21],
     [13, 15],
     [18, 16],
     [20, 29],
     [33, 6],
     [26, 19],
     [6, 18],
     [43, 17],
     [2, 26],
     [37, 29],
     [4, 9],
     [2, 23],
     [14, 16],
     [30, 19],
     [41, 15],
     [43, 2],
     [25, 13],
     [33, 10],
     [44, 29],
     [25, 18],
     [5, 16],
     [25, 16],
     [8, 23],
     [37, 20],
     [17, 26],
     [38, 5],
     [10, 10],
     [11, 18],
     [16, 17],
     [27, 10],
     [36, 5],
     [30, 26],
     [34, 13],
     [23, 23],
     [23, 1],
     [11, 27],
     [17, 19],
     [35, 13],
     [32, 2],
     [26, 14],
     [18, 14],
     [14, 21],
     [42, 13],
     [25, 20],
     [25, 13],
     [15, 25],
     [22, 18],
     [42, 22],
     [8, 18],
     [7, 24],
     [11, 17],
     [24, 7],
     [36, 17],
     [36, 18],
     [18, 23],
     [26, 3],
     [33, 8],
     [14, 28],
     [10, 12],
     [2, 11],
     [37, 14],
     [13, 3],
     [32, 13],
     [38, 24],
     [37, 13],
     [24, 24],
     [16, 17],
     [11, 11],
     [39, 6],
     [31, 17],
     [9, 28],
     [16, 20],
     [10, 22],
     [33, 5],
     [8, 1],
     [15, 5],
     [1, 16],
     [38, 13],
     [9, 27],
     [8, 7],
     [35, 14],
     [26, 7],
     [13, 27],
     [20, 23],
     [32, 26],
     [24, 5],
     [14, 5],
     [6, 26],
     [22, 8],
     [40, 23],
     [18, 14],
     [44, 4],
     [8, 5],
     [21, 21],
     [7, 3],
     [19, 27],
     [22, 12],
     [2, 5],
     [35, 11],
     [22, 29],
     [34, 23],
     [20, 29],
     [37, 8],
     [19, 4],
     [24, 2],
     [34, 6],
     [26, 2],
     [38, 29],
     [30, 21],
     [40, 20],
     [32, 25],
     [31, 22],
     [32, 9],
     [44, 18],
     [38, 16],
     [35, 26],
     [13, 7],
     [19, 25],
     [29, 27],
     [35, 17],
     [36, 1],
     [32, 14],
     [8, 20],
     [27, 26],
     [39, 9],
     [31, 14],
     [41, 23],
     [12, 28],
     [11, 9],
     [43, 8],
     [13, 20],
     [34, 17],
     [25, 22],
     [40, 20],
     [16, 10],
     [6, 20],
     [34, 27],
     [9, 24],
     [34, 6],
     [24, 8],
     [44, 25],
     [39, 25],
     [34, 8],
     [34, 25],
     [34, 1],
     [36, 15],
     [14, 1],
     [43, 10],
     [27, 9],
     [24, 5],
     [20, 4],
     [44, 6],
     [7, 26],
     [26, 26],
     [42, 9],
     [42, 23],
     [4, 6],
     [3, 17],
     [31, 28],
     [25, 13],
     [17, 20],
     [26, 24],
     [35, 9],
     [2, 26],
     [38, 21],
     [18, 23],
     [2, 23],
     [41, 6],
     [6, 7],
     [35, 2],
     [25, 1],
     [15, 10],
     [23, 14],
     [36, 18],
     [7, 14],
     [33, 20],
     [1, 7],
     [22, 18],
     [25, 10],
     [27, 2],
     [42, 8],
     [23, 17],
     [10, 27],
     [17, 20],
     [35, 4],
     [3, 11],
     [43, 22],
     [33, 15],
     [1, 9],
     [2, 21],
     [43, 28],
     [22, 4],
     [5, 17],
     [39, 5],
     [44, 7],
     [38, 20],
     [36, 14],
     [2, 18],
     [28, 27],
     [37, 9],
     [11, 2],
     [30, 20],
     [32, 19],
     [26, 9],
     [23, 11],
     [44, 17],
     [27, 15],
     [41, 6],
     [33, 15],
     [42, 17],
     [31, 12],
     [43, 5],
     [11, 10],
     [36, 22],
     [19, 12],
     [7, 5],
     [29, 17],
     [1, 23],
     [7, 11],
     [36, 4],
     [36, 8],
     [2, 19],
     [35, 9],
     [8, 15],
     [18, 16],
     [2, 6],
     [12, 6],
     [26, 11],
     [7, 19],
     [8, 10],
     [28, 18],
     [40, 8],
     [5, 18],
     [8, 21],
     [41, 3],
     [41, 27],
     [24, 26],
     [30, 8],
     [14, 15],
     [16, 13],
     [30, 26],
     [4, 20],
     [5, 12],
     [7, 13],
     [13, 19],
     [15, 26],
     [27, 16],
     [36, 15],
     [39, 13],
     [42, 8],
     [2, 11],
     [43, 23],
     [32, 10],
     [29, 6],
     [22, 22],
     [37, 10],
     [15, 18],
     [7, 28],
     [23, 4],
     [34, 8],
     [31, 16],
     [16, 12],
     [32, 23],
     [31, 19],
     [28, 2],
     [20, 21],
     [6, 18],
     [9, 18],
     [7, 14],
     [33, 19],
     [41, 11],
     [19, 12],
     [25, 27],
     [12, 8],
     [33, 9],
     [43, 17],
     [15, 1],
     [4, 25],
     [30, 23],
     [2, 9],
     [3, 21],
     [25, 4],
     [1, 4],
     [30, 21],
     [29, 4],
     [14, 16],
     [20, 14],
     [39, 1],
     [6, 18],
     [39, 22],
     [1, 4],
     [14, 7],
     [13, 9],
     [35, 6],
     [18, 19],
     [19, 25],
     [36, 4],
     [38, 26],
     [10, 18],
     [4, 15],
     [43, 16],
     [31, 13],
     [30, 22],
     [7, 16],
     [40, 9],
     [23, 12],
     [29, 14],
     [44, 14],
     [39, 8],
     [12, 5],
     [28, 25],
     [43, 11],
     [28, 1],
     [2, 17],
     [26, 14],
     [26, 14],
     [19, 3],
     [13, 15],
     [29, 26],
     [36, 22],
     [31, 1],
     [36, 25],
     [18, 7],
     [35, 28],
     [27, 3],
     [7, 29],
     [40, 19],
     [7, 20],
     [29, 10],
     [10, 8],
     [37, 21],
     [27, 2],
     [3, 27],
     [39, 14],
     [27, 13],
     [15, 11],
     [29, 1],
     [43, 16],
     [16, 16],
     [40, 22],
     [36, 29],
     [41, 3],
     [18, 29],
     [37, 6],
     [26, 6],
     [17, 13],
     [43, 27],
     [29, 26],
     [27, 24],
     [26, 14],
     [1, 19],
     [6, 13],
     [44, 1],
     [40, 25],
     [14, 26],
     [35, 25],
     [3, 2],
     [30, 16],
     [5, 20],
     [23, 28],
     [40, 18]]

test = Solution()
print(test.nearestHotel3(A, B))
# print(test.nearestHotel2(A, B))