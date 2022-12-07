from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, root, k):
        q = deque([(root)])
        node = root
        parent = {}
        while q:
            node = q.popleft()

            if node.val == k:
                break

            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)

        p = []
        while node:
            p.append(node.val)
            node = parent[node] if node in parent else None

        return p[::-1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
k = 15
test = Solution()
print(test.solve(root, k))