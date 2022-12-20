from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return

        node = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return node

    def buildTreeIterative(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        s = [(TreeNode(), root, preorder, inorder, False)]

        while s:
            parent, node, pre, inn, left = s.pop()

            if left:
                parent.left = node
            else:
                parent.right = node
            if not inn: continue
            i = inn.index(pre[0])
            child = TreeNode(pre[0])
            s.append((node, child, pre[i + 1:], inn[i + 1:], False))
            s.append((node, child, pre[1:i + 1], inn[:i], True))

        return root.left


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
# preorder = [3, 1, 2, 4, 5]
# inorder = [1, 2, 3, 4, 5]
test = Solution()
x = test.buildTree(preorder, inorder)
y = test.buildTreeIterative(preorder, inorder)
print(10)
