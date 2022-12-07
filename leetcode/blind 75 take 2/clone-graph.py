from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraphBFS(self, root: 'Node') -> 'Node':
        if not root: return
        cloneMap = {root: Node(root.val)}

        queue = deque([root])
        while queue:
            node = queue.popleft()

            for n in node.neighbors:
                if n not in cloneMap:
                    cloneMap[n] = Node(n.val)
                    queue.append(n)
                cloneMap[node].neighbors.append(cloneMap[n])
        return cloneMap[root]

    def cloneGraphDFS(self, root: 'Node') -> 'Node':
        if not root: return
        cloneMap = {root: Node(root.val)}

        s = [root]
        while s:
            node = s.pop()

            for n in node.neighbors:
                if n not in cloneMap:
                    cloneMap[n] = Node(n.val)
                    s.append(n)
                cloneMap[node].neighbors.append(cloneMap[n])
        return cloneMap[root]

    def cloneGraphBFSVal(self, root: 'Node') -> 'Node':
        if not root: return
        cloneMap = {root.val: Node(root.val)}

        queue = deque([root])
        while queue:
            node = queue.popleft()

            for n in node.neighbors:
                if n.val not in cloneMap:
                    cloneMap[n.val] = Node(n.val)
                    queue.append(n)
                cloneMap[node.val].neighbors.append(cloneMap[n.val])
        return cloneMap[root.val]