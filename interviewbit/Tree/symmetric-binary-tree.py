from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        q = deque([(root, 0)])
        res = []
        while q:
            node, depth = q.popleft()
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            q += [(x, depth + 1) for x in (node.left, node.right) if x]

        for level in res[1:]:
            if level != level[::-1] or len(level) % 2:
                return 0

        return 1



root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(1)
# root.right.left = TreeNode(4)
# root.right.left.right = TreeNode(5)

test = Solution()
print(test.isSymmetric(root))
