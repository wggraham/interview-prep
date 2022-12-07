from collections import deque
from sys import maxsize
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def cntMatrix(self, t1, t2):
        def explore(node):
            left = explore(node.left) if node.left else 0
            right = explore(node.right) if node.right else 0
            return left + right + 1

        q = deque([(t1, t2, -maxsize, maxsize)])
        total = 0
        while q:
            node1, node2, left_val, right_val = q.popleft()

            if node1.left and node2.left:
                q.append((node1.left, node2.left, left_val, node1.val - 1))
            elif not node1.left and node2.left:
                count = explore(node2.left)
                if count > node1.val - left_val:
                    return -1
                else:
                    total += count
            elif node1.left and not node2.left:
                return -1
            if node1.right and node2.right:
                q.append((node1.right, node2.right, node1.val + 1, right_val))
            elif not node1.right and node2.right:
                count = explore(node2.right)
                if count > right_val - node1.val:
                    return -1
                else:
                    total += count
            elif node1.right and not node2.right:
                return -1

        return total


t1 = TreeNode(788912528)
# t1.left = TreeNode(9)
# t1.right = TreeNode(20)
t2 = TreeNode(7)
t2.left = TreeNode(6)
t2.right = TreeNode(8)
t2.left.left = TreeNode(5)

# t2.right.left = TreeNode(6)

t1 = TreeNode()
test = Solution()
print(test.cntMatrix(t1, t2))


