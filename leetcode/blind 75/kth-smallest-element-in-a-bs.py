from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = [root]
        node = None
        while s and k > 0:
            node = s.pop()

            while node.left:
                s.append(node)
                node = node.left

            k -= 1
            if node.right:
                s.append(node.right)
            else:
                while k > 0 and s and not node.right:
                    node = s.pop()
                    k -= 1
                if node.right:
                    s.append(node.right)
        return node.val

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        node = root
        while k > 0:
            if node:
                s.append(node)
                node = node.left
                continue
            node = s.pop()
            v = node.val
            node = node.right
            k -= 1

        return v


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

test = Solution()
print(test.kthSmallest(root, 3))
