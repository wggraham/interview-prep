# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        total = 0

        def getTotal(node, p):
            nonlocal total
            if not node.left and not node.right:
                total += int(''.join(p))
                return
            if node.left: getTotal(node.left, p + [str(node.left.val)])
            if node.right: getTotal(node.right, p + [str(node.right.val)])

        getTotal(A, [str(A.val)])
        return total % 1003


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
test = Solution()
print(test.sumNumbers(root))


