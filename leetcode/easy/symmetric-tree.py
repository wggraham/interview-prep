from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        s = [(root, root)]

        while s:
            l, r = s.pop()
            if not r or l.val != r.val: return False
            s += [(l.left, r.right)] if l.left else []
            s += [(l.right, r.left)] if l.right else []

        return True


test = Solution()
