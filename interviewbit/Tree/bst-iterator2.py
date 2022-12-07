# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.node = root
        self.s = []
        self.getLeftEdge()

    def goLeft(self):
        self.s.append(self.node)
        self.node = self.node.left

    def getLeftEdge(self):
        while self.node.left:
            self.goLeft()

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.node is not None

    # @return an integer, the next smallest number
    def next(self):
        v = self.node.val
        if not self.s:
            self.node = None
            return v
        self.node = self.s.pop()

        self.getLeftEdge()
        if self.node.right:
            self.s.append(node.right)
        elif self.s:
            self.node = self.s.pop()
            if self.node.right:
                self.s.append(self.node.right)

        return v


# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(8)

i = BSTIterator(root)
while i.hasNext():
    print(i.next(), end=' ')
