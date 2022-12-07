from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def explore(node):
            if not node: return False, False, ''
            foundStart = True if node.val == startValue else False
            foundEnd = True if node.val == destValue else False

            fs, fe, pl = explore(node.left)
            ffs, ffe, pr = explore(node.right)
            if fs and fe:
                return fs, fe, pl
            if ffs and ffe:
                return ffs, ffe, pr

            if fs or fe:
                pl = 'L' + pl
            if ffs or ffe:
                pr = 'R' + pr

            if (ffs or fs) and (ffe or fe or foundEnd):
                if fs:
                    path = 'U' * len(pl) + pr
                else:
                    path = 'U' * len(pr) + pl

                return True, True, path
            path = ''
            if len(pl):
                path = pl
            elif len(pr):
                path = pr
            return ffs or fs or foundStart, ffe or fe or foundEnd, path
        return explore(root)[2]


root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(4)
# root.left.left.left = TreeNode(6)
# root.left.left.left.right = TreeNode(2)

test = Solution()
print(test.getDirections(root,2,1))

