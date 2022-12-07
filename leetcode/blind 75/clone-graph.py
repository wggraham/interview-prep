# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        nn = Node(node.val)
        d = {node.val: nn}
        s = [(node, nn)]

        while s:
            oNode, nNode = s.pop()

            for n in oNode.neighbors:
                if n.val not in d:
                    t = Node(n.val)
                    d[n.val] = t
                    s.append((n, t))
                nNode.neighbors.append(d[n.val])
        return nn