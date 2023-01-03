from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        leaves, parent = [], {root: None}
        s = [root]
        while s:
            node = s.pop()

            if not node.left and not node.right:
                leaves.append(node)

            if node.right:
                parent[node.right] = node
                s.append(node.right)
            if node.left:
                parent[node.left] = node
                s.append(node.left)

        diameter = 0
        deepest = defaultdict(int)
        for node in leaves:
            depth = 0
            while node:
                diameter = max(diameter, deepest[node] + depth)
                deepest[node] = max(depth, deepest[node])
                node = parent[node]
                depth += 1
        return diameter

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal diameter
            if not node: return 0
            d1, d2 = dfs(node.left), dfs(node.right)
            diameter = max(diameter, d1 + d2)
            return max(d1, d2) + 1

        diameter = 0
        dfs(root)
        return diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
test = Solution()
print(test.diameterOfBinaryTree2(root))
