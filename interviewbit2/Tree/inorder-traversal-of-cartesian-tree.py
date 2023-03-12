class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, A):
        def build(i, j):
            if i > j:
                return

            root_val, root_idx = A[i], i
            for k in range(i, j + 1):
                if A[k] > root_val:
                    root_val, root_idx = A[k], k

            root = TreeNode(root_val)
            root.left = build(i, root_idx - 1)
            root.right = build(root_idx + 1, j)

            return root

        return build(0, len(A) - 1)

    def buildTree2(self, A):
        if not A: return
        root = TreeNode(A[0])
        for val in A[1:]:
            node = TreeNode(val)
            if val > root.val:
                node.left = root
                root = node
                continue

            temp = root
            while temp.right and temp.right.val > val:
                temp = temp.right

            node.left, temp.right = temp.right, node

        return root

    def buildTree3(self, A):
        if not A: return

        max_idx = A.index(max(A))
        root = TreeNode(A[max_idx])
        root.left = self.buildTree3(A[:max_idx])
        root.right = self.buildTree3(A[max_idx+1:])

        return root


A = [1, 2, 3]
test = Solution()
x = test.buildTree(A)
y = test.buildTree2(A)
print(10)
