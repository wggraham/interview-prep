from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, root):
        q = deque([root])
        parent = {root: None}
        while q:
            node = q.popleft()
            if sum(1 for x in (node.left, node.right) if x) % 2:
                if parent[node] and parent[node].left == node:
                    parent[node].left = node.left if node.left else node.right
                if parent[node] and parent[node].right == node:
                    parent[node].right = node.left if node.left else node.right
                if node.left:
                    parent[node.left] = parent[node]
                else:
                    parent[node.right] = parent[node]
            elif node.right and node.left:
                parent[node.left] = node
                parent[node.right] = node

            q += [node.left] if node.left else []
            q += [node.right] if node.right else []

        return root



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)

test = Solution()
x = test.solve(root)
print(10)