from collections import defaultdict, deque, Counter
from heapq import heapify, heapreplace


class Node:
    def __init__(self):
        self.children = []
        self.parent = None
        self.maxDepths = [0, 0]
        heapify(self.maxDepths)


def buildTree(parents):
    d = {}
    for i, p in enumerate(parents):
        node = Node()
        d[i] = node

        if p == -1: continue
        d[i].parent = d[p]
        d[p].children.append(node)

    return getLeafNodeList(d)


def getLeafNodeList(nodeMap):
    leaves = []
    numChildren = Counter()
    for _, node in nodeMap.items():
        numChildren[node] = len(node.children)
        if not len(node.children):
            leaves.append(node)
    return leaves, numChildren


class Solution:
    def __init__(self):
        self.maxDistance = 0

    def exploreIterative(self, leaves, numChildren):
        d = deque(leaves)

        while d:
            node = d.popleft()
            numChildren[node.parent] -= 1
            self.maxDistance = max(self.maxDistance, sum(node.maxDepths))
            if not node.parent:
                continue

            if not numChildren[node.parent]:
                d.append(node.parent)
            heapreplace(node.parent.maxDepths, max(node.maxDepths[1] + 1, node.parent.maxDepths[0]))

    def explore(self, node):
        for c in node.children:
            depth = self.explore(c)
            heapreplace(node.maxDepths, max(node.maxDepths[0], depth + 1))
        self.maxDistance = max(self.maxDistance, node.maxDepths[0] + node.maxDepths[1])
        return node.maxDepths[1]

    def solve(self, A):
        leaves, numChildren = buildTree(A)
        self.exploreIterative(leaves, numChildren)
        return self.maxDistance


A = [-1, 0, 1, 1, 2, 0, 5, 0, 3, 0, 0, 2, 3, 1, 12, 14, 0, 5, 9, 6, 16, 0, 13, 4, 17, 2, 1, 22, 14, 20, 10, 17, 0, 32,
     15, 34, 10, 19, 3, 22, 29, 2, 36, 16, 15, 37, 38, 27, 31, 12, 24, 29, 17, 29, 32, 45, 40, 15, 35, 13, 25, 57, 20,
     4, 44, 41, 52, 9, 53, 57, 18, 5, 44, 29, 30, 9, 29, 30, 8, 57, 8, 59, 59, 64, 37, 6, 54, 32, 40, 26, 15, 87, 49,
     90, 6, 81, 73, 10, 8, 16]
test = Solution()
print(test.solve(A))
