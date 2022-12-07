from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preOrder(self, root):
        if not root: return []
        return [root.val] + self.preOrder(root.left) + self.preOrder(root.right)

    def postOrder(self, root):
        if not root: return []
        return self.postOrder(root.left) + self.postOrder(root.right) + [root.val]

    def inOrder(self, root):
        if not root: return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def preOrderIterative(self, root):
        s, res = [root], []
        while s:
            node = s.pop()
            res.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return res

    def postOrderIterative(self, root):
        s, res = [root], []
        while s:
            node = s.pop()
            res.append(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return res[::-1]

    def postOrderIterativeHardWay(self, root):
        s, res, visited = [root], [], set()
        while s:
            node = s.pop()
            if node.val in visited:
                res.append(node.val)
                continue

            visited.add(node.val)
            s.append(node)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return res

    def inOrderIterative(self, root):
        s, res = [root], []
        visited = set()

        while s:
            node = s.pop()
            if node.val in visited:
                res.append(node.val)
                continue

            if node.right:
                s.append(node.right)

            visited.add(node.val)
            s.append(node)

            if node.left:
                s.append(node.left)
        return res

    def inOrderIterative2(self, root):
        s, res = [root], []
        seen = set()

        while s:
            node = s.pop()
            while node.left and node.left.val not in seen:
                s.append(node)
                seen.add(node.val)
                node = node.left

            res.append(node.val)

            if node.right:  # if a right child exists enqueue it
                s.append(node.right)
                seen.add(node.right.val)
        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return

        s = [root]
        while s:
            node = s.pop()

            while node.left:
                s.append(node)
                node = node.left

            k -= 1
            if k == 0:
                return node.val

            if node.right:
                s.append(node.right)
            else:
                node = s.pop()
                k -= 1
                if k == 0:
                    return node.val

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        s = [root]
        visited = set()

        while s:
            node = s.pop()
            if node.val in visited:
                k -= 1
                if k == 0:
                    return node.val
                continue

            if node.right:
                s.append(node.right)

            visited.add(node.val)
            s.append(node)

            if node.left:
                s.append(node.left)

    def kthSmallest3(self, root, k):
        s = []

        while True:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

    def kthSmallestRecursive(self, root, k):
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        return inorder(root)[k - 1]

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.right = TreeNode(4)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
test = Solution()
# print(test.preOrder(root))
# print(test.preOrderIterative(root))
# print(test.postOrder(root))
# print(test.postOrderIterative(root))
# print(test.postOrderIterativeHardWay(root))
# print(test.inOrder(root))
# print(test.inOrderIterative(root))
# print(test.inOrderIterative2(root))
print(test.kthSmallest2(root, 3))
print(test.kthSmallest3(root, 3))
