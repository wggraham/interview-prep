from collections import defaultdict, deque


class Solution:
    def solve(self, n, matrix):
        adj = defaultdict(list)
        for a, b in matrix:
            adj[a].append(b)

        q, seen = deque([1]), set()
        while q:
            node = q.popleft()
            if node == n:
                return 1
            for a in adj[node]:
                if a in seen: continue
                seen.add(a)
                q.append(a)

        return 0


A = 5
B = [[1, 2],
     [4, 1],
     [2, 4],
     [3, 4],
     [5, 2],
     [1, 3]]
B = [[1, 2],
     [2, 3],
     [3, 4],
     [4, 5]]

test = Solution()
print(test.solve(A, B))
