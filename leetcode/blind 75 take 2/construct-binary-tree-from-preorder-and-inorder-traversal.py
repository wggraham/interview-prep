from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return

        root = TreeNode(preorder[0])
        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])

        return root


preorder = [3, 9, 12, 6, 20, 15, 7]
inorder = [9, 6, 12, 3, 15, 20, 7]
# preorder = [1, 2, 3]
# inorder = [2, 3, 1]
preorder = [1, 2]
inorder = [1, 2]
test = Solution()
x = test.buildTree(preorder, inorder)
print(x)
