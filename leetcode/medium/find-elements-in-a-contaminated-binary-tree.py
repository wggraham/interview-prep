from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.vals = set()
        s = deque([(self.root, 0)])
        while s:
            node, val = s.popleft()
            self.vals.add(val)
            if node.left:
                s.append((node.left, 2 * x + 1))
            if node.right:
                s.append((node.right, 2 * x + 2))



    def find(self, target: int) -> bool:
        return target in self.vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)