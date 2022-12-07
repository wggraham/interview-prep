from typing import List, Optional
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0, 0)])
        l, r = 0, 0
        verts = defaultdict(lambda: defaultdict(SortedList))
        depths = defaultdict(SortedSet)
        while q:
            node, vert, depth = q.popleft()
            l, r = min(l, vert), max(r, vert)
            verts[vert][depth].add(node.val)
            depths[vert].add(depth)
            if node.left: q.append((node.left, vert - 1, depth + 1))
            if node.right: q.append((node.right, vert + 1, depth + 1))

        return [[v for j in depths[i] for v in verts[i][j]] for i in range(l, r + 1)]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
test = Solution()
print(test.verticalTraversal(root))
