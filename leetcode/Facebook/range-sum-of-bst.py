from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def explore(node):
            if not node: return 0
            ans = explore(node.left) + explore(node.right)
            return ans + node.val if low <= node.val <= high else ans

        return explore(root)