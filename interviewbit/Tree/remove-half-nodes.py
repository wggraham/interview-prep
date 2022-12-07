# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        if not A: return
        s = [A]

        while s:
            node = s.pop()
            if node.left:
                if node.left.left and not node.left.right:
                    node.left = node.left.left
                elif node.left.right and not node.left.left:
                    node.left = node.left.right
                s.append(node.left)
            if node.right:
                if node.right.left and not node.right.right:
                    node.right = node.right.left
                elif node.right.right and not node.right.left:
                    node.right = node.right.right
                s.append(node.right)
        return A


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.right = TreeNode(6)
test = Solution()
b = test.solve(head)
print(10)