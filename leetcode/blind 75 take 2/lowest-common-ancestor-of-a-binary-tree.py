# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False, False, None

            p1, q1, a1 = dfs(node.left)
            p2, q2, a2 = dfs(node.right)
            ancestor = a1 if not a2 else a2
            pFound = p1 or p2 or p == node
            qFound = q1 or q2 or q == node
            if pFound and qFound and not ancestor:
                ancestor = node
            return pFound, qFound, ancestor

        return dfs(root)[2]


root = TreeNode(3)
root.left = p = TreeNode(1)
root.left.right = q = TreeNode(2)

test = Solution()
x = test.lowestCommonAncestor(root, p, q)
print(x.val)
