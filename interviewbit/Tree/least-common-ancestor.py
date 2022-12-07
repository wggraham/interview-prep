from sys import maxsize
from collections import deque
from copy import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lca(self, root, x, y):
        xlst, ylst = None, None

        s = [(root, [])]
        while s:
            node, p = s.pop()
            if node.val == x:
                p.append(x)
                xlst = p
            if node.val == y:
                p.append(y)
                ylst = p
            if xlst and ylst:
                break

            if node.right:
                s.append((node.right, p + [node.val]))
            if node.left:
                s.append((node.left, p + [node.val]))

        if not xlst or not ylst:
            return -1
        lca = -1
        for x,y in zip(xlst, ylst):
            if x != y:
                break
            lca = x
        return lca


def deSer(a):
    root = TreeNode(a[0])
    q = deque([root])
    for i in range(1, len(a), 2):
        node = q.popleft()
        if a[i] != -1:
            node.left = TreeNode(a[i])
            q.append(node.left)
        if i+1 < len(a) and a[i+1] != -1:
            node.right = TreeNode(a[i+1])
            q.append(node.right)

    return root


a = "73 15 20 34 35 5 14 16 26 -1 25 23 -1 30 3 36 -1 -1 7 24 11 32 -1 -1 21 -1 -1 -1 29 4 9 -1 33 13 -1 -1 -1 -1 22 31 -1 27 19 1 -1 12 18 6 -1 -1 -1 2 -1 -1 -1 -1 10 -1 -1 -1 -1 8 -1 28 -1 -1 -1 -1 -1 17 -1 -1 -1 -1"
a = a.split(' ')
a = [int(x) for x in a]
x = 33
y = 5

test = Solution()
print(test.lca(deSer(a), x, y))
