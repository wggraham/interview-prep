from typing import Optional, List
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0)])
        l, r = 0, 0
        verts = defaultdict(list)
        while q:
            node, vert = q.popleft()
            verts[vert].append(node.val)
            l, r = min(l, vert), max(r, vert)
            if node.left: q.append((node.left, vert - 1))
            if node.right: q.append((node.right, vert + 1))

        return [verts[i] for i in range(l, r+1)]



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
test = Solution()
print(test.verticalOrder(root))