from sys import maxsize
from collections import defaultdict


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def find_closest_leaf(self, root: TreeNode, k: int) -> int:
        s = [root]
        parent = defaultdict()
        parent[root] = None

        def findClosest(n):
            nonlocal parent
            s = [(n, 0)]
            seen = {n}
            minHops = maxsize
            while s:
                node, hop = s.pop()
                if node and node not in parent:
                    s.append((node, hop + 1))

                if not node.left and not node.right and node != n and hop < minHops:
                    minHops = hop
                if parent[node] and parent[node] not in seen:
                    s.append((parent[node], hop + 1))
                    seen.add(parent[node])
                for nd in [node.right, node.left]:
                    if not nd: continue
                    if nd not in seen:
                        s.append((nd, hop + 1))
                        parent[nd] = node
                        seen.add(nd)

            return minHops

        res = 0
        while s:
            node = s.pop()
            if node.val == k:
                res = findClosest(node)
                break
            for n in [node.right, node.left]:
                if not n: continue
                parent[n] = node
                s.append(n)
        return res


a = TreeNode(4)
a.left = TreeNode(2)
a.right = TreeNode(-5)
a.right.left = TreeNode(-2)
a.right.right = TreeNode(6)
a.right.left.left = TreeNode(7)
a.right.right.left = TreeNode(10)
a.right.right.left.right = TreeNode(1)
a.right.left.left.left = TreeNode(11)

test = Solution()
print(test.find_closest_leaf(a, -5))
