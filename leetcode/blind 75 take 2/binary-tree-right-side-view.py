from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depths = {}
        q = deque([(root, 0)])
        maxDepth = 0
        while q:
            node, depth = q.popleft()
            if depth not in depths:
                depths[depth] = node.val
                maxDepth = depth

            if node.right:
                q.append((node.right, depth + 1))
            if node.left:
                q.append((node.left, depth + 1))

        return [depths[i] for i in range(maxDepth + 1)]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
test = Solution()
print(test.rightSideView(root))
