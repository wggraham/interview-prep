from typing import List
from copy import deepcopy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        res = []

        def buildTree(n, node, root):
            nonlocal res
            if n == 1:
                return
            if n == 0:
                res.append(deepcopy(root))
                return
            if n == 2:
                node.left = TreeNode(0)
                node.right = TreeNode(0)
                res.append(deepcopy(root))
                return
            if n > 2:
                node.left = TreeNode(0)
                node.right = TreeNode(0)
                buildTree(n - 2, node.left, root)
                node.left.left = None
                node.left.right = None
                buildTree(n - 2, node.right, root)

        root = TreeNode(0)
        buildTree(n - 1, root, root)
        return res

test = Solution()
print(test.allPossibleFBT(7))
