class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root):
        self.node = root
        self.stack = []
        while self.node:
            self.__iterate__()

        self.val = self.__iterate__()

    def __iterate__(self):
        if self.node:
            self.stack.append(self.node)
            self.node = self.node.left
            return
        if not self.stack:
            return

        self.node = self.stack.pop()
        val = self.node.val
        self.node = self.node.right
        return val

    def hasNext(self):
        return self.val is not None

    def next(self):
        val = self.val
        t = self.__iterate__()
        while t is None and self.stack:
            t = self.__iterate__()
        self.val = t
        return val

# Your BSTIterator will be called like this:

# i = BSTIterator(root)
# while i.hasNext():
#     print(i.next())
