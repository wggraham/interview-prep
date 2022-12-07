from heapq import heapify, heappop, heappush
from sys import maxsize

class Solution:
    def solve(self, n, matrix):
        bridges = [(matrix[i][2], matrix[i][j]) for i in range(len(matrix)) for j in range(2)]
        heapify(bridges)
        adj, total, edge = [[] for _ in range(n+1)], maxsize, None
        for island1, island2, cost in matrix:
            adj[island1].append((cost, island2))
            adj[island2].append((cost, island1))
            if cost < total:
                total = cost
                edge = (island1, island2)

        unconnected = {i for i in range(1, n + 1) if i != edge[0] and i != edge[1]}
        edges = [x for x in adj[edge[0]] + adj[edge[1]] if x[1] in unconnected]
        heapify(edges)

        while unconnected:
            while edges[0][1] not in unconnected:
                heappop(edges)

            subtotal, isl = heappop(edges)
            unconnected.remove(isl)
            total += subtotal
            for cost, island in adj[isl]:
                if island in unconnected:
                    heappush(edges, (cost, island))

        return total


A = 4
B = [[1, 2, 1],
     [2, 3, 4],
     [1, 4, 3],
     [4, 3, 2],
     [1, 3, 10]]

test = Solution()
print(test.solve(A, B))
