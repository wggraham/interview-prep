from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, t1, t2):
        root = TreeNode(t1.val + t2.val)
        q = deque([(root, t1, t2)])

        while q:
            tree, t1, t2 = q.popleft()

            if t1 and t2:
                if t1.left and t2.left:
                    tree.left = TreeNode(t1.left.val + t2.left.val)
                    q.append((tree.left, t1.left, t2.left))
                elif t1.left:
                    tree.left = TreeNode(t1.left.val)
                    q.append((tree.left, t1.left, None))
                elif t2.left:
                    tree.left = TreeNode(t2.left.val)
                    q.append((tree.left, t2.left, None))
                if t1.right and t2.right:
                    tree.right = TreeNode(t1.right.val + t2.right.val)
                    q.append((tree.right, t1.right, t2.right))
                elif t1.right:
                    tree.right = TreeNode(t1.right.val)
                    q.append((tree.right, t1.right, None))
                elif t2.right:
                    tree.right = TreeNode(t2.right.val)
                    q.append((tree.right, t2.right, None))
            elif t1:
                if t1.left:
                    tree.left = TreeNode(t1.left.val)
                    q.append((tree.left, t1.left, None))
                if t1.right:
                    tree.right = TreeNode(t1.right.val)
                    q.append((tree.right, t1.right, None))
            elif t2:
                if t2.left:
                    tree.left = TreeNode(t2.left.val)
                    q.append((tree.left, t2.left, None))
                if t2.right:
                    tree.right = TreeNode(t2.right.val)
                    q.append((tree.right, t2.right, None))

        return root
