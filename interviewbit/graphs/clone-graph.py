from collections import deque, defaultdict


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def cloneGraph(self, node):
        if not node: return

        nr = UndirectedGraphNode(node.label)
        seen = defaultdict()
        seen[node.label] = nr
        q = deque([(node, nr)])

        while q:
            on, nn = q.popleft()

            for n in on.neighbors:
                if not seen[n.label]:
                    node = UndirectedGraphNode(n.label)
                    seen[n.label] = node
                    q.append((n, node))
                nn.neighbors.append(seen[n.label])

        return nr
