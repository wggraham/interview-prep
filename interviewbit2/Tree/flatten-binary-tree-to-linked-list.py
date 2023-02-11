class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # doesn't work
    def flatten(self, A):
        def explore(node, parent):
            head, nxt, a, b = node, None, 0, 0
            if not node.left and not res[1]:
                res[1] = True
                res[0] = node
            if node.left:
                head, a = explore(node.left, node)
            if node.right:
                nxt, b = explore(node.right, node)

            node.left = None
            node.right = nxt if nxt else parent
            return head, a + b + 1

        res = [None, False]
        _, count = explore(A, None)
        node = res[0]
        for _ in range(count - 1):
            node = node.right
        node.right = None
        return res[0]

    def flatten2(self, root):
        stack, node, count = [], root, 0

        while node or stack:
            count += 1
            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                node = node.left
            elif stack:
                node.left = stack.pop()
                node = node.left
            else:
                break

        node = root
        while node:
            node.right = node.left
            node.left = None
            node = node.right

        return root

    def flatten3(self, A):
        root = node = A

        while node:
            if node.left:
                prev = node.left
                while prev.right:
                    prev = prev.right
                prev.right = node.right
                node.right = node.left
                node.left = None

            node = node.right

        return root

    def flatten6(self, root):
        node = root
        while node:
            if not node.left:
                node = node.right
                continue

            prev = node.left
            while prev.right: prev = prev.right
            prev.right, node.right, node.left, node = node.right, node.left, None, node.left

        return root

    def flatten8(self, root):
        node = root
        while True:
            while node and not node.left: node = node.right
            if not node: break
            prev = node.left
            while prev.right: prev = prev.right
            prev.right, node.right, node.left, node = node.right, node.left, None, node.left

        return root

    def flatten4(self, root):
        def explore(node):
            if not node or (not node.left and not node.right):
                return node

            if node.right:
                prev_right = explore(node.right)
                if node.left:
                    prev_left = explore(node.left)
                    prev_left.right = node.right
                    node.right = node.left
                    node.left = None
                return prev_right

            prev_left = explore(node.left)
            node.right = node.left
            node.left = None
            return prev_left

        explore(root)
        return root

    # doesn't work
    def flatten5(self, root):
        def explore(node):
            if not node or (not node.left and not node.right):
                return node

            prev_right, prev_left = explore(node.right), explore(node.left)
            if node.right and prev_left:
                prev_left.right = node.right

            node.right = node.left
            node.left = None
            return prev_right if prev_right else prev_left

        explore(root)
        return root


A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)
test = Solution()
x = test.flatten5(A)
print(10)
