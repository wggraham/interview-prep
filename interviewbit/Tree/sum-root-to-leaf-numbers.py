from locale import atoi

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, A):
        total = 0

        def sumPaths(node, pSum):
            nonlocal total
            if not node.left and not node.right:
                total += atoi(''.join(pSum + [str(node.val)]))
                return
            if node.left:
                sumPaths(node.left, pSum + [str(node.val)])
            if node.right:
                sumPaths(node.right, pSum + [str(node.val)])

        sumPaths(A, [])
        return total


tree = TreeNode(1)
#tree.left = TreeNode(1)
tree.right = TreeNode(2)

test = Solution()
print(test.sumNumbers(tree))

