# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers

    def recoverTree(self, A):
        l = []

        def explore(node, mx, mn):
            nonlocal l
            if not node:
                return mx, mn
            mx, mn = max(node.val, mx), min(node.val, mn)
            lx, ln = explore(node.left, mx, mn)
            if lx > mx:
                l = [mx, lx]
            rx, rn = explore(node.right, mx, mn)
            if rn < mn:
                l = [rn, mn]
            if lx > rn:
                l = [rn, lx]
            return mx, mn
        explore(A, A.val, A.val)
        return l


tree = TreeNode(2)
tree.left = TreeNode(3)
tree.right = TreeNode(1)

test = Solution()
print(test.recoverTree(tree))
