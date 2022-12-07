from copy import copy

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        total = B
        res = []
        def getPaths(node, pSum, pTotal):
            nonlocal res, total
            if not node.left and not node.right:
                if pTotal == total:
                    res.append(pSum)
            if node.left: getPaths(node.left, pSum + [node.left.val], pTotal + node.left.val)
            if node.right: getPaths(node.right, pSum + [node.right.val], pTotal + node.right.val)
        getPaths(A, [A.val], A.val)
        return res

test = Solution()
root = TreeNode(1000)
root.left = TreeNode(2000)
root.left.left = TreeNode(-3001)
print(test.pathSum(root, -1))
