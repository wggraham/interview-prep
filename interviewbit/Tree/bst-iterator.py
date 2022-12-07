from collections import defaultdict, deque
from itertools import pairwise


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
        self.seen = set(root)
        self.parent = defaultdict()
        self.stack = deque([root])

    def iterate(self, node):
        if not node.left and not node.right:
            return None
        # still have to preorder essentially
        # with stack to pop back
        while self.stack:
            node = self.stack.popleft()

            # traverse to next smallest node, saving parent
            while node.left and node.left not in self.seen:
                self.stack.append(node)
                self.seen.add(node.left)
                node = node.left
            # now at left most edge (aka smallest remaining value)

        # in order traversal

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        node = self.iterate(node)
        return True if node else False

    # @return an integer, the next smallest number
    def next(self):
        self.node = self.iterate(self.node)
        return self.node.val


def iterativeInOrderTraversal(root):
    if not root:
        return None

    s = [root]
    seen = set(root)
    res = []
    while s:
        node = s.pop()
        while node.left and node.left not in seen:
            node = node.left
            s.append(node)
            seen.add(node)

        res.append(node.val)
        if node.right:
            s.append(node.right)
    return res


def buildBST(lst):
    root = TreeNode(lst[0])
    lst = lst[1:]
    s = deque([root])
    for l, r in pairwise(lst):
        node = s.popleft()
        if l and l != -1:
            node.left = TreeNode(l)
            s.append(node.left)
        if r and r != -1:
            node.right = TreeNode(r)
            s.append(node.right)
    return root


t = [1, 2, 3]
tree = buildBST(t)
print(iterativeInOrderTraversal(tree))
