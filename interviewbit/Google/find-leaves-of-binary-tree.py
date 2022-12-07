from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        parent = {root: None}
        leaves = []
        q = deque([(root)])
        while q:
            node = q.popleft()
            if not node.left and not node.right:
                leaves.append(node)
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)

        q = deque([(node, 0) for node in leaves])
        res = []
        seen = set()
        while q:
            node, depth = q.popleft()
            if len(res) < (depth + 1):
                res.append([])
            res[depth].append(node.val)
            if parent[node] and ((parent[node] in seen and parent[node].left and parent[node].right) or
                                 (parent[node] not in seen and parent[node].left and not parent[node].right) or
                                 (parent[node] not in seen and parent[node].right and not parent[node].left)):
                q.append((parent[node], depth + 1))
            else:
                seen.add(parent[node])

        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
test = Solution()
print(test.findLeaves(root))
