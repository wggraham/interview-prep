from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        q, res = deque([(root, 0)]), []
        while q:
            node, depth = q.popleft()
            if depth == len(res):
                res.append([])

            res[depth].append(node.val)
            q += [(x, depth + 1) for x in [node.left, node.right] if x]

        for i in range(len(res)):
            res[i] = res[i][::-1] if i % 2 else res[i]

        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

test = Solution()
print(test.zigzagLevelOrder(root))
