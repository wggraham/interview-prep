from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, root):
        q = deque([(root, 1)])
        res = []
        while q:
            node, depth = q.popleft()
            if depth > len(res):
                res.append(node.val)
            if node.right:
                q.append((node.right, depth + 1))
            if node.left:
                q.append((node.left, depth + 1))
        return res