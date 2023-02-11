from collections import Counter, defaultdict
from typing import List


class Solution:
    # doesn't work
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def explore(node, nodes):
            if node in dp:
                s = frozenset(nodes)
                if s in dp[node]:
                    return dp[node][s]

            if not nodes:
                return 0
            visit, s = set(), frozenset(nodes)
            for a in adj[node]:
                if a in nodes:
                    nodes.remove(a)
                    visit.add(a)

            for a in visit:
                dp[node][s] += explore(a, nodes)
            dp[node][s] += len(s)
            return dp[node][s]

        dp = defaultdict(Counter)
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        res = [0] * n
        for i in range(n):
            res[i] = explore(i, {j for j in range(n) if j != i})

        return res

    def sumOfDistancesInTree2(self, n: int, edges: List[List[int]]) -> List[int]:
        def set_subtree_depths(node, prev, depth):
            res[0] += depth
            subtree[node] += sum(set_subtree_depths(a, node, depth + 1) for a in adj[node] if a != prev)
            return subtree[node]

        def get_sum_distances(node, prev):
            for a in adj[node]:
                if a == prev: continue
                res[a] = n + res[node] - 2 * subtree[a]
                get_sum_distances(a, node)

        res, subtree, adj = [0] * n, [1] * n, defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        set_subtree_depths(0, -1, 0)
        get_sum_distances(0, -1)
        return res


n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
test = Solution()
print(test.sumOfDistancesInTree(n, edges))
print(test.sumOfDistancesInTree2(n, edges))
