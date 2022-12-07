# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = (p, q) if p.val <= q.val else (q, p)
        s = [root]
        while s:
            node = s.pop()
            if p.val <= node.val <= q.val:
                return node
            if p.val <= node.val:
                s.append(node.left)
            else:
                s.append(node.right)


