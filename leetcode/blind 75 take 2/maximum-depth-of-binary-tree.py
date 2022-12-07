from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = [(root, 1)]
        deepest = 0
        while s:
            node, depth = s.pop()

            if not node.left and not node.right:
                deepest = max(deepest, depth)

            if node.right: s.append((node.right, depth + 1))
            if node.left: s.append((node.left, depth + 1))

        return deepest