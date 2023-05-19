from sys import maxsize
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def get_sum(node):
            nonlocal max_sum
            if not node: return 0
            left_sum, right_sum = get_sum(node.left), get_sum(node.right)
            max_sum = max(max_sum, node.val, max(left_sum + right_sum, left_sum, right_sum) + node.val)
            return max(left_sum, right_sum, 0) + node.val

        max_sum = -maxsize
        get_sum(root)
        return max_sum

    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        def get_sum(node):
            nonlocal max_sum
            if not node: return 0
            left_sum, right_sum = max(0, get_sum(node.left)), max(0, get_sum(node.right))
            max_sum = max(max_sum, left_sum + right_sum + node.val)
            return max(left_sum, right_sum) + node.val

        max_sum = -maxsize
        get_sum(root)
        return max_sum


root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(3)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
test = Solution()
print(test.maxPathSum(root))

