# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
       self.root = None

class Solution:
    def constructAncestors(self, node, left=True):
        parent = {}
        if left:
            while node.left:
                parent[node.left] = node
                node = node.left
        else:
            while node.right:
                parent[node.right] = node
                node = node.right
        return node, parent

    def incLeft(self, node, parent):
        if node == self.root:
            return node, parent
        if parent[node].left == node:
            node = parent[node]
        else:
            node = parent[parent[node]].right
            node, p = self.constructAncestors(node)
            parent.update(p)
        return node, parent

    def decRight(self, node, parent):
        if node == self.root:
            return node, parent
        if parent[node].right == node:
            node = parent[node]
            node, p = self.constructAncestors(node)
            parent.update(p)
        else:
            node = parent[node]
        return node, parent

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        self.root = A
        left, lp = self.constructAncestors(A)
        right, rp = self.constructAncestors(A, False)

        while left.val < right.val:
            if left.val + right.val == B:
                return 1
            if left.val + right.val < B:
                left, p = self.incLeft(left, lp)
                lp.update(p)
            if left.val + right.val > B:
                right, p = self.decRight(right, rp)
                rp.update(p)

        return 0


root = TreeNode(10)
root.left = TreeNode(9)
root.right = TreeNode(20)
k = 19
test = Solution()
print(test.t2Sum(root, k))
