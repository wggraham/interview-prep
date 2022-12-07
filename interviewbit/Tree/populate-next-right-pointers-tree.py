# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        s = [root]
        while len(s):
            d = []
            for i in range(len(s)):
                if s[i].left:
                    d.append(s[i].left)
                if s[i].right:
                    d.append(s[i].right)
                s[i].next = s[i + 1] if i + 1 < len(s) else None
            s = d

