from collections import defaultdict, deque
import itertools
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(dict)
        q = deque([(root, 0, 0)])
        mn, mx = 0, 0
        while q:
            node, col, depth = q.popleft()
            mn = min(mn, col)
            mx = max(mx, col)
            if depth in d[col]:
                d[col][depth] = [min(d[col][depth][0], node.val)] + [max(d[col][depth][0], node.val)]
            else:
                d[col][depth] = [node.val]
            if node.left:
                q.append((node.left, col - 1, depth + 1))
            if node.right:
                q.append((node.right, col + 1, depth + 1))

        return [list(itertools.chain.from_iterable(d[x].values())) for x in range(mn, mx + 1)]


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
test = Solution()
print(test.verticalTraversal(root))
